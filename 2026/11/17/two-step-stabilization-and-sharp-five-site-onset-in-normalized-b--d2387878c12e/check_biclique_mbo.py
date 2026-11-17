"""Reproducible exact-rational checks for binary heat-threshold dynamics on bicliques.

Public verification only; standard-library Python, no downloads.
"""
from fractions import Fraction as F
from itertools import product

def one_step_formula(m, n, bits, r):
    assert len(bits)==m+n and F(0)<r<F(1)
    a=F(sum(bits[:m]), m); b=F(sum(bits[m:]),n)
    h=(1+r*r)/2; j=(1-r*r)/2; c=h-r
    values=[r*bits[i]+c*a+j*b for i in range(m)] + [r*bits[i]+c*b+j*a for i in range(m,m+n)]
    # Tie-preserving at exactly one half.
    return tuple((1 if z>F(1,2) else 0 if z<F(1,2) else bits[i]) for i,z in enumerate(values))

def one_step_series(m,n,bits,r):
    """Independently evaluate exp[t(P-I)] via spectral decomposition of P.
    P^2 is partwise averaging; P^3=P.  We use r=e^-t and even/odd power series identities.
    """
    N=m+n
    # P sends a side to the mean on the opposite side.
    P=[F(sum(bits[m:]),n)]*m + [F(sum(bits[:m]),m)]*n
    # P squared sends a side to its own mean.
    P2=[F(sum(bits[:m]),m)]*m + [F(sum(bits[m:]),n)]*n
    co=(1-r*r)/2
    ce=(1-r)**2/2
    values=[r*bits[i]+co*P[i]+ce*P2[i] for i in range(N)]
    return tuple((1 if z>F(1,2) else 0 if z<F(1,2) else bits[i]) for i,z in enumerate(values))

def one_step_counts(m,n,k,l,r):
    a=F(k,m); b=F(l,n)
    c=(1-r)**2/2; j=(1-r*r)/2
    if a+b==1: return (k,l)
    if a+b<1:
        return (k if r+c*a+j*b>=F(1,2) else 0, l if r+c*b+j*a>=F(1,2) else 0)
    return (m if c*a+j*b>F(1,2) else k, n if c*b+j*a>F(1,2) else l)

cnt=0
for m in range(1,6):
 for n in range(1,6):
  for bits in product((0,1),repeat=m+n):
   for r in (F(1,40),F(3,20),F(1,4),F(1,2),F(7,10),F(19,20)):
    new=one_step_formula(m,n,bits,r)
    assert new==one_step_series(m,n,bits,r)
    k=sum(bits[:m]); l=sum(bits[m:]); knew=sum(new[:m]); lnew=sum(new[m:]);
    assert (knew,lnew)==one_step_counts(m,n,k,l,r)
    two=one_step_formula(m,n,new,r)
    three=one_step_formula(m,n,two,r)
    assert two==three,(m,n,bits,r,new,two,three)
    cnt+=1
print('EXACT_RATIONAL_ONE_STEP_AND_THIRD_SECOND_EQUALITY_PASS',cnt)
# Verify all possible small graphs fail to have genuinely two-step behavior until 5 vertices.
for total in range(2,5):
 for m in range(1,total):
  n=total-m
  for bits in product((0,1),repeat=total):
   for R in range(1,200):
    r=F(R,200)
    first=one_step_formula(m,n,bits,r)
    assert one_step_formula(m,n,first,r)==first
print('SMALL_GRAPH_SHARPNESS_NO_TWO_STAGE_UP_TO_N4_PASS')
# Exact five-vertex witness: one active vertex in each part of K_(2,3).
bits=(1,0,1,0,0); r=F(3,20)
first=one_step_formula(2,3,bits,r)
second=one_step_formula(2,3,first,r)
assert first==(0,0,1,0,0) and second==(0,0,0,0,0)
a=F(1,2);b=F(1,3);c=(1-r)**2/2;j=(1-r*r)/2
assert r+c*a+j*b==F(2369,4800) and r+c*b+j*a==F(2471,4800)
assert r+c*b==F(649,2400)
print('FIVE_SITE_SHARP_TWO_STEP_WITNESS_PASS',first,second)
print('ALL_NORMALIZED_BICLIQUE_MBO_CHECKS_PASS')
