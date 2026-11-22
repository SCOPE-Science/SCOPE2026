"""Independent exhaustive verifier for the two opposite binary-run inputs."""
from itertools import product, combinations
from math import comb

def is_subsequence(pattern, word):
    i = 0
    for symbol in word:
        if i < len(pattern) and pattern[i] == symbol:
            i += 1
    return i == len(pattern)

def predicted(a,b,c,d):
    def branch(a,b,c,d):
        if a == 1:
            return comb(d+b-1,b)
        if d == 1:
            return comb(a+c-1,c)
        return comb(a+c-2,c-1)*comb(d+b-2,b-1)
    return branch(a,b,c,d)+branch(c,d,a,b)

def minimal(w,u,v):
    if not(is_subsequence(u,w) and is_subsequence(v,w)):
        return False
    return all(not(is_subsequence(u,w[:i]+w[i+1:]) and is_subsequence(v,w[:i]+w[i+1:])) for i in range(len(w)))

checks=0
words=0
for a,b,c,d in product(range(1,4),repeat=4):
    u='0'*a+'1'*b;v='1'*c+'0'*d
    n=a+b+c+d-1
    found=[]
    for x in product('01',repeat=n):
        w=''.join(x)
        if minimal(w,u,v):found.append(w)
    assert len(found)==predicted(a,b,c,d),(a,b,c,d,len(found),predicted(a,b,c,d))
    assert all(not minimal(''.join(x),u,v) for x in product('01',repeat=n+1)),(a,b,c,d)
    checks+=1;words+=len(found)
print('EXHAUSTIVE_OK parameter_tuples=',checks,'maximal_minimal_words=',words)
