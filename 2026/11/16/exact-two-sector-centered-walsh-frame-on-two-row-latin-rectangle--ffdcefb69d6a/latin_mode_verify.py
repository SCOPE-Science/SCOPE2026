"""Independent exact mode-energy sampler for two-row Latin rectangles."""
import itertools
from fractions import Fraction

def derangements(n):
    for p in itertools.permutations(range(n)):
        if not any(i==p[i] for i in range(n)):
            yield p

def verify(n):
    count=0
    total=[0,0]; total2=[0,0]
    for p in itertools.permutations(range(n)):
        for d in derangements(n):
            # row0 uses p, row1 uses p composed with d
            vals=[]
            for r in (0,1):
                row=p if r==0 else tuple(p[d[i]] for i in range(n))
                vals.append(sum((1 if i==0 else -1)*(1 if row[i]==0 else (-1 if row[i]==1 else 0)) for i in (0,1)))
            for z,stat in enumerate((vals[0]+vals[1], vals[0]-vals[1])):
                total[z]+=stat;total2[z]+=stat*stat
            count+=1
    for z,exp in enumerate((Fraction(n-2,(n-1)**2),Fraction(n,(n-1)**2))):
        variance=Fraction(total2[z],count)-Fraction(total[z],count)**2
        lam=variance/Fraction(8)
        assert lam==exp,(n,z,lam,exp)
    print(n,count,'mode variances',tuple(Fraction(x,count) for x in total2),'normalized eigenvalues',Fraction(n-2,(n-1)**2),Fraction(n,(n-1)**2))
for n in (2,3,4,5):verify(n)
