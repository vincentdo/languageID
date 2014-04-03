import sys
import random
from collections import namedtuple

lang = ['eng', 'deu', 'ita', 'spa', 'fra']

file_suffix = '_wikipedia_2010_100K-sentences.txt'
corpora_input = '../../data/corpora/'
test_output = '../../data/test/'
dev_output = '../../data/dev/'
train_output = '../../data/train/'

TRAIN_MAX = 30000
SAMPLE_LENGTH = 40

random.seed()

test_output = open(test_output + 'test', 'w')
dev_output = open(dev_output + 'dev', 'w')

test_files = [test_output, dev_output]

for i in xrange(len(lang)):
  input_file = open(corpora_input + lang[i] + file_suffix)
  output_file = open(train_output + lang[i] + '_train', 'w')
  for line in input_file:
    (j, sentence) = line.strip().split('\t')
    if (int(j) <= TRAIN_MAX):
      # Extracting training set
      output_file.write(sentence + '\n')
    else:
      if not output_file.closed:
        output_file.close()
      else: 
        start_bound = random.randint(0, len(sentence))
        end_bound = start_bound + random.randint(15,50)
        f = random.choice(test_files)
        f.write(str(sentence[start_bound:end_bound]) + '\n')

test_output.close()
dev_output.close()