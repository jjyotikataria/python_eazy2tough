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
