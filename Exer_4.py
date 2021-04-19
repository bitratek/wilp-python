# 4. Given an array which may contain duplicates, print all elements
# and their frequencies

Array = ['sudhir', 1, 3, 'sudhir', 'babu', 'babu', 'bitra', 'bitra', 'sudhir']
hist = dict()
for element in Array:
    hist[element] = hist.get(element,0) + 1

for key in hist:
    print(key,' ', hist[key])
