import subprocess
import sys
import os
import pandas as pd
pwd = os.getcwd()
args = sys.argv
filename1 = args[1]#csv file from cytoscape (KEGG)
filename2 = args[2]#results of sailfish, after exclude variants // format : tsv  ##NCBI gene ID,Gene_symbol,iTreg,nTreg,Naive....


def process_run(command):
	res = subprocess.run(command, stdout=subprocess.PIPE)
	sys.stdout.buffer.write(res.stdout)

#filename1 = "KEGG_mouse_TCA.tsv.csv"
#filename2 = "sail_prac2.csv"
name1 = filename1.split('.')[0]
name2 = filename2.split('.')[0]
process_run(["mkdir","{0}_{1}".format(name1,name2)])

df1 = pd.read_csv(filename2,index_col="NCBI gene ID",sep="\t")

index_list = df1.index.values
df_list = []
f1 = open(filename1,'r')
d1 = f1.read().split("\n")

f2 = open("{0}_{1}/{0}_{1}.attr".format(name1,name2),'w')
f2.write("shared name\theat maps\n")

for i in range(len(d1)-1):
    if i > 0:
        datas = d1[i].split("\t")
        data2 = datas[2].split("|")
        data18 = datas[18]
        for k in range(len(data2)):
            data2i_split = data2[k].split(":")
            id_first = data2i_split[0].strip('"') #'"mmu' -> 'mmu'
            id_second = data2i_split[1].strip('"') #'33282"' -> '33282'
            if id_first == "mmu" and id_second in index_list:
                df_list.append(id_second)


            elif id_first == "mmu" :
                print("{0} is not found".format(data2[k]))
                df_list = []

        if len(df_list) > 0 :
            df2 = df1.loc[df_list]
            df2.to_csv("{0}_{1}/{2}.csv".format(name1,name2,data18))
            data18i = data18.split(":")
            f2.write("{0}\timage:file:{1}/{2}_{3}/{4}_{5}.png\n".format(data18,pwd,name1,name2,data18i[1],data18i[2]))
            df_list = []

f1.close()
f2.close()

#cd **csvが作られたディレクトリ**
#ls *.csv | parallel --no-notice --eta -j 1 -a - '/usr/bin/python3 ../Cat_sailfish_cytocsv_2.py {}'




