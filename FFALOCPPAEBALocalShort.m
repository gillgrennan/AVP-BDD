%%%   FFA/LOC/PPA/EBA LOCALIZER: FFALOCPPAEBALocalGray.m     %%%
%%%                                          %%%   
%%%     modified from localizers from AN & JP%%%ttttttttt
%%%                                          %%%
%%%  11/17/09: Wrote it. (JP)
%%%  2/23/11: Modified from FFALocal.m (JP)
%%%  8/4/11: Changed houses to Scenes. (JP)  
%%%  2/24/12: Modified output/bg color (DM)
%%%  6/27/12: Modified fixation at start and filename. Added EBA. General
%%%  updates.
%%%  7/20/17: Modified for grayscale images. Updated case sensitive
%%%  functions. (JP)
%%%  9/20/24: Modified for BEAM experiment at UW-CHN (JP)
%%%  01/15/25: Modified for AVP-BDD experiment at UW-CHN (GG)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% Initialize %%
clear; clc;
rand('state', sum(clock*100));
utilitypath = strcat(pwd,'\utility');
addpath(utilitypath);
datapath = strcat(pwd,'\data');
addpath(datapath);

%% Get Subject Info %%
prompt={'Subject ID', 'TR Length (in ms)', 'At Scanner? Yes=1, No=0', ...
    'Order: Order1=1, Order2=0', 'Run Number', 'Session', 'Sync pulses to ignore','Testing?'};
def={'','1000','1','1','','1','0','0'};
title='SETUP FFA/LOC/PPA/EBA LOCALIZER...';
lineNo=1;
   
answer=inputdlg(prompt,title,lineNo,def);
SubjID = char(answer(1,:));
TRtime =str2num(char(answer(2,:)));
atscanner =str2num(char(answer(3,:)));
PickCond =str2num(char(answer(4,:)));
runnumber =str2num(char(answer(5,:)));
Session = str2num(char(answer(6,:)));
sync_ignore_max = str2num(char(answer(7,:)));
testing = str2num(char(answer(8,:)));

scanstart = fix(clock);

%% Create SubjData folder if there isn't one already, then assign filenames

%% set up path to save directory %%
curpath = pwd;

dt = datetime('now');
ds = sprintf('%2d%2d%2d%2d%d',month(dt),day(dt),hour(dt),minute(dt),round(second(dt)));

% setup data directory

