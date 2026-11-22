"""Finite algebra and numerical diagnostics for product-walk source eigenvalues.

This is a reproducibility diagnostic, not a computer proof of any all-parameter
or infinite-dimensional assertion. Requires Python 3, sympy, scipy.
"""
from collections import defaultdict
from itertools import product
from math import exp
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import i0e
import sympy as S

checks = 0

def check(c, message):
    global checks
    assert bool(c), message
    checks += 1

def moment(jumps, d, k):
    cur = {(0,)*d: S.Integer(1)}
    for _ in range(k):
        nxt = defaultdict(lambda:S.Integer(0))
        for x,val in cur.items():
            for i in range(d):
                for dz, weight in jumps.items():
                    z = list(x)
                    z[i] += dz
                    nxt[tuple(z)] += val*S.Integer(weight)
        cur = nxt
    return cur.get((0,)*d,S.Integer(0))

families = [
    {-1:1, 1:1},
    {-1:2, 1:2},
    {-2:2,-1:1,1:1,2:2},
    {-3:1,-1:3,1:3,3:1},
]
for jumps in families:
    assert all(jumps.get(-z)==a for z,a in jumps.items())
    v = S.Integer(sum(a*a for a in jumps.values()))
    w = moment(jumps,1,3)
    u = moment(jumps,1,4)
    check(moment(jumps,1,2)==v,'one-coordinate second moment')
    for d in range(1,5):
        check(moment(jumps,d,1)==0,'first adjacency moment')
        check(moment(jumps,d,2)==d*v,'second moment factorization')
        check(moment(jumps,d,3)==d*w,'third moment factorization')
        check(moment(jumps,d,4)==d*u+3*d*(d-1)*v*v,'fourth moment factorization')

z,d,v,w,u = S.symbols('z d v w u')
a1=d*v
b2=d*w
c3=d*u+(d*d-3*d)*v*v
s=1/z+a1*z+b2*z*z+c3*z**3
G=1/s+a1/s**3+b2/s**4+(d*u+3*d*(d-1)*v*v)/s**5
check(S.simplify(S.series(G-z,z,0,6).removeO())==0,'formal resolvent reversion')
curv=S.simplify(c3-2*c3.subs(d,d+1)+c3.subs(d,d+2))
check(curv==2*v*v,'universal curvature coefficient')
check(c3.subs({v:2,w:0,u:6})==4*d*d-6*d,'nearest-neighbor coefficient')

# Independent Laplace-resolvent numerical diagnostics for the nearest-neighbor walk.
def green(lam,dimension,rate=1.):
    val,err = quad(lambda t:exp(-lam*t)*i0e(2*rate*t)**dimension,
                   0,float('inf'),epsabs=3e-12,epsrel=3e-12,limit=150)
    return val

def eigen(beta,dimension):
    return brentq(lambda lam:beta*green(lam,dimension)-1,
                  1e-8,beta,xtol=2e-12)

for beta in (10.,20.,40.,80.):
    e=[eigen(beta,k) for k in (2,3,4)]
    check(e[0]>e[1]>e[2]>0,'strict dimension decrease')
    diff=e[0]-2*e[1]+e[2]
    check(diff>0,'strict dimension convexity')
    check(all(abs(beta*green(x,i)-1)<1e-9 for x,i in zip(e,(2,3,4))),
          'resolvent roots')
    print('beta=',beta,'eigenvalues=',*[f'{x:.12f}' for x in e],
          'curvature=',format(diff,'.12g'),'beta^3 curvature=',f'{beta**3*diff:.9f}')

check(abs(80.**3*(e[0]-2*e[1]+e[2])-8.)<0.08,'high-intensity curvature diagnostic')
print('PASS',checks,'algebraic and numerical assertions')
