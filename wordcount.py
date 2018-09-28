# put your code here.

def word_count(filename):
	file = open(filename,"r")

	words = []


	for line in file:
		line = line.rstrip()
		line_list = line.split(" ")
		for word in line_list:
			words.append(word)

	dict_2 = {}
	
	for word in words:
		dict_2[word] = dict_2.get(word, 0) + 1

	for i, j in dict_2.items():
		print("{} {}".format(i,j))


word_count("twain.txt")