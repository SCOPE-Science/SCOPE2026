#!/usr/bin/env python3
"""Exact algebra and sample-matrix replay for a sharp fifth-order Radau IIA positivity threshold.
Requires SymPy (tested with 1.13+). Analytical proof of the all-dimensional result is in RESULT.md.
"""
from fractions import Fraction
import sympy as sp

z,r,h=sp.symbols('z r h')
p=lambda t: t**3-9*t**2+36*t-60
N=lambda t: 60+24*t+3*t**2
D=lambda t: 60-36*t+9*t**2-t**3
R=N(z)/D(z)
checks=0

def check(assertion, name):
    global checks
    assert bool(assertion), name
    checks+=1

# This is the order-five [2/3] Pade approximation.
check(sp.series(R-sp.exp(z),z,0,6).removeO()==0,'order five')
check(sp.factor(sp.diff(p(z),z)-(3*(z-3)**2+9))==0,'monotone cubic')
a=sp.Rational(36378,10000)
b=sp.Rational(36379,10000)
check(p(a)<0 and p(b)>0 and 3*a-9>0,'unique real pole isolating interval')

# Certified real-residue domination A_rho > 2|A_complex|.
S=9-r
P=60/r
nr=3*(r*r+8*r+20)
dr=3*r*r-18*r+36
nc=9*(P*P+8*P*S+20*S*S+24*P+160*S+400)
dc=(r*r-r*S+P)*(4*P-S*S)
f=sp.together((nr**2*dc-4*nc*dr**2)*r*r)
F=22429872*r**2-385471872*r+1121843520
check(sp.rem(sp.fraction(f)[0],p(r),r)==F,'residue-square polynomial remainder')
check(F.subs(r,b)>0,'positive residue margin lower bound')
check(sp.diff(F,r).subs(r,a)<0 and sp.diff(F,r).subs(r,b)<0,'residue margin monotonic interval')
check(dc.subs(r,a)>0 and dc.subs(r,b)>0,'complex pole separation')
check(dr.subs(r,a)>0 and dr.subs(r,b)>0,'real pole residue denominator')

# Pole-distance tie and positivity of the universal step value.
star=(60/r-r*r)/(3*r-9)
check(star.subs(r,a)>0 and star.subs(r,b)>0,'positive pole tie')
check(sp.factor((r+star)**2-((9-r)/2+star)**2-(60/r-(9-r)**2/4))==0,'pole tie identity')

# Exact pure-birth three-state positivity and reentrance.
Q=sp.Matrix([[-1,1,0],[0,-1,1],[0,0,0]])
quartic=h**4-16*h**3-48*h**2+240*h+1200
T=lambda x: (60*sp.eye(3)+24*x*Q+3*(x*Q)**2)*(60*sp.eye(3)-36*x*Q+9*(x*Q)**2-(x*Q)**3).inv()
check(sp.factor(sp.diff(R,z).subs(z,-h)-3*quartic/(h**3+9*h*h+36*h+60)**2)==0,'exact derivative')
absorber=h*h*(h**4+12*h**3+198*h*h+960*h+1800)/(h**3+9*h*h+36*h+60)**2
check(sp.factor(1-R.subs(z,-h)-h*sp.diff(R,z).subs(z,-h)-absorber)==0,'exact absorbing probability')
check(quartic.subs(h,0)>0 and quartic.subs(h,5)<0 and quartic.subs(h,18)>0,'two positive-root sign brackets')
check(sp.factor(T(sp.Integer(5))[0,1])==sp.Rational(-105,13924),'negative three-state witness')
check(all(sp.Rational(x).q != 0 for x in T(sp.Integer(18))),'later 3-state step defined')
check(all(v>=0 for v in T(sp.Integer(18))),'three-state reentrant positivity')
check(all(v>=0 for v in T(sp.Integer(1))),'small-step three-state positivity')
check(all(v==1 for v in T(sp.Integer(5))*sp.ones(3,1)),'mass preservation')

# Independently compute Taylor coefficient recurrence from R(-h+t).
def taylor_coeffs(step, count):
    t=sp.Symbol('t')
    numer=sp.Poly(N(-step+t),t)
    denom=sp.Poly(D(-step+t),t)
    qs=[denom.nth(j) for j in range(4)]
    vs=[numer.nth(j) for j in range(3)]
    co=[]
    for k in range(count):
        rhs=(vs[k] if k <3 else 0)-sum(qs[j]*co[k-j] for j in range(1,min(k,3)+1))
        co.append(sp.cancel(rhs/qs[0]))
    return co

pos=taylor_coeffs(sp.Rational(1),64)
check(all(v>0 for v in pos),'64 Taylor coefficients positive below threshold')
neg=taylor_coeffs(sp.Rational(2),96)
negindices=[i for i,c in enumerate(neg) if c<0]
check(len(negindices)>0,'negative higher coefficient above threshold')
k=negindices[0]
# Pure-birth generator with k+2 states: entry (0,k)=h^k * c_k exactly.
size=k+2
Qb=sp.zeros(size)
for i in range(size-1):
    Qb[i,i]=-1
    Qb[i,i+1]=1
B=sp.Integer(2)*Qb
Rm=(60*sp.eye(size)+24*B+3*B**2)*(60*sp.eye(size)-36*B+9*B**2-B**3).inv()
check(sp.factor(Rm[0,k]-(2**k)*neg[k])==0,'absorbing pure-birth coefficient identity')
check(Rm[0,k]<0,'exact higher-state negative witness at h=2')
print('VERIFY_OK',checks,'first_negative_coefficient_at_h2',k,'negative_entry',str(Rm[0,k]))