savepath = strcat(pwd, '\data\'); 

% check for code super-directory
data_dir = strcat(pwd, '\data');
if ~exist(data_dir, 'dir')
    mkdir(data_dir);
end

mlog(mfilename, [pwd '\data\']);

MatFileName = strcat(savepath, SubjID, 'run-', num2str(runnumber), '_task-VisCatLocalizer', '_', ds);
DataFileName = strcat(MatFileName, '.tsv');



%% PsychToolbox Setup %%
%need this for some of the os x things?
AssertOpenGL;
%choose the display screen (needed if multiple monitors attached)
% screenNumber = max(Screen('Screens'));
screenNumber = 2; %for CHN
% Suppress Splash Screen
Screen('Preference','VisualDebugLevel', 0);
KbName('UnifyKeyNames');
Screen('Preference', 'SkipSyncTests', 1);

% response key
respkey = KbName('g'); % 71 = g at CHN red/green buttons

HideCursor;
esc_key = KbName('escape'); %this key kills script during the experiment

black=BlackIndex(screenNumber); %bkgd color for the inst will be black
gray=GrayIndex(screenNumber); %bkgd color for experiment will be gray
bkgdColor = gray;
textColor = black;
w=Screen('OpenWindow', screenNumber);
ifi = Screen('GetFlipInterval', w);
slack = ifi / 2;

%get / display screen 
Screen(w,'FillRect', gray);%gray
%always writes to an offscreen buffer window � flip to see changes  made
Screen('Flip', w);
% set font; display text
Screen('TextFont',w, 'Times');
Screen('TextSize',w, 18);
%Screen('TextStyle', w, 0);
DrawFormattedText(w, 'Preloading images...', 'center', 'center', black);
Screen('Flip', w);



%% Load Stimuli %%
load adults;
load child;
load body;
load limbs;
load cars;
load instruments;
load corridors;
load houses;
load scramobjects;

%% Setup Fixation Cross %%%
fixation_dark=repmat(gray,30,30);
fixation_dark(13:16,:)=0;
fixation_dark(:,13:16)=0;

% %% Scan & Experiment Parameters %%
% TR = 2.0; 
% 
% NumBlocks = 20; %% 3 repetitions of 4 conditions
% totalOffBlocks = 12;
% 
% TRsPerBlock = 8;
% FixTRs = 3;
% StimsPerBlock = 16;
% trialDuration = 1;
% stimPresentationLength = 0.8; %0.75;
% BlockLength = TR * TRsPerBlock;
% FixLength = TR * FixTRs;
% StartFixTime = 12;
% EndFixTime = 6;
% [junk junk NumStims] = size(adults); %Grayscale
% % [junk junk junk NumStims] = size(faces);  %Color
% ITI = trialDuration - stimPresentationLength; 
% TasksPerBlock = 2;

%% Scan & Experiment Parameters %%
% Updated: 9-16-2024 (JP)
TR = 1.0; 

NumBlocks = 16; %% 3 repetitions of 4 conditions
%totalOffBlocks = 12;

TRsPerBlock = 14;
FixTRs = 4;
StimsPerBlock = 14;
trialDuration = 1;
stimPresentationLength = 0.8; %0.75;
BlockLength = TR * TRsPerBlock;
FixLength = TR * FixTRs;
StartFixTime = 10;
EndFixTime = 6;
[junk junk NumStims] = size(adults); %Grayscale
% [junk junk junk NumStims] = size(faces);  %Color
ITI = trialDuration - stimPresentationLength; 
TasksPerBlock = 2;
trig = 84; % KeyCode for trigger key at CHN


%% Condition Orders
% 1=Adults, 2=Children, 3=Bodies, 4=Limbs, 5=Cars, 6=Instruments, 7=Houses, 8=Corridors, 9=Scram-objects 
if PickCond == 1 
        CondOrder = [3, 7, 1, 9, 7, 9, 1, 3, 7, 3, 9, 1, 9, 3, 1, 7];
    else	
        CondOrder = [6, 2, 5, 1, 9, 7, 3, 8, 4, 9, 6, 2, 5, 1, 9, 7, 3, 8, 4, 9];
end	%if stimtype


%% Create matrix for trial order and Shuffle
%trialMatrix = zeros(NumStims,NumBlocks);  
temp = 1:NumStims;
AdultStimOrder = Shuffle(temp);
ChildStimOrder = Shuffle(temp);
BodyStimOrder = Shuffle(temp);
LimbStimOrder = Shuffle(temp);
CarStimOrder = Shuffle(temp);
InstrumentStimOrder = Shuffle(temp);
HouseStimOrder = Shuffle(temp);
CorridorStimOrder = Shuffle(temp);
ScrambledStimOrder = Shuffle(temp);

AdultTrial = 1;
ChildTrial = 1;
BodyTrial = 1;
LimbTrial = 1;
CarTrial = 1;
InstrumentTrial = 1;
HouseTrial = 1;
CorridorTrial = 1;
ScrambledTrial = 1;


%% Create matrix for Task and Shuffle
Matrix = zeros(StimsPerBlock,NumBlocks);  
Matrix(1:TasksPerBlock,:) = 1;
TaskMatrix = Shuffle(Matrix);

%Make sure there are no task trials back to back  (2 tasks per block
%hard-coded)
for i = 1:NumBlocks
    
    taskind = find(TaskMatrix(:,i));
    disttask = diff(taskind); 
    
    while disttask == 1 | TaskMatrix(1,i) == 1
        reshuffle = Shuffle(TaskMatrix(:,i));
        TaskMatrix(:,i) = reshuffle;       
        taskind = find(TaskMatrix(:,i));
        disttask = diff(taskind); 
    end %while  
        
end

%% Set up datafile %%

% save non-event information in json
output_info.MatlabVersion = version;
output_info.Begin = datestr(now);
output_info.SubjID = SubjID;
output_info.RunNumber = runnumber;
output_info.TR = TR;
output_info.TotalBlocks = NumBlocks;
json_filename = strcat(MatFileName, '.json');
j = jsonencode(output_info);
json_file = fopen(json_filename, 'wt');
fprintf(json_file, '%s', j);
fclose(json_file);

datafile = fopen(DataFileName,'wt');
fprintf(datafile,'%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n', ...
    'onset', 'duration', 'trial No.', 'block', ...
    'adult(1)/child(2)/body(3)/limb(4)/car(5)/instrument(6)/house(7)/corridor(8)/scrambled(9)', ...
    'trial', 'TR','stim no.', 'stimEndTime(s)', 'trialEndTime(s)', 'response', 'correct?', 'RT(ms)');

%% Show Instructions %%
inst_horzpos=50;
top_vertpos=100;
inst_vertpos=40;
inst_color=textColor;

Screen('FillRect', w, bkgdColor);
Screen('TextFont',w, 'Arial');
Screen('TextSize',w, 34);
%0=normal,1=bold,2=italic,4=underline,8=outline,32=condense,64=extend
%Screen('TextStyle', w);

DrawFormattedText(w, 'Concentrate on display.\nPush button when image repeats.', 'center', 'center', black);
Screen('Flip', w);


% wait 4 seconds before switching to fixation
WaitSecs(4);

Screen('PutImage', w, fixation_dark);
Screen('Flip', w); %show offscreen buffer that has fixation


%% Set Things Up %%
FlushEvents('keyDown');
%stimtype = FirstCond;  %Faces = 1, Object = 0
samediff = 0;
TrialCount = 1;

%% set up event list for PRT %%
masterEventList = [];
fixations = [];
fixStart = 0;
fixEnd = 0;

%% Suppress Keyboard Output to Command Window
ListenChar(2);

%% if at scanner, wait for trigger %%
sync_count = 0;
keyCodes = zeros(256,1);

fprintf('\n\n Waiting for Sync Pulse...\n\n');

if atscanner == 1
    while keyCodes(trig)==0 && sync_count <= sync_ignore_max
        keyCodes(1:256) = 0;
        [secs, keyCodes, deltaSecs] = KbStrokeWait;
        if keyCodes(trig) ~= 0
            keyCodes(1:256) = 0;
            sync_count = sync_count + 1;
            fprintf('Sync pulses received: %d\n', sync_count);
        end
    end
else KbWait;
end

keyCodes(1:256) = 0;

ExptStartTime = GetSecs;

fprintf('\n\n GOT SYNC! EXPERIMENT STARTED!\n');
%% Wait For Initial Fixation Time %%
WaitSecs(StartFixTime);

%%%%%%%%%%%%%%%%%%%%%%%
%% MAIN PROGRAM LOOP %%
%%%%%%%%%%%%%%%%%%%%%%%

for block = 1:NumBlocks
    
    blockStart = GetSecs - ExptStartTime;
    fixEnd = blockStart;
    fixations = [fixations; fixStart, fixEnd];
   
	for trial = 1:StimsPerBlock
        
		samediff = TaskMatrix(trial, block);

        %% For first stim in the block or a new stim (samediff=0) %%
		if samediff == 0
            %% Get pict from pick %%
            if CondOrder(block) == 1 %adults
                    pick = AdultStimOrder(AdultTrial);
                    %pict = faces(:, :, :, pick);  % Color
                    pict = adults(:, :, pick);  %Grayscale
                    AdultTrial = AdultTrial+1;
            elseif CondOrder(block) == 2 %children
                    pick = ChildStimOrder(ChildTrial);
                    %pict = objects(:, :, :, pick);  % Color
                    pict = child(:, :, pick);  %Grayscale
                    ChildTrial = ChildTrial+1;
            elseif CondOrder(block) == 3 %bodies	
                    pick = BodyStimOrder(BodyTrial);
                    %pict = scenes(:, :, :, pick);  % Color
                    pict = body(:, :, pick);  %Grayscale
                    BodyTrial = BodyTrial+1;
            elseif CondOrder(block) == 4 %limbs
                    pick = LimbStimOrder(LimbTrial);
                    %pict = scramobjects(:, :, :, pick);  % Color
                    pict = limbs(:, :, pick);  %Grayscale
                    LimbTrial = LimbTrial+1;  
            elseif CondOrder(block) == 5 %cars
                    pick = CarStimOrder(CarTrial);
                    %pict = scramobjects(:, :, :, pick);  % Color
                    pict = cars(:, :, pick);  %Grayscale
                    CarTrial = CarTrial+1;  
            elseif CondOrder(block) == 6 %instruments
                    pick = InstrumentStimOrder(InstrumentTrial);
                    %pict = scramobjects(:, :, :, pick);  % Color
                    pict = instruments(:, :, pick);  %Grayscale
                    InstrumentTrial = InstrumentTrial+1;  
            elseif CondOrder(block) == 7 %houses
                    pick = HouseStimOrder(HouseTrial);
                    %pict = scramobjects(:, :, :, pick);  % Color
                    pict = houses(:, :, pick);  %Grayscale
                    HouseTrial = HouseTrial+1; 
            elseif CondOrder(block) == 8 %corridors
                    pick = CorridorStimOrder(CorridorTrial);
                    %pict = scramobjects(:, :, :, pick);  % Color
                    pict = corridors(:, :, pick);  %Grayscale
                    CorridorTrial = CorridorTrial+1;  
            else    %scrambled objects
                    pick = ScrambledStimOrder(ScrambledTrial);
                    %pict = bodyparts(:, :, :, pick);  % Color
                    pict = scramobjects(:, :, pick);  %Grayscale
                    ScrambledTrial = ScrambledTrial+1;                   
            end	%if stimtype
  		end %if stim
            
        %% Copy pict to the window %%
        Screen('PutImage', w, pict);
            
        
	    %% Figure out time for Trial %%
        StimEndTime = ExptStartTime + StartFixTime + ((block-1)*(BlockLength+FixLength)) ...
            + (trial * trialDuration) - ITI - slack;
        TrialEndTime = StimEndTime + ITI;
       
        %% Setup Response Stuff %%
        accuracy = 0;
        rt=0;
        keyCodes(1:256) = 0;       
        
        %% Show Stimulus %%
        trcount= round((GetSecs-ExptStartTime)/TR);
        PresTime = Screen('Flip', w);
       
        %% Wait for Button Press %%
        while (GetSecs < StimEndTime)
          if keyCodes(respkey)==0
                [keyPressed, secs, keyCodes] = KbCheck;
          end
        end

        %% Show Blank for ITI %%
        Screen(w,'FillRect', gray);
        Screen('Flip', w);
        
        %% Wait for Button Press %%
        %while (GetSecs < StimEndTime)
        while (GetSecs < TrialEndTime)
          if keyCodes(respkey) ==0
                [keyPressed, secs, keyCodes] = KbCheck;
                rt = secs - PresTime;
          end
        end
         
        
        %% Check response %%
        if keyCodes(respkey)
            resp=1; %responded
        else
            resp=0; %didn't respond
        end
 
        %% Record Response Info %%
        accuracy =(resp==samediff);

        %% Record end of Trial time %%
        end_time_trial = GetSecs; 
        PresTime=PresTime-ExptStartTime;
        StimEndTime=StimEndTime-ExptStartTime;
        TrialEndTime=TrialEndTime-ExptStartTime;
        
        %% Record Data in Matrix %%
        ExptRecord(TrialCount,1) = TrialCount;
        ExptRecord(TrialCount,2) = block;
        ExptRecord(TrialCount,3) = CondOrder(block);
        ExptRecord(TrialCount,4) = trial;
        ExptRecord(TrialCount,5) = trcount;
        ExptRecord(TrialCount,6) = pick ;
        ExptRecord(TrialCount,7) = PresTime;
        ExptRecord(TrialCount,8) = StimEndTime;
        ExptRecord(TrialCount,9) = TrialEndTime;
        ExptRecord(TrialCount,10) = resp;
        ExptRecord(TrialCount,11) = accuracy;
        ExptRecord(TrialCount,12) = rt;
        fprintf(datafile,'%.4f\t%.4f\t%d\t%d\t%d\t%d\t%d\t%d\t%.4f\t%.4f\t%d\t%d\t%.4f\n', ...
                 PresTime, TrialEndTime - PresTime, TrialCount, block, CondOrder(block), trial, ...
                 trcount, pick, StimEndTime, TrialEndTime, resp, accuracy, rt);
        
        %% Output to Command Window %%
        TimeNow = GetSecs - ExptStartTime;
        tr_indiv_end= round((GetSecs-ExptStartTime)/TR);
        fprintf(sprintf('\nBlock: %d  Trial: %d  Stim: %i Task?: %d Response: %i Accuracy: %i TimeNow: %3.2f TR: %i',block,trial,pick,samediff,resp,accuracy,TimeNow,tr_indiv_end));
        
        
        %% Update Count of All Trials
        TrialCount = TrialCount + 1;
        
	end	%for stim		
    
    blockEnd = GetSecs - ExptStartTime
    masterEventList = [masterEventList; blockStart, blockEnd, CondOrder(block)];
    fixStart = blockEnd;
    
    %% Show Fixation Between Blocks %%
    Screen('PutImage', w, fixation_dark);
    Screen('Flip', w); %show offscreen buffer that has fixation
	%% Fixation Period Between Blocks %%
    WaitSecs(FixLength);


   
end %for block	

WaitSecs(EndFixTime);

fprintf('Total experiment time: %.4f', GetSecs - ExptStartTime);

ListenChar(0);
Screen('CloseAll');



fixEnd = GetSecs - ExptStartTime;
fixations = [fixations; fixStart, fixEnd];

%% generate prt file %%
for i = 1:length(fixations)
    masterEventList = [masterEventList; fixations(i,1), fixations(i,2), 9];
end
masterEventList = sortrows(masterEventList,1);
masterEventList(:,1:2) = floor(masterEventList(:,1:2).*1000);
% 1=Adults, 2=Children, 3=Bodies, 4=Limbs, 5=Cars, 6=Instruments, 7=Houses, 8=Corridors, 9=Scram-objects
% MakePRT(masterEventList, [MatFileName '.prt'],{'adults','children','bodies','limbs','cars','instruments', 'houses', ...
%                                                                                     'corridors', 'scrambled', 'fixation'}, ...
%                                                                                     'Combo Localizer', TRtime/1000);
clear adults;
clear child;
clear body;
clear limbs;
clear cars;
clear instruments;
clear houses;
clear corridors;
clear scramobjects;

save(MatFileName);





































