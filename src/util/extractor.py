import sys
import random
from collections import namedtuple

lang = ['en', 'deu', 'ita', 'spa', 'fra']

file_suffix = '_wikipedia_2010_100K_sentences.txt'

TRAIN_MAX = 30000

random.seed()

test_output = open('test', 'w')
dev_output = open('dev', 'w')

test_files = [test_output, dev_output]

for i in xrange(len(lang)):
	input_file = open(lang + 'file_suffix')
  output_file = open(lang + '_train', 'w')
	for line in input_file:
    (i, sentence) = line.strip().split()
    if (i <= TRAIN_MAX):
      # Extracting training set
      output_file.write(sentence + '\n')
    else:
      if not out_file.closed:
        output_file.close()
      else: 
        start_bound = random.randint(0, len(line)-1)
        end_bound = random.randint(0, len(line)-1)
        f = random.choice(test_files)
        f.write(str(sentence[start_bound:end_bound]))

test_output.close()
dev_output.close()






