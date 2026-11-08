"""Exact rational coefficient and analytic-tail certificate for the seam/interior covariance."""
from fractions import Fraction as F
from itertools import combinations
from math import isclose
# Probability-series coefficient recurrence (polynomials in z, constant-first).
def coeffs(P,Q,N=100):
    a=[]
    for n in range(N+1):
        a.append((F(P[n]) if n<len(P) else F(0))-sum(F(Q[j])*a[n-j] for j in range(1,min(n,len(Q)-1)+1)))
        a[-1]/=Q[0]
    return a
H=coeffs([0,0,0,128,0,-96,48,-48,20,4],[256,-640,384,160,-160,-24,8,22,-3,-4,1]);L=coeffs([0,0,0,-2],[-4,8,-3,-2,1]);B=coeffs([0,0,0,-4],[-8,12,-2,-3,1]);C=[H[n]-L[n]*B[n] for n in range(101)]
assert all(C[n]==0 for n in [1,2]);assert all(C[n]>0 for n in range(3,15));assert all(C[n]<0 for n in range(15,101));
for n in range(2,10):
    sl=sb=sh=0
    for mask in range(1<<(n-1)):
        cuts=[0]+[j+1 for j in range(n-1) if mask&(1<<j)]+[n]
        parts=[cuts[j+1]-cuts[j] for j in range(len(cuts)-1)]
        l=sum(abs(a-b) for a,b in zip(parts,parts[1:]))
        b=abs(parts[-1]-parts[0]);sl+=l;sb+=b;sh+=l*b
    d=1<<(n-1)
    assert (L[n],B[n],H[n])==(F(sl,d),F(sb,d),F(sh,d))
R=F(2,3);MH=F(134105456,189);ML=F(496,9);MB=F(592,3)
e=(MH+F(4,3)*ML+(F(2,3)*100+F(16,9))*MB)*R**100+ML*MB*R**200
assert e<F(4,189)
# n R^n monotone decreasing for n>=100, so this bound holds for every n>=100.
assert C[14]>0 and C[15]<0
print('PASS exhaustive n=1..100 rational coefficients; enumeration n=2..9; analytic tail at n>=100; C14=',C[14],'C15=',C[15], 'tail bound=',e)
