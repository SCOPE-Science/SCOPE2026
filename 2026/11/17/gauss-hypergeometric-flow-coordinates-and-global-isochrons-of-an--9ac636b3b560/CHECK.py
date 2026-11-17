import mpmath as mp
from scipy.integrate import solve_ivp
import math,cmath
import sympy as sp
mp.mp.dps=40
# Exact check against the source polynomial coefficients.
x,z,h,w=sp.symbols('x z h w',real=True,nonzero=True)
shear=w*(x*x-h)*x/(2*h)
y=z-shear
f3=-w/(2*h)
f2=-3*w*w*(x**3-h*x)/(4*h*h)
f1=-sp.Rational(3,8)*(w/h)**3*x**6+3*w**3*x**4/(4*h*h)-w*(3*w*w+20)*x*x/(8*h)+w
f0=-x*(w*w*x**4-h*w*w*x*x+4*h*h)*(w*w*x**4-2*h*w*w*x*x+h*h*w*w+4*h*h)/(16*h**4)
zd=sp.factor(f3*y**3+f2*y**2+f1*y+f0+sp.diff(shear,x)*y)
assert sp.simplify(y-(z+w*(h-x*x)*x/(2*h)))==0
assert sp.simplify(zd-(-x+w*(h-2*x*x-z*z)*z/(2*h)))==0
assert sp.simplify(2*x*y+2*z*zd-w*(x*x+z*z)*(1-(x*x+z*z)/h))==0
# Numerical Gauss equation check on each radial component.
for W in [mp.mpf('1'),mp.mpf('2.5'),mp.mpf('3.6')]:
 O=mp.sqrt(1-W**2/16)
 a=1j/W;b=mp.mpf('.25')+1j*O/W
 def F(u): return u**a*abs(1-u)**b*mp.hyp2f1(a+b,a+b+mp.mpf('.5'),mp.mpf('.5')+2*b,1-u)
 for qq in [mp.mpf('.1'),mp.mpf('.7'),mp.mpf('1.3'),mp.mpf('2')]:
  residual=qq**2*(1-qq)**2*mp.diff(F,qq,2)+qq*(1-qq)*(1-3*qq/2)*mp.diff(F,qq)+F(qq)/W**2
  assert abs(residual)<mp.mpf('1e-23')


def phase(x,z,w,h=1):
 q=mp.mpf(str((x*x+z*z)/h)); W=mp.mpf(str(w)); Om=mp.sqrt(1-W*W/16)
 if abs(q-1)<mp.mpf('1.e-13'): return float(mp.arg(mp.mpc(x,(z+W*x/4)/Om)))
 def f(u):
  a=1j/W; b=mp.mpf('.25')+1j*Om/W
  return u**a*abs(1-u)**b*mp.hyp2f1(a+b,a+b+mp.mpf('.5'),1+2j*Om/W,1-u)
 F=f(q);G=W*q*(1-q)*mp.diff(f,q)
 A=(mp.mpf(x)*mp.conj(G)-mp.mpf(z)*mp.conj(F))/(F*mp.conj(G)-G*mp.conj(F))
 return float(mp.arg(A*((abs(1-q)/q)**(1j*Om/W))))

for w,x0,z0 in [(1,.2,.3),(2,1.8,.1),(3,-1.3,.5),(1,1,0),(3,0,.5)]:
 omega=math.sqrt(1-w*w/16)
 d0=phase(x0,z0,w)
 def rhs(t,Y):
  x,z=Y
  return [z+w*.5*(1-x*x)*x,-x+w*.5*(1-2*x*x-z*z)*z]
 sol=solve_ivp(rhs,(0,5),[x0,z0],rtol=2e-12,atol=1e-13,dense_output=True)
 for t in [0,.3,1,3,5]:
  x,z=sol.sol(t)
  d=phase(x,z,w)
  err=cmath.phase(cmath.exp(1j*(d-d0+omega*t)))
  assert abs(err)<2e-9,(w,t,err)
 print('w',w,'q0',x0*x0+z0*z0,'phase identity max test pass')
print('GLOBAL_ISOCHRON_HYPERGEOMETRIC_CHECK_OK')
