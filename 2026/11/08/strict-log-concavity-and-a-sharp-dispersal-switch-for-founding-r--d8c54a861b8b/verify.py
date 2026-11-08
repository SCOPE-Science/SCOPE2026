#!/usr/bin/env python3
"""Reproduce exact finite-state and polynomial certificates for founder-pair establishment.
Requires SymPy. Run from the directory containing hessian_certificate.json.
"""
import json
import itertools
from fractions import Fraction
from pathlib import Path
import sympy as sp

a, b, B, h, m = sp.symbols('a b B h m', positive=True)
J = a*a + 5*a*b + 21*a + 6*b*b + 45*b + 84
D = (a*a*b*b + 5*a*b**3 + 21*a*b*b + 15*a*b + 3*a
     + 6*b**4 + 45*b**3 + 141*b*b + 195*b + 108)
P = b*b*J/D
M = sp.Matrix([
    [a/sp.Integer(3)+b+2, -a/sp.Integer(3), -b, 0],
    [-3, 3*b+3, 0, -3*b],
    [-1, 0, a/sp.Integer(3)+2*b/sp.Integer(3)+3, -a/sp.Integer(3)],
    [0, -1, -3, 2*b+4],
])
y = sp.Matrix([0, 0, 2*b/sp.Integer(3), 2*b])
assert sp.factor(M.det()) != 0
u = M.inv() * y
assert sp.cancel(u[1] - P) == 0
assert sp.simplify(P.subs({a:0,b:sp.Rational(1,2)}) - sp.Rational(1,2)**2*(6*sp.Rational(1,2)**2+45*sp.Rational(1,2)+84)/(6*sp.Rational(1,2)**4+45*sp.Rational(1,2)**3+141*sp.Rational(1,2)**2+195*sp.Rational(1,2)+108))==0

def hess(v, w):
    # Second derivative of log(b^2 J / D); no transcendental simplification.
    def log_second(F):
        return (F * sp.diff(F, v, w) - sp.diff(F,v)*sp.diff(F,w))/F**2
    return sp.cancel(log_second(J) - log_second(D) - (2/b**2 if v==b and w==b else 0))

haa, hbb, hab = hess(a,a), hess(b,b), hess(a,b)
minor = sp.cancel(haa*hbb-hab*hab)
cert = json.loads(Path(__file__).with_name('hessian_certificate.json').read_text('utf-8'))
assert cert['meaning'] == 'exact numerator monomials of the specified rational derivatives'
for label, expression, sign in [
    ('minus_Haa', -haa, 1), ('minus_Hbb', -hbb, 1), ('det_H', minor, 1)
]:
    numerator, denominator = sp.fraction(sp.cancel(expression))
    poly = sp.Poly(numerator, a, b)
    terms = [[int(ex[0]), int(ex[1]), int(co)] for ex, co in poly.terms()]
    assert terms == cert[label]
    assert all(co*sign > 0 for _,_,co in terms)
    expected_den = ((J*D)**2 if label=='minus_Haa' else
                    b**2*(J*D)**2 if label=='minus_Hbb' else
                    b**2*(J*D)**3)
    assert sp.cancel(denominator/expected_den - 1) == 0

F = sp.factor(P.subs({a:B*(1-m),b:B*h*m}))
Q = (228*B**4*h**4 + (-65*B**4+2025*B**3)*h**3
     + (-493*B**3+6714*B**2)*h**2
     + (-1080*B**2+10320*B)*h + 6048-672*B)
edge_d = sp.factor(sp.diff(F,m).subs(m,1))
edge_formula = B**2*h**2*Q/(3*(B**2*h**2+5*B*h+9)**2*(2*B**2*h**2+5*B*h+4)**2)
assert sp.cancel(edge_d - edge_formula) == 0
assert sp.factor(Q.subs(h,1)) == 163*B**4+1532*B**3+5634*B**2+9648*B+6048
# Ascending coefficient sign transitions in h occur at B = 9, 86/9, 6714/493, 405/13.
assert 9 < sp.Rational(86,9) < sp.Rational(6714,493) < sp.Rational(405,13)

# Independent state-generator evaluation: use all states where target count < 2,
# not the reduced four-state equations. Reproduce exact probabilities via Fractions.
def solve_fraction(mat, rhs):
    n=len(mat)
    aug=[list(mat[k]) + [rhs[k]] for k in range(n)]
    for c in range(n):
        pivot = next(k for k in range(c,n) if aug[k][c] != 0)
        aug[pivot],aug[c]=aug[c],aug[pivot]
        inv=aug[c][c]
        aug[c]=[x/inv for x in aug[c]]
        for k in range(n):
            if k!=c:
                z=aug[k][c]
                if z: aug[k]=[aug[k][j]-z*aug[c][j] for j in range(n+1)]
    return [r[-1] for r in aug]

def independent_probability(A,C):
    # Reach two in destination before failure, with exact rates for capacity three.
    # States with i<2 and j<2 are sterile, hence absorbing failures.
    states=[(i,j) for i in (2,3) for j in (0,1)]
    loc={state:k for k,state in enumerate(states)}
    n=len(states)
    Z=[[Fraction(0) for _ in range(n)] for __ in range(n)]
    rhs=[Fraction(0) for _ in range(n)]
    for x, (i,j) in enumerate(states):
        transitions=[]
        transitions.append(((i-1,j),Fraction(i)))
        if j>0:transitions.append(((i,j-1),Fraction(j)))
        if i<3:transitions.append(((i+1,j),A*Fraction(i*(i-1)*(3-i),6)))
        if j<3:transitions.append(((i,j+1),C*Fraction(i*(i-1)*(3-j),6)))
        for dest,rate in transitions:
            Z[x][x]+=rate
            if dest[1]>=2:rhs[x]+=rate
            elif dest in loc:Z[x][loc[dest]]-=rate
    return solve_fraction(Z,rhs)[loc[(3,0)]]

checked=0
for A,C in itertools.product([Fraction(1,3),Fraction(1),Fraction(2),Fraction(7,2),Fraction(9)],
                             [Fraction(1,5),Fraction(1),Fraction(3),Fraction(9,2),Fraction(12)]):
    observed=independent_probability(A,C)
    predicted=Fraction(sp.Rational(P.subs({a:sp.Rational(A.numerator,A.denominator),
                                          b:sp.Rational(C.numerator,C.denominator)})))
    assert observed == predicted
    checked+=1

print('PASS: four-state exact formula; 3 Hessian coefficient certificates;')
print('      strict joint log-concavity; endpoint derivative; threshold ordering;')
print('      %d independently generated exact-rate state checks.' % checked)
print('Certificate term counts:', {k:len(cert[k]) for k in ('minus_Haa','minus_Hbb','det_H')})
