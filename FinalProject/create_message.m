%% Script to create test message with preamble
% https://www.mathworks.com/help/comm/ref/comm.preambledetector-system-object.html
% Create a preamble

% 6 bit preamble
p1 = [0 1 2 3 3 2 1 0]';
p = [p1; p1]; % Length of preamble is 16
% Run the preamble through QPSK modulator
modulation_order = 4;
initial_phase = pi/modulation_order;
prb = pskmod(p, modulation_order, modulation_order, 'gray');

% Create a Preamble Detector using the preamble prb
prbdet = comm.PreambleDetector(prb)

% Generate a sequence of random symbols

% First sequence represents the last 20 symbols from a previous packet
% Second sequence represents the symbols from a current packet
d1 = randi([0 3],20,1);
d2 = randi([0 3],100,1);

% Now we modulate the two sequences using QPSK
x1 = pskmod(d1,4,pi/4,'gray');
x2 = pskmod(d2,4,pi/4,'gray');

% Create a sequence of modulated symbols consisting of the remanent of a
% previous packet, the preamble, and then the current packet.
y = [x1; prb; x2];

% Let's add some Gaussian White noise
z = awgn(y, 10);
scatterplot(z)
% Determine the preamble index and the detection metric
[idx, detmet] = prbdet(z);

% Get the number of elements in idx
no_elements = numel(idx)
% Because the number of elements is greater than one, we may need to
% increase our detection metric threshold

% Display the 5 largest detection metrics
detmetSort = sort(detmet, 'descend');
detmetSort(1:5);

% Increase the threshold and determine the preamble index from the message
prbdet.Threshold = 15;
idx = prbdet(z) % Should be 36
% 36: Sum of the preamble length is 16, remaining samples in the previous
% packet were 20, so this indicates the preamble was successfully detected

%%
% Save the preamble and second message as a binary file
fileID = fopen('data_source_matlab.bin', 'w');
fwrite(fileID, [p; d2], 'uint8');
fclose(fileID);