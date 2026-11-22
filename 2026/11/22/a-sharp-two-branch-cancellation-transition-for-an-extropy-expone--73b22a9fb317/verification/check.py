"""Independent symbolic and numerical checks for the two-uniform NDSE contrast.

Requirements: Python 3.10+, sympy, mpmath. This verifies finite algebra and
integrals; the global root-count and CLT arguments are proved in RESULT.md.
"""
import itertools
from fractions import Fraction
import math
import random
import sympy as s
import mpmath as mp

p, b, x = s.symbols('p b x', real=True)
c = p+(1-p)/b
Slo = 1-c*x
Shi = (1-p)*(1-x/b)
I = s.integrate(Slo**3,(x,0,1))+s.integrate(Shi**3,(x,1,b))
mu=(p+(1-p)*b)/2
D=s.factor(mu-3*I)
P= s.expand(4*b*b*D)
P_expected=(3*b**3-9*b**2+9*b-3)*p**3+(-9*b**3+24*b**2-21*b+6)*p**2+(7*b**3-16*b**2+12*b-3)*p-b**3
Q=32*b**4-144*b**3+39*b**2+18*b-9
checks=0
def check(q, note):
    global checks
    assert bool(q), note
    checks += 1

check(s.simplify(P-P_expected)==0, 'exact survival integral polynomial')
check(s.factor(s.discriminant(P,p)-3*b*b*(b-1)**6*Q)==0, 'cubic discriminant')
check(s.factor(D.subs(p,0)+b/4)==0, 'large-uniform endpoint')
check(s.factor(D.subs(p,1)+s.Rational(1,4))==0, 'small-uniform endpoint')
check(s.expand(Q.subs(b,1+s.Symbol('t'))) == 32*s.Symbol('t')**4-16*s.Symbol('t')**3-201*s.Symbol('t')**2-208*s.Symbol('t')-64, 'threshold shift')
check(s.factor(D.subs({p:s.Rational(1,2),b:6})-s.Rational(89,384))==0, 'exact positive witness')
check(s.factor(D.subs(b,6)-(125*p**3-400*p**2+335*p-72)/48)==0,'b6 cubic')

mp.mp.dps=65
bc=mp.findroot(s.lambdify(b,Q,'mpmath'),(mp.mpf('4.1'),mp.mpf('4.3')))
pc=mp.findroot(lambda pp: s.lambdify((p,b),s.diff(D,p),'mpmath')(pp,bc),mp.mpf('.60'))
Db=s.lambdify((p,b),s.diff(D,b),'mpmath')(pc,bc)
Dpp=s.lambdify((p,b),s.diff(D,p,2),'mpmath')(pc,bc)
K=mp.sqrt(-2*Db/Dpp)
check(abs(s.lambdify((p,b),D,'mpmath')(pc,bc))<mp.mpf('1e-52'),'double zero')
check(abs(s.lambdify((p,b),s.diff(D,p),'mpmath')(pc,bc))<mp.mpf('1e-52'),'double stationary')
check(Dpp<0 and Db>0 and K>0, 'square-root onset')
check(mp.mpf('4.18')<bc<mp.mpf('4.181'), 'critical ratio')
check(mp.mpf('.597')<pc<mp.mpf('.598'),'critical mixture')

roots=s.polys.polytools.intervals(P.subs(b,6),eps=s.Rational(1,10**13))
check(len(roots)==3,'three real roots at six')
rootnums=[]
for (a,z),mult in roots:
    r=mp.mpf(str(a.p))/mp.mpf(str(a.q)) if a==z else (mp.mpf(str(a.p))/a.q+mp.mpf(str(z.p))/z.q)/2
    rootnums.append(r)
check(0<rootnums[0]<rootnums[1]<1<rootnums[2], 'two interior zeros at six')
check(abs(rootnums[0]-mp.mpf('0.33468469733745'))<mp.mpf('1e-10'), 'first root')
check(abs(rootnums[1]-mp.mpf('0.85691019734991'))<mp.mpf('1e-10'), 'second root')

