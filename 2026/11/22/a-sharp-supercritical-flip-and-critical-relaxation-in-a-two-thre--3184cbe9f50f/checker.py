"""Reproduce algebraic checks for a two-threshold planar affine relay.
Run: python checker.py (requires SymPy; mpmath is installed with SymPy).
The rigorous proof is in RESULT.md; these tests corroborate its identities.
"""
import sympy as S
from mpmath import mp

z, X = S.symbols('z X', positive=True, real=True)
p = z-1
q = (z-1)*(z+2)/((z-2)*(z+1))
T = 1-S.sqrt(1+2*S.sqrt(X**2+4*z)+X**2-4*z)
assert S.simplify(T.subs(X,p)-p) == 0 or S.simplify(T.subs(X,p)-p).subs(z,S.Rational(3,2)) == 0
zc=S.sqrt(2)
Tc=T.subs(z,zc)
pc=zc-1
for order, target in [(1,-1),(2,-12+8*S.sqrt(2)),(3,-480+342*S.sqrt(2))]:
    actual=S.diff(Tc,X,order).subs(X,pc)
    assert S.simplify(S.radsimp(actual-target)) == 0, (order,actual,target)
assert S.simplify(S.diff(q,z).subs(z,zc)+4) == 0
B=S.simplify(S.diff(Tc,X,3).subs(X,pc)/6 + (S.diff(Tc,X,2).subs(X,pc)/2)**2)
assert S.nsimplify(B,[S.sqrt(2)]) == 9*S.sqrt(2)-12
assert float(B)>0
for mu in [S.Rational(1,2),S.Rational(2),S.Rational(5),S.Rational(11,2),S.Rational(6),S.Rational(7)]:
    xp=mu/2-2; xs=-mu/2-2
    assert S.simplify(xs**2-xp**2-4*mu)==0
    H=lambda t:t-t*t/4
    assert S.simplify(H(xp)-H(xs)-2*mu)==0
    assert float(xp)<2 and float(xs)<float(xp)
    zz=mu/4
    assert abs(float(T.subs({z:zz,X:xp/2}) - xp/2))<1e-12
mp.dps=65
znum=mp.sqrt(2)
muc=4*znum
Bnum=9*znum-12
f=lambda x,mu: 2-mp.sqrt(4+4*mp.sqrt(x*x+4*mu)+x*x-4*mu)
for delta in [mp.mpf('0.004'),mp.mpf('0.002')]:
    mu=muc+delta
    pnum=mu/2-2
    x=pnum+mp.mpf('0.2')
    for _ in range(30000): x=f(x,mu)
    xnext=f(x,mu)
    assert abs(xnext-x)>mp.mpf('0.001')
    assert abs(f(xnext,mu)-x)<mp.mpf('1e-12')
    predicted=2*mp.sqrt(delta/Bnum)
    assert abs(abs(x-pnum)-predicted) < mp.mpf('0.025')
# Critical reciprocal-square coefficient, finite n as supporting evidence.
x=2*(znum-1)+mp.mpf('0.15')
pnum=2*(znum-1)
for n in range(1,30001):
    x=f(x,muc)
assert abs(30000*(x-pnum)**2-2/Bnum)<mp.mpf('0.03')
print('All exact derivative, fixed-point, transversality, and supplementary orbit tests passed.')
print('Critical cubic coefficient B:',9*S.sqrt(2)-12)
print('Critical n*(x_n-p)^2 limit:',2/Bnum)
