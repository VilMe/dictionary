# put your code here.

import re
from collections import Counter
import sys

def word_count(filename):
	file = open(filename,"r")

	words = []


	for line in file:
		line = line.rstrip()
		line = re.sub(r'[^\w\s]','',line)
		line_list = line.split(" ")
		for word in line_list:
			words.append(word)

	# dict_2 = {}

	# for word in words:
	# 	dict_2[word.lower()] = dict_2.get(word.lower(), 0) + 1
	cnt = Counter()
	for word in words:
		cnt[word] += 1

	cnt_key = sorted(cnt)

	print(cnt_key)

	for key in cnt_key:
		print("{} {}".format(key,cnt[key]))


word_count(sys.argv[1])