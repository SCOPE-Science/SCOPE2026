"""Independent symbolic and high-precision checks of symmetric three-site Matern 3/2 quadrature."""
import sympy as sp
from mpmath import mp

a, t, x = sp.symbols('a t x', positive=True)
k = lambda z: (1+t*z)*sp.exp(-t*z)
c,d = k(a),k(2*a)
b0=2*(2-(2+t)*sp.exp(-t))/t
b1=(4-(2+t*(1-a))*sp.exp(-t*(1-a))-(2+t*(1+a))*sp.exp(-t*(1+a)))/t
N=sp.expand(b0*(1+d)-2*c*b1)
H=sp.expand(t*sp.exp(t*(1+2*a))*N)
H2=(4*sp.exp(t)*(sp.exp(a*t)-1)**2-8*a*t*sp.exp(t)*(sp.exp(a*t)-1)
    +2*a*t*(sp.exp(2*a*t)-1)+2*a*(1-a)*t**2*(sp.exp(2*a*t)-1))
assert sp.simplify(sp.expand(H-H2))==0
p4=-a*a*(a*a-12*a+6)/3
p5=-a*a*(2*a**3-11*a*a+2)/3
p6=-a*a*(47*a**4-180*a**3-45*a*a+15)/90
for j,p in [(4,p4),(5,p5),(6,p6)]:
 assert sp.simplify(sp.diff(H2,t,j).subs(t,0)/sp.factorial(j)-p)==0
# Independent combinatorial coefficient identity, j >= 7.
for j in range(7,31):
 P=2*((1+2*a)**j-2*(1+a)**j+1)-4*a*j*((1+a)**(j-1)-1)+a*j*(2*a)**(j-1)+a*(1-a)*j*(j-1)*(2*a)**(j-2)
 # With P=(j!/2)[t^j] H, verify using the closed exponential coefficients.
 raw=2*((1+2*a)**j-2*(1+a)**j+1)-4*a*j*((1+a)**(j-1)-1)+a*j*(2*a)**(j-1)+a*(1-a)*j*(j-1)*(2*a)**(j-2)
 assert sp.simplify(raw-P)==0
 coeff=sp.expand(H2).diff(t,j).subs(t,0)/sp.factorial(j)
 assert sp.simplify(sp.expand(P-j*sp.factorial(j-1)*coeff/2))==0
 # The intermediate powers are strictly nonnegative, the top two combine positively.
 coeffs=[sp.expand(P).coeff(a,l) for l in range(j+1)]
 assert coeffs[2]==-2*j*(j-1) and coeffs[3]==0
 assert coeffs[4]==12*sp.binomial(j,4)
 assert all(coeffs[l]>0 for l in range(4,j-1))
 assert coeffs[j-1]>0 and coeffs[j]<0
 assert coeffs[j-1]+coeffs[j]>0

# Numerical matrix equations, both below and above the sharp boundary; use exact quadrature integrals.
mp.dps=70
alpha=mp.mpf(6)-mp.sqrt(30)
for astr in ['0.1','0.3','0.5','0.521','0.5227744249483388','0.523','0.6','1']:
 aa=mp.mpf(astr)
 for tt in [mp.mpf('0.02'),mp.mpf('0.1'),mp.mpf('0.5'),mp.mpf('2'),mp.mpf('10')]:
  kk=lambda z:(1+tt*abs(z))*mp.exp(-tt*abs(z))
  K=mp.matrix([[kk(0),kk(aa),kk(aa)],[kk(aa),kk(0),kk(2*aa)],[kk(aa),kk(2*aa),kk(0)]])
  B=mp.matrix([mp.quad(lambda y:kk(y),[-1,0,1]),mp.quad(lambda y:kk(y-aa),[-1,aa,1]),mp.quad(lambda y:kk(y+aa),[-1,-aa,1])])
  # reorder: center, plus, minus
  w=mp.lu_solve(K,B)
  assert max(abs(z) for z in (K*w-B))<mp.mpf('1e-55')
  assert w[1]>0 and w[2]>0
  if aa>alpha: assert w[0]>0
  if aa<alpha-mp.mpf('0.001') and tt<mp.mpf('0.03'): assert w[0]<0
print('PASS symbolic identities, coefficient positivity structure through j=30, 40 high-precision matrix checks')
