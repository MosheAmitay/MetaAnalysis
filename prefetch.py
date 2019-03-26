import subprocess,os

for line in open("mazaltov.txt"):
#    subprocess.call("/data/home/mamitay/NGS/convertSRA_Fastq/sratoolkit.2.9.1-1-ubuntu64/bin/prefetch "+str(line.split()[-1]))
    command= "/data/home/mamitay/NGS/convertSRA_Fastq/sratoolkit.2.9.1-1-ubuntu64/bin/prefetch "+str(line.split()[-1])
    os.system(command)


