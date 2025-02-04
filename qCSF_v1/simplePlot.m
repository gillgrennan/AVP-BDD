%%
clear

sID = 'AM_RE_IA_24';

outputDir = ([cd filesep 'output' filesep sID]);
eyeL = dir([outputDir filesep sID '_L_*.mat']);
eyeL = load([eyeL.folder filesep eyeL.name]);
eyeR = dir([outputDir filesep sID '_R_*.mat']);
eyeR = load([eyeR.folder filesep eyeR.name]);
eyeB = dir([outputDir filesep sID '_B_*.mat']);
eyeB = load([eyeB.folder filesep eyeB.name]);


%%
figure(1); clf; hold on;

cmap = bone(5);


plotB = plot(log10(eyeB.qcsf.stimuli.frequency),eyeB.qcsf.data.estSensitivity(eyeB.qcsf.data.trial,:),...
    'o:','lineWidth',4,'MarkerSize',6, 'DisplayName', 'binocular', 'Color', cmap(1,:));
plotL = plot(log10(eyeL.qcsf.stimuli.frequency),eyeL.qcsf.data.estSensitivity(eyeL.qcsf.data.trial,:),...
    '<-','lineWidth',4,'MarkerSize',6, 'DisplayName', 'left eye', 'Color', cmap(2,:));
plotR = plot(log10(eyeR.qcsf.stimuli.frequency),eyeR.qcsf.data.estSensitivity(eyeR.qcsf.data.trial,:),...
    '>-','lineWidth',4,'MarkerSize',6, 'DisplayName', 'right eye', 'Color', cmap(3,:));


axis([log10(eyeL.qcsf.stimuli.frequency([1 end]))' -log10(eyeL.qcsf.stimuli.contrast([end 1]))'])


set(gca,'Yaxislocation','left','Xtick',log10([.5 1 2 5 10 20]),'XtickLabel',([.5 1 2 5 10 20]),'Ytick',log10([2 10 50 200 500 1000]),'Yticklabel',([2 10 50 200 500 1000]))
xlabel('spatial frequency')
ylabel('sensitivity')
set(gca,'Fontname','Arial','FontSize',18)

legend('Location','northeast')
axis square

saveas(gca, [sID '-CSF.fig'])