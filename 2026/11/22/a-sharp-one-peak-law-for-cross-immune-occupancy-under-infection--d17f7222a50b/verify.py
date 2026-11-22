"""Exact and numerical checks for a cross-immune occupancy theorem.
Run: python verify.py  (requires SymPy; SciPy optional for numeric checks).
"""
import sympy as s
from random import Random
m, a, b, d, g, k, c = s.symbols('m a b d g k c', positive=True)
p = 1-(m+a)/b
I = (m*p+g*k*c)/(m+a)
R=p-I-c
Q=s.factor(b*g*c**2+(d*g*k+(d+g)*(m+a)+m*b/k)*c-d*a*p)
# Direct residual identity (no division by potentially vanishing expressions)
assert s.factor((d*k*R-c*(b*I+m+g*k)) + k*Q/(m+a))==0
S=(m+a)/b
assert s.factor((m*(1-S)-b*S*I+g*k*c))==0
assert s.factor(b*S*I-(m+a)*I)==0
assert s.factor(R+I+c+S-1)==0
H=d*g*k+(d+g)*(m+a)+m*b/k
Cprime=-c*s.diff(H,k)/(2*b*g*c+H)
assert s.factor(s.diff(H,k)-(d*g-m*b/k**2))==0
# Exact instance: no reinfection and a finite peak at k=2
pp={m:1,a:1,b:4,d:1,g:1}
assert s.simplify(p.subs(pp)-s.Rational(1,2))==0
h1=s.simplify(H.subs(pp).subs(k,1));h2=s.simplify(H.subs(pp).subs(k,2))
c0=(s.sqrt(89)-9)/8
c2=(3*s.sqrt(2)-4)/4
assert s.simplify((b*g*c*c+H*c-d*a*p).subs(pp).subs({k:1,c:c0}))==0
assert s.simplify((b*g*c*c+H*c-d*a*p).subs(pp).subs({k:2,c:c2}))==0
istar=s.simplify(I.subs(pp).subs({k:2,c:c2}))
assert s.simplify(istar-3*(s.sqrt(2)-1)/4)==0
assert s.simplify(1/istar-4*(s.sqrt(2)+1)/3)==0
assert c2>c0 and c0>0
# Independent stationary residual checks for 60 rational admissible sets.
rng=Random(43)
for _ in range(60):
    mm=s.Rational(rng.randint(1,5),rng.randint(1,4))
    aa=s.Rational(rng.randint(1,5),rng.randint(1,4))
    bb=mm+aa+s.Rational(rng.randint(1,8),rng.randint(1,3))
    dd=s.Rational(rng.randint(1,5),rng.randint(1,4))
    gg=s.Rational(rng.randint(1,5),rng.randint(1,4))
    kk=s.Rational(rng.randint(1,15),rng.randint(1,4))+1
    subs={m:mm,a:aa,b:bb,d:dd,g:gg,k:kk}
    hh=H.subs(subs); EE=(d*a*p).subs(subs); AA=(b*g).subs(subs)
    cc=s.simplify(2*EE/(hh+s.sqrt(hh*hh+4*AA*EE)))
    zz=I.subs(subs).subs(c,cc)
    rr=R.subs(subs).subs(c,cc)
    assert all(float(z)>0 for z in [cc,zz,rr])
    assert abs(float((d*k*R-c*(b*I+m+g*k)).subs(subs).subs(c,cc))) <1e-15
    assert float(zz)<float(p.subs(subs))
print('SYMBOLIC_IDENTITIES_PASS, EXACT_PEAK_PASS, RATIONAL_CASES=60, ALL_CHECKS_PASS')
# Independent proof ingredients for monotonicity of the prevalence root.
eps,z,G=s.symbols('eps z G',nonnegative=True)
Dg=(m+d*G)*(m+g*G)+b*z*m
Kg=b*z+m+(d+g)*G
assert s.simplify(s.diff(Kg,G)*Dg-Kg*s.diff(Dg,G)+G*d*g*(G*(d+g)+2*b*z+2*m))==0
D_eps=s.expand(Dg.subs(G,1+eps*z));K_eps=s.expand(Kg.subs(G,1+eps*z))
d0=(m+d)*(m+g); d1=eps*(d*(m+g)+g*(m+d))+b*m; d2=d*g*eps**2
k0=m+d+g;k1=b+eps*(d+g)
assert s.simplify(D_eps-(d0+d1*z+d2*z*z))==0
assert s.simplify(K_eps-(k0+k1*z))==0
assert s.factor(k1*d1-k0*d2-(b*b*m+2*b*eps*(m*(d+g)+d*g)+eps**2*(m*(d*d+d*g+g*g)+d*g*(d+g))))==0
print('MONOTONICITY_IDENTITIES_PASS')
