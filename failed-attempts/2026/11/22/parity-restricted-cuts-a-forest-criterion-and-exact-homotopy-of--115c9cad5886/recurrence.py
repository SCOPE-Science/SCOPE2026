"""Independent labeled-component recurrence for parity-constrained cut faces."""
from functools import lru_cache
from math import comb
from verify import polynomial

@lru_cache(None)
def count(n, even_only):
    if n==0:return (1,)
    out=[0]*(n+1)
    for s in range(1,n+1):
        if even_only and s%2:continue
        trees=1 if s==1 else s**(s-2)
        ways=comb(n-1,s-1)*trees
        rest=count(n-s,even_only)
        for k,c in enumerate(rest):out[k+s-1]+=ways*c
    return tuple(out)

if __name__=='__main__':
    for n in [4,5,6,8,10]:
        a=count(n,False)
        b=count(n,True)
        f=[a[i]-b[i] for i in range(n+1)]
        assert f==polynomial(n)
        beta=sum((-1)**i*x for i,x in enumerate(f))
        print('n',n,'f',f,'top_Betti',beta)
