from common_imports import *
from SAR_ADC_seq_item_vsc import *

class SAR_ADC_monitor(uvm_monitor):

	def build_phase(self):
		self.mon_ap = uvm_analysis_port.create("mon_ap", self)
		self.dut = cocotb.top

	async def run_phase(self):
		while True:

			await RisingEdge(self.dut.clk)

			rsp_seq_item = SAR_ADC_seq_item_vsc.create("rsp_seq_item")

			rsp_seq_item.rst_n			=	self.dut.rst_n.value
			rsp_seq_item.sample_rate	=	self.dut.sample_rate.value
			rsp_seq_item.V_in			=	self.dut.V_in.value
			rsp_seq_item.D_out			=	self.dut.D_out.value
			rsp_seq_item.EOC			=	self.dut.EOC.value
			rsp_seq_item.V_target		= 	self.dut.SH.V_target.value
			
			# if self.dut.EOC.value == 1:
			# 	self.logger.info("=========================================================")
			# 	self.logger.info(f"V_target = {self.dut.SH.V_target}")
			# 	print(f"V_target = {self.dut.SH.V_target}")
			# 	self.logger.info("=========================================================")
			self.mon_ap.write(rsp_seq_item)
			self.logger.debug(f"{self.get_type_name()}: MONITORED {rsp_seq_item}")