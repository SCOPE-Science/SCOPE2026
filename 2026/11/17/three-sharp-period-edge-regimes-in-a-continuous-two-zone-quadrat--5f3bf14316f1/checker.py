#!/usr/bin/env python3
"""Standalone symbolic and numerical checks for the two-zone quadratic center.

Only standard Python plus SymPy and mpmath are required.  The proof in
RESULT.md, rather than this finite test, establishes asymptotic statements.
"""
import sympy as sp
import mpmath as mp

q,c,k=sp.symbols('q c k', real=True, positive=True)
u=sp.exp(-q)
U=(1-c)*q+(1-2*c)*(u-1)+c*(u**2-1)/2
assert sp.simplify(sp.diff(U,q)-(1-u)*(1-c*(1-u)))==0
assert sp.simplify(U.subs(q,0))==0
assert sp.simplify(sp.diff(U,q,2).subs(q,0)-1)==0
qs=sp.log(k/(k-1))
Es=1-1/(2*k)+(k-1)*sp.log(1-1/k)
assert sp.simplify(sp.expand_log((U.subs({c:k,q:qs})-Es),force=True))==0
assert sp.simplify(sp.diff(U,q).subs({c:k,q:qs}))==0
assert sp.simplify(sp.diff(U,q,2).subs({c:k,q:qs})+(k-1)/k)==0
# The critical potential and transformed equation are elementary identities.
assert sp.simplify(U.subs(c,1)-(1-u)**2/2)==0
x,y=sp.symbols('x y',real=True)
# q=-ln(1-y), qdot=y'=x(1-y) divided by (1-y).
assert sp.simplify((x*(1-y))/(1-y)-x)==0
# hamiltonian conservation in either zone, with dq/dt=x.
assert sp.simplify(x*(-y+c*y**2)+(y-c*y**2)*x)==0

mp.mp.dps=40

def potential(z,a):
    return (1-a)*z+(1-2*a)*mp.expm1(-z)+a/2*mp.expm1(-2*z)

def potential_s(z,a):
    # q>=0, high-precision numerically stable: integral of (1-e^-q)(1-a(1-e^-q)).
    return potential(z,a)

def bisect(f,lo,hi,n=130):
    flo=f(lo)
    for _ in range(n):
        m=(lo+hi)/2
        if (f(m)>0)==(flo>0):lo=m
        else:hi=m
    return (lo+hi)/2

def period_half(E,a,positive):
    if positive:
        lo,hi=mp.mpf(0),mp.mpf(1)
        if a>1:
            hi=mp.log(a/(a-1))
            barrier=1-1/(2*a)+(a-1)*mp.log(1-1/a)
            assert 0<E<barrier, (E, barrier)
        else:
            while potential(hi,a)<E:hi*=2
        qturn=bisect(lambda t:potential(t,a)-E,lo,hi)
        # q=sqrt transform at turning endpoint.
        f=lambda s:mp.sqrt(2)*2*qturn*s/mp.sqrt(max(mp.mpf('1e-65'),E-potential(qturn*(1-s*s),a)))
        return mp.quad(f,[0,mp.mpf('0.01'),mp.mpf('0.1'),1])
    else:
        lo=mp.mpf(-1)
        while potential(lo,a)<E:lo*=2
        qturn=bisect(lambda t:potential(t,a)-E,lo,mp.mpf(0))
        # integrate q=qturn+(0-qturn)*s^2 to regularize endpoint.
        L=-qturn
        f=lambda s:mp.sqrt(2)*2*L*s/mp.sqrt(max(mp.mpf('1e-65'),E-potential(qturn+L*s*s,a)))
        return mp.quad(f,[0,mp.mpf('0.01'),mp.mpf('0.1'),1])

# The quadrature is a supplementary consistency test, not a proof.
for a, b, E in [(mp.mpf('0.4'),mp.mpf('0.8'),mp.mpf('100')), (mp.mpf('1'),mp.mpf('0.7'),mp.mpf('0.4999')), (mp.mpf('2'),mp.mpf('0.7'),(mp.mpf('0.75')-mp.log(2))-mp.mpf('0.0000000001'))]:
    if a<1:limit=2*mp.sqrt(2*E)/(1-a)
    elif a==1:limit=mp.pi*mp.sqrt(2)/mp.sqrt(mp.mpf('0.5')-E)
    else:
        delta=(mp.mpf("0.75")-mp.log(2))-E
        limit=mp.sqrt(a/(a-1))*mp.log(1/delta)
    P=period_half(E,a,True)+period_half(E,b,False)
    assert P>0 and mp.isfinite(P)
    if limit is not None:assert mp.mpf('0.65')<P/limit<mp.mpf('1.5'),(a,P,limit)
print('PASS: symbolic potential, stationary point, curvature, energy and critical identities; three positive periods and edge comparisons')
