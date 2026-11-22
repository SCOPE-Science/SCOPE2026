#!/usr/bin/env python3
"""Exact rational verification of a coexistence-capacity theorem for a behavioral SIRS system.
Run with CPython 3; no nonstandard dependencies. This program checks the rational example,
not the general concavity argument given in the accompanying mathematical proof.
"""
from fractions import Fraction as F
from itertools import permutations

p = dict(a=F(1,2),e=F(1,2),beta=F(3), gamma=F(2,3),mu=F(1,3),delta=F(1,3),xi=F(4,3),c=F(41,140),kappa=F(169,420),epsilon=F(1,10))

def b(x): return (1-p['a']*x)*(1-p['e']*x)
def bp(x): return -p['a']*(1-p['e']*x)-p['e']*(1-p['a']*x)
def alpha(x,I): return -p['c']+p['a']*p['xi']*p['beta']*I*(1-p['e']*x)+p['kappa']*(2*x-1)
def f(S,I,x):
    beta=p['beta']; mu=p['mu']; gamma=p['gamma']; delta=p['delta']
    return (mu-beta*b(x)*S*I+delta*(1-S-I)-mu*S, beta*b(x)*S*I-(gamma+mu)*I, p['epsilon']*x*(1-x)*alpha(x,I))
def jac(S,I,x):
    beta=p['beta']; mu=p['mu']; gamma=p['gamma']; delta=p['delta']; eps=p['epsilon']
    c=p['a']*p['xi']*beta*(1-p['e']*x)
    a_x=-p['a']*p['xi']*beta*I*p['e']+2*p['kappa']
    z=eps*x*(1-x)
    return [[-beta*b(x)*I-delta-mu,-beta*b(x)*S-delta,-beta*bp(x)*S*I],
            [beta*b(x)*I, beta*b(x)*S-gamma-mu, beta*bp(x)*S*I],
            [F(0),z*c, eps*(1-2*x)*alpha(x,I)+z*a_x]]
def det(M):
    n=len(M)
    return sum(((-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n)))*prod(M[i][perm[i]] for i in range(n)) for perm in permutations(range(n)))
def prod(v):
    z=F(1)
    for x in v:z*=x
    return z

def char_coeffs(M):
    trace=sum(M[i][i] for i in range(3))
    C1=-trace
    C2=M[0][0]*M[1][1]-M[0][1]*M[1][0]+M[0][0]*M[2][2]-M[0][2]*M[2][0]+M[1][1]*M[2][2]-M[1][2]*M[2][1]
    C3=-det(M)
    return C1,C2,C3

rho=p['beta']/(p['gamma']+p['mu'])
K=(p['delta']+p['mu'])/(p['delta']+p['mu']+p['gamma'])
def endemic(x): return K*(1-F(1)/(rho*b(x)))
def G(x): return alpha(x,endemic(x))
def Gp(x):
    # Analytic derivative of -c-k+2kx + P(1-ex)-P/[rho(1-ax)]
    P=p['a']*p['xi']*p['beta']*K
    return 2*p['kappa']-P*p['e'] - P*p['a']/(rho*(1-p['a']*x)**2)

equilibria=[
   ('disease_free_no_adherence',(F(1),F(0),F(0))),
   ('endemic_no_adherence',(F(1,3),F(1,3),F(0))),
   ('lower_endemic_partial',(F(64,147),F(83,294),F(1,4))),
   ('upper_endemic_partial',(F(64,75),F(11,150),F(3,4))),
   ('disease_free_partial',(F(1),F(0),F(146,169))),
   ('disease_free_full_adherence',(F(1),F(0),F(1))),
]
assert rho==3 and K==F(1,2)
assert p['a']*p['xi']*p['beta']*K==1
# Both sides have, after multiplication by (2-x), polynomials of degree at most two.
# Three distinct rational evaluations therefore certify the entire factorization.
def Gfact(x): return F(2)*(4*x-3)*(4*x-1)/(F(105)*(x-2))
for z in [F(0), F(1,4), F(1,2), F(3,4), F(1)]:
    assert G(z)==Gfact(z),(z,G(z),Gfact(z))
assert G(F(1,4))==G(F(3,4))==0
assert Gp(F(1,4))>0 and Gp(F(3,4))<0
assert alpha(F(146,169),F(0))==0
assert alpha(F(0),endemic(F(0)))==F(-1,35)
assert alpha(F(1),F(0))==F(23,210)
print('Rho =',rho,', K =',K,'; G roots = [1/4,3/4]; cutoff infection x < 2-2/sqrt(3)')
for name,eq in equilibria:
    S,I,x=eq
    assert S>=0 and I>=0 and 1-S-I>=0 and 0<=x<=1
    assert f(*eq)==(0,0,0),(name,f(*eq))
    C1,C2,C3=char_coeffs(jac(*eq))
    det_rhs=p['epsilon']*x*(1-x)*p['beta']*b(x)*I*(p['mu']+p['delta']+p['gamma'])*Gp(x) if 0<x<1 and I>0 else 0
    if det_rhs: assert det(jac(*eq))==det_rhs
    sink=(C1>0 and C2>0 and C3>0 and C1*C2>C3)
    print(name,'point:',eq,'char c1,c2,c3:',(C1,C2,C3),'RH gap:',C1*C2-C3,'sink?',sink)
    if name in {'endemic_no_adherence','upper_endemic_partial','disease_free_full_adherence'}:assert sink
    else: assert not sink

assert char_coeffs(jac(*equilibria[3][1]))==(F(248267,336000), F(8989,84000), F(11,42000))
assert char_coeffs(jac(*equilibria[2][1]))==(F(614017,470400), F(20281,23520), -F(83,58800))
assert char_coeffs(jac(*equilibria[3][1]))[0]*char_coeffs(jac(*equilibria[3][1]))[1]-char_coeffs(jac(*equilibria[3][1]))[2] == F(2224280063,28224000000)
print('PASS: six exact physical equilibria, three sinks, exact Routh-Hurwitz margins, Jacobian reduction.')