# Fixed-sample direct U-statistic identity for a deterministic sample.
def U(sample):
    triples=list(itertools.combinations(sample,3))
    return sum(sum(z)/3-3*min(z) for z in triples)/len(triples)
for n in [3,4,5,8]:
    for j in range(7):
        rng=random.Random(37*n+j)
        sample=[rng.random()*6 for _ in range(n)]
        direct=sum(sample)/n-3*sum(min(z) for z in itertools.combinations(sample,3))/math.comb(n,3)
        check(abs(U(sample)-direct)<2e-13, 'U-statistic kernel')

# Alternative CLT projection H(x)=x-9 E[min(x,X2,X3)], with G=integral of S^2.
b6=s.Integer(6)
r=(5*p+1)/6
rhi=(1-p)/6
Glo=x-r*x*x+r*r*x**3/3
Ghi=Glo.subs(x,1)+(1-p)**2*((x-1)-(x*x-1)/6+(x**3-1)/108)
Hlo=x-9*Glo
Hhi=x-9*Ghi
EH=s.factor(r*s.integrate(Hlo,(x,0,1))+rhi*s.integrate(Hhi,(x,1,6)))
EH2=s.factor(r*s.integrate(Hlo*Hlo,(x,0,1))+rhi*s.integrate(Hhi*Hhi,(x,1,6)))
VarH=s.factor(EH2-EH**2)
check(s.simplify(EH-(125*p**3-400*p**2+415*p-168)/16)==0,'projection mean')
check(s.simplify(VarH+(1640625*p**6-8125000*p**5+14743750*p**4-11518000*p**3+2940825*p**2+653240*p-345024)/26880)==0,'projection variance')

p_f=s.lambdify(p,P.subs(b,6),'mpmath')
var_f=s.lambdify(p,VarH,'mpmath')
for index,guess in enumerate([mp.mpf('.33'),mp.mpf('.86')]):
    pp=mp.findroot(p_f,guess)
    mu0=3-mp.mpf(5)*pp/2
    variance=var_f(pp)/mu0**2
    z=mp.sqrt(2)*mp.erfinv(2*mp.mpf('.05')-1)
    power=mp.erfc(-z*mp.sqrt(mp.mpf('0.8')/variance)/mp.sqrt(2))/2
    check(variance>0, 'strict alternative variance')
    check(abs(p_f(pp))<mp.mpf('1e-50'),'exact root residual')
    if index==0:
        check(abs(variance-mp.mpf('.60103119368594'))<mp.mpf('1e-11'),'first variance')
        check(abs(power-mp.mpf('.0288689045081563'))<mp.mpf('1e-11'),'first limit rejection')
    else:
        check(abs(variance-mp.mpf('1.41841748723468'))<mp.mpf('1e-11'),'second variance')
        check(abs(power-mp.mpf('.108360616550845'))<mp.mpf('1e-11'),'second limit rejection')
    print('weight',index+1,'p=',mp.nstr(pp,18),'variance=',mp.nstr(variance,18),'alpha.05 limit=',mp.nstr(power,18))

# Exact survival integral versus direct numerical quadrature, independently.
for bb in [s.Rational(3,2),s.Integer(4),s.Integer(5),s.Integer(6),s.Integer(10)]:
  for pp in [s.Rational(1,4),s.Rational(1,2),s.Rational(3,4)]:
    cm=pp+(1-pp)/bb
    quad=mp.quad(lambda y:(1-float(cm)*y)**3,[0,1])+mp.quad(lambda y:(1-float(pp))**3*(1-y/float(bb))**3,[1,float(bb)])
    exact=mp.mpf(str(s.N(I.subs({b:bb,p:pp}),40)))
    check(abs(quad-exact)<mp.mpf('1e-12'),'direct numerical integration')
print('bcritical=',mp.nstr(bc,22),'pcritical=',mp.nstr(pc,22),'onset=',mp.nstr(K,19))
print(checks,'checks passed')
