# About this project 
This is the official code implementation for `Building a reference Transcriptome for *Juniperus squamata* (Cupressaceae) based on Single-molecule real-time sequencing`.  
We wrote the python script to carry out the GO annotation.

# How to use the code
## Required files:
File 1: idmappping.tb.gz  
File 2: BLAST alignment result (`NR_blast_result.tab` below) 
## Run  
Step 1: `python 1_get_nr_go.py idmapping.tb.gz >  Nr_go.list`  
Step 2: `python 2_get_gene_nr_id.py NR_blast_result.tab> Res_Nr.id`  
Step 3: `python 3_get_annotation.py Nr_go.list Res_Nr.id`  
**The new file *js.go.annotation* created by the script is the GO annotation results**

# Q&A  
If you have any question about this project, please not hesitate to contact the corresponding author at: `maokangshan@163.com` 