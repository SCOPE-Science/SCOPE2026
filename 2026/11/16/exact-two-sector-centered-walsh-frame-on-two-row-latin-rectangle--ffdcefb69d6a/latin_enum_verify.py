"""Exact exhaustive two-row Latin rectangle covariance checks, no external data."""
from itertools import permutations
from fractions import Fraction
import math

def check(n):
    perms=list(permutations(range(n)))
    count=0
    features=[]
    # all 2xn latin rectangles, represented by two symbol permutations
    for a in perms:
        for b in perms:
            if all(a[j] != b[j] for j in range(n)):
                count+=1
                features.append((a,b))
    assert count==math.factorial(n)*sum((-1)**j*math.comb(n,j)*math.factorial(n-j) for j in range(n+1))
    # directly count conditional joint occurrences for all relative pair positions to expose all orbits
    reps=[(0,0,0),(0,0,1),(0,1,0),(0,1,1), (1,0,0),(1,0,1),(1,1,0),(1,1,1)]
    for r,j,k in reps:
        hits=sum((a[0]==0 and (a if r==0 else b)[j]==k) for a,b in features)
        p=Fraction(hits,count)
        if r==0:
            target=Fraction(1,n) if j==k==0 else (Fraction(0) if j==0 or k==0 else Fraction(1,n*(n-1)))
        else:
            target=Fraction(0) if j==k==0 else (Fraction(1,n*(n-1)) if (j==0) != (k==0) else Fraction(n-2,n*(n-1)**2))
        assert p==target,(n,(r,j,k),p,target)
    print('n',n,'N',count,'single & pair joint checks',len(reps),'expected lambda:',Fraction(4*(n-2),(n-1)**2),Fraction(4*n,(n-1)**2))
for n in range(2,6):check(n)
