#!/usr/bin/env python3
"""Reproducibility checks for the growing-parameter superoscillation norm law.

Requirements: Python 3.10+, sympy 1.14+, mpmath 1.3+.
No external data. Finite tests corroborate but do not prove the asymptotic theorem.
"""
import sympy as sp
import mpmath as mp

r, c, y, z = sp.symbols('r c y z', real=True)
# With r=1/n, c*n*sin(y*sqrt(r))**2 has expansion
# c*y**2-c*y**4*r/3+O(r**2). Its logarithmic correction is q(y).
w = c * sp.sin(y * sp.sqrt(r))**2 / r
expansion = sp.series(w, r, 0, 2).removeO().expand()
assert sp.simplify(expansion - (c*y*y - c*y**4*r/3)) == 0
q = -c*y**4/(3*(1+c*y*y))
y_star_sq = (c-1)/c
assert sp.simplify(q.subs(y**4, y_star_sq**2).subs(y**2,y_star_sq) + (c-1)**2/(3*c**2)) == 0
f = -y*y + sp.log(1+c*y*y)
assert sp.simplify(sp.diff(f,y).subs(y**2,y_star_sq)) == 0 # check derivative symbolically after dividing by y
# Correct derivative and curvature identities at nonzero critical point.
assert sp.simplify((sp.diff(f,y)/y).subs(y**2,y_star_sq)) == 0
assert sp.simplify(sp.diff(f,y,2).subs(y**2,y_star_sq)+4*(c-1)/c) == 0
assert sp.simplify(f.subs(y**2,y_star_sq) - (sp.log(c)-1+1/c)) == 0
# Critical quartic coefficient from log(1+t).
t = sp.symbols('t', real=True)
assert sp.expand(sp.series(sp.log(1+t)-t,t,0,3).removeO()).coeff(t,2) == -sp.Rational(1,2)

mp.mp.dps = 48

def S(n,c):
    n, c = mp.mpf(n), mp.mpf(str(c))
    if c < 1:
        f = lambda x: mp.exp(-x*x + n*mp.log1p(c*n*mp.sin(x/n)**2))
        edges = [0,1,3,7,15]
        return 2/mp.sqrt(mp.pi)*sum(mp.quad(f,[a,b]) for a,b in zip(edges,edges[1:]))
    if c == 1:
        scale = n**mp.mpf('0.25')
        f = lambda u: mp.exp(-(scale*u)**2+n*mp.log1p(n*mp.sin(scale*u/n)**2))
        edges = [0,mp.mpf('.5'),1,2,4,8]
        return 2*scale/mp.sqrt(mp.pi)*sum(mp.quad(f,[a,b]) for a,b in zip(edges,edges[1:]))
    m = mp.sqrt((c-1)/c)
    f = lambda yy: mp.exp(n*(-yy*yy+mp.log1p(c*n*mp.sin(yy/mp.sqrt(n))**2)))
    edges = sorted(set([mp.mpf('0'),m/3, m, m+mp.mpf('.5'),2*m, max(8,4*m)]))
    return 2*mp.sqrt(n/mp.pi)*sum(mp.quad(f,[a,b]) for a,b in zip(edges,edges[1:]))

def asym(n,c):
    n, c = mp.mpf(n), mp.mpf(str(c))
    if c < 1: return 1/mp.sqrt(1-c)
    if c == 1: return (2**(-mp.mpf(3)/4)*mp.gamma(mp.mpf('0.25'))/mp.sqrt(mp.pi))*n**mp.mpf('0.25')
    return mp.sqrt(2*c/(c-1))*mp.exp(-(c-1)**2/(3*c*c))*mp.exp(n*(mp.log(c)-1+1/c))

case_results=[]
for cval in ['0.4','1','1.3','2','4']:
    ratios=[]
    for nval in (80,160,320):
        ratio = S(nval,cval)/asym(nval,cval)
        ratios.append(ratio)
    assert abs(ratios[-1]-1) < (mp.mpf('0.028') if cval in ('1','1.3') else mp.mpf('0.007'))
    assert abs(ratios[-1]-1) < abs(ratios[0]-1)
    case_results.append((cval, [mp.nstr(x,9) for x in ratios]))

print('SUPEROSCILLATION_NORM_VERIFY_PASS',len(case_results),'symbolic-identities=6')
for cval,ratios in case_results:
    print('parameter',cval,'ratios(n=80,160,320)',*ratios)
