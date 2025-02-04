% clear all;
% close all;
% clc;
rng('shuffle');

% Directories
homedir = cd;
addpath([homedir filesep]);

% Input
sID = input('Subject ID? ', 's');
sID = upper(sID);
savedir = [homedir filesep 'output' filesep sID];

if ~isfolder(savedir)
    mkdir(savedir);
end

time.startExp = datestr(now);

% Keyboard settings
KbName('UnifyKeyNames');
escapeKey = KbName('ESCAPE');
escapeKey2 = KbName('q');
leftKey = KbName('LeftArrow');
leftKey2 = KbName('4');
rightKey = KbName('RightArrow');
rightKey2 = KbName('6');

[keybIndices, keybNames] = GetKeyboardIndices;

% Stimulus and display settings
stim.center = [0,0];    
stim.size = [2,2];    
stim.sigma = 1.5;       
screenRes = Screen('Rect', 0);

display.resolution = screenRes(3:4);   
display.width = 15; 
display.dist = 136;  
display.screen = 0; 
display.pxPerDeg = angle2pix(display,1);
display.angPerPix = pix2angle(display,1);
display.stereomode = 0; 

% quick CSF settings
numTrials = 120;
priors = [75 1 2.5 .1];
qcsf = setupQCSF;
qcsf = setupPriors(qcsf, priors);

try
    % Load relevant stuff
    load('gammaTable_example.mat', 'gammaTable');
    Screen('Preference', 'SkipSyncTests', 1);
    
    % Open the screen
    PsychImaging('PrepareConfiguration');
    PsychImaging('AddTask', 'General', 'Enable11BitFrameBuffer');
    PsychImaging('AddTask', 'General', 'NormalizedHighresColorRange', 1);
    PsychImaging('AddTask', 'General', 'EnablePseudoGrayOutput');
    
    [theScreen, theScreenArea] = PsychImaging('OpenWindow', 0, 0.5, [], [], 2, display.stereomode);
    Screen('LoadNormalizedGammaTable', theScreen, gammaTable * [1 1 1]);
    Screen('BlendFunction', theScreen, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    Priority(MaxPriority(theScreen));
    
    % just for information (not important to do if you don't care)
    ifi = Screen('GetFlipInterval', theScreen);
    calculatedFrameRate = 1/ifi; %#ok<*NOPTS>
    
    gray = 0.5; 
    background = gray;
    text.size = 40;
    text.color = 1;
    Screen('TextSize', theScreen, text.size);
    flipHandle = Screen('Flip', theScreen);
    HideCursor;
    ListenChar(2);
    
    beepHigh = MakeBeep(2000,0.02) * 0.1;
    beepLow = MakeBeep(1000,0.02) * 0.1;
    %% Do the experiment
    for trial = 1:numTrials
        qcsf.data.trial = trial;
        [qcsf, SF, contrast] = runQCSF(qcsf, 'pretrial');
        
        CR = ceil(2 * rand);
        if CR == 1
            orient = -45; % in degress
        else
            orient = 45;
        end
        
        % spatial coordinates
        [x,y] = meshgrid(linspace(-stim.size(1)/2,...
            stim.size(1)/2,...
            angle2pix(display,stim.size(1))),...
            linspace(-stim.size(2)/2,...
            stim.size(2)/2,...
            angle2pix(display,stim.size(2))));
        
        % ramp
        ramp = cos(orient*pi/180)*x + sin(orient*pi/180)*y;
        
        % Make the Gaussian window
        Gauss = exp(-((x-stim.center(1)).^2+(y-stim.center(2)).^2)/(2*stim.sigma^2));
        
        grating = sin(2*pi*ramp*SF) .* Gauss * contrast;      
        
        grating = grating/2 +0.5;
       
        gratingTex = Screen('MakeTexture', theScreen, grating);
        Screen('DrawTexture', theScreen, gratingTex, [], CenterRect(Screen('Rect', gratingTex), theScreenArea));
        
        Screen('Flip', theScreen);
        pause(0.5);
        
        responded = 0;
        while responded == 0
            [secs, keyCode, deltaSecs] = KbWait();
            if any(find(keyCode, 1) == [leftKey leftKey2 rightKey rightKey2 escapeKey escapeKey2])
                responded = 1;
            end
        end
        
        if any(find(keyCode,1) == [rightKey rightKey2])
            if CR == 1
                response = 1;
                Snd('Play',beepHigh,44100);
            else
                response = 0;
                Snd('Play',beepLow,44100);
            end
        elseif any(find(keyCode,1) == [leftKey leftKey2])
            if CR == 2
                response = 1;
                Snd('Play',beepHigh,44100);
            else
                response = 0;
                Snd('Play',beepLow,44100);
            end
        elseif any(find(keyCode,1) == [escapeKey escapeKey2])
            break;
        end
        
        % record and update
        Screen('FillRect', theScreen, background);
        Screen('Flip', theScreen);
        qcsf.data.history(trial,:) = [trial SF contrast response]; % updating the experimental history
        qcsf = runQCSF(qcsf, 'posttrial', SF, contrast, response);
        
        WaitSecs(1);
        
    end
    
    time.endExp = datestr(now);
    save([savedir filesep sID '_qCSF_' datestr(now, 'yy-mm-dd_HH-MM') '.mat'], 'qcsf', 'stim', 'display', 'sID', 'time', 'numTrials');
    qcsf = runQCSF(qcsf, 'plot experiment');
    fprintf('  sensitivity (AULCSF)  = %6.3f \n', qcsf.data.estAULCSF(numTrials));
    
    screen_clut = [linspace(0,1,256)' linspace(0,1,256)' linspace(0,1,256)'];
    Screen('LoadNormalizedGammaTable', theScreen, screen_clut);
    Screen('CloseAll');
    ListenChar(0);
    ShowCursor;
    
catch ME
    time.endExp = datestr(now);
    save([savedir filesep sID '_qCSF_' datestr(now, 'yy-mm-dd_HH-MM') '.mat'], 'qcsf', 'stim', 'display', 'sID', 'time', 'numTrials', 'ME');
    Screen('CloseAll');
    ListenChar(0);
    ShowCursor;
    rethrow(ME);
end
