#!/usr/bin/env python
import sys
import csv

def writeDataTracks(fn, out=sys.stdout):
	reader = csv.reader(open(fn), delimiter=',', quotechar='"')
	head = reader.next()
	for row in reader:
		row = dict(zip(head, row))
		#print row
		row['ChrArm'] = row['ChrArm'].replace('L', 'S').replace('S', '')
		if row['ChrArm'][-1] not in ('A', 'B'):
			continue
		if row['cM'] != 'NA':
			row_out = ['chr%s' % row['ChrArm'], row['cM'], row['cM'], row['f_mut']]
			out.write('\t'.join(row_out) + '\n')
def writeBands(fn, out=sys.stdout):
	reader = csv.reader(open(fn), delimiter=',', quotechar='"')
	head = reader.next()
	color = 'gneg'
	for band in sorted(set([(row[1], row[2]) for row in reader])):
		if band[0][1] not in ('A', 'B'):
			continue
		label = '%s_%s' % (band[0][0], band[1])
		row_out = ['band', 'chr%s' % band[0], label, label, band[1], band[1], color]
		if color == 'gneg':
			color = 'gpos50'
		else:
			color = 'gneg'

		out.write('\t'.join(row_out) + '\n')

def main():
	with open(sys.argv[1] + '.dataTrack', 'wb') as out:
		writeDataTracks(sys.argv[1], out=out)
	with open(sys.argv[2] + '.bands', 'wb') as out:
		writeBands(sys.argv[2], out=out)


	pass

if __name__ == '__main__': main()
