#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Fm Recv
# Generated: Sun Apr 26 20:18:50 2020
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys
import time


class FM_RECV(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Fm Recv")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Fm Recv")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "FM_RECV")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate_ursp = samp_rate_ursp = 200000
        self.samp_rate = samp_rate = 48000
        self.gain = gain = 120
        self.fc = fc = 15000
        self.f_cut_off = f_cut_off = 15000
        self.beta = beta = 4

        ##################################################
        # Blocks
        ##################################################
        self._gain_range = Range(0, 200, 10, 120, 200)
        self._gain_win = RangeWidget(self._gain_range, self.set_gain, "Gain", "counter_slider", float)
        self.top_layout.addWidget(self._gain_win)
        self._fc_range = Range(0, 15000, 1000, 15000, 200)
        self._fc_win = RangeWidget(self._fc_range, self.set_fc, "Carrier Frequency", "counter_slider", float)
        self.top_layout.addWidget(self._fc_win)
        self._f_cut_off_range = Range(0, 15000, 1000, 15000, 200)
        self._f_cut_off_win = RangeWidget(self._f_cut_off_range, self.set_f_cut_off, "f_cut_off", "counter_slider", float)
        self.top_layout.addWidget(self._f_cut_off_win)
        self._beta_range = Range(0, 4, 1, 4, 200)
        self._beta_win = RangeWidget(self._beta_range, self.set_beta, "beta", "counter_slider", float)
        self.top_layout.addWidget(self._beta_win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("addr=192.168.10.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate_ursp)
        self.uhd_usrp_source_0.set_center_freq(1340e6, 0)
        self.uhd_usrp_source_0.set_gain(gain, 0)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_source_0.set_bandwidth(200e6, 0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=samp_rate,
                decimation=samp_rate_ursp,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"Recieved Wave Signal", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.30)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.low_pass_filter_1_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, f_cut_off, 100, firdes.WIN_HAMMING, beta))
        self.low_pass_filter_1 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, f_cut_off, 100, firdes.WIN_HAMMING, beta))
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(62.8e-3, 4, False)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink("/root/SDR_Class/Lab3/RECV_PIANO.wav", 1, samp_rate, 8)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, fc, 700e-3, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, fc, 700e-3, 0)
        self.analog_pwr_squelch_xx_0 = analog.pwr_squelch_cc(-70, 1e-4, 0, True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.blocks_complex_to_float_0, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_1, 1))    
        self.connect((self.blocks_complex_to_arg_0, 0), (self.blocks_wavfile_sink_0, 0))    
        self.connect((self.blocks_complex_to_arg_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_delay_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))    
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.blocks_complex_to_arg_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_1_0, 0))    
        self.connect((self.blocks_multiply_xx_1, 0), (self.low_pass_filter_1, 0))    
        self.connect((self.digital_costas_loop_cc_0, 0), (self.analog_pwr_squelch_xx_0, 0))    
        self.connect((self.low_pass_filter_1, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.low_pass_filter_1_0, 0), (self.blocks_float_to_complex_0, 1))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_xx_1, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.digital_costas_loop_cc_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "FM_RECV")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate_ursp(self):
        return self.samp_rate_ursp

    def set_samp_rate_ursp(self, samp_rate_ursp):
        self.samp_rate_ursp = samp_rate_ursp
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate_ursp)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate, self.f_cut_off, 100, firdes.WIN_HAMMING, self.beta))
        self.low_pass_filter_1_0.set_taps(firdes.low_pass(1, self.samp_rate, self.f_cut_off, 100, firdes.WIN_HAMMING, self.beta))
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.uhd_usrp_source_0.set_gain(self.gain, 0)
        	

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.analog_sig_source_x_0.set_frequency(self.fc)
        self.analog_sig_source_x_1.set_frequency(self.fc)

    def get_f_cut_off(self):
        return self.f_cut_off

    def set_f_cut_off(self, f_cut_off):
        self.f_cut_off = f_cut_off
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate, self.f_cut_off, 100, firdes.WIN_HAMMING, self.beta))
        self.low_pass_filter_1_0.set_taps(firdes.low_pass(1, self.samp_rate, self.f_cut_off, 100, firdes.WIN_HAMMING, self.beta))

    def get_beta(self):
        return self.beta

    def set_beta(self, beta):
        self.beta = beta
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate, self.f_cut_off, 100, firdes.WIN_HAMMING, self.beta))
        self.low_pass_filter_1_0.set_taps(firdes.low_pass(1, self.samp_rate, self.f_cut_off, 100, firdes.WIN_HAMMING, self.beta))


def main(top_block_cls=FM_RECV, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
