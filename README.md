# Cytoscape_heatmap
Mapping heatmaps on the KEGG pathway using Cytoscape

## Requirements:
- python3.6 
    - pandas ( pandas>=0.22.0 )
    - matplotlib ( matplotlib>=2.0.2 )
    - seaborn ( seaborn>=0.8.1)
- python3-tk (version>=3.5.1-1)

## Usage :
1. $wget http://rest.kegg.jp/get/{KEGG pathway ID}/kgml -O {KEGG pathway ID}.xml 
2. Cytoscape : File -> import -> Network -> select {KEGG pathway ID}.xml
3. Cytoscape : export csv from "Table Pannel", ##この後csvからtsvに変換する必要あり　用修正
4. $python3 Cat_sailfish.nv_cytocsv.py exported_csv.tsv analysed_data.tsv

analysed_data.tsv  

| Gene_symbol | NCBI gene ID | Naive | iTreg | nTreg | Th1 | Th2 | Th17 |
----|----|----|----|----|----|----|----
| Pzp	        | 11287	     |0.0105 | 0     | 0     | 0   | 0   | 0.057 |
| Aanat	     | 11298	     |0.3728 | 0     | 1.165 | 0.193 | 0.0891 | 0.3320 |
| Aatk	     | 11302	     |0.10661225 |	0 | 2.452 | 0.00595 | 0.0113 | 0.0185 |
| Abca1       | 11303        |6.683 | 2.184 | 3.846 | 1.760 | 1.630 | 2.203 |
......

5. $cd {exported_csv}_{analysed_data}  
   $ls *.csv | parallel --no-notice --eta -j 1 -a - 'python3 ../Cat_sailfish_cytocsv_2.py {}'
   
## Result : 
file:///media/daiya/HDCZ-UT/Cytoscape_heatmap_practice/Sailfish2Cytoscape_mmu00020/Citrate%20cycle%20(TCA%20cycle)%20%5Bmmu00020%5D.png
