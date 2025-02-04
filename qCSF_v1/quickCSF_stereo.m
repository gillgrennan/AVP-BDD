% clear all;
% close all;
% clc;
rng('shuffle');

% Quick CSF, by Kim but HEAVILY taken from Woon Ju! Thanks Woon Ju!

%% Directories
homedir = cd;
addpath([homedir filesep '/qCSF_v1']);

%% Input
sID = input('subject ID? ', 's');
sID = upper(sID);
savedir = [homedir filesep 'output' filesep sID];

if ~isfolder(savedir)
    mkdir(savedir);
end

while 1
    eye = input('(L)eft eye, (R)ight eye, or (B)inocular run? ', 's');
    switch lower(eye)
        
        case 'l'
            disp('You selected the LEFT eye')
            break
        case 'r'
            disp('You selected the RIGHT eye')
            break
        case 'b'
            disp('You selected BINOCULAR')
            break
    end
    
end

time.startExp = datestr(now);

if lower(eye) == 'b'
       %% Alignment Task
    offsetL = [0 0];
    offsetR = [0 0];
    %addpath('/home/viscog/GitHub/Nonius')
    %[offsetL, offsetR] = alignment_task('cornermatch', sID, 'eyeAdjust', 'l', 'useBgPattern', 'y', 'useJoystick', 'n');
else
    offsetL = [0 0];
    offsetR = [0 0];
end

%% Keyboard settings

KbName('UnifyKeyNames');

escapeKey = KbName('ESCAPE');
escapeKey2 = KbName('q');

leftKey = KbName('LeftArrow');
leftKey2 = KbName('4');
rightKey = KbName('RightArrow');
rightKey2 = KbName('6');

[keybIndices, keybNames] = GetKeyboardIndices;
% 
% % select the correct index
% for i = 1:length(keybNames)
%     if strcmpi('Logitech Logitech Illuminated Keyboard', keybNames{i})
%         keyboardnum = keybIndices(i);
%         break
%     end
% end

%% Stimulus and display settings

stim.center = [0,0];    % centre of the stimulus (in degrees of VA - usually set this to 0)
stim.size = [2,2];    % width/height of the stimulus prior to gaussian envelope GG: USED TO BE 15,15 -- CHANGED TO BE SMALLER ON MAC
stim.sigma = 1.5;       % gaussian envelope over the grating (in degree of visual angle)

screenRes = Screen('Rect', 0);
%screenRes(3) = screenRes(3)/2; % because the stereoscope screen is two monitors side-by-side

display.resolution = screenRes(3:4);   % [width,height] (pixels)
display.width = 15; % measure the physical width of your screen in cm; GG: CHANGED TO BE 15CM FROM 70.1 
display.dist = 136;  % in cm; measure your viewing distance
display.screen = 0; % 0 = laptop screen or main computer screen, 1 = external
display.pxPerDeg = angle2pix(display,1);
display.angPerPix = pix2angle(display,1);
display.stereomode = 4;



%% quick CSF settings
numTrials = 120;

