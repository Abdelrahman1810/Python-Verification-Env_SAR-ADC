from common_imports import *
from shared_var import *
from SAR_ADC_seq_item_vsc import *

class SAR_ADC_base_sequence(uvm_sequence, uvm_report_object):
    
    def seq_print(msg: str):
        uvm_root().logger.info(msg)

    def __init__(self, name="SAR_ADC_base_sequence"):
        super().__init__(name)
    
    async def body(self):
        raise UVMNotImplemented  


# # # # # # # # # # # # # # 
# #  SAR_ADC Test Seqs  # #
# # # # # # # # # # # # # #

class SAR_ADC_reset_sequence(SAR_ADC_base_sequence):

    async def body(self):
        for _ in range(RESET_LOOP):
            item = SAR_ADC_seq_item_vsc.create("item")
            await self.start_item(item)
            item.reset()
            await self.finish_item(item)

class SAR_ADC_Mode1_sequence(SAR_ADC_base_sequence):

    async def body(self):
        for _ in range(LOOP_MODE1):
            item = SAR_ADC_seq_item_vsc.create("item")
            await self.start_item(item)
            item.randomize()
            item.mode(0)
            await self.finish_item(item)

class SAR_ADC_Mode2_sequence(SAR_ADC_base_sequence):

    async def body(self):
        for _ in range(LOOP_MODE2):
            item = SAR_ADC_seq_item_vsc.create("item")
            await self.start_item(item)
            item.randomize()
            item.mode(1)
            await self.finish_item(item)

class SAR_ADC_Mode3_sequence(SAR_ADC_base_sequence):

    async def body(self):
        for _ in range(LOOP_MODE3):
            item = SAR_ADC_seq_item_vsc.create("item")
            await self.start_item(item)
            item.randomize()
            item.mode(2)
            await self.finish_item(item)

class SAR_ADC_Mode4_sequence(SAR_ADC_base_sequence):

    async def body(self):
        for _ in range(LOOP_MODE4):
            item = SAR_ADC_seq_item_vsc.create("item")
            await self.start_item(item)
            item.randomize()
            item.mode(3)
            await self.finish_item(item)
