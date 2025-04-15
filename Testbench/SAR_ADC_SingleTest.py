from common_imports import *
from SAR_ADC_env import *
from SAR_ADC_sequence import *
from SAR_ADC_bfm import *

@pyuvm.test()
class SAR_ADC_base_test(uvm_test):
	def build_phase(self):
		vsc.vsc_solvefail_debug(1)
		self.env = SAR_ADC_env.create("env", self)

	def end_of_elaboration_phase(self):
		self.seq1 = SAR_ADC_Mode1_sequence.create("seq1")
		self.seq2 = SAR_ADC_Mode2_sequence.create("seq2")
		self.seq3 = SAR_ADC_Mode3_sequence.create("seq3")
		self.seq4 = SAR_ADC_Mode4_sequence.create("seq4")


	def start_of_simulation_phase(self):
		self.bfm = SAR_ADC_bfm()

	async def run_phase(self):
		self.raise_objection()

		# Clock generation
		await self.bfm.generate_clock()

		# Starting the sequence
		self.logger.info(f"{self.get_type_name()}, Starting sequence 1 , {self.seq1.get_type_name()}")
		await self.seq1.start(self.env.agt.sqr)
		self.logger.info(f"{self.get_type_name()}, Starting sequence 2 , {self.seq2.get_type_name()}")
		await self.seq2.start(self.env.agt.sqr)
		self.logger.info(f"{self.get_type_name()}, Starting sequence 3 , {self.seq3.get_type_name()}")
		await self.seq3.start(self.env.agt.sqr)
		self.logger.info(f"{self.get_type_name()}, Starting sequence 4 , {self.seq4.get_type_name()}")
		await self.seq4.start(self.env.agt.sqr)
		self.logger.info(f"{self.get_type_name()}, Finished sequence, {self.seq4.get_type_name()}")

		self.drop_objection()

	def final_phase(self):
		uvm_factory().print(0)
		self.logger.info("----------------------------------------------------------------------")
		self.logger.info(f"End of {self.get_type_name()}")
		self.logger.info("----------------------------------------------------------------------")
