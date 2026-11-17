#!/usr/bin/env python3
"""Reproduce the algebra and sample fast-HMM Hopf shifts for a four-substrate cycle."""
import sympy as sp
import numpy as np
from scipy.optimize import brentq
s,z,eps=sp.symbols('s z eps', real=True)
a0,b0,g0=sp.symbols('alpha beta gamma', positive=True)
x1,x2,c1,c2,c3,A,B=sp.symbols('x1 x2 c1 c2 c3 A B')
tau=(a0+b0+g0)/(a0*g0)
e=sp.Rational(411,20)-c1-c2
x3=91+50*tau*eps-x1-x2-c1-c2-c3-eps*(A+B)
v1=2400*e*x1-sp.Rational(1,2)*c1
v2=sp.Rational(102,5)*e*x2-2*c2
F=sp.Matrix([-v1+g0*B,sp.Rational(5,2)*c1-v2,v1-sp.Rational(5,2)*c1,v2-100*c2,(s+5)*x3-(s+5)*c3,(5*c3-a0*A+b0*B)/eps,(a0*A-(b0+g0)*B)/eps])
y=sp.Matrix([x1,x2,c1,c2,c3,A,B]); eq={x1:sp.Rational(1,2),x2:50,c1:20,c2:sp.Rational(1,2),c3:10,B:50/g0,A:50*(b0+g0)/(a0*g0)}
assert all(sp.simplify(f.subs(eq))==0 for f in F)
J=F.jacobian(y).subs(eq)
J0=J[:5,:5].subs(eps,0)
J0[0,4]=5  # singular-limit transfer from C3 to X1
P=sp.factor((z*sp.eye(5)-J0).det(method='berkowitz'))
N=50*z**5+100*z**4*s+122801*z**4+244852*z**3*s+14332133*z**3+26827251*z**2*s+157881855*z**2+113030565*z*s+566682825*z+3181788000*s+15908940000
assert sp.simplify(P-N/50)==0
# The fast transfer matrix gives Q=1+tau*eps*z+eps**2*z**2/(alpha*gamma).
Q=1+tau*eps*z+eps**2*z**2/(a0*g0)
# At order eps, the effective slow Jacobian changes only in its fifth column.
J1=sp.zeros(5,5); J1[0,4]=-5*tau*z; J1[4,4]=-5*tau*(s+5)
M=z*sp.eye(5)-J0
Dchar=sp.Integer(0)
for j in range(5):
 C=M.copy(); C[:,j]=-J1[:,j]; Dchar+=C.det(method='berkowitz')
assert sp.simplify(Dchar+153000*tau*(400*z-1)*(s+5))==0
# Verify the transfer by directly eliminating the 2 fast columns from the full Jacobian.
# The fast-slow Schur complement at a sample rational parameter point equals the formula.
Jc=J.subs({a0:2,b0:3,g0:5,s:13,eps:sp.Rational(1,1000)})
zv=sp.Rational(17,3)
block=zv*sp.eye(2)-Jc[5:7,5:7]
Schur=Jc[:5,:5]+Jc[:5,5:7]*block.inv()*Jc[5:7,:5]
qv=Q.subs({a0:2,b0:3,g0:5,eps:sp.Rational(1,1000),z:zv})
tv=tau.subs({a0:2,b0:3,g0:5})
Expected=J0.subs(s,13)
Expected[0,4]=5/qv
Expected[4,4]=-36-5*sp.Rational(1,1000)*18*(tv+sp.Rational(1,1000)*zv/10)/qv
assert Schur==Expected
# Root isolation: the Hopf frequency squared t is the large positive root of this quartic.
t=sp.symbols('t');H=2500*t**4+13646747301*t**3+166084766332929*t**2-19531770063345000*t+2434067820000000
lo=sp.Rational(11636267,100000);hi=sp.Rational(11636268,100000)
assert H.subs(t,lo)<0<H.subs(t,hi)
assert sum(1 for (lr,m) in sp.polys.polytools.intervals(H,eps=sp.Rational(1,10000000)) if m==1 and lr[0]>116 and lr[1]<117)==1
import mpmath as mp
mp.mp.dps=55
T=mp.findroot(sp.lambdify(t,H,'mpmath'),(116,117))
SS=(50*T*T-14332133*T+566682825)/(244852*T-113030565)
WW=mp.sqrt(T); lam=1j*WW
PF=sp.lambdify((z,s),P,'mpmath');PL=sp.lambdify((z,s),sp.diff(P,z),'mpmath');PS=sp.lambdify((z,s),sp.diff(P,s),'mpmath')
baseR=-153000*(400*lam-1)*(SS+5)
le=-baseR/PL(lam,SS);ls=-PS(lam,SS)/PL(lam,SS)
co=-le.real/ls.real
freq=(le+co*ls).imag
assert abs(PF(lam,SS))<mp.mpf('1e-40')
assert mp.mpf(670)<co<mp.mpf(671) and mp.mpf(4)<freq<mp.mpf(5)
assert ls.real<0 and le.real>0
# Numerical full-Jacobian continuation at finite K, two independent rates triples.
for params in ((1,1,1),(2,3,5)):
 alpha,beta,gamma=params
 tauval=(alpha+beta+gamma)/(alpha*gamma)
 jf=sp.lambdify((s,eps),J.subs({a0:alpha,b0:beta,g0:gamma}),'numpy')
 def hopfval(ss,ee):
  vals=np.linalg.eigvals(np.array(jf(ss,ee),dtype=float))
  near=min(vals,key=lambda v:abs(v.imag-float(WW)))
  return near.real
 for K in (10000,100000,1000000):
  sh=brentq(lambda ss:hopfval(ss,1/K),float(SS)-0.5,float(SS)+1.0,xtol=2e-12)
  quotient=(sh-float(SS))*K/tauval
  tolerance=22 if K==10000 else (3 if K==100000 else 0.5)
  assert abs(quotient-float(co))<tolerance,(params,K,quotient)
 print('rate triple',params,'residence tau=',tauval,'sample 1/K slope=',quotient)
print('VERIFY_OK equilibria=1 exact_schur=1 base_charpoly=1 universal_first_order=1 isolated_Hopf=1 rates=2 finite_K=6')
print('Hopf_s',mp.nstr(SS,20),'Hopf_omega',mp.nstr(WW,20),'slope_per_tau',mp.nstr(co,20),'omega_per_tau',mp.nstr(freq,20))
