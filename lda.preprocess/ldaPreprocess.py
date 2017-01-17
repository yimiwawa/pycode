
file_path = "D:\IdeaProjects\spark-test\lda-train.dat"
documents = [line.strip().split(" ") for line in open(file_path)]

dict = []
for doc in documents:
    dict += doc
dict = list(set(dict))

dict_num = len(dict)
w = open("D:\IdeaProjects\spark-test\lda-train-tf-vector.dat","w")
for doc in documents:
    vec = [0 for i in xrange(dict_num)]
    for term in doc:
        ind = dict.index(term)
        vec[ind] += 1
    vec = [str(i) for i in vec]
    w.write(' '.join(vec))
    w.write("\n")