import sys, argparse


def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--first', required=True, action='store', help='First')
	parser.add_argument('-l', '--last', required=True, action='store', help='Last')
	parser.add_argument('-o', '--outputfile', required=True, action='store', help='Output file')
	my_args = parser.parse_args()
	return my_args


def letra_dni(dni):
	letras="TRWAGMYFPDXBNJZSQVHLCKEO"
	valor = dni%23
	return letras[valor]


def main():
	args = get_args()
	first = args.first
	last  = args.last
	outfile = args.outputfile
	dni_arr = []
	init_range = 0
	for i in range(int(first),int(last)+1):
		dni_arr.append(format(i, '08d')+letra_dni(i))
	with open(outfile, 'w') as f:
		for item in dni_arr:
	       		f.write("%s\n" % item)


if __name__ == "__main__":
    main()