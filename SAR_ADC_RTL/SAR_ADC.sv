`timescale 1ns/1fs

// `ifdef QUESTA
// `endif
	import mgc_rnm_pkg::*;


module SAR_ADC #(
	parameter real 	V_SCALE 	= 16.0,
	parameter 			NUM_BITS	= 4
) (
	input logic                   clk,
	input logic                   rst_n,
    input logic   [1:0]           sample_rate,
    input real                    V_in,
    
	output logic   [NUM_BITS-1:0]  D_out,
    output logic                   EOC
);

	wreal4state V1_CMP, V2_CMP;
	logic CMP_out;

	// For feedback (Input to DAC)
	logic [NUM_BITS-1:0] D_out_internal;
	assign D_out = D_out_internal;

	// Digital Blocks
	// Interface Connections
	SAR_Controller_if 												CTRLif 	(.clk(clk));
	SAR_if 						#(.NUM_BITS(NUM_BITS))	SARif 	(.clk(clk));

	// CTRL Block Inputs
	assign CTRLif.rst_n = rst_n;
	assign CTRLif.sample_rate = sample_rate;

	// SAR Block Inputs
	assign SARif.rst_n = rst_n;
	assign SARif.sample_sig = CTRLif.sample_sig;
	assign SARif.comparator_out = CMP.cmp_out;
	
	// ADC Outputs
	assign D_out_internal = SARif.digital_signal;
	assign EOC 			= SARif.valid;

	// Digital Design Blocks
	SAR_Controller 		CTRL 		(.intf(CTRLif));
	SAR 							SAR0 		(.intf(SARif));

	// Analog (SV-RNM) Blocks

	sample_n_hold 												SH 	(	.clk(CTRLif.sample_sig),
																						.Vin(V_in), 					.V_target(V1_CMP));
	comparator 														CMP (	.clk(clk),
																							.V1(V1_CMP), 					.V2(V2_CMP),
																							.cmp_out(CMP_out));

	DAC 					#(.V_SCALE(V_SCALE), .NUM_BITS(NUM_BITS))
																				D2A (	.D_in(D_out_internal), 	.A_out(V2_CMP));

endmodule : SAR_ADC