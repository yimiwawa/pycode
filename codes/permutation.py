__author__ = 'xinhua'

def permutation(a, k, m):
    if k == m:
        print a[0:(m+1)]
    else:
        for j in range(k, m+1):
            a[j], a[k] = a[k], a[j]
            permutation(a, k + 1, m)
            a[j], a[k] = a[k], a[j]

a = list("abc")
permutation(a, 0, 3)