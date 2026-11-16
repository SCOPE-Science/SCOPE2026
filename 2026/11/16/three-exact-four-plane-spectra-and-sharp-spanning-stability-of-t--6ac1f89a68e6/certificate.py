"""Exact algebraic certificate for four-subspace spectra of the real harmonic
EITFF(11,11,3). Run: python certificate.py --all, or --rep 0 through 5.
Requires Python 3 and SymPy 1.14 (earlier compatible versions may also work).
Uses exact arithmetic in Q(zeta_55), not floating point.
"""
from pathlib import Path
from fractions import Fraction
import argparse
import itertools
import json
import sympy as sp

DATA=json.loads(Path(__file__).with_name('spectra.json').read_text(encoding='utf-8'))
K=sp.QQ.algebraic_field(sp.exp(2*sp.pi*sp.I/55))
z=K.unit
one,zero=K.one,K.zero
q=lambda a,b=1: K.from_sympy(sp.Rational(a,b))
z11=z**5
z5=z**11
z10=-(z5**3)
chi={pow(2,k,11):z10**k for k in range(10)}
def gauss(k):
    return sum((z11**(-x))*(chi[x]**k) for x in range(1,11))
omega=gauss(6)/gauss(1)
c=(z5+z5**-1)*q(1,2)
h=(z5-z5**-1)*q(1,2)
B=[]
for x in range(11):
    if x==0:
        B.append([[one if r==s==0 else zero for s in range(3)] for r in range(3)])
        continue
    leg=1 if pow(x,5,11)==1 else -1
    v=[one,chi[x]*(q(leg)*c+h*omega),chi[x]**-1*(q(leg)*c+h/omega)]
    vc=[one,chi[x]**-1*(q(leg)*c-h/omega),chi[x]*(q(leg)*c-h*omega)]
    weight=[q(4,15),q(11,30),q(11,30)]
    B.append([[v[r]*vc[s]*weight[s] for s in range(3)] for r in range(3)])
M=[[[sum((z11**(d*x))*B[x][r][s] for x in range(11))*q(3,11)
      for s in range(3)] for r in range(3)] for d in range(11)]
assert all(M[0][r][s]==(one if r==s else zero) for r in range(3) for s in range(3))

def gram(S):
    return [[M[(S[j//3]-S[i//3])%11][i%3][j%3]
             for j in range(12)] for i in range(12)]

def coefficients(A):
    # Faddeev-LeVerrier recurrence over a characteristic-zero field.
    n=len(A)
    B=[[one if i==j else zero for j in range(n)] for i in range(n)]
    cs=[one]
    for k in range(1,n+1):
        C=[[sum((A[i][h]*B[h][j] for h in range(n)),zero)
             for j in range(n)] for i in range(n)]
        ck=-sum((C[i][i] for i in range(n)),zero)*q(1,k)
        cs.append(ck)
        for i in range(n):
            C[i][i]+=ck
        B=C
    return cs

def check_orbits():
    allsets=set(itertools.combinations(range(11),4));unseen=set(allsets)
    for rep in DATA['representatives']:
        S=tuple(rep)
        assert S in unseen
        orbit={tuple(sorted((a*x+b)%11 for x in S))
               for a in (1,3,4,5,9) for b in range(11)}
        assert len(orbit)==55 and orbit<=unseen
        unseen-=orbit
    assert not unseen
    print('PASS: 330 four-subsets partition into six square-affine orbits of 55')

def exact_expected(cls):
    d=DATA['classes'][cls]
    tau=z5**2+z5**3
    return [q(Fraction(a).numerator,Fraction(a).denominator)
            +tau*q(Fraction(b).numerator,Fraction(b).denominator)
            for a,b in zip(d['a'],d['b'])]+[zero]

def check_rep(i):
    S=DATA['representatives'][i]
    actual=coefficients(gram(S))
    cls=DATA['class_by_representative'][i]
    expected=exact_expected(cls)
    assert actual==expected, ('characteristic coefficients differ',i)
    assert actual[-1]==zero and actual[-2]!=zero
    print('PASS: representative %d %s class %s exact degree-12 polynomial, one zero root'% (i,S,cls))

def check_roots():
    t=sp.symbols('t');tau=-(1+sp.sqrt(5))/2
    for cls,d in DATA['classes'].items():
        coeff=[sp.Rational(a)+sp.Rational(b)*tau for a,b in zip(d['a'],d['b'])]
        p=sp.Poly(sum(v*t**(11-j) for j,v in enumerate(coeff)),t,extension=sp.sqrt(5))
        lo,hi=[sp.Rational(v) for v in d['min_root_interval_rational']]
        assert p.eval(0)!=0 and sp.N(p.eval(0))<0
        assert p.count_roots(0,lo)==0
        assert p.count_roots(0,hi)==1
        print('PASS: class %s minimum root strictly between %s and %s'%(cls,lo,hi))

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--rep',type=int,choices=range(6))
    group.add_argument('--all',action='store_true')
    group.add_argument('--roots',action='store_true')
    args=parser.parse_args()
    if args.roots:
        check_roots()
    else:
        check_orbits()
        for i in (range(6) if args.all else [args.rep]):
            check_rep(i)
