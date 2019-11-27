

def Sort(content, *sort):
  """
   the *sort means that it can accept multiple parameters.
  This functionality helps you create variable automatically using pyhton dictionaries.
    you can increment or change the values as you like.
  """
    sorts = 0
    num = 0
    indexs = []
    sorting_algorithms = []
    for i in range(len(sort)): # Automatically create the variables base on the number of sorting algorithms added.
        if sorts != len(sort):
            indexs.append(num)
            sorts+=1
        sorting_algorithms.append('sort_%s' %sorts)
    algorithm = dict(zip(sorting_algorithms, indexs))
    a = [k for (k, v) in algorithm.items() if v == 0]
    ins = 0
    urls_d = {}
    for url in algorithm:
        if url == a[ins]:
            algorithm[url] += 1
        ins+=1
    print(algorithm)
