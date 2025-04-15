# SAR_ADC Signals Waveforms
add wave -position insertpoint  \
sim:/SAR_ADC/*

.vcop Action toggleleafnames

run -all

# Generate a TXT Coverage Report
vcover report ../Coverage_Reports/Exported_by_PyVSC/sar_adc_coverage.ucdb -details -annotate -all -output ../Coverage_Reports/Exported_by_PyVSC/coverage_report_TXT.txt

# Generate an HTML Coverage Report
vcover report -html -output ../Coverage_Reports/Exported_by_PyVSC/coverage_report_HTML -details -annotate ../Coverage_Reports/Exported_by_PyVSC/sar_adc_coverage.ucdb

quit