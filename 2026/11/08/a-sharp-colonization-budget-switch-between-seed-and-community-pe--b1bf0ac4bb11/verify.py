#!/usr/bin/env python3
"""Exact CTMC validation for a three-habitat recolonization model.

Uses SymPy for symbolic identities, and independent Fraction Gaussian
elimination for rational samples. All computations are finite checks;
the all-parameter proof is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
import sympy as sp

a,b,s,p=sp.symbols('a b s p',nonnegative=True)
H=(s+1)*(s+6)
TC=(s+2+p)*(H+(s+3)*p)/(2*(H+(2*s+7)*p))
AF=(s+3)**2*p**2+(2*s**3+20*s**2+60*s+56)*p +s**4+12*s**3+51*s**2+84*s+44
TF=AF/(2*(s+2)*(H+(2*s+7)*p))

def symbol_generator(w1,w2):
    Q=sp.zeros(7)
    for m in range(1,8):
        i=m-1
        for v in range(3):
            if (m>>v)&1:
                dest=m^(1<<v); rate=sp.Integer(1)
            else:
                dest=m|(1<<v)
                rate=(w1 if (v==0 and (m&2)) or (v==1 and (m&1)) else 0)
                rate+=(w2 if (v==2 and (m&2)) or (v==1 and (m&4)) else 0)
            if not rate: continue
            Q[i,i]+=rate
            if dest:Q[i,dest-1]-=rate
    return Q
Q=symbol_generator(a,b)
sol=Q.inv()*sp.ones(7,1)
assert sp.cancel(sol[1]-TC.subs({s:a+b,p:a*b}))==0
assert sp.cancel(sol[6]-TF.subs({s:a+b,p:a*b}))==0
assert sp.cancel(TC-TC.subs(p,0)-p*((s+3)*p+s-2)/(2*(H+(2*s+7)*p)))==0
assert sp.cancel(TC.subs(p,s*s/4)-TC.subs(p,0)-s*s*(s-1)/(8*(2*s+3)))==0
assert sp.cancel(TC-TC.subs(p,s*s/4)-(4*p-s*s)*((s+3)*(2*s+3)*p+(s-1)*(s+1)*(s+6))/(8*(2*s+3)*(H+(2*s+7)*p)))==0
N=(2*s**3+19*s**2+60*s+63)*p*p+(2*s**4+26*s**3+114*s**2+198*s+108)*p+3*s**4+26*s**3+71*s**2+76*s+28
assert sp.cancel(sp.diff(TF,p)-N/(2*(s+2)*(H+(2*s+7)*p)**2))==0
print('Symbolic generator inversions, rational identities, derivative: PASS (6)')

def exact_time(u,v,start):
    # Independent Fraction row elimination, no SymPy matrix routines.
    Q=[[F(0) for _ in range(8)] for _ in range(7)]
    for mask in range(1,8):
        row=Q[mask-1]
        for j in range(3):
            if mask&(1<<j):
                rate=F(1); nxt=mask^(1<<j)
            else:
                rate=(u if (j==0 and mask&2) or (j==1 and mask&1) else F(0))
                rate+=(v if (j==2 and mask&2) or (j==1 and mask&4) else F(0))
                nxt=mask|(1<<j)
            row[mask-1]+=rate
            if nxt:row[nxt-1]-=rate
        row[7]=F(1)
    for j in range(7):
        k=next(k for k in range(j,7) if Q[k][j])
        Q[j],Q[k]=Q[k],Q[j]
        pivot=Q[j][j]
        Q[j]=[x/pivot for x in Q[j]]
        for i in range(7):
            if i!=j:
                c=Q[i][j]
                if c:Q[i]=[x-c*y for x,y in zip(Q[i],Q[j])]
    return Q[start-1][7]

def full_formula(S,P):
    hh=(S+1)*(S+6)
    num=(S+3)**2*P**2+(2*S**3+20*S**2+60*S+56)*P+S**4+12*S**3+51*S**2+84*S+44
    return num/(2*(S+2)*(hh+(2*S+7)*P))

def center_formula(S,P):
    hh=(S+1)*(S+6)
    return (S+2+P)*(hh+(S+3)*P)/(2*(hh+(2*S+7)*P))

n=0
for den in (1,2,3,5,7):
    for au,bu in product(range(5),repeat=2):
        if not (au+bu):continue
        u,v=F(au,den),F(bu,den)
        S,P=u+v,u*v
        assert exact_time(u,v,2)==center_formula(S,P)
        assert exact_time(u,v,7)==full_formula(S,P)
        n+=2
print('Independent exact Fraction Markov reward solves: PASS (%d)'%n)
# Endpoint/balanced comparisons and exact boundary equality.
for S in (F(1,4),F(1,2),F(3,4),F(1),F(5,4),F(2),F(7)):
    end=center_formula(S,F(0)); balanced=center_formula(S,S*S/4)
    assert (balanced>end)==(S>1)
    assert (balanced==end)==(S==1)
    assert full_formula(S,S*S/4)>full_formula(S,F(0))
print('Exact parameter-regime comparisons: PASS (21)')
