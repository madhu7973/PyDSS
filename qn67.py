# from collections import Counter
  
# data_list = ['eyes','nose','ears','mouth','ears']
  
# split() returns list of all the words in the string
# split_it = data_set.split()
  
# Pass the split_it list to instance of Counter class.
# Counter = Counter(data_list)
  
# most_common() produces k frequently encountered
# input values and their respective counts.
# most_occur = Counter.most_common()
  
# print(most_occur)

from collections import Counter
  
data_set = ['eyes','nose','ears','mouth','ears']
  
# split() returns list of all the words in the string
# split_it = data_set.split()
  
# Pass the split_it list to instance of Counter class.
Counter = Counter(data_set)
  
# most_common() produces k frequently encountered
# input values and theirrespective counts.
most_occur = Counter.most_common(1)
  
print(most_occur)
