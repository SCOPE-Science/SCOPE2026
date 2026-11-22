"""Independent exhaustive test of common centralizers in type-A 0-Hecke monoids.

Each product with a simple generator is constructed by its left or right
bubble-antisort action; a separate routine checks the descent/fixed-point
classification, and closed formula is evaluated with integer arithmetic.
"""
from itertools import permutations
from math import comb, factorial


def right_mult(w, i):
    w = list(w)
    if w[i-1] < w[i]:
        w[i-1], w[i] = w[i], w[i-1]
    return tuple(w)


def left_mult(w, i):
    w = list(w)
    loc_i = w.index(i)
    loc_next = w.index(i+1)
    if loc_i < loc_next:
        w[loc_i], w[loc_next] = w[loc_next], w[loc_i]
    return tuple(w)


def predicted(n, i):
    if n == 3:
        assert i == 1
        return 2
    m = n-3
    dd = sum(comb(m,t)**2 * factorial(m-t) for t in range(min(3,m)+1))
    ff = factorial(m)
    mixed = ((i-1)**2+(n-i-2)**2)*factorial(n-4)
    return dd,ff,mixed,dd+ff+mixed


def classify(w, i):
    n = len(w)
    inv=[0]*(n+1)
    for j,v in enumerate(w,1):
        inv[v]=j
    def kind(j):
        if w[j-1] == j and w[j] == j+1:
            return 'F'
        if w[j-1] > w[j] and inv[j] > inv[j+1]:
            return 'D'
        return None
    a,b=kind(i),kind(i+1)
    return (a+b) if a is not None and b is not None else None


def run():
    print('n  common-centralizer counts in positions i=1,...,n-2')
    for n in range(3,10):
        counts=[0]*(n-2)
        strata=[dict(DD=0,DF=0,FD=0,FF=0) for _ in counts]
        for w in permutations(range(1,n+1)):
            for i in range(1,n-1):
                direct=left_mult(w,i)==right_mult(w,i) and left_mult(w,i+1)==right_mult(w,i+1)
                code=classify(w,i)
                assert direct == (code is not None), (n,i,w,direct,code)
                if direct:
                    counts[i-1]+=1
                    strata[i-1][code]+=1
        for j,v in enumerate(counts,1):
            p=predicted(n,j)
            if n>=4:
                dd,ff,mixed,total=p
                assert v==total, (n,j,v,total)
                assert strata[j-1]['DD']==dd
                assert strata[j-1]['FF']==ff
                assert strata[j-1]['DF']+strata[j-1]['FD']==mixed
                assert strata[j-1]['FD']==(j-1)**2*factorial(n-4)
                assert strata[j-1]['DF']==(n-j-2)**2*factorial(n-4)
            else:
                assert v==p
        print(n, counts)
    print('All direct products, classifications, individual strata, and formulas agree.')

if __name__=='__main__':
    run()
