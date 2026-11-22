#!/usr/bin/env python3
"""Exact-rational, self-contained verification of three-site TASEP-LK jump statistics.

Run: python verify_counts.py
Requires: sympy; numpy is used only for an optional separate numerical check.
"""
import sympy as S

w = S.symbols('w', positive=True)
labels = ('in', 'ex', 'ad', 'de', 'hop')
Q = S.zeros(8)
J = {name: S.zeros(8) for name in labels}

for x in range(8):
    transitions = []
    if not x & 1:
        transitions.append((x | 1, S.Integer(1), 'in'))
    if x & 4:
        transitions.append((x & ~4, S.Integer(1), 'ex'))
    if not x & 2:
        transitions.append((x | 2, w, 'ad'))
    else:
        transitions.append((x & ~2, w, 'de'))
    for k in range(2):
        if x >> k & 1 and not x >> (k+1) & 1:
            transitions.append((x ^ (1 << k) ^ (1 << (k+1)), S.Integer(1), 'hop'))
    for y, rate, kind in transitions:
        Q[y, x] += rate
        Q[x, x] -= rate
        J[kind][y, x] += rate

one = S.ones(1, 8)
assert one * Q == S.zeros(1, 8)
A = Q.copy()
A[7,:] = one
rhs = S.zeros(8, 1)
rhs[7] = 1
Ainv = A.inv()
pi = Ainv * rhs
D = 9*w+7
G = 3*w*w+5*w+3
E = 2*w+1
expected_pi = S.Matrix([(E)/(2*D), (4*w+3)/(2*D),
                        (w+1)/D, (4*w+3)/(2*D),
                        (w+1)/(2*D), (w+1)/D,
                        (w+1)/(2*D), E/(2*D)])
assert all(S.cancel(x)==0 for x in pi-expected_pi)
assert all(S.cancel(x)==0 for x in Q*pi)
assert all(S.cancel(x)==0 for x in one*pi-S.ones(1,1))
means = {}
u = {}
for kind in labels:
    m = S.factor((one*J[kind]*pi)[0])
    v = (m*S.eye(8)-J[kind])*pi
    v[7] = 0
    means[kind] = m
    u[kind] = Ainv*v
    assert all(S.cancel(z)==0 for z in Q*u[kind]-(m*pi-J[kind]*pi))
    assert S.cancel((one*u[kind])[0])==0

expected_means = {'in':(6*w+5)/(2*D), 'ex':(6*w+5)/(2*D),
                  'ad':w/2, 'de':w/2, 'hop':(6*w+5)/D}
for kind in labels:
    assert S.cancel(means[kind]-expected_means[kind])==0, kind

cross = {}
for i, a in enumerate(labels):
    for b in labels[i+1:]:
        cross[a,b] = S.factor((one*(J[a]*u[b]+J[b]*u[a]))[0])

six_cross = {
('in','ex'): (576*w**5+2584*w**4+4826*w**3+4597*w**2+2212*w+429)/(4*E*D**3*G),
('in','hop'): (270*w**3+687*w**2+556*w+143)/(2*D**3),
('ad','hop'): -3*w/(2*D**2),
('ad','de'): w**2*(54*w**3+139*w**2+134*w+47)/(4*E*D*G),
('ex','ad'): w*(180*w**4+626*w**3+866*w**2+555*w+138)/(4*E*D**2*G),
('in','ad'): -w*(180*w**4+662*w**3+944*w**2+621*w+156)/(4*E*D**2*G),
}
expected_cross = {
 ('in','ex'): six_cross['in','ex'],
 ('in','ad'): six_cross['in','ad'],
 ('in','de'): six_cross['ex','ad'],
 ('in','hop'): six_cross['in','hop'],
 ('ex','ad'): six_cross['ex','ad'],
 ('ex','de'): six_cross['in','ad'],
 ('ex','hop'): six_cross['in','hop'],
 ('ad','de'): six_cross['ad','de'],
 ('ad','hop'): six_cross['ad','hop'],
 ('de','hop'): six_cross['ad','hop'],
}
assert set(expected_cross)==set(cross)
for pair in cross:
    assert S.cancel(cross[pair]-expected_cross[pair])==0, pair
    numer,denom=S.fraction(S.cancel(expected_cross[pair]))
    pn=S.Poly(numer,w); pd=S.Poly(denom,w)
    assert all(c>=0 for c in pn.all_coeffs()) or all(c<=0 for c in pn.all_coeffs())
    assert all(c>=0 for c in pd.all_coeffs())

