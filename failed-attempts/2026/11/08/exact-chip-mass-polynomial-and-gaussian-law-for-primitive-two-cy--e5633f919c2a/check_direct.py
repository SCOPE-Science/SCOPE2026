from itertools import product
from math import comb

def chip_next(xs):
    n=len(xs); fire=[int(v>=2) for v in xs]
    return tuple(xs[i]-2*fire[i]+fire[(i-1)%n]+fire[(i+1)%n] for i in range(n))
def formula(n):
    coeff={}
    for r in range(n//2+1):
        if (r-n)%2: continue
        m=n*comb(n-r,r)//(n-r)
        for j in range(n-2*r+1):
            v=n+r+j
            coeff[v]=coeff.get(v,0)+2*m*comb(n-2*r,j)
    return {k:v for k,v in sorted(coeff.items()) if v}

tot=0
for n in range(3,10):
    counts={}
    for c in product(range(4),repeat=n):
        d=chip_next(c)
        if d!=c and chip_next(d)==c:
            counts[sum(c)]=counts.get(sum(c),0)+1
        tot+=1
    expected=formula(n)
    assert counts==expected,(n,counts,expected)
    print('n',n,'states_tested',4**n,'primitive2',sum(counts.values()),'nonzero_mass',min(counts),max(counts),'PASS')
print('TOTAL_STATES_TESTED',tot,'DIRECT_CHECK_PASS')
