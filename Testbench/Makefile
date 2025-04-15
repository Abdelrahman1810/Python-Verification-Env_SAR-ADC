# Makefile

# Force GUI mode and export variables
GUI = 1
WAVES = 1
SIM ?= questa
TOPLEVEL_LANG ?= verilog

# RTL Files 
VERILOG_SOURCES += ../SAR_ADC_RTL/DAC.sv  ../SAR_ADC_RTL/SAR.sv  ../SAR_ADC_RTL/SAR_ADC.sv  ../SAR_ADC_RTL/SAR_Controller.sv  ../SAR_ADC_RTL/SAR_Controller_if.sv  ../SAR_ADC_RTL/SAR_if.sv  ../SAR_ADC_RTL/comparator.sv  ../SAR_ADC_RTL/sample_n_hold.sv  ../SAR_ADC_RTL/sampler_gm.sv  ../SAR_ADC_RTL/sampler_gm_if.sv
# VERILOG_SOURCES += SAR_ADC_SVA.sv SVA_bind.sv

# Top-level and module
TOPLEVEL = SAR_ADC

# MODULE is the basename of the Python test file
#	# to run Single Test
# MODULE = SAR_ADC_SingleTest
#	# to run Mutli Test
MODULE = SAR_ADC_MultiTest

# Compilation arguments
VLOG_ARGS += -mfcu -cuname -timescale=1ns/1fs

# Use setup.tcl for waveform configuration
SIM_ARGS += -do setup.tcl

# Include Cocotb's Makefile AFTER variable exports
include $(shell cocotb-config --makefiles)/Makefile.sim

# Clean target
.PHONY: clean
clean::
	rm -rf __pycache__ modelsim.ini transcript vsim.wlf *.ucdb *.txt *.xml
	# rm -rf ../Coverage_Reports/Exported_by_PyVSC/*
	clear

cover:
	clear
	open transcript
	open ../Coverage_Reports/Exported_by_PyVSC/coverage_report_HTML/index.html
	open ../Coverage_Reports/Exported_by_PyVSC/coverage_report_TXT.txt
# PyUCIS-Viewer target
.PHONY: pyucis
pyucis::
	pyucis-viewer ../Coverage_Reports/Exported_by_PyVSC/sar_adc_coverage.xml