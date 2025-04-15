from common_imports import *
from SAR_ADC_agent import *
from SAR_ADC_coverage import *

class SAR_ADC_env(uvm_env):

	def build_phase(self):
		self.agt = SAR_ADC_agent.create("agt", self)
		self.cvg = SAR_ADC_coverage.create("cvg", self)

	def connect_phase(self):
		self.agt.agt_ap.connect(self.cvg.cov_export)
		ConfigDB().set(None, "*", "SQR", self.agt.sqr)