"""Independent direct fixed-weight k-mer multiset verifier."""
from itertools import combinations
from collections import defaultdict, Counter

def empirical(n,k):
    d=defaultdict(list)
    for a,b in combinations(range(n),2):
        w=''.join('1' if j in (a,b) else '0' for j in range(n))
        spectrum=tuple(sorted(Counter(w[t:t+k] for t in range(n-k+1)).items()))
        d[spectrum].append((a,b))
    return [tuple(sorted(g)) for g in d.values() if len(g)>1]

def prediction(n,k):
    r=n-k+1
    c=k-r-1
    if k<=r: raise ValueError('requires k > (n+1)/2')
    m=r-c
    return [tuple((a,a+r) for a in range(c,r))] if m>=2 else []

cases=0
for n in range(5,57):
    for k in range((n+1)//2+1,n+1):
        got=empirical(n,k)
        exp=prediction(n,k)
        assert sorted(got)==sorted(exp),(n,k,got,exp)
        cases+=1
print(f'PASS: {cases} complete fixed-weight spectrum partitions over n=5..56 and all k>(n+1)/2')
for n in range(5,35):
    first=next(k for k in range(1,n+1) if not empirical(n,k))
    assert first == (2*n+1)//3+1,(n,first)
print('PASS: sharp first-injective read length for all n=5..34')
