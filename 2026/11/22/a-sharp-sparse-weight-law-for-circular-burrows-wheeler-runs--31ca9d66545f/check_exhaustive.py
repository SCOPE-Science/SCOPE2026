"""Independent exhaustive cyclic-rotation check for the sparse BWT theorem."""
from itertools import combinations
from math import comb, factorial

def bwt(word):
    n = len(word)
    rotations = [(word[i:] + word[:i], word[(i-1)%n]) for i in range(n)]
    rotations.sort(key=lambda t:t[0])
    return ''.join(t[1] for t in rotations)

def runs(word):
    return 1+sum(word[i]!=word[i-1] for i in range(1,len(word)))

def restricted_partitions(s,k):
    if s<0:return 0
    f=[0]*(s+1);f[0]=1
    for part in range(1,k+1):
        for m in range(part,s+1):f[m]+=f[m-part]
    return f[s]

cases=0; marked=0
for k in range(1,6):
    maximum=21 if k<=4 else 17
    for n in range(k+1,maximum+1):
        num=0
        for places in combinations(range(n),k):
            w=''.join('1' if j in places else '0' for j in range(n))
            g=[(places[(i+1)%k]-places[i]-1)%n for i in range(k)]
            certified=(min(g)>=1 and all(abs(x-y)>=2 for i,x in enumerate(g) for y in g[i+1:]))
            output=bwt(w)
            assert output.count('1')==k
            assert runs(output)<=2*k
            if certified:
                assert runs(output)==2*k
                num+=1;marked+=1
            cases+=1
        exact=n*factorial(k-1)*restricted_partitions(n-k*(k+1),k)
        assert num==exact,(n,k,num,exact)
print('EXHAUSTIVE_OK cases=%d certified=%d' % (cases,marked))
