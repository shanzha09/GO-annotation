import sys 
go_id = open(sys.argv[1],"r") 
trinity_id = open(sys.argv[2], "r")  

swiss_go = {} 
for line in go_id:
     swiss_go[line.rstrip().split('\t')[0]] = line.rstrip().split('\t')[1]

trinity_swiss = {} 
for line in trinity_id:
     print(line.rstrip().split('\t'))
     trinity_swiss[line.rstrip().split('\t')[0]] = line.rstrip().split('\t')[1]  

#print(swiss_go)
#print(trinity_swiss)
with open("js.go.annotation","w") as out:
     for key, value in trinity_swiss.items():
         if value in  swiss_go:
             string = key + '\t' + swiss_go[value] + '\n'
             print(string)
             out.write(string)
