#!/usr/bin/env python3
"""Exact, standard-library checks of the two-patch occupancy allocation theorem.

Run: python3 verify.py

Polynomial identities establish the finite algebra used by the analytic proof.
Rational Markov-chain checks are independent finite diagnostics, not proofs of
any universal sign or optimization claim.
"""
from fractions import Fraction as F
from itertools import product

NV=5
ZERO=(0,)*NV
class Poly:
    def __init__(self, coefficients=None):
        if isinstance(coefficients,dict):
            self.d={k:F(v) for k,v in coefficients.items() if v}
        elif isinstance(coefficients,Poly): self.d=coefficients.d.copy()
        else: self.d={ZERO:F(coefficients)} if coefficients else {}
    def __add__(self,o):
        o=P(o);r=self.d.copy()
        for k,v in o.d.items():r[k]=r.get(k,F(0))+v
        return Poly(r)
    __radd__=__add__
    def __neg__(self):return Poly({k:-v for k,v in self.d.items()})
    def __sub__(self,o):return self+(-P(o))
    def __rsub__(self,o):return P(o)+(-self)
    def __mul__(self,o):
        o=P(o);r={}
        for k,v in self.d.items():
            for j,w in o.d.items():
                ij=tuple(a+b for a,b in zip(k,j));r[ij]=r.get(ij,F(0))+v*w
        return Poly(r)
    __rmul__=__mul__
    def __truediv__(self,o):return self*F(1,o)
    def __eq__(self,o):return self.d==P(o).d
    def derivative(self,i):
        return Poly({tuple(q-(1 if a==i else 0) for a,q in enumerate(k)):v*k[i]
                     for k,v in self.d.items() if k[i]})

def P(x):return x if isinstance(x,Poly) else Poly(x)
def var(i):return Poly({tuple(1 if j==i else 0 for j in range(NV)):F(1)})
checks=0
def check(ok,msg):
    global checks
    if not ok:raise AssertionError(msg)
    checks+=1

L,M,e1,e2,t=[var(i) for i in range(NV)]
C=2*L+M+e1+e2; delta=e1-e2
h=L*(e1+e2)+e1*e2; k=L*L+L*M/2
D=C*(h+k)+L*delta*t-2*L*t*t
N=C*k-L*delta*t-2*L*t*t
H=C*h+2*L*delta*t
w00=e1*e2*C; w10=e2*L*(C-2*t);w01=e1*L*(C+2*t);w11=N
m=M/2+t; mback=M/2-t
check(w00+w10+w01+w11==D,'normalization polynomial')
check(D-N==H,'H identity')
check(-2*L*w00+e1*w10+e2*w01==0,'00 balance')
check(L*w00-(e1+L+m)*w10+e2*w11==0,'10 balance')
check(L*w00-(e2+L+mback)*w01+e1*w11==0,'01 balance')
check((L+m)*w10+(L+mback)*w01-(e1+e2)*w11==0,'11 balance')
check(D.derivative(4)==L*delta-4*L*t,'regional derivative')
check(H.derivative(4)==2*L*delta,'linear complement')
G=H*D.derivative(4)-H.derivative(4)*D
check(G==-L*(delta*C*(h+2*k)+4*C*h*t+4*L*delta*t*t),'co-occupation derivative')
check(G.derivative(4)==-4*L*H,'strict derivative monotonicity')

# Independent 4-state stationary solver via exact Gaussian elimination.
def stationary(l,mm,a,b,x):
    z=F(0);q=[[z for _ in range(4)] for _ in range(4)]
    def trans(i,j,r):q[i][j]+=r;q[i][i]-=r
    trans(0,1,l);trans(0,2,l)
    trans(1,0,a);trans(1,3,l+x)
    trans(2,0,b);trans(2,3,l+mm-x)
    trans(3,1,b);trans(3,2,a)
    aug=[[q[j][i] for j in range(4)]+[F(0)] for i in range(4)]
    aug[3]=[F(1)]*4+[F(1)]
    for i in range(4):
        j=next(j for j in range(i,4) if aug[j][i])
        aug[i],aug[j]=aug[j],aug[i]
        pivot=aug[i][i];aug[i]=[a/pivot for a in aug[i]]
        for j in range(4):
            if j==i:continue
            pivot=aug[j][i]
            aug[j]=[a-pivot*b for a,b in zip(aug[j],aug[i])]
    return tuple(row[-1] for row in aug)

def closed(l,mm,a,b,x):
    c=2*l+mm+a+b;de=a-b;u=x-mm/2
    hh=l*(a+b)+a*b;kk=l*l+l*mm/2
    den=c*(hh+kk)+l*de*u-2*l*u*u
    assert den>0
    return (a*b*c/den,b*l*(c-2*u)/den,a*l*(c+2*u)/den,
            (c*kk-l*de*u-2*l*u*u)/den)

vals=(F(1,3),F(1),F(2),F(5,2),F(4))
for l,mm,a,b in product(vals,repeat=4):
    for frac in (F(0),F(1,5),F(1,2),F(4,5),F(1)):
        x=mm*frac
        exact=stationary(l,mm,a,b,x)
        check(exact==closed(l,mm,a,b,x),f'stationary mismatch {l,mm,a,b,x}')
        check(all(p>0 for p in exact), 'stationary positivity')
        # Regional occupancy derivative at equal allocation sign of e1-e2.
        left=1-closed(l,mm,a,b,mm*F(49,100))[0]
        right=1-closed(l,mm,a,b,mm*F(51,100))[0]
        check((right>left)-(right<left)==(a>b)-(a<b),'regional side')
        # Joint occupancy derivative at equal allocation opposite sign.
        left=closed(l,mm,a,b,mm*F(49,100))[3]
        right=closed(l,mm,a,b,mm*F(51,100))[3]
        check((right>left)-(right<left)==(a<b)-(a>b),'joint side')

# Concrete rational case and isolation of unique quadratic root.
l,mm,a,b=F(1),F(4),F(2),F(1)
c=2*l+mm+a+b; de=a-b; hh=l*(a+b)+a*b;kk=l*l+l*mm/2
xA=mm/2+de/4
check(xA==F(9,4),'regional optimum')
def sg(x):
    u=x-mm/2
    return -l*(de*c*(hh+2*kk)+4*c*hh*u+4*l*de*u*u)
check(sg(F(1443,1000))>0 and sg(F(1444,1000))<0,'interior optimizer isolation')
check(closed(l,mm,a,b,F(1443,1000))[3] > closed(l,mm,a,b,mm/2)[3], 'joint advantage')
check((1-closed(l,mm,a,b,xA)[0]) > (1-closed(l,mm,a,b,mm/2)[0]),'regional advantage')
print('PASS',checks,'exact assertions; 10 multivariate polynomial identities and independent rational CTMC diagnostics')
print('Example: regional optimum m1=9/4, joint optimum m1=(-41+3*sqrt(214))/2 in (1443/1000,1444/1000)')
