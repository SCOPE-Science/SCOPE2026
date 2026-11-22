"""Independent border-position checker plus symbolic bridge crossing counts."""
from itertools import product

def computed(w):
    n=len(w)
    occurrences={}
    for i in range(n):
        for j in range(i+1,n+1):
            s=w[i:j]
            occurrences.setdefault(s,[]).append((i,j))
    def closed(s):
        if len(s)==1:return True
        for t in range(len(s)-1,0,-1):
            if s[:t]!=s[-t:]:continue
            if sum(1 for p in range(len(s)-t+1) if s[p:p+t]==s[:t])==2:return True
        return False
    cache={s:closed(s) for s in occurrences}
    return {(i,j) for pairs in occurrences.values() for i,j in pairs
            if cache[w[i:j]] and (i==0 or not cache[w[i-1:j]])
            and (j==n or not cache[w[i:j+1]])}

def analytic(a,b,k):
    period=a+b
    seq=[(r//2*period+(a if r%2 else 0), b if r%2 else a)
         for r in range(2*k)]
    intervals=[(0,k*period)]
    intervals += [(s,s+z) for s,z in seq]
    intervals += [(s+z-t,seq[r+2][0]+t)
                  for r,(s,z) in enumerate(seq[:-2]) for t in range(1,z)]
    return set(intervals)

cases=0
for a,b,k in product(range(1,5),range(1,5),range(2,5)):
    w=('0'*a+'1'*b)*k
    observed=computed(w)
    exact=analytic(a,b,k)
    assert observed==exact,(a,b,k,observed^exact)
    cases+=1
for a,b,k in product(range(1,18),range(1,18),range(3,18)):
    n=(a+b)*k
    vals=analytic(a,b,k)
    assert len(vals)==n-(a+b)+3
    assert all(sum(i<c<j for i,j in vals)<=a+b-1 for c in range(1,n))
    assert all(sum(i<m*(a+b)<j for i,j in vals)==a+b-1 for m in range(1,k))
print('BORDER_CHECK_OK cases=',cases,'independent word checks; symbolic cases=',17*17*15)
