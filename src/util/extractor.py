import sys
from collections import namedtuple

lang = ['en', 'deu', 'ita', 'spa', 'fra']

file_suffix = '_wikipedia_2010_100K_sentences.txt'

TRAIN_MAX = 30000

test_output = open('test', 'w')
dev_output = open('dev', 'w')

for i in xrange(len(lang)):
	input_file = open(lang + 'file_suffix')
  output_file = open(lang + '_train', 'w')
	for line in input_file:
    (i, sentence) = line.strip().split()
    if (i <= TRAIN_MAX):
      # Extracting training set
      output_file.write(sentence + '\n')
    else
      output_file.close()