F={a:S.factor(1+2*(one*J[a]*u[a])[0]/means[a]) for a in labels}
Fx=(3240*w**6+14688*w**5+27890*w**4+28080*w**3+15475*w**2+4270*w+429)/(2*E*(6*w+5)*D**2*G)
Fa=(54*w**4+179*w**3+246*w**2+161*w+42)/(2*E*D*G)
Fh=(270*w**3+687*w**2+556*w+143)/((6*w+5)*D**2)
for a, form in [('in',Fx),('ex',Fx),('ad',Fa),('de',Fa),('hop',Fh)]:
    assert S.cancel(F[a]-form)==0, a

dFx=S.factor(S.diff(Fx,w))
dFa=S.factor(S.diff(Fa,w))
dFh=S.factor(S.diff(Fh,w))
assert S.cancel(dFh+4*(567*w**3+711*w**2+24*w-146)/((6*w+5)**2*D**3))==0
assert all(z>0 for z in S.Poly(S.fraction(dFx)[0],w).all_coeffs())
assert all(z<0 for z in S.Poly(S.fraction(dFa)[0],w).all_coeffs())
assert all(z>0 for z in S.Poly(S.fraction(dFx)[1],w).all_coeffs())
assert all(z>0 for z in S.Poly(S.fraction(dFa)[1],w).all_coeffs())
p=S.Poly(567*w**3+711*w**2+24*w-146,w)
assert p.eval(0)<0 and p.eval(1)>0
assert all(c>0 for c in S.Poly(S.diff(p.as_expr(),w),w).all_coeffs())
root=S.nsolve(p.as_expr(),S.Rational(2,5))
assert S.Rational(3838,10000) < root < S.Rational(3840,10000)
print('Verified stationary distribution, five mean count rates, ten covariances, five Fano factors,')
print('strict cross-covariance signs and derivatives, unique hopping-noise maximum.')
print('hopping extremum location =', root)
print('hopping extremum Fano =', S.N(Fh.subs(w,root),15))
print('Fano limits: injection/extraction:', S.limit(Fx,w,0),S.limit(Fx,w,S.oo))
print('Fano limits: adsorption/desorption:', S.limit(Fa,w,0),S.limit(Fa,w,S.oo))
print('Fano limits: hopping:', S.limit(Fh,w,0),S.limit(Fh,w,S.oo))

try:
    import numpy as np
    from scipy.linalg import eigvals
    for w0 in (0.3,2.0):
        q=np.asarray(Q.subs(w,w0)).astype(float)
        js={a:np.asarray(J[a].subs(w,w0)).astype(float) for a in labels}
        h=1e-3
        def scgf(fields):
            tilted=q.copy()
            for a,z in fields.items(): tilted+=(np.exp(z)-1)*js[a]
            return max(eigvals(tilted).real)
        for a,b in (('in','ex'),('ex','ad'),('in','ad'),('ad','hop')):
            fd=(scgf({a:h,b:h})-scgf({a:h,b:-h})-scgf({a:-h,b:h})+scgf({a:-h,b:-h}))/(4*h*h)
            exact=float(cross[a,b].subs(w,w0))
            assert abs(fd-exact)<3e-5,(w0,a,b,fd,exact)
    print('Separate tilted-generator eigenvalue finite differences: passed.')
except ImportError:
    print('Optional independent SciPy finite-difference check skipped (SciPy unavailable).')
