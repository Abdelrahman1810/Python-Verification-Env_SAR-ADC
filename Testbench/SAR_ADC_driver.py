from common_imports import *
from SAR_ADC_bfm import *

class SAR_ADC_driver(uvm_driver):

	def build_phase(self):
		self.dut = cocotb.top
		
	def start_of_simulation_phase(self):
		self.bfm = SAR_ADC_bfm()

	async def run_phase(self):
		await self.bfm.reset()
		while True:

			stim_seq_item = await self.seq_item_port.get_next_item()

			await self.drive(stim_seq_item)
			
			self.seq_item_port.item_done()

	async def drive(self, stim_seq_item):
		self.dut.rst_n.value 		= int(stim_seq_item.rst_n)
		self.dut.sample_rate.value 	= stim_seq_item.sample_rate
		self.dut.V_in.value 		= (stim_seq_item.V_in)/100000.0
		# self.dut.V_in.value 		= (stim_seq_item.V_in)
		await FallingEdge(self.dut.clk)