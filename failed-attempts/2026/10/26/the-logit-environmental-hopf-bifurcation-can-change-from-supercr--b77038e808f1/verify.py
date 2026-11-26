#!/usr/bin/env python3
"""Independent exact-symbolic checks for logit environmental Hopf criticality."""
import sympy as S
from fractions import Fraction

p,q,A,w=S.symbols('p q A omega', positive=True)
# Here q and A are formal real quantities despite positive=True, which does not influence simplification.
fu=q/p
fw=q*w*w/p
fuw=w*(A-q/p)
fuuu=(q*q-2*p)/p**2
fuww=(q*q-2*p)*w*w/p**2-2*A*q*w*w/p
L=S.factor((fuuu+fuww+fuw*(fu+fw)/w)/16)
assert S.factor((L-(-2*(1+w*w)+A*q*(1-w*w))/(16*p)).subs(p,(1-q*q)/4))==0

# Check the same formula by averaging polar derivatives independently.
c,s,om=S.symbols('c s om',real=True)
f20,f11,f02,f30,f12,g11,g12=S.symbols('f20 f11 f02 f30 f12 g11 g12',real=True)
F2=f20*c*c+f11*c*s+f02*s*s
G2=g11*c*s
F3=f30*c**3+f12*c*s*s
G3=g12*c*s*s
rr=S.expand(c*F2+s*G2)
ang=S.expand(c*G2-s*F2)
cub=S.expand(c*F3+s*G3)
raw=S.expand(cub-rr*ang/om)
mean=0
for t in S.Add.make_args(raw):
 ex=t.as_powers_dict(); i=int(ex.get(c,0)); j=int(ex.get(s,0))
 if i%2==0 and j%2==0:
  mean+=(t/c**i/s**j)*(S.factorial2(i-1)*S.factorial2(j-1)/S.factorial2(i+j) if i+j else 1)
assert S.simplify(mean-(f02*f11+f11*f20+om*(f12+3*f30))/(8*om))==0
sub={f20:fu/2, f11:fuw,f02:fw/2,f30:fuuu/6,f12:fuww/2,om:w}
assert S.simplify(mean.subs(sub)-L)==0

th,h,r,t,v=S.symbols('theta h r t v',real=True)
k=1+th; D=r+t+th*(v-h); a=v-h-r-t
pp=th/k**2; qq=(th-1)/k
Q=S.factor(a*(th-1)/D)
assert S.factor(2*D-a*(th-1))== k*(r+t+v-h)
assert S.simplify(D*(Q+2)-((3-th)*(r+t)+(3*th-1)*(v-h)))==0

# Exact enclosures using alternating rational bounds on log(5) through atanh:
# log(5) = 2 * sum_{j>=0} (2/3)^(2j+1)/(2j+1)
# The omitted tail is <= 2*z^(2N+1)/((2N+1)*(1-z*z)).
z=S.Rational(2,3); N=70
lo=2*sum((z**(2*j+1))/S.Integer(2*j+1) for j in range(N))
hi=lo+2*z**(2*N+1)/(S.Integer(2*N+1)*(1-z*z))
assert lo> S.Rational(1609,1000) and hi<S.Rational(161,100)

def critical(theta,hh,rr,tt,vv,ll):
 kk=1+theta;DD=rr+tt+theta*(vv-hh); aa=vv-hh-rr-tt
 P=theta/kk**2; Q0=aa*(theta-1)/DD
 M=kk*(rr*vv+hh*tt)/DD
 beta=(1/P+aa*kk*ll/DD)/M
 ni=(rr-theta*hh-kk*ll/beta)/DD
 kap=beta*DD*P*ni*(1-ni)
 return S.factor(beta),S.factor(ni),S.factor(kap),S.factor(Q0)
# Interval certificate via derivative monotonicity on short rational intervals and substitution endpoints.
th0=S.Rational(1,5); par=(th0,S.Integer(1),S.Integer(2),S.Integer(1),S.Integer(100))
for val in [lo,hi]:
 bh,nh,kapa,qqq=critical(*par,val)
 assert 0<nh<S.Rational(1,10)
 assert S.Rational(9,100)<kapa<S.Rational(1,10)
 assert bh>S.Rational(6,5)
 assert qqq==-S.Rational(64,19)
# Entire interval certified by rational interval arithmetic on basic positive terms.
def I(x): return (x,x)
def add(X,Y): return(X[0]+Y[0],X[1]+Y[1])
def neg(X):return(-X[1],-X[0])
def mult(X,Y):
 vals=[aa*bb for aa in X for bb in Y]
 return (min(vals),max(vals))
def div(X,Y):
 assert Y[0]>0 or Y[1]<0
 return mult(X,(1/Y[1],1/Y[0]))
K=(lo,hi)
# beta=228/335+32*L/67, n=(9/5-(6/5)*L/beta)/(114/5)
BB=add(I(S.Rational(228,335)),mult(I(S.Rational(32,67)),K))
NN=div(add(I(S.Rational(9,5)),neg(div(mult(I(S.Rational(6,5)),K),BB))),I(S.Rational(114,5)))
CAP=mult(mult(mult(BB,I(S.Rational(114,5)*S.Rational(5,36))),NN),add(I(1),neg(NN)))
assert S.Rational(9,100)<CAP[0]<=CAP[1]<S.Rational(1,10)
# At epsilon=1: 13*kap<13/10 <51; epsilon=100: 1300*kap>117 >51.
assert S.Rational(13,1)*CAP[1]<51 and 1300*CAP[0]>51
# Numeric reference cross-check
B,Nn,KK,QQ=critical(S.Rational(4,5),S.Rational(1,2),S.Rational(3,2),S.Rational(1,2),S.Rational(1,4),S.log(S.Rational(5,4)))
assert QQ==S.Rational(1,4)
assert 0<float(Nn)<1 and float(B)>0
assert S.simplify((-2*(1+w*w)+QQ*(1-w*w))/(16*S.Rational(20,81))+81*(7+9*w*w)/1280)==0
print('PASS: symbolic Lyapunov formula, independent polar averaging, payoff sign phase, source example, exact log(5) enclosures, subcritical counterexample.')
print('rational interval of kappa:',*[str(S.N(x,12)) for x in CAP])
