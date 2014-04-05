import sys
import random
from collections import namedtuple

lang = ['eng', 'deu', 'ita', 'spa', 'fra']

file_suffix = '_wikipedia_2010_100K-sentences.txt'
corpora_dir = '../../data/corpora/'
test_dir = '../../data/test/'
dev_dir = '../../data/dev/'
train_dir = '../../data/train/'
solution_dir = '../../data/solution/'

TRAIN_MAX = 1000
OTHER_MAX = 4000

random.seed()

test_output = open(test_dir + 'test', 'w')
dev_output = open(dev_dir + 'dev', 'w')

test_files = [test_output, dev_output]

for i in xrange(len(lang)):
  input_file = open(corpora_dir + lang[i] + file_suffix)
  output_file = open(train_dir + lang[i] + '_train', 'w')
  for line in input_file:
    (j, sentence) = line.strip().split('\t')
    if (int(j) <= TRAIN_MAX):
      # Extracting training set
      output_file.write(sentence + '\n')
    elif (int(j) <= OTHER_MAX):
      if not output_file.closed:
        output_file.close()
      else: 
        # Extracting dev and test data
        start_bound = random.randint(0, len(sentence))
        end_bound = start_bound + random.randint(20,50)
        f = random.choice(test_files)
        f.write(lang[i] + '\t' + str(sentence[start_bound:end_bound]) + '\n')

test_output.close()
dev_output.close()

# Sanitize dev and test data to remove samples
# that are too short
test_output = open(test_dir + 'test')
clean_test_output = open(test_dir + 'clean_test', 'w')

Sample = namedtuple('Sample', 'language sentence')
test_data = []
for line in test_output:  
  if len(line) >= 20:
    # sys.stderr.write(line)
    (language, sentence) = line.strip().split('\t')
    sample = Sample(language, sentence)
    test_data.append(sample)
    clean_test_output.write(language + '\t' + sentence + '\n')

dev_output = open(dev_dir + 'dev')
clean_dev_output = open(dev_dir + 'clean_dev', 'w')

dev_data = []
for line in dev_output:  
  if len(line) >= 20:
    # sys.stderr.write(line)
    (language, sentence) = line.strip().split('\t')
    sample = Sample(language, sentence)
    dev_data.append(sample)
    clean_dev_output.write(language + '\t' + sentence + '\n')

# Create dataset for dev, testing, and their respective solutions
test_set = open(test_dir + 'test_set', 'w')
test_solution = open(solution_dir + 'test_solution', 'w')
dev_set = open(dev_dir + 'dev_set', 'w')
dev_solution = open(solution_dir + 'dev_solution', 'w')

for i in xrange(0, 4000):
  test_sample = random.choice(test_data)
  dev_sample = random.choice(dev_data)
  test_set.write(test_sample.sentence + '\n')
  test_solution.write(test_sample.language + '\n')
  dev_set.write(dev_sample.sentence + '\n')
  dev_solution.write(dev_sample.language + '\n')