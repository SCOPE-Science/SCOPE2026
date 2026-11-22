"""Check algebra and reproducible examples for an idealized two-zone tracer model.
Finite numerical tests supplement, rather than replace, the analytical argument.
Requires sympy and mpmath. Run: python verify.py
"""
import sympy as sp
import mpmath as mp

z,a,b,u,v,S1,S2=sp.symbols('z a b u v S1 S2')
M=sp.Matrix([[z+a+u,-u],[-v,z+b+v]])
L=sp.factor((sp.Matrix([[1,-1]])*M.inv()*sp.Matrix([S1,S2]))[0]/z)
expected=( (S1-S2)*z+b*S1-a*S2 )/(z*(z*z+(a+b+u+v)*z+a*b+a*v+b*u))
assert sp.simplify(L-expected)==0
assert sp.simplify(z*L - (z*(S1-S2)+b*S1-a*S2)/(z*z+(a+b+u+v)*z+a*b+a*v+b*u))==0

# Exact example a=4,b=1,u=v=2,S1=2,S2=1.
t=sp.symbols('t',nonnegative=True)
D0=(14*sp.exp(-2*t)-9*sp.exp(-7*t)-5)/35
D1=(7*(1-sp.exp(-2*t))-sp.Rational(9,7)*(1-sp.exp(-7*t))-5*t)/35
assert sp.simplify(sp.diff(D1,t)-D0)==0
assert sp.simplify(sp.diff(D0,t).subs(t,0)-1)==0
assert sp.simplify(D0.subs(t,0))==0
assert sp.simplify(sp.limit(D0,t,sp.oo)+sp.Rational(1,7))==0
assert sp.factor(sp.together(L.subs({a:4,b:1,u:2,v:2,S1:2,S2:1})-sp.Rational(1,1)/z*(z-2)/((z+2)*(z+7))))==0
assert sp.simplify(D0-(sp.Rational(1,5)*(sp.exp(-2*t)-sp.exp(-7*t))-sp.Rational(2,1)*(sp.Rational(1,5)*((1-sp.exp(-2*t))/2-(1-sp.exp(-7*t))/7))))==0

mp.mp.dps=65
C=lambda x:(14*mp.exp(-2*x)-9*mp.exp(-7*x)-5)/35
J=lambda x:(7*(1-mp.exp(-2*x))-mp.mpf(9)/7*(1-mp.exp(-7*x))-5*x)/35
r0=mp.findroot(C,(mp.mpf('.3'),mp.mpf('.7')))
r1=mp.findroot(J,(mp.mpf('.8'),mp.mpf('1.2')))
assert abs(r0-mp.mpf('0.4856232949537298861419551463398633435239'))<mp.mpf('1e-37')
assert abs(r1-mp.mpf('0.9216519013066324467582080213393840650207'))<mp.mpf('1e-37')
assert r0<r1 and C(mp.mpf('0.1'))>0 and C(2)<0
assert J(mp.mpf('0.1'))>0 and J(2)<0

# Independent matrix evolution comparison, two random parameter sets and every sample time.
A=mp.matrix([[-6,2],[2,-3]])
S=mp.matrix([2,1]); I=mp.eye(2)
for tt in [mp.mpf(x)/13 for x in range(1,151)]:
 state=mp.inverse(A)*(mp.expm(A*tt)-I)*S
 assert abs((state[0]-state[1])-C(tt))<mp.mpf('1e-57')

# Verify temporal crossover ordering for first 7 iterated integrals from positive kernel,
# using positive quadrature and bisection (not an infinite proof).
rlo,rhi=mp.mpf(2),mp.mpf(7)
B=lambda tt:(mp.exp(-rlo*tt)-mp.exp(-rhi*tt))/(rhi-rlo)
F0=B

def F(j,tt):
 if j==0: return F0(tt)
 return mp.quad(lambda s:(tt-s)**(j-1)/mp.factorial(j-1)*B(s), [0,tt])
roots=[]
for j in range(5):
 def expr(x):return F(j,x)-2*F(j+1,x)
 lo,hi=mp.mpf('0.05'),mp.mpf(200)
 assert expr(lo)>0 and expr(hi)<0
 for _ in range(75):
  mid=(lo+hi)/2
  if expr(mid)>0:lo=mid
  else:hi=mid
 roots.append((lo+hi)/2)
assert all(roots[i]<roots[i+1] for i in range(4))
assert abs(roots[0]-r0)<mp.mpf('1e-18')
assert abs(roots[1]-r1)<mp.mpf('1e-18')

# Exact rational samples of the derivative of the instantaneous sign crossover.
def first_root(k):
 delta=mp.sqrt(9+4*k*k);slow=(5+2*k-delta)/2;fast=slow+delta
 def ratio(tt):
  bval=(mp.exp(-slow*tt)-mp.exp(-fast*tt))/delta
  ival=((1-mp.exp(-slow*tt))/slow-(1-mp.exp(-fast*tt))/fast)/delta
  return bval/ival
 lo,hi=mp.mpf('.01'),mp.mpf('8')
 for _ in range(180):
  mid=(lo+hi)/2
  if ratio(mid)>2:lo=mid
  else:hi=mid
 return (lo+hi)/2
ks=list(map(mp.mpf,['0.1','0.5','2','10','100']))
tks=[first_root(k) for k in ks]
assert all(tks[i]>tks[i+1] for i in range(len(tks)-1))
assert abs(tks[2]-r0)<mp.mpf('1e-50')
limit=mp.mpf(2)/5*mp.log(mp.mpf(9)/4)
assert all(x>limit for x in tks)
print('PASS: exact symbolic transfer identities, exact example, 150 independent matrix observations,')
print('five chronological integral crossovers, monotonic exchange numerical checks.')
print('t0 =',mp.nstr(r0,36));print('t1 =',mp.nstr(r1,36));print('large exchange limit =',mp.nstr(limit,36))
print('first five horizon roots =',[mp.nstr(x,15) for x in roots])
