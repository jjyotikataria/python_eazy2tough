# python3 /home/jyoti.k/bs_metrics_tsv.py file_to_parse
from openpyxl import Workbook
import os
import sys
import re
import pandas as pd

#with open(sys.argv[1],"r") as file:
#       file_data = file.read()
        #print(my_file.read())
df = pd.read_csv(sys.argv[1], header = None, sep ="\t")
#df[0]
#print(df[0])
new = df[(df[0] == "TOTAL_PF_READS (count)") | (df[0] == "PCT_ALIGNED_READS (%)") | (df[0] == "PCT_CHIMERIC_READS (%)") | (df[0] == "MEDIAN_INSERT_SIZE (count)" ) | (df[0] == "PCT_EXON_250X (%)") | (df[0] == "COVERAGE_MAD (count)") | (df[0] == "MEDIAN_BIN_COUNT_CNV_TARGET (count)") | (df[0] == "USABLE_MSI_SITES (count)") | (df[0] == "PCT_PF_UQ_READS (%)") | (df[0] == "PCT_READ_ENRICHMENT (%)") | (df[0] == "MEAN_TARGET_COVERAGE (count)") | (df[0] == "PCT_TARGET_250X (%)") | (df[0] == "PCT_TARGET_0.4X_MEAN (%)") | (df[0] == "PCT_EXON_100X (%)")]
header = df.iloc[[19]]
#new.set_index(header, inplace = True)

new.drop_duplicates(inplace = True, keep = "last")
new.sort_values([0], ascending = False, inplace = True)
final = pd.concat([header,new], axis =0)
#print(new)
#print(final)

final.to_excel("Pid_ESR1_Mutation.xlsx", sheet_name="BaseSpace Stats",index = False, header=False)  ## Deleted both column names and index names from the file


#Input:
 TruSight Tumor 170	
For Research Use Only. Not for use in diagnostic procedures.	
	
[Analysis Details]	
Report Date	12-01-2021
Report Time	12:43:36
Pipeline Version	2.0.1
	
[Run Metrics]	
Metric (UOM)	Value
NA	
	
[Sample Status]	
	20297379
COMPLETED_ALL_STEPS	TRUE
FAILED_STEPS	NA
STEPS_NOT_EXECUTED	NA
	
[DNA Library QC Metrics for Small Variant Calling]	
Metric (UOM)	20297379
PCT_CHIMERIC_READS (%)	0
MEDIAN_INSERT_SIZE (count)	167
PCT_EXON_250X (%)	96.3
	
[DNA Library QC Metrics for Copy Number Variant Calling]	
Metric (UOM)	20297379
PCT_CHIMERIC_READS (%)	0
COVERAGE_MAD (count)	0.15
MEDIAN_BIN_COUNT_CNV_TARGET (count)	13.3
	
[DNA Library QC Metrics for MSI]	
Metric (UOM)	20297379
USABLE_MSI_SITES (count)	83
	
[DNA Expanded Metrics]	
Metric (UOM)	20297379
TOTAL_PF_READS (count)	124639794
PCT_PF_UQ_READS (%)	15
PCT_READ_ENRICHMENT (%)	87.7
MEAN_TARGET_COVERAGE (count)	1552.4
PCT_TARGET_250X (%)	95
PCT_TARGET_0.4X_MEAN (%)	89.8
PCT_EXON_100X (%)	97.5
PCT_ALIGNED_READS (%)	99.8
   
#Output         


Metric (UOM)	20297379
COVERAGE_MAD (count)	0.15
MEAN_TARGET_COVERAGE (count)	1552.4
MEDIAN_BIN_COUNT_CNV_TARGET (count)	13.3
MEDIAN_INSERT_SIZE (count)	167
PCT_ALIGNED_READS (%)	99.8
PCT_CHIMERIC_READS (%)	0.0
PCT_EXON_100X (%)	97.5
PCT_EXON_250X (%)	96.3
PCT_PF_UQ_READS (%)	15.0
PCT_READ_ENRICHMENT (%)	87.7
PCT_TARGET_0.4X_MEAN (%)	89.8
PCT_TARGET_250X (%)	95.0
TOTAL_PF_READS (count)	124639794
USABLE_MSI_SITES (count)	83









