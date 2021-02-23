with open('first.txt','r') as firstfile, open('second.txt','a') as secondfile: 

	for line in firstfile: 
			
			# write content to second file 
			secondfile.write(line)