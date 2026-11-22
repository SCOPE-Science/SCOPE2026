"""Exact intersection checks for matrix-pencil surface canonical classes.

Coordinates are a pullback of a plane line followed by total transforms
of exceptional divisors. Their intersection matrix is diag(1,-1,...,-1).
This is a finite consistency check, not a substitute for the curve argument.
"""
from fractions import Fraction
from itertools import combinations, product

def dot(a,b):
    return a[0]*b[0]-sum(x*y for x,y in zip(a[1:],b[1:]))

def classify(groups, regular):
    maxes=[max(g) for g in groups]
    k=sum(maxes)
    assert k>=2
    negk=[Fraction(-1) for _ in range(k)]
    antik=(Fraction(3),*negk)
    line=(Fraction(1),*negk)
    assert dot(line,line)==1-k
    assert dot(antik,line)==3-k
    A=[]; retained=[]; i=1
    for sizes in groups:
        for j in range(1,max(sizes)+1):
            v=[Fraction(0)]*(k+1)
            v[i]=Fraction(1)
            if j<max(sizes): v[i+1]=Fraction(-1)
            A.append(tuple(v))
            retained.append(j in sizes)
            i+=1
    assert len(A)==k and len(retained)==k
    if regular:
        coef=Fraction(3-k,k-1)
        D=tuple(x+coef*y for x,y in zip(antik,line))
        assert dot(D,line)==0
        assert dot(D,D)==Fraction(4*k,k-1)
        assert all(dot(D,a)==(0 if a!=A[sum(maxes[:idx+1])-1] else Fraction(2,k-1))
                   for idx in range(len(groups)) for a in A[sum(maxes[:idx]):sum(maxes[:idx+1])])
        assert (all(len(g)==1 for g in groups)) == (not any(retained[j] for j in range(k) if j not in [sum(maxes[:idx+1])-1 for idx in range(len(groups))]))
    else:
        D=antik
        assert dot(D,D)==9-k
        assert all(dot(D,a)==(0 if a!=A[sum(maxes[:idx+1])-1] else 1)
                   for idx in range(len(groups)) for a in A[sum(maxes[:idx]):sum(maxes[:idx+1])])
        if k>=4:
            b=Fraction(k-3,k-1)
            pos=tuple(x-b*y for x,y in zip(D,line))
            assert dot(pos,line)==0
            assert dot(pos,pos)==Fraction(4*k,k-1)
            assert dot(D,D)==dot(pos,pos)+b*b*dot(line,line)
    # Zero curve not contracted by resolution equals an intermediate size.
    z=sum(retained[j] and j not in [sum(maxes[:idx+1])-1 for idx in range(len(groups))] for j in range(k))
    return k,z

count=0
for k in range(2,8):
  for s in range(1,min(k,4)+1):
    for cut in combinations(range(1,k),s-1):
      maxes=[b-a for a,b in zip((0,)+cut, cut+(k,))]
      opts=[[tuple(sub) for r in range(1,m+1) for sub in combinations(range(1,m),r-1)] for m in maxes]
      # every subset includes maximal size
      opts=[[(a+(m,)) for a in op] for op,m in zip(opts,maxes)]
      for groups in product(*opts):
        for regular in (False,True):
          x=classify(groups,regular)
          assert x[0]==k
          count+=1
print('EXACT_INTERSECTION_CASES_OK',count)
print('ANTICANONICAL_VOLUME_AND_NULL_CURVE_TESTS_OK')
