"""Independent finite-size check of the joint rank/settling-depth enumerator.
All formulas are exact integers; the proof does not depend on this check.
"""
from itertools import product
from collections import Counter
from math import comb

N=9
# A polynomial in x and u represented by {(n,r): integer}.
def add(*xs):
    z=Counter()
    for p in xs:
        for k,v in p.items():z[k]+=v
    return {k:v for k,v in z.items() if v}
def neg(p):return {k:-v for k,v in p.items()}
def mul(a,b):
    z=Counter()
    for (n,r),c in a.items():
        for (m,s),d in b.items():
            if n+m<=N:z[n+m,r+s]+=c*d
    return {k:v for k,v in z.items() if v}
def geom(t):
    out={(0,0):1}; power={(0,0):1}
    for _ in range(N):
        power=mul(power,t)
        out=add(out,power)
    return out
X={(1,0):1};U={(0,1):1}; ONE={(0,0):1}
Ts=[X]
Fs=[]
for h in range(N):
    B=mul(U,X) if h==0 else mul(mul(U,X),geom(Ts[h-1]))
    Fs.append(geom(B))
    if h<N-1:
        Tprev=Ts[-1]
        Ts.append(add(X,mul(mul(mul(X,U),Tprev),geom(Tprev))))

for n in range(1,N+1):
    brute=Counter()
    for f in product(*(range(i+1) for i in range(n))):
        if any(f[i]>f[i+1] for i in range(n-1)):continue
        r=len(set(f)); d=0
        for i in range(n):
            j=i; k=0
            while f[j]!=j:
                j=f[j]; k+=1
            d=max(d,k)
        brute[r,d]+=1
    dp=Counter()
    for h in range(n):
        for r in range(1,n+1):
            v=Fs[h].get((n,r),0)-(Fs[h-1].get((n,r),0) if h else 0)
            if v:dp[r,h]=v
    assert brute==dp,(n,brute,dp)
    for r in range(1,n):
        assert brute.get((r,r),0)==comb(n+r-3,2*r-2)
        assert all(d<=r for rr,d in brute if rr==r)
    print('n=%d, maps=%d, rank-depth strata=%d, maximal-depth-column=%s OK'%(n,sum(brute.values()),len(brute),[brute.get((r,r),0) for r in range(1,n)]))
print('VERIFY_OK')
