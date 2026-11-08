"""Symbolic and finite numerical checks; not an independent proof."""
import sympy as s
import numpy as np
u,v,w,b=s.symbols('u v w b',real=True)
f=lambda z:s.sin(z)*s.exp(b*s.cos(z))
angles=[0,u,u+v]
vel=[-sum(f(angles[i]-angles[j]) for j in range(3)) for i in range(3)]
forces=[f(u),f(v),f(w)]
check=[vel[1]-vel[0],vel[2]-vel[1],vel[0]-vel[2]]
target=[-2*forces[0]+forces[1]+forces[2],forces[0]-2*forces[1]+forces[2],forces[0]+forces[1]-2*forces[2]]
for i in range(3):
 assert s.simplify((check[i]-target[i]).subs(w,2*s.pi-u-v).expand(trig=True))==0
z=s.symbols('z',real=True)
assert s.simplify(s.diff(f(z),z)-s.exp(b*s.cos(z))*(s.cos(z)-b*s.sin(z)**2))==0
t=s.symbols('t',positive=True)
a=s.acos(-t);g=2*s.pi-2*a
assert s.simplify(s.sin(g)/s.sin(a)-2*t)==0
assert s.simplify(s.cos(a)-s.cos(g)-(1-2*t)*(1+t))==0
for x in [s.Rational(1,20),s.Rational(1,4),s.Rational(2,5),s.Rational(49,100)]:
 assert float(s.log(2*x))<float(2*x-1)
 assert float(-1/(1+x)) < -2/3
for beta in [-2,-0.8,-0.5,-0.2,0,2]:
 d=np.exp(-beta/2)*(-.5-.75*beta)
 J=-d*np.array([[2.,-1.,-1.],[-1.,2.,-1.],[-1.,-1.,2.]])
 assert np.allclose(np.linalg.eigvalsh(J),sorted([0.,-3*d,-3*d]),atol=1e-12)
print('VERIFY_OK gap_equations=3 exact_force_derivative=1 trigonometric_identities=2 strict_samples=4 equilateral_Jacobians=6')
