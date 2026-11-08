"""Exact finite-cycle halo calculations by direct bitset enumeration.
This program checks finite cases; the accompanying mathematical proof covers all n.
Run: python3 verify.py
"""
from fractions import Fraction
from math import ceil

def predicted_halo(n, k, alpha):
    # strict threshold: largest integer strictly below k/alpha
    return min(n, (k*alpha.denominator-1)//alpha.numerator)

def direct_halo(n, mask, alpha):
    p,q=alpha.numerator,alpha.denominator
    result=0
    for j in range(n):
        hits=0
        good=False
        for length in range(1,4*n+1):
            hits += (mask >> ((j+length-1)%n)) & 1
            if hits*q>p*length:
                good=True
                break
        result += good
    return result

cases=0
for n in range(2,11):
    breakpoints=sorted({Fraction(p,q) for q in range(2,n+1)
                        for p in range(1,q)})
    points=[Fraction(0),*breakpoints,Fraction(1)]
    levels=sorted(set(breakpoints)|{(a+b)/2 for a,b in zip(points,points[1:])})
    for alpha in levels:
        actual=[0]*(n+1)
        for mask in range(1,1<<n):
            k=mask.bit_count()
            h=direct_halo(n,mask,alpha)
            assert h<=predicted_halo(n,k,alpha), (n,alpha,mask,h,k)
            actual[k]=max(actual[k],h)
        for k in range(1,n+1):
            p=predicted_halo(n,k,alpha)
            # Blocks attain every fixed-cardinality upper bound.
            assert direct_halo(n,(1<<k)-1,alpha)==p,(n,k,alpha)
            assert actual[k]==p,(n,k,alpha)
        cases += 1
    crit=Fraction(n-1,n)
    assert max(Fraction(predicted_halo(n,k,crit),k)
               for k in range(1,n+1))==1
    below=(Fraction(n-2,n-1)+crit)/2
    assert max(Fraction(predicted_halo(n,k,below),k)
               for k in range(1,n+1))==Fraction(n,n-1)

alpha=Fraction(3,5)
n=10
best=max((Fraction(predicted_halo(n,k,alpha),k),k,predicted_halo(n,k,alpha))
         for k in range(1,n+1))
assert best==(Fraction(8,5),5,8)
for alpha in (Fraction(1,3),Fraction(3,5),Fraction(7,11)):
    for n in (100,1000,10000):
        k=int(alpha*n)-1
        if k>=1:
            c=max(Fraction(predicted_halo(n,j,alpha),j)
                  for j in range(1,n+1))
            assert Fraction(1,alpha)-Fraction(1,k)<=c<=Fraction(1,alpha)
print('VERIFY_OK all_critical_levels_and_midpoints_n=2..10',
      'number_level_cases='+str(cases),
      'sharp_cardinality_upper_bounds=True',
      'contiguous_block_extremizers=True',
      'n10_alpha3/5_C=8/5',
      'finite_plateau_jump=True',
      'large_n_bounds=True')
