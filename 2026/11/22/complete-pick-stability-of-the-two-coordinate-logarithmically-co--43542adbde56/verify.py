"""Independent finite exact-algebra checks for the stated two-step kernel formulas.
These do not establish the infinite-dimensional Pick property; the proof does.
"""
from fractions import Fraction as F

def det2(m):
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]

def checks(a,b,u):
    a,b,u = map(F, (a,b,u))
    assert a>=1 and b>=a and a*a*u*u <= (a*a-1)*(b*b-a*a)
    D=((a*a-1,a*u),(a*u,b*b+u*u-1))
    W=((a*a+u*u-1,b*u),(b*u,b*b-a*a))
    assert det2(D)==(a*a-1)*(b*b-1)-u*u
    assert det2(W)==(a*a-1)*(b*b-a*a)-a*a*u*u
    assert D[0][0]>=0 and D[1][1]>=0 and det2(D)>=0
    assert W[0][0]>=0 and W[1][1]>=0 and det2(W)>=0
    gam=1/(b*b); eta=(a*a-1)/(a*a*b*b); x=u/(a*b)
    R=((1-gam,x),(x,x*x+eta))
    H=((gam-eta-gam*gam,(gam-eta)*x),((gam-eta)*x,(gam-eta)*x*x+gam*eta))
    assert R[0][0]>=0 and R[1][1]>=0 and det2(R)>=0
    assert H[0][0]>=0 and H[1][1]>=0 and det2(H)>=0
    assert det2(R)==(1-gam)*eta-gam*x*x
    assert det2(H)==(gam-eta-gam*gam)*gam*eta - gam*gam*(gam-eta)*x*x
    for z,w in [(F(0),F(0)),(F(1,5),F(2,7)),(F(-1,4),F(1,3))]:
        t=z*w; Qz=1+x*z; Qw=1+x*w; qw=Qz*Qw
        K=1+t*(gam-eta*t)/(qw*(1-t))
        RR=1-(gam-eta*t)/qw
        HH=gam*RR-eta
        F_exact=1-1/K
        F_decomp=gam*t/qw + t*t*HH/(qw*(1-t*RR))
        assert F_exact==F_decomp
        assert K>0
    return 1

cases=[(1,1,0),(1,3,0),(2,2,0),(2,3,0),(2,3,1),(2,4,1),(3,5,1),(3,5,2),(4,6,3)]
for case in cases: checks(*case)
# Exhaustive small rational grid of admissible integral parameters.
count=0
for a in range(1,8):
 for b in range(a,12):
  for u in range(-8,9):
   if a*a*u*u <= (a*a-1)*(b*b-a*a):
    count+=checks(a,b,u)
print('PASS:',len(cases)+count,'exact-rational admissible cases; kernel identity, PSD determinants and constraints')
