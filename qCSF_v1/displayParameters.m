
display.viewDist = 57; %120; 
display.screenWidth = 54.5; %40.5;%69.84; 
%display.screenSize = [54.5 30.3]; %[40.5 28.8]; %w/h, cm's
display.screenRefreshRate = 120;%60;
display.gamma = 2.17; %2.0;%1.56;%1.85; 
display.screenResolution = [1920 1080]; %[1024 768];% [800 600];

size_1degree = 2 * display.viewDist * tan(pi/360);
ppd = round(display.screenResolution(1) / display.screenWidth * size_1degree);
