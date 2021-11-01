import sys
import gzip

with gzip.open(sys.argv[1],"r") as f:
	for line in f:
		line = line.decode()
		lsplit = line.rstrip().split("\t")
		if lsplit[7]:
			line = lsplit[3] + "\t" + lsplit[7]
			print(line)
