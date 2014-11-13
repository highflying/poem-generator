import random
def syllables_sentence(sentence):
	words = sentence.strip(".:;?!").replace("_", " ").replace("-", " ").split(" ")
	syllable_count = 0
	for word in words:
		syllable_count += syllables(word)
	return syllable_count
def syllables(word):
	count = 0
	vowels = "aeiouy"
	word = word.lower().strip(".:;?!")
	if word[0] in vowels:
	    count +=1
	for index in range(1,len(word)):
	    if word[index] in vowels and word[index-1] not in vowels:
	        count +=1
	if word.endswith("e"):
	    count -= 1
	if word.endswith("le"):
	    count+=1
	if count == 0:
	    count +=1
	return count
def load(file):
	ins = open(file,"r")
	line = random.choice(ins.readlines())
	ins.close()
	return line.replace("\n", " ").replace("\r", "").replace(" ", "").replace("_", "-")
def noun():
	return load("nouns")
def verb():
	return load("verbs")
def adjective():
	return load("adjectives")
def adverb():
	return load("adverbs")
def gen_sentence():
	part1 = noun().capitalize() + " " + verb()
	part2 = noun() + " are " + adjective()
	while syllables_sentence(part1) != syllables_sentence(part2):
		part1 = noun().capitalize() + " " + verb()
		part2 = noun() + " are " + adjective()
	return part1+", "+part2+".\n"
poem = "Roses are red, Violets are blue;\n"+gen_sentence()+gen_sentence()+gen_sentence()+gen_sentence()+gen_sentence()+gen_sentence()
print(poem)