#!/usr/bin/env python3
"""Exact symbolic and matrix checks for two-leader inverse-square friendship optimization.
Only the SymPy package is required. Finite checks corroborate the all-parameter proof.
"""
import itertools
import sympy as sp

m, t = sp.symbols('m t', positive=True)
a = 1+t
H = sp.factor(a**-2+(m-1)*(1+(1+2*t)**-2))
S = sp.factor((m-1)/(1+2*t)**2+m**2+2*m-sp.Rational(11,4))
schur = 4-2/a
btrace2 = 2/a**2+(m-2)*(1+(1+2*t)**-2)
q2 = 2/a**2+2*(m-2)
q3 = 2/a**3+2*(m-2)
D = sp.factor(btrace2+(1+q2)**2/schur**2+2*q3/schur)
Q = (4*m**2+4*m-39)*t**2+(8*m**2-46)*t+4*m**2+4*m-11
assert sp.factor(D-H-Q/(4*(1+2*t)**2))==0
assert sp.factor(S-H-(m**2+m-sp.Rational(7,4)-1/a**2))==0
assert sp.factor(D-(H+Q/(4*(1+2*t)**2)))==0
threshold=(-7+2*sp.sqrt(61))/15
assert sp.simplify(Q.subs(m,2).subs(t,threshold))==0
assert (sp.sqrt(61)>6)==sp.S.true
symbolic_checks=5


def build(mv,tv):
    L=sp.zeros(2*mv+1)
    for j in range(mv):
        v,w=2*j+1,2*j+2
        for i,k,c in [(0,v,sp.S.One),(0,w,sp.S.One),(v,w,tv)]:
            L[i,i]+=c;L[k,k]+=c;L[i,k]-=c;L[k,i]-=c
    return L


def orbit(pair):
    a,b=pair
    if a==0: return 'H'
    if (a-1)//2==(b-1)//2: return 'S'
    return 'D'


checks=0
for mv in range(2,8):
    for tv in [sp.Rational(1,5),sp.Rational(1,3),sp.Rational(1,2),sp.Rational(3,5),sp.S.One,sp.S(3),sp.S(5)]:
        L=build(mv,tv)
        formulas={name:sp.factor(expr.subs({m:mv,t:tv}))
                  for name,expr in [('H',H),('S',S),('D',D)]}
        vals={}
        for pair in itertools.combinations(range(2*mv+1),2):
            followers=[k for k in range(2*mv+1) if k not in pair]
            G=L.extract(followers,followers)
            assert G.det()!=0
            I=G.inv()
            value=sp.trace(I**2)
            typ=orbit(pair)
            assert value==formulas[typ],(mv,tv,pair,value,formulas[typ])
            vals[pair]=value
            checks+=2
        minimum=min(vals.values())
        winners={p for p,v in vals.items() if v==minimum}
        compare=sp.factor(Q.subs({m:mv,t:tv}))
        typ='H' if compare>0 else ('D' if compare<0 else 'HD')
        want={p for p in vals if orbit(p) in (['H','D'] if typ=='HD' else [typ])}
        assert winners==want,(mv,tv,typ,winners,want)
        assert all(vals[p]>minimum for p in vals if orbit(p)=='S')
        checks+=2
    print('m={} all exact leader-pair checks passed'.format(mv))

# Algebraic verification of unequal first-/second-order decisions.
assert sp.factor(Q.subs(m,3))==9*t*t+26*t+37
assert sp.simplify(threshold-sp.Rational(1,3))>0
assert sp.factor(Q.subs(m,2))==-15*t*t-14*t+13
checks+=3
print('SYMBOLIC_IDENTITIES_OK',symbolic_checks+3)
print('EXACT_MATRIX_AND_ORBIT_CHECKS_OK',checks-3)
print('TOTAL_CHECKS',checks+symbolic_checks)
print('THRESHOLD',threshold,'=',threshold.evalf(15))
