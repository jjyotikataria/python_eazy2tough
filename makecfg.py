############################################################################################
# Script to make cfg for fastqc input automatically
# Pre-requisite : R1 and R2 files should be having extension _R1.fastq.gz and _R2.fastq.gz
# Args : PID
# How to run?
# python3 makecfg.py P123 PE
# python3 makecfg.py P1234 SE
# python3 makecfg.py P12345 PE2
############################################################################################



import shlex
import os, sys, glob
import subprocess

if sys.argv[2] == "PE" :

        r1_path = glob.glob(os.getcwd()+"/*_R1.fastq.gz")
        r2_path = glob.glob(os.getcwd()+"/*_R2.fastq.gz")
        sample_list = glob.glob("*_R1.fastq.gz")
        f = open("cfg", "w")
        f.write("PID\t"+"Fastqc_Report"+"\t\t\t\n")
        f.write("EID\t"+"_"+sys.argv[1]+"\t\t\t\n")
        for i in zip(sorted(sample_list), sorted(r1_path), sorted(r2_path)):
                sample_name = i[0].split("_R1.")[0]
                f.write("PE\t"+sample_name+"\t\t"+i[1]+"\t"+i[2]+"\n")
        f.write("MAIL\tjyoti.kataria@medgenome.com\t\t\t\n")

elif sys.argv[2] == "SE" :
        r1_path = glob.glob(os.getcwd()+"/*_R1.fastq.gz")
        sample_list = glob.glob("*_R1.fastq.gz")
        f = open("cfg", "w")
        f.write("PID\t"+"Fastqc_Report_"+sys.argv[1]+"\t\t\t\n")
        f.write("EID\tqc\t\t\t\n")
        for i in zip(sorted(sample_list), sorted(r1_path)) :
                sample_name = i[0].split("_R1.")[0]
                f.write("PE\t"+sample_name+"\t\t"+i[1]+"\t"+i[1]+"\n")
        f.write("MAIL\tjyoti.kataria@medgenome.com\t\t\t\n")

elif sys.argv[2] == "PE2" :
        r1_path = glob.glob(os.getcwd()+"/*_R1_001.fastq.gz")
        r2_path = glob.glob(os.getcwd()+"/*_R2_001.fastq.gz")
        sample_list = glob.glob("*_R1_001.fastq.gz")
        f = open("cfg", "w")
        f.write("PID\t"+"Fastqc_Report_"+sys.argv[1]+"\t\t\t\n")
        f.write("EID\t" + "qc\t\t\t\n")
        for i in zip(sorted(r1_path), sorted(r2_path), sorted(sample_list)):
                sample_name = i[2].split("_R1_001.fastq.gz")[0]
                f.write("PE\t"+sample_name+"\t\t"+i[0]+"\t"+i[1]+"\n")
        f.write("MAIL\tjyoti.kataria@medgenome.com\t\t\t\n")
