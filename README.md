# Cytoscape_heatmap
mapping Heatmaps on the KEGG pathway using Cytoscape


1. $wget http://rest.kegg.jp/get/{KEGG pathway ID}/kgml -O {KEGG pathway ID}.xml 
2. Cytoscape : File -> import -> Network -> select {KEGG pathway ID}.xml
3. Cytoscape : export csv from "Table Pannel", ##この後csvからtsvに変換する必要あり　用修正
4. $python3 Cat_sailfish.nv_cytocsv.py analysed_data.tsv exported_csv.tsv
   analysed_data.tsv 
   Gene_symbol	NCBI gene ID	Naive	iTreg	nTreg	Th1	Th2	Th17
Pzp	11287	0.01053564	0	0	0	0	0.057099685
Aanat	11298	0.3728	0	1.1653215	0.19301675	0.08917725	0.332045725
Aatk	11302	0.10661225	0	2.4529935497	0.00595155	0.011312495	0.01857358
Abca1	11303	6.683085	2.1842385	3.8461315	1.760885	1.630601591	2.203619
Abca4	11304	2.13384915	0	1.12282915	3.03684	3.04433	6.655490915
Abca2	11305	65.1747395	89.58350064	115.017919605	48.257814	46.250851	87.337856
Abcb7	11306	17.495405	4.25466	7.309245	13.72085	8.931265	17.4682465

   
