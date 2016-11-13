import os
import re
import csv
import shutil
import datetime

excludeFormat = ['.+\.part$','.+\.crdownload$']
rootDir = os.path.dirname(os.path.abspath(__file__))

def logDate():
	return '['+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'] '

log = open(rootDir+'/autofileaway.log', 'a')
with open(rootDir+'/autofileaway.rules.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for rows in spamreader:
		if len(rows) < 3:
			continue
			
		srcFolder = rows[0]
		srcFormat = rows[1]
		dstFolder = rows[2]

		# go thru files
		for f in os.listdir(srcFolder):
			exclude = False
			for ef in excludeFormat:
				if re.search(ef, f):
					print f, 'match exclude rule', ef
					exclude = True
					continue
			
			if not exclude and re.search(srcFormat, f):
				if len(rows) > 3:
					dstFormat = rows[3]
					print f, 'match', srcFormat, '->', dstFormat
					dstFileName = re.sub(srcFormat, dstFormat, f)
				else:
					print f, 'match', srcFormat
					dstFileName = f
				
				srcFull = srcFolder+'/'+f
				dstFull = dstFolder+'/'+dstFileName
				
				if os.path.isdir(srcFull):
					print srcFull, 'is a folder, skipping'
					continue

				print srcFull, 'renamed', dstFull
				
				if os.path.exists(dstFull):	
					log.write(logDate()+'Already exists\n')
					log.write(logDate()+dstFull+'\n\n')
					continue
				
				if not os.path.exists(dstFolder):	
					os.mkdir(dstFolder)
				
				shutil.move(srcFull, dstFull)
				log.write(logDate()+srcFull+'\n')
				log.write(logDate()+dstFull+'\n\n')

log.close()

