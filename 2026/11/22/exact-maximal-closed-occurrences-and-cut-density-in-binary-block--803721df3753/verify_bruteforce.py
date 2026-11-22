"""Independent direct exhaustive enumeration of maximal closed occurrences."""
from itertools import product

def is_closed(f):
    if len(f) == 1:
        return True
    for t in range(1, len(f)):
        b = f[:t]
        if f[-t:] != b:
            continue
        occurrences = sum(f[i:i+t] == b for i in range(len(f)-t+1))
        if occurrences == 2:
            return True
    return False

def actual(w):
    n=len(w)
    return {(i,j) for i in range(n) for j in range(i+1,n+1)
            if is_closed(w[i:j])
            and (i==0 or not is_closed(w[i-1:j]))
            and (j==n or not is_closed(w[i:j+1]))}

def predicted(a,b,k):
    p=a+b
    ans={(0,k*p)}
    for r in range(2*k):
        start=r//2*p+(a if r%2 else 0)
        ell=b if r%2 else a
        ans.add((start,start+ell))
        if r+2<2*k:
            for t in range(1,ell):
                ans.add((start+ell-t,start+p+t))
    return ans

cases=0
for a,b,k in product(range(1,6),range(1,6),range(2,6)):
    w=('0'*a+'1'*b)*k
    if len(w)>40:
        continue
    A=actual(w);P=predicted(a,b,k)
    assert A==P,(a,b,k,sorted(A-P),sorted(P-A))
    assert len(A)==(k-1)*(a+b)+3,(a,b,k)
    counts=[sum(i<c<j for i,j in A) for c in range(1,len(w))]
    assert max(counts)==a+b-1,(a,b,k,counts)
    for m in range(1,k):
        assert counts[m*(a+b)-1]==a+b-1,(a,b,k,m)
    cases+=1
print('BRUTEFORCE_OK cases=',cases,'range a,b <=5, 2<=k<=5, word length<=40')
