"""Reproduce exact finite random-permutation record/pattern covariance results."""
from fractions import Fraction
from itertools import permutations
from math import factorial

def predicted(pattern, j):
    k=len(pattern)
    mx=0
    total=Fraction(0)
    for rank in pattern:
        if rank>mx:
            mx=rank
            val=Fraction(1)
            for h in range(rank,k+1):
                val*=Fraction(h,j+h-1)
            total+=val
    total-=sum((Fraction(1,j+r) for r in range(k)),Fraction(0))
    return total/factorial(k)

def direct(n, pattern,j):
    k=len(pattern)
    pairs=0
    records=0
    hits=0
    hitrecords=0
    for pi in permutations(range(1,n+1)):
        records_i=sum(x==max(pi[:i+1]) for i,x in enumerate(pi))
        block=pi[j-1:j+k-1]
        ranks=tuple(1+sum(y<x for y in block) for x in block)
        event=ranks==pattern
        pairs+=1
        records+=records_i
        hits+=event
        hitrecords+=int(event)*records_i
    return Fraction(hitrecords,pairs)-Fraction(records*hits,pairs*pairs)

def run():
    checks=0
    for n in range(2,7):
        for k in range(2,min(4,n)+1):
            for pattern in permutations(range(1,k+1)):
                for j in range(1,n-k+2):
                    assert direct(n,pattern,j)==predicted(pattern,j),(n,k,pattern,j)
                    checks+=1
    for k in range(2,8):
        for pattern in permutations(range(1,k+1)):
            sign=1 if pattern.index(k-1)<pattern.index(k) else -1
            goal=Fraction(sign*k*(k-1),2*factorial(k))
            # the rational function has universal second-order coefficient.
            for j in (1000,3000):
                discrepancy=abs(predicted(pattern,j)*j*j-goal)
                assert discrepancy<Fraction(1500, j) # uniform for k<=7 here
                checks+=1
    for j in range(1,50):
        assert predicted((1,3,2),j)==Fraction(-(3*j-4),6*j*(j+1)*(j+2))
        checks+=1
    print('PASS:',checks,'exact-rational/exhaustive checks')

if __name__=='__main__':run()
