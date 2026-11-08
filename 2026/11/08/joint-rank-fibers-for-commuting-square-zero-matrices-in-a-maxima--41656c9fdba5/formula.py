"""Independent integer-combinatorial evaluator for rank strata of commuting square-zero pairs."""
from math import prod
from pathlib import Path

def gaussian(n,k,q):
    if k<0 or k>n:return 0
    num=prod(q**(n-j)-1 for j in range(k))
    den=prod(q**(k-j)-1 for j in range(k))
    assert num%den==0
    return num//den

def gl(n,q):return prod(q**n-q**j for j in range(n))
def rank_matrices(n,t,q):return gaussian(n,t,q)*prod(q**n-q**j for j in range(t))
def strata(r,q):
    result={}
    for s in range(r//2+1):
        h=r-2*s
        c=gaussian(r,s,q)*gaussian(r-s,s,q)*gl(s,q)*q**(2*s*(r-s))
        for t in range(h+1):result[(s,2*s+t)]=c*rank_matrices(h,t,q)
    return result

expected={
(2,1):{(0,0):1,(0,1):1},
(2,2):{(0,0):1,(0,1):9,(0,2):6,(1,2):12},
(3,2):{(0,0):1,(0,1):32,(0,2):48,(1,2):72},
(4,2):{(0,0):1,(0,1):75,(0,2):180,(1,2):240},
(5,2):{(0,0):1,(0,1):144,(0,2):480,(1,2):600},
(2,3):{(0,0):1,(0,1):49,(0,2):294,(0,3):168,(1,2):336,(1,3):336}}
for (q,r), want in expected.items():
    got=strata(r,q)
    assert got==want,((q,r),got,want)
    print('rank strata pass',q,r,sum(got.values()))
for q in (2,3,4,5,7,8,9):
    for r in range(1,9):
        D=strata(r,q)
        assert sum(v for (s,b),v in D.items() if b==0)==1
        assert all(0<=s<=r//2 and 2*s<=b<=r and v>0 for (s,b),v in D.items())
        if r>=2:assert sum(v for (s,b),v in D.items() if b==r)>gl(r,q)
    print('symbolic rank feasibility pass',q,'r=1..8')
print('ALL_BIVARIATE_RANK_FORMULA_PASS')
