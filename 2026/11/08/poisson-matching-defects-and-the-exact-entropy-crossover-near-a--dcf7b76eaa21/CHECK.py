"""Exact finite checks supporting the near-complete circular graph theorem."""
from fractions import Fraction as Q
from math import factorial, comb

def antipodal_defect(x,y,q):
    s=min((x-y)%1,(y-x)%1)
    return s>(1-q)/2

assertions=0
for L in (10,12,16,20,24,30,40):
    for t in range(1,L//3):
        q=Q(2*t,L)
        # On an evenly spaced circle, an open antipodal arc contains 2t-1 points.
        for x in range(L):
            neigh={y for y in range(L) if antipodal_defect(Q(x,L),Q(y,L),q)}
            assert len(neigh)==2*t-1
            assertions+=1
            # Conditional on x, the two other locations are independent.
            for y in range(L):
                count=sum(antipodal_defect(Q(x,L),Q(y,L),q)
                          and antipodal_defect(Q(x,L),Q(z,L),q) for z in range(L))
                assert count == (2*t-1 if y in neigh else 0)
                assertions+=1
for n in range(2,45):
    for m in range(n//2+1):
        expected=factorial(n)//(factorial(n-2*m)*2**m*factorial(m))
        if m==0: actual=1
        else: actual=comb(n,2*m)*factorial(2*m)//(2**m*factorial(m))
        assert actual==expected
        assertions+=1
print('exact rational and combinatorial assertions passed:',assertions)
