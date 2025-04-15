from common_imports import *
from SAR_ADC_driver import *
from SAR_ADC_monitor import *

class SAR_ADC_agent(uvm_agent):

	def build_phase(self):
		self.sqr = uvm_sequencer("sqr", self)
		self.drv = SAR_ADC_driver.create("drv", self)
		self.mon = SAR_ADC_monitor.create("mon", self)
		self.agt_ap = uvm_analysis_port.create("agt_ap", self)

	def connect_phase(self):
		self.drv.seq_item_port.connect(self.sqr.seq_item_export)
		self.mon.mon_ap.connect(self.agt_ap)