import itertools
import os

script_dir = os.getcwd()
rel_path = "/german/german.dic"
abs_file_path = os.path.join(script_dir, rel_path)

def read_wordlist(list,length):
    wordlist=[]
    with open(list) as infile:
        for line in infile:
            if len(line.lower().strip()) <= length:
                wordlist.append(line.lower().strip())
    return  wordlist

def generate_permutations(word):
    per_list = []
    for L in range(0, len(word)+1):
      for subset in itertools.permutations(word, L):
        per_list.append(''.join(map(str, subset)))
    return per_list

wordlist = read_wordlist('german.dic',10)
wordlist += read_wordlist('austriazismen.txt',10)
wordlist += read_wordlist('helvetismen.txt',10)

per=generate_permutations('nadinedanz')

res = set(per).intersection(wordlist)

print(res)
