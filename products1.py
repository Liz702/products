def open_file(filename,products):
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,价格' in line:
				continue
			name, price=line.strip().split(',')
			products.append([name, price])
		print(products)
def input_file(products):
	while True:
		name = input('请输入商品名称： ')
		if name == 'q':
			break
		price = input('请输入商品价格： ')
		products.append([name, price])
	print(products)
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('商品,价格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')
def main():
	products = []
	filename = 'products.csv'
	import os
	if os.path.isfile(filename):
		open_file(filename, products)
	else:
		print('找不到文件')
	input_file(products)
	write_file(filename, products)
main()

