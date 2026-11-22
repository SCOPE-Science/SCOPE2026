"""Independent symbolic and quadrature checks for the origin-reset gyrator drift-torque theorem.
Requires sympy and mpmath. Run with: python verify.py
"""
import sympy as sp
import mpmath as mp
r,u,S,H,k,w=sp.symbols('r u S H k w',positive=True)
a,b=1+u,1-u
D=(r+2)**2-4*u**2
# The generator-derived stationary first nonzero moments.
uu=2*S/(r+2*a)
vv=2*S/(r+2*b)
uv=2*H/(r+2)
uuvv=sp.factor((2*S*(uu+vv)+8*H*uv)/(r+4))
vq=sp.factor(uuvv-uv**2)
vq_exp=8*S**2*(r+2)/((r+4)*D)+4*H**2*(3*r+4)/((r+2)**2*(r+4))
assert sp.simplify(vq-vq_exp)==0
cv2=sp.factor(vq/uv**2)
cv2_target=2*k*(r+2)**3/((r+4)*((r+2)**2-4*w))+(3*r+4)/(r+4)
assert sp.simplify(cv2.subs(S**2,k*H**2).subs(u**2,w)-cv2_target)==0
P=r**2+4*(1-w)*r+4-20*w
B=sp.expand(k*(r+2)**2*P+2*((r+2)**2-4*w)**2)
Bcoeff=[sp.expand(B).coeff(r,j) for j in range(4,-1,-1)]
assert sp.simplify(sp.diff(cv2_target,r)-4*B/((r+4)**2*((r+2)**2-4*w)**2))==0
assert all(sp.expand(g-h)==0 for g,h in zip(Bcoeff,[k+2,8*k+16-4*k*w,24*k+48-36*k*w-16*w,32*k+64-96*k*w-64*w,16*(k*(1-5*w)+2*(1-w)**2)]))
wL=(k+2)/(3*k+2)
wQ=6*(k+2)/(9*k+4)
assert sp.factor(wQ-wL)==(k+2)*(9*k+8)/((3*k+2)*(9*k+4))
assert sp.factor((k*(1-5*w)+2*(1-w)**2).subs(w,wL))==-2*k*(k+2)*(3*k+4)/(3*k+2)**2
# Independent age-mixture quadrature at five nontrivial parameter tuples.
mp.mp.dps=45
cases=[(.4,.32,1.7,.6),(.65,.9,2.3,1.1),(.85,1.5,3.2,.9),(.2,4.0,1.1,.8),(.95,.47,2.,1.)]
for uv,rv,sv,hv in cases:
 aa,bb=1+uv,1-uv
 def age_integrand(t):
  cu=sv/aa*(-mp.expm1(-2*aa*t))
  cv=sv/bb*(-mp.expm1(-2*bb*t))
  cc=hv*(-mp.expm1(-2*t))
  return rv*mp.exp(-rv*t)*(cu*cv+2*cc**2)
 direct=mp.quad(age_integrand,[0,1,mp.inf])
 gen=float(uuvv.subs({r:rv,u:uv,S:sv,H:hv}))
 assert abs(float(direct)-gen)<2e-11*(1+abs(gen)),(uv,rv,float(direct),gen)
# Check one-root structure and numerical optimum for k=4, u=0.8.
pol=sp.Poly(B.subs({k:4,w:sp.Rational(16,25)}),r)
roots=sp.nroots(pol,maxsteps=200)
pos=[float(sp.re(v)) for v in roots if abs(float(sp.im(v)))<1e-10 and float(sp.re(v))>0]
assert len(pos)==1
z=pos[0]
fun=sp.lambdify(r,cv2_target.subs({k:4,w:sp.Rational(16,25)}),'mpmath')
assert fun(z)<fun(0) and fun(z)<fun(3*z) and z>0
print('PASS: exact moments, derivative, coefficient boundaries, five independent Gaussian-age quadratures, unique-root numerical instance')
print('example k=4,u=0.8: optimum r =',z,'min squared CV =',float(fun(z)),'no-reset value =',float(fun(0)))
