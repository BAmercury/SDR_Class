%% Script to read data from GNURadio and detect the preamble

% Recall that the test message is 100 symbols and the preamble is 16
% symbols
%% Create Preamble Project (See create_message script for what was used)
% 6 bit preamble
p1 = [0 1 2 3 3 2 1 0]';
p = [p1; p1];
% Run the preamble through QPSK modulator
modulation_order = 4;
initial_phase = pi/modulation_order;
prb = pskmod(p, modulation_order, modulation_order, 'gray');

% Create a Preamble Detector object using the preamble prb
rx_prbdet = comm.PreambleDetector(prb, 'Detections', 'All');
tx_prbdet = comm.PreambleDetector(prb, 'Detections', 'All');

%% Now load the TX and RX messages
RX_file_id = fopen('data/Trial9_RX_byte.bin','rb');
RX_dat = fread(RX_file_id, 'uint8');
fclose(RX_file_id);
TX_file_id = fopen('data/Trial9_TX_byte.bin','rb');
TX_dat = fread(TX_file_id, 'uint8');
fclose(TX_file_id);
%% Try to detect the preamble index in both messages, start with RX
% Code needs to be tuned
x2 = pskmod(RX_dat,4,pi/4,'gray');
% Set Threshold
rx_prbdet.Threshold = 7.9
[rx_idx, rx_detmet] = rx_prbdet(x2);

rx_no_elements = numel(rx_idx)

% Display the 5 largest detection metrics
rx_detmetSort = sort(rx_detmet, 'descend');
rx_detmetSort(1:5)

% Display the first few RX indicies, the spacing between them should be 116
rx_idx(1)
rx_idx(2)
rx_idx(3)

%% Now for the TX
x1 = pskmod(TX_dat,4,pi/4,'gray');

% Set Threshold
tx_prbdet.Threshold = 7.9;

[tx_idx, tx_detmet] = tx_prbdet(x1);

tx_no_elements = numel(tx_idx)

% Display the 5 largest detection metrics
tx_detmetSort = sort(tx_detmet, 'descend');
tx_detmetSort(1:5)

% Display the first few TX indicies, the spacing between them should be 116
tx_idx(1)
tx_idx(2)
tx_idx(3)

%% Try some plotting


%plot(TX_dat)
%hold on;
%plot(RX_dat)


% these indicies indicate the index where the preamble ends
tx_index = 16;
tx_index2 = 132
rx_index = 248;
rx_index2 = 364;
plot(TX_dat(tx_index:tx_index2));
hold on;
plot(RX_dat(rx_index:rx_index2));
legend('TX', 'RX')
[number, ratio] = biterr(TX_dat(tx_index:tx_index2), RX_dat(rx_index:rx_index2))

