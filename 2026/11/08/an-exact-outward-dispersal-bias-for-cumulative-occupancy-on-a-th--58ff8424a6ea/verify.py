#!/usr/bin/env python3
"""Exact verification of three-patch asymmetric-colonization rewards.
Requires SymPy. Run: python verify.py
"""
import sympy as sp

a,b,S,d=sp.symbols('a b S d', positive=True)
# Transient states are bit masks 001,...,111; center is bit 010.
states=list(range(1,8))
Q=sp.zeros(7)
for i,state in enumerate(states):
    for site in range(3):
        present=bool(state & (1 << site))
        if present:
            nxt=state & ~(1<<site)
            rate=sp.Integer(1)
        else:
            nxt=state | (1<<site)
            if site==1:
                rate=b * int(bool(state&1)) + b * int(bool(state&4))
            else:
                rate=a * int(bool(state&2))
        if rate==0:
            continue
        Q[i,i]+=rate
        if nxt:
            Q[i,nxt-1]-=rate
ones=sp.ones(7,1)
occupancy=sp.Matrix([state.bit_count() for state in states])
E=sp.factor((Q.inv()*ones)[6])
Z=sp.factor((Q.inv()*occupancy)[6])
Den=2*(a+b+2)*(2*a+2*b+3)
E_expected=(4*a*a*b*b+10*a*a*b+10*a*b*b+10*a*a+10*b*b+37*a*b+31*a+31*b+22)/Den
Z_expected=(6*a*a*b*b+14*a*a*b+11*a*b*b+10*a*a+9*b*b+37*a*b+27*a+27*b+18)/((a+b+2)*(2*a+2*b+3))
assert sp.cancel(E-E_expected)==0
assert sp.cancel(Z-Z_expected)==0
assert sp.cancel(Z - Z.xreplace({a:b,b:a}) - (a-b)*(3*a*b+a+b)/((a+b+2)*(2*a+2*b+3)))==0
q=sp.symbols('q',nonnegative=True)
E_q=(4*q*q+(10*S+17)*q+10*S*S+31*S+22)/(2*(S+2)*(2*S+3))
assert sp.cancel(E_q.subs({S:a+b,q:a*b})-E)==0
Z_d=sp.factor(Z.subs({a:(S+d)/2,b:(S-d)/2}))
G=12*d**3-9*d**2-(12*S**2+50*S+72)*d+3*S**2+4*S
assert sp.cancel(sp.diff(Z_d,d)-G/(8*(S+2)*(2*S+3)))==0
assert sp.expand(G.subs(d,S)+4*S*(14*S+17))==0
assert sp.expand(G.subs(d,sp.Rational(1,4))+(68*S+147)/8)==0
# Independently check the transient generator and closed forms for several rational rates.
from fractions import Fraction

def solve_fraction(matrix, rhs):
    m=len(rhs)
    rows=[[Fraction(matrix[i,j]) for j in range(m)]+[Fraction(rhs[i])] for i in range(m)]
    for c in range(m):
        r=next(i for i in range(c,m) if rows[i][c])
        rows[c],rows[r]=rows[r],rows[c]
        v=rows[c][c]
        rows[c]=[x/v for x in rows[c]]
        for i in range(m):
            if i==c: continue
            v=rows[i][c]
            if v: rows[i]=[rows[i][j]-v*rows[c][j] for j in range(m+1)]
    return [row[-1] for row in rows]

cases=0
for aa in (sp.Rational(1,8),sp.Rational(1,2),sp.Rational(1),sp.Rational(5,3),sp.Rational(7)):
    for bb in (sp.Rational(0),sp.Rational(2,5),sp.Rational(1),sp.Rational(4)):
        M=Q.subs({a:aa,b:bb})
        e=solve_fraction(M,[1]*7)[6]
        z=solve_fraction(M,[k.bit_count() for k in states])[6]
        assert e==Fraction(E_expected.subs({a:aa,b:bb}))
        assert z==Fraction(Z_expected.subs({a:aa,b:bb}))
        cases+=1
print('PASS: symbolic Markov rewards, budget and bias identities; independent fraction elimination',cases,'rate cases')
