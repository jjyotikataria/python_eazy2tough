## Finding correlation between two arrays with unequal rows but same no. of columns
## Example
## S.No.	gene	 | sample_1	sample_1_3_5_UN-1	sample_1_3_5_UN-2	sample_2_4_6_IN-0	sample_2_4_6_IN-1	sample_2_4_6_IN-2			S.No.	gene	sample_1_3_5_UN-0	sample_1_3_5_UN-1	sample_1_3_5_UN-2	sample_2_4_6_IN-0	sample_2_4_6_IN-1	sample_2_4_6_IN-2
## 1	RP11-532F6.3	| 2.36963	1.16141	9.64204	373.661	39.0196	41.3678			1	IFNA5	0.0370669	0	0.103379	27.0557	4.58319	2.61305
## 2	RP11-202G18.1	| 0	1.55249	4.05267	19.6194	89.2114	13.0774			2	IFNA14	0	0.0342008	1.59663	267.141	20.4919	15.9262
## 3	RP11-44K6.4	7.62856	14.8251	147.758	1463.71	1293.82	844.67			3	IFNW1	0.0347554	0.0161221	0.412091	42.4463	5.62014	5.01917





for i in range(lines.shape[0]):
    for j in range(lines2.shape[0]):
        results[i,j] = np.corrcoef(lines[i],lines2[j])[0,1]
        
        
