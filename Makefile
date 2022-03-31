NUMFILE = 1
CC= python3
PROBLEM = hitori$(NUMFILE).txt
LOGIC = hitori$(NUMFILE).lp
SOLUTION = solution$(NUMFILE).txt

encode: 
	$(CC) encode.py $(PROBLEM) $(LOGIC)

decode: 
	$(CC) decode.py $(SOLUTION) hitoriKB.lp $(LOGIC)

solve:
	$(CC) encode.py $(PROBLEM) $(LOGIC)
	$(CC) decode.py $(SOLUTION) hitoriKB.lp $(LOGIC)

clean:
	rm -rf merge.lp $(LOGIC) $(SOLUTION) 
