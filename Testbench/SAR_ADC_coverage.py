from common_imports import *
from SAR_ADC_seq_item_vsc import *

@vsc.covergroup
class SARADCCoverGroup(object):
    def __init__(self):
        self.with_sample(
            rst_n=vsc.bit_t(1),
            sample_rate=vsc.bit_t(2),
            EOC=vsc.bit_t(1),
            V_in=vsc.bit_t(22),
            D_out=vsc.bit_t(4)
        )


        self.cp_V_in = vsc.coverpoint(self.V_in, bins={
            "V_in_range": vsc.bin_array( [], [0, 3], [4, 7], [8, 11], [12, 15])
        })
        
        # Reset state coverage
        self.cp_preset = vsc.coverpoint(self.rst_n, bins=dict(
            reset_active=vsc.bin(0),   # Never hit
            reset_inactive=vsc.bin(1)  # Always hit
        ))
        
        # mode selected coverage
        self.cp_psample_rate = vsc.coverpoint(self.sample_rate, bins=dict(
            mod1=vsc.bin(0),
            mod2=vsc.bin(1),
            mod3=vsc.bin(2),
            mod4=vsc.bin(3)
        ))

        # EOC coverage
        self.cp_pEOC = vsc.coverpoint(self.EOC, bins=dict(
            taken=vsc.bin(1),
        ))

        # D_out coverage
        self.cp_pD_out = vsc.coverpoint(self.D_out, bins={
            # taken=vsc.bin(1),
            "D_out_range": vsc.bin_array( [], [0, 15])
        })

        # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # # ----------- Start Cross Coverage ------------ # #
        # # # # # # # # # # # # # # # # # # # # # # # # # # #

        self.cross_EOC_D_out        = vsc.cross([self.cp_pEOC, self.cp_pD_out])
        self.cross_EOC_V_in         = vsc.cross([self.cp_pEOC, self.cp_V_in])        
        
        # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # # ----------- Finish Cross Coverage ----------- # #
        # # # # # # # # # # # # # # # # # # # # # # # # # # #
        

class SAR_ADC_coverage(uvm_component):
    def build_phase(self):
        self.cov_fifo = uvm_tlm_analysis_fifo("cov_fifo", self)
        self.cov_get_port = uvm_get_port("cov_get_port", self)
        self.cov_export = self.cov_fifo.analysis_export
        self.cg = SARADCCoverGroup()

    def connect_phase(self):
        self.cov_get_port.connect(self.cov_fifo.get_export)

    async def run_phase(self):
        while True:
            try:
                item = await self.cov_get_port.get()
                self.logger.info(f"Coverage received item: {item}")
                self.cg.sample(
                    item.rst_n,
                    item.sample_rate,
                    item.EOC,
                    item.V_in,
                    item.D_out
                )
                self.logger.debug(f"{self.get_type_name()}: SAMPLED {item}")
                self.logger.debug(f"Instance Coverage = {self.cg.get_inst_coverage()}")
            except Exception as e:
                pass

    def report_phase(self):
        self.logger.info("cg total coverage=%f" % (self.cg.get_coverage()))
        vsc.report_coverage(details=False)
        vsc.write_coverage_db(filename="../Coverage_Reports/Exported_by_PyVSC/sar_adc_coverage.xml",  fmt='xml',      libucis=None)
        vsc.write_coverage_db(filename="../Coverage_Reports/Exported_by_PyVSC/sar_adc_coverage.ucdb", fmt='libucis',  libucis="/home/salby/mentor/questa/questasim/linux_x86_64/libucis.so")