% Set priors
priors = [75 1 2.5 .1];
% (1) peak gain
% (2) peak frequency
% (3) bandwidth (full width at half maximum - FWHM - in octaves
% (4) truncation level on the low-frequency side.

qcsf = setupQCSF;
qcsf = setupPriors(qcsf,priors);

try
    %% Load relevant stuff
    
    % Stimulus and display parameters
    load('gammaTable_example.mat', 'gammaTable');
    
    % I get a FATAL ERROR if I don't do this when I use the stereo:
    % (I don't mind too much since we're not doing intense timing here)
    Screen('Preference', 'SkipSyncTests', 1);
    
catch ME
    disp('Error in loading the stuff. Sorry. Check the very top of your script for file paths?');
    rethrow(ME);
end


%% Open the screen and prepare stuff
try
    % Uses a lower-level imaging tool to optimize stereo presentation (I think)
    PsychImaging('PrepareConfiguration');
    PsychImaging('AddTask', 'General', 'Enable11BitFrameBuffer'); 
    PsychImaging('AddTask', 'General', 'NormalizedHighresColorRange', 1);    
    PsychImaging('AddTask', 'General', 'EnablePseudoGrayOutput');
    
    % Open the screen using the imaging pipeline
    [theScreen, theScreenArea] = PsychImaging('OpenWindow', 0, 0.5, [], [], 2, [display.stereomode]);

    % Initialize the gamma table to linearize the display
    Screen('LoadNormalizedGammaTable', theScreen, gammaTable*[1 1 1]);
    
    % Generally recommended for graphics
    Screen('BlendFunction', theScreen, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    Priority(MaxPriority(theScreen)); % helps on my laptop sometimes
    
    % just for information (not important to do if you don't care)
    ifi = Screen('GetFlipInterval', theScreen);
    calculatedFrameRate = 1/ifi; %#ok<*NOPTS>
    
    % Colour settings
    gray = 0.5; % range 0-1
    background = gray;
    
    % Text settings
    text.size = 40;
    text.color = 1;
    
    % Setting the screen text size
    Screen('TextSize', theScreen, text.size);
    
    % Flip (show) the screen
    flipHandle = Screen('Flip', theScreen);
    
    % Hide cursor
    HideCursor;
    ListenChar(2);
    
catch ME
    disp('Error in opening the screen.')
    Screen('CloseAll');
    rethrow(ME);
end

%% Do the experiment

try
    
    ListenChar(2);
    %ApplyKbFilter; GG: Not sure what this does and can't find the function
    %online 
    
        beepHigh = MakeBeep(2000,0.02) * 0.1;
        beepLow = MakeBeep(1000,0.02) * 0.1;
    %% Go through trials
    for trial = 1:numTrials
        
        % Set up the parameters for the next trial
        qcsf.data.trial = trial;
        [qcsf,SF,contrast] = runQCSF(qcsf, 'pretrial');
        
        % Determine whether stim is -45 or 45 deg (or 0/90, or whatever you end up picking)
        CR = ceil(2*rand);
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
       
        % Generate the texture
        gratingTex = Screen('MakeTexture', theScreen, grating);
        texrect = Screen('Rect', gratingTex);
        switch lower(eye)
            
            case 'b'
                
                % This means they selected binocular
                Screen('SelectStereoDrawBuffer', theScreen, 0);  % 0 = left, 1 = right
                Screen('FillRect', theScreen, 0.5);
                Screen('DrawTexture', theScreen, gratingTex, [], CenterRect(texrect, [0 0 display.resolution]) + [offsetL offsetL]);
                Screen('SelectStereoDrawBuffer', theScreen, 1);  % 0 = left, 1 = right
                Screen('DrawTexture', theScreen, gratingTex, [], CenterRect(texrect, [0 0 display.resolution]) + [offsetR offsetR]);
                
            case 'l'
                
                % Present qCSF to the left eye, blank to the right eye
                Screen('SelectStereoDrawBuffer', theScreen, 0);  % 0 = left, 1 = right
                Screen('DrawTexture', theScreen, gratingTex);
                
                Screen('SelectStereoDrawBuffer', theScreen, 1);  % 0 = left, 1 = right
                Screen('FillRect', theScreen, background);
                
            case 'r'
                
                % Prsent qCSF to the right eye, blank to the left eye
                Screen('SelectStereoDrawBuffer', theScreen, 1);  % 0 = left, 1 = right
                Screen('DrawTexture', theScreen, gratingTex);
                
                Screen('SelectStereoDrawBuffer', theScreen, 0);  % 0 = left, 1 = right
                Screen('FillRect', theScreen, background);
        end
        
        
        Screen('Flip', theScreen);
        pause(0.5);
        
        responded = 0
        while responded == 0
            [secs, keyCode, deltaSecs] = KbWait();
            if any(find(keyCode,1) == [leftKey leftKey2 rightKey rightKey2 escapeKey escapeKey2])
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

    save([homedir filesep 'output' filesep sID filesep sID '_' eye '_qCSF' datestr(now, 'yy-mm-dd_HH-MM') '.mat'], 'qcsf', 'stim', 'display', 'sID', 'eye', 'time', 'numTrials');
    qcsf = runQCSF(qcsf,'plot experiment');
    fprintf('  sensitivity (AULCSF)  = %6.3f \n', qcsf.data.estAULCSF(numTrials));
    fprintf('  peak gain = %6.3f \n', 10.^qcsf.data.estCSF(numTrials,1));
    fprintf('  peak freq = %6.3f \n', 10.^qcsf.data.estCSF(numTrials,2));
    fprintf('  bandwidth = %6.3f \n', 10.^qcsf.data.estCSF(numTrials,3));
    fprintf('  truncation = %6.3f \n', 10.^qcsf.data.estCSF(numTrials,4));
    
    screen_clut = [linspace(0,1,256)' linspace(0,1,256)' linspace(0,1,256)'];
    Screen('LoadNormalizedGammaTable',theScreen,screen_clut);
    Screen('CloseAll');
    ListenChar(0);
    ShowCursor;
    
    
catch ME
    time.endExp = datestr(now);
    save([homedir filesep 'output' filesep sID filesep sID '_' eye '_qCSF' datestr(now, 'yy-mm-dd_HH-MM') '.mat'], 'qcsf', 'stim', 'display', 'sID', 'eye', 'time', 'numTrials', 'ME');
    screen_clut = [linspace(0,1,256)' linspace(0,1,256)' linspace(0,1,256)'];
    Screen('LoadNormalizedGammaTable',theScreen,screen_clut);
    Screen('CloseAll');
    ListenChar(0);
    ShowCursor;
    rethrow(ME);
    
end

