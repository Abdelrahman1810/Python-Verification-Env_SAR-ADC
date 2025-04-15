from common_imports import *

@vsc.randobj
class SAR_ADC_seq_item_vsc(uvm_sequence_item):
    def __init__(self, name="sar_adc_seq_item"):
        super().__init__(name)
        # SystemVerilog input: rst_n (active-low reset)
        self.rst_n = vsc.rand_bit_t(1)

        # V_in in SV is 'real', but pyvsc doesn't support float directly.
        # We'll scale it by 1000 to make it an int in [100, 15999] (i.e., 0.1 to <16.0)
        self.V_in = vsc.rand_uint32_t()
        
        # Not randomizing sample_rate as per your request
        self.sample_rate = 0  # Default, could be configured later outside of randomization

        
        self.D_out  = 0
        self.EOC   = 0
        self.V_target = 0.0

    # Constraint for rst_n: asserted (0) 3% of the time, deasserted (1) 97%
    @vsc.constraint
    def rst_distribution(self):
        vsc.dist(self.rst_n, [vsc.weight(1, 97), vsc.weight(0, 3)])

    # Constrain V_in to range 0.1 to <16.0 by scaling it (100 → 15999)
    @vsc.constraint
    def v_in_range(self):
        # self.V_in.inside(vsc.rangelist(vsc.rng(10000, 1600000)))  # 0.1V to <16.0V
        self.V_in.inside(vsc.rangelist(vsc.rng(10000, 1600000)))  # 0.1V to <16.0V

    def __str__(self):
        return (f"\nName: {self.get_full_name()} \
                \nrst_n:  {self.rst_n} \
                \nV_in:   {self.V_in} V \
                \nsample_rate: {self.sample_rate}")

    def reset(self):
        self.rst_n = 0
        self.V_in = 0.0
        self.sample_rate = 0

    def mode(self, a):
        self.sample_rate = a
        
# print("start")
# item = SAR_ADC_seq_item_vsc()
# for _ in range(100):
#     item.randomize()
#     print(item.rst_n, item.V_in/100000.0, item.sample_rate)
##########################################################

