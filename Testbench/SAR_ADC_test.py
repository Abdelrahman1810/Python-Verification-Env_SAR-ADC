from common_imports import *
from SAR_ADC_env import *
from SAR_ADC_sequence import *
from SAR_ADC_bfm import *

class SAR_ADC_base_test(uvm_test):
	def build_phase(self):
		vsc.vsc_solvefail_debug(1)
		self.env = SAR_ADC_env.create("env", self)

	def end_of_elaboration_phase(self):
		self.seq = SAR_ADC_base_sequence.create("seq")

	def start_of_simulation_phase(self):
		self.bfm = SAR_ADC_bfm()

	async def run_phase(self):
		self.raise_objection()

		# Clock generation
		await self.bfm.generate_clock()

		# Starting the sequence
		self.logger.info(f"{self.get_type_name()}, Starting sequence, {self.seq.get_type_name()}")
		await self.seq.start(self.env.agt.sqr)
		self.logger.info(f"{self.get_type_name()}, Finished sequence, {self.seq.get_type_name()}")

		self.drop_objection()

	def final_phase(self):
		uvm_factory().print(0)
		self.logger.info("----------------------------------------------------------------------")
		self.logger.info(f"End of {self.get_type_name()}")
		self.logger.info("----------------------------------------------------------------------")

@pyuvm.test()
class SAR_ADC_Mode1_test(SAR_ADC_base_test):

	def build_phase(self):
		uvm_factory().set_type_override_by_type(SAR_ADC_base_sequence, SAR_ADC_Mode1_sequence)
		super().build_phase()

@pyuvm.test()
class SAR_ADC_Mode2_test(SAR_ADC_base_test):
	
	def build_phase(self):
		uvm_factory().set_type_override_by_type(SAR_ADC_base_sequence, SAR_ADC_Mode2_sequence)
		super().build_phase()

@pyuvm.test()
class SAR_ADC_Mode3_test(SAR_ADC_base_test):

	def build_phase(self):
		uvm_factory().set_type_override_by_type(SAR_ADC_base_sequence, SAR_ADC_Mode3_sequence)
		super().build_phase()

@pyuvm.test()
class SAR_ADC_Mode4_test(SAR_ADC_base_test):
	
	def build_phase(self):
		uvm_factory().set_type_override_by_type(SAR_ADC_base_sequence, SAR_ADC_Mode4_sequence)
		super().build_phase()
