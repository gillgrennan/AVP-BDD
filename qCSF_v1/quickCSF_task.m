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
stim.size = [20,20];
stim.sigma = 4;

% quick CSF settings
numTrials = 12;
priors = [75 1 2.5 .1];
qcsf = setupQCSF;
qcsf = setupPriors(qcsf, priors);

displayParameters % execute .m file common to all the experiments -- FROM BEAM EXPERIMENTS

display.resolution = display.screenResolution;
display.width = display.screenWidth;
display.dist = display.viewDist;
display.screen = 0;
display.pxPerDeg = angle2pix(display,1);
display.angPerPix = pix2angle(display,1);
display.stereomode = 0;

% Fixation cross parameters
fixCrossSize = 10; % Length of fixation cross arms
fixCrossColor = [1 1 1]; % White color


try
    % Load relevant stuff
    %load('gammaTable_example.mat', 'gammaTable');
    Screen('Preference', 'SkipSyncTests', 1);

    % Open the screen
    PsychImaging('PrepareConfiguration');
    PsychImaging('AddTask', 'FinalFormatting', 'DisplayColorCorrection', 'SimpleGamma');
    PsychImaging('AddTask', 'General', 'Enable11BitFrameBuffer');
    PsychImaging('AddTask', 'General', 'NormalizedHighresColorRange', 1);
    PsychImaging('AddTask', 'General', 'EnablePseudoGrayOutput');
    screenNumber = 0;

    %[theScreen, theScreenArea] = PsychImaging('OpenWindow', 0, 0.5, [], [], 2, display.stereomode);
    [theScreen, theScreenArea] = PsychImaging('OpenWindow', screenNumber, .5); % Open a new window with a gray background

    %Screen('LoadNormalizedGammaTable', theScreen, gammaTable * [1 1 1]);
    PsychColorCorrection('SetEncodingGamma', theScreen, 1/display.gamma);

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
    
    %% Practice section
    % Begin Practice Section
    Screen('FillRect', theScreen, background);
    DrawFormattedText(theScreen, 'Practice: Respond what direction the lines are facing (L or R)\n\nPress any key to start.', 'center', 'center', text.color);
    Screen('Flip', theScreen);
    KbWait([], 2);

    numPracticeTrials = 10;
    for trial = 1:numPracticeTrials
        % Randomly choose a spatial frequency for practice
        SF = randi([1, 10]) * 0.5;  % Random SF between 0.5 and 5.0
        contrast = 0.5; 

        CR = ceil(2 * rand);
        if CR == 1
            orient = 45;
        else
            orient = -45;
        end

        % Display fixation cross
        Screen('FillRect', theScreen, background);
        Screen('DrawLine', theScreen, fixCrossColor, theScreenArea(3)/2 - fixCrossSize, theScreenArea(4)/2, ...
            theScreenArea(3)/2 + fixCrossSize, theScreenArea(4)/2, 2);
        Screen('DrawLine', theScreen, fixCrossColor, theScreenArea(3)/2, theScreenArea(4)/2 - fixCrossSize, ...
            theScreenArea(3)/2, theScreenArea(4)/2 + fixCrossSize, 2);
        Screen('Flip', theScreen);
        WaitSecs(0.5);

        % spatial coordinates
        [x, y] = meshgrid(linspace(-stim.size(1)/2, stim.size(1)/2, angle2pix(display, stim.size(1))), ...
            linspace(-stim.size(2)/2, stim.size(2)/2, angle2pix(display, stim.size(2))));
        r = sqrt(x.^2 + y.^2);

        ramp = cos(orient * pi / 180) * x + sin(orient * pi / 180) * y;

        % Make the Gaussian window for fading
        Gauss = exp(-(r.^2) / (2 * stim.sigma^2));

        % Make circular mask (1 inside the circle, 0 outside)
        circleMask = r <= stim.size(1)/2;
        circleMask = double(circleMask);

        % Combine grating with Gaussian window and circular mask
        grating = sin(2 * pi * ramp * SF) .* Gauss .* circleMask * 0.5;
        grating = grating / 2 + 0.5;

        % Apply Gaussian texture on top for smooth fading
        fadeSigma = stim.size(1) / 4;
        GaussianTexture = exp(-(r.^2) / (2 * fadeSigma^2));
        grating = grating .* GaussianTexture + gray * (1 - GaussianTexture);

        % Create and draw the texture
        gratingTex = Screen('MakeTexture', theScreen, grating);
        Screen('DrawTexture', theScreen, gratingTex, [], CenterRect(Screen('Rect', gratingTex), theScreenArea));

        % Flip the screen to show the Gabor patch
        Screen('Flip', theScreen);
        WaitSecs(0.2); % Present Gabor for 200 ms

        Screen('FillRect', theScreen, .5);
        DrawFormattedText(theScreen, 'L or R?', 'center', 'center', [1 1 1]);
        Screen('Flip', theScreen);

        responded = 0;
        while responded == 0
            [secs, keyCode, deltaSecs] = KbWait();
            if any(find(keyCode, 1) == [leftKey leftKey2 rightKey rightKey2 escapeKey escapeKey2])
                responded = 1;
            end
        end

        if any(find(keyCode,1) == [escapeKey escapeKey2])
            break;
        end

        Screen('FillRect', theScreen, background);
        Screen('Flip', theScreen);
        WaitSecs(0.5);
    end

    % Prompt after practice section
    Screen('FillRect', theScreen, background);
    DrawFormattedText(theScreen, 'Are you ready to begin the actual experiment?\n\nPress any key to continue.', 'center', 'center', text.color);
    Screen('Flip', theScreen);
    KbWait([], 2);

    %% Do the experiment
    for trial = 1:numTrials
        qcsf.data.trial = trial;
        [qcsf, SF, contrast] = runQCSF(qcsf, 'pretrial');

        CR = ceil(2 * rand);
        if CR == 1
            orient = 45; % in degress
        else
            orient = -45;
        end
        % Display fixation cross
        Screen('FillRect', theScreen, background);
        Screen('DrawLine', theScreen, fixCrossColor, theScreenArea(3)/2 - fixCrossSize, theScreenArea(4)/2, ...
            theScreenArea(3)/2 + fixCrossSize, theScreenArea(4)/2, 2);
        Screen('DrawLine', theScreen, fixCrossColor, theScreenArea(3)/2, theScreenArea(4)/2 - fixCrossSize, ...
            theScreenArea(3)/2, theScreenArea(4)/2 + fixCrossSize, 2);
        Screen('Flip', theScreen);
        WaitSecs(0.5); % Show fixation cross for 500 ms

        % spatial coordinates
        [x, y] = meshgrid(linspace(-stim.size(1)/2, stim.size(1)/2, angle2pix(display, stim.size(1))), ...
            linspace(-stim.size(2)/2, stim.size(2)/2, angle2pix(display, stim.size(2))));
        r = sqrt(x.^2 + y.^2); % Radial distance from the center

        % ramp for sine wave
        ramp = cos(orient * pi / 180) * x + sin(orient * pi / 180) * y;

        % Make the Gaussian window for fading
        Gauss = exp(-(r.^2) / (2 * stim.sigma^2));

        % Make circular mask (1 inside the circle, 0 outside)
        circleMask = r <= stim.size(1)/2;
        circleMask = double(circleMask);

        % Combine grating with Gaussian window and circular mask
        grating = sin(2 * pi * ramp * SF) .* Gauss .* circleMask * contrast;
        grating = grating / 2 + 0.5;

        % Apply Gaussian texture on top to ensure smooth fading into the background
        fadeSigma = stim.size(1) / 4; % Adjust for smoother fading
        GaussianTexture = exp(-(r.^2) / (2 * fadeSigma^2));
        grating = grating .* GaussianTexture + gray * (1 - GaussianTexture);

        % Create and draw the texture
        gratingTex = Screen('MakeTexture', theScreen, grating);
        Screen('DrawTexture', theScreen, gratingTex, [], CenterRect(Screen('Rect', gratingTex), theScreenArea));

        % Flip the screen to show the Gabor patch
        Screen('Flip', theScreen);
        WaitSecs(0.5); %Present gabor for 500ms

        Screen('FillRect',theScreen,.5);
        DrawFormattedText(theScreen, 'L or R?', 'center', 'center', [1 1 1]);
        Screen('Flip',theScreen);

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
                %Snd('Play',beepHigh,44100);
            else
                response = 0;
                %Snd('Play',beepLow,44100);
            end
        elseif any(find(keyCode,1) == [leftKey leftKey2])
            if CR == 2
                response = 1;
                %Snd('Play',beepHigh,44100);
            else
                response = 0;
                %Snd('Play',beepLow,44100);
            end
        elseif any(find(keyCode,1) == [escapeKey escapeKey2])
            break;
        end


        % record and update
        Screen('FillRect', theScreen, background);
        Screen('Flip', theScreen);
        qcsf.data.history(trial,:) = [trial SF contrast response]; % updating the experimental history
        qcsf = runQCSF(qcsf, 'posttrial', SF, contrast, response);

        WaitSecs(0.5); %500 ms fixation
    end

    time.endExp = datestr(now);
    save([savedir filesep sID '_qCSF_' datestr(now, 'yy-mm-dd_HH-MM') '.mat'], 'qcsf', 'stim', 'display', 'sID', 'time', 'numTrials');
    qcsf = runQCSF(qcsf, 'plot experiment');
    fprintf('  sensitivity (AULCSF)  = %6.3f \n', qcsf.data.estAULCSF(numTrials));

    screen_clut = [linspace(0,1,256)' linspace(0,1,256)' linspace(0,1,256)'];
    Screen('LoadNormalizedGammaTable', theScreen, (0:255)'*ones(1,3)./255,2);
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