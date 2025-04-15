from common_imports import *
logger = logging.getLogger("coroutines")
logging.basicConfig(level=logging.NOTSET)
logger.setLevel(logging.INFO)

class SAR_ADC_bfm(metaclass=utility_classes.Singleton):
	def __init__(self):
		self.dut = cocotb.top
		
	async def generate_clock(self):
		c = Clock(cocotb.top.clk, 5, 'ns')
		await cocotb.start(c.start())

	async def reset(self):
		self.dut.rst_n.value  		= 0        
		self.dut.sample_rate.value  = 0
		self.dut.V_in.value    		= 0.10
		await FallingEdge(self.dut.clk)   	   
		self.dut.rst_n.value  		= 1        

	async def prepare_data(self, item):
		self.dut.PWDATA.value   = item.PWDATA
		self.dut.PWRITE.value   = int(item.PWRITE)
		self.dut.PADDR.value    = item.PADDR
		await RisingEdge(self.dut.clk)
