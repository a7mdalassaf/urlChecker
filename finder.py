#!/usr/bin/python3
import urllib.request
import sys 
import time 

startTime = time.time()

# lines = tuple(open(sys.argv[1]))
path = tuple(open(sys.argv[2]))
lines = [line.rstrip('\n') for line in open(sys.argv[1])]

counter= 0 

for x in range(len(lines[:])): 
	for p in range(len(path[:])):
		try: 
			urls = lines[x]+path[p]
			r = urllib.request.urlopen(urls)
			print(r.getcode(), 'OK')
			print(urls)
			counter+=1 
		except Exception as e:
			pass
print ('Time: ', time.time()-startTime)
print('URLs: ', counter)