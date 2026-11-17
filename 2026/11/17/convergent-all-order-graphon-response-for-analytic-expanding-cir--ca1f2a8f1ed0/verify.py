"""Reproduce exact first/second Fourier response for a two-block graphon.
Requires SymPy. This finite check is not a proof of all-order convergence.
"""
from fractions import Fraction
import sympy as S
pi,I=S.pi,S.I

def add(*polys):
    out={}
    for p in polys:
        for k,v in p.items(): out[k]=S.expand(out.get(k,0)+v)
    return {k:v for k,v in out.items() if S.simplify(v)!=0}

def mul(a,b):
    out={}
    for k,v in a.items():
        for j,w in b.items():out[k+j]=S.expand(out.get(k+j,0)+v*w)
    return {k:S.simplify(v) for k,v in out.items() if S.simplify(v)!=0}

def scale(a,c): return {k:S.expand(v*c) for k,v in a.items()}
def deriv(a,n=1): return {k:S.expand(v*(2*pi*I*k)**n) for k,v in a.items()}
def P(a): return {k//2:v for k,v in a.items() if k%2==0}
def diff(a,b): return add(a,scale(b,-1))
def zero(a): return all(S.simplify(v)==0 for v in a.values())

def sin(k):return {k:1/(2*I),-k:-1/(2*I)}
def cos(k):return {k:S.Rational(1,2),-k:S.Rational(1,2)}
W=[[S.Integer(1), S.Rational(1,4)], [S.Rational(1,4),S.Rational(1,2)]]
D=[S.simplify(sum(W[i][j] for j in range(2))/2) for i in range(2)]
E=[S.simplify(sum(W[i][j]*D[j] for j in range(2))/2) for i in range(2)]
assert D==[S.Rational(5,8),S.Rational(3,8)]
assert E==[S.Rational(23,64),S.Rational(11,64)]
for z in range(2):
    a0=scale(cos(2),D[z]); a1=scale(cos(2),pi*E[z])
    u1=scale(sin(1),2*pi*D[z])
    u2=add(scale(sin(1),2*pi*pi*E[z]),scale(add(cos(2),cos(1)),-4*pi*pi*D[z]**2))
    lhs1=diff(u1,P(u1)); rhs1=scale(deriv(P(a0)),-1)
    lhs2=diff(u2,P(u2))
    rhs2=add(scale(deriv(P(add(mul(a0,u1),a1))),-1),scale(deriv(P(mul(a0,a0)),2),S.Rational(1,2)))
    assert zero(diff(lhs1,rhs1)),(z,'first',diff(lhs1,rhs1))
    assert zero(diff(lhs2,rhs2)),(z,'second',diff(lhs2,rhs2))
    assert zero(P({k:v for k,v in u1.items() if k==0}))
    assert zero(P({k:v for k,v in u2.items() if k==0}))
print('VERIFY_OK', 'blocks=2', 'symbolic_fourier_equations=4', 'degree_profiles='+str(D), 'neighbor_degree_profiles='+str(E))
