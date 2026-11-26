import sympy as S
p,g,s,u,r,z,theta=S.symbols('p g s u r z theta', positive=True)
q=u+r
H=q*(g+p+s+r)+p*s
A=S.Matrix([[p,-p,0],[-r,g+s+r,-s],[-q,0,q]])
M=(A+z*S.eye(3))
phi=S.factor(g*M.inv()[0,1]) # starting G; density gamma Prob_E(t) ; row0,col1 inverse expected
assert S.simplify(phi-g*p*(q+z)/(z**3+(g+p+s+u+2*r)*z**2+(g*p+H)*z+g*p*q))==0,phi
w1=S.factor(-S.diff(phi,z).subs(z,0));w2=S.factor(S.diff(phi,z,2).subs(z,0));w3=S.factor(-S.diff(phi,z,3).subs(z,0))
assert S.simplify(w1-H/(g*p*q))==0
F=S.factor((w2-w1**2)/w1**2)
expected=1+2*g*p*(p*s-q**2)/H**2
assert S.simplify(F-expected)==0, S.factor(F-expected)
S3=S.factor(3*(w2-w1**2)**2/w1**4-(w3-3*w2*w1+2*w1**3)/w1**3)
x=S.symbols('x',positive=True)
Scrit=S.factor(S3.subs(r,x-u).subs(s,x**2/p))
Hcrit=S.factor(H.subs(r,x-u).subs(s,x**2/p))
assert S.factor(Scrit-(1-6*g**2*p**2*x**2/Hcrit**3))==0,(Scrit,Hcrit)
# Independent tilted generator: characteristic implicit equation and expansion
L=S.Matrix([[-p,r+g*S.exp(theta),q],[p,-(g+s+r),0],[0,s,-q]])
t=S.symbols('t')
poly=S.det(t*S.eye(3)-L)
# convert to t coefficients and evaluate theta=0
assert S.simplify(poly.subs({theta:0,t:0}))==0
vals=[(1,1,1,S.Rational(1,5)),(2,S.Rational(3,2),3,1),(S.Rational(5,4),S.Rational(1,3),S.Rational(7,8),S.Rational(1,4))]
for pp,gg,ss,uu in vals:
 for rr in [0,S.Rational(1,3),2]:
  sub={p:pp,g:gg,s:ss,u:uu,r:rr}
  f=S.factor(poly.subs(sub))
  a=S.diff(f, t).subs({t:0,theta:0})
  b=S.diff(f,theta).subs({t:0,theta:0})
  c1=S.factor(-b/a)
  c2=S.factor(-(S.diff(f,theta,2).subs({t:0,theta:0})+2*S.diff(f,t,theta).subs({t:0,theta:0})*c1+S.diff(f,t,2).subs({t:0,theta:0})*c1**2)/a)
  c3=S.factor(-(S.diff(f,theta,3).subs({t:0,theta:0})+3*S.diff(f,t,theta,2).subs({t:0,theta:0})*c1+3*S.diff(f,t,2,theta).subs({t:0,theta:0})*c1**2+S.diff(f,t,3).subs({t:0,theta:0})*c1**3+3*(S.diff(f,t,theta).subs({t:0,theta:0})+S.diff(f,t,2).subs({t:0,theta:0})*c1)*c2)/a)
  assert S.simplify(c1-g*p*q/H).subs(sub)==0
  assert S.simplify(c2/c1-expected.subs(sub))==0
  assert S.simplify(c3/c1-S3.subs(sub))==0
print('PASS: rational renewal transform, all three waiting-time moments, exact Fano law, critical 3rd count-cumulant deficit, 9 independent rational tilted-generator tests')
