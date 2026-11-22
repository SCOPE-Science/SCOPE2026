"""Exact symbolic checks for the three-vertex hub-control Gramian design.
Requires Python >=3.10 and SymPy >=1.10; run: python verify.py.
No external data or network access is required.
"""
import sympy as s

mu,u,v=s.symbols('mu u v',positive=True)
L=s.Matrix([[u+v,-u,-v],[-u,u,0],[-v,0,v]])
A=mu*s.eye(3)+L
b=s.Matrix([1,0,0])
K=s.Matrix.hstack(b,A*b,A*A*b)
assert s.factor(K.det() - u*v*(v-u)) == 0
z=s.symbols('z0:9'); X=s.Matrix(3,3,z)
sol=s.solve(list(A*X+X*A-b*b.T),z,dict=True)
assert len(sol)==1
W=X.subs(sol[0])
S=u+v; p=u*v
D=p**2*(u-v)**2/(32*mu*(mu+S)**2*(4*mu**2+4*mu*S+3*p)**2*(mu**2+2*mu*S+3*p))
assert s.factor(W.det()-D)==0

x,t=s.symbols('x t',positive=True)
AA=4*t*t+4*t+3*x; BB=t*t+2*t+3*x
F=x*x*(1-4*x)/(AA**2*BB)
g=2/x-4/(1-4*x)-6/AA-3/BB
assert s.factor(s.diff(F,x)/F-g)==0
Q=(108*t*t+120*t+9)*x*x+12*t*(t+1)*(4*t*t+8*t-1)*x-8*t*t*(t+1)*(t+2)
assert s.factor(g*x*(1-4*x)*AA*BB+Q)==0
assert s.factor(Q.subs(x,s.Rational(1,4)))==(2*t+1)*(2*t+3)*(4*t+1)*(4*t+3)/16
assert s.simplify(Q.subs(x,s.Rational(1,6))-(12*t*t+16*t+3)/12)==0
assert s.factor(s.diff(g,t) - (6*(8*t+4)/AA**2+3*(2*t+2)/BB**2))==0

r=s.sqrt(5); c=s.Rational(2,3)*(1+r)
assert s.simplify((Q.subs({x:c*t})/t**2).limit(t,0))==0
# The high-damping two leading orders in the stationary equation cancel.
assert s.limit(Q.subs(x,s.Rational(1,6)-1/(48*t*t))/t**2,t,s.oo)==0
K_asym=s.simplify(c*c/(32*(4+3*c)**2*(2+3*c)))
assert s.simplify(K_asym-(5*s.sqrt(5)-11)/1152)==0

for T in (s.Rational(1,100),s.Rational(1,10),s.Rational(1,2),s.Integer(1),s.Integer(10),s.Integer(100)):
    a=s.N(108*T*T+120*T+9,50)
    bb=s.N(12*T*(T+1)*(4*T*T+8*T-1),50)
    cc=s.N(-8*T*T*(T+1)*(T+2),50)
    xx=(-bb+s.sqrt(bb*bb-4*a*cc))/(2*a)
    assert 0<xx<s.Rational(1,6)
    assert abs(float(g.subs({x:xx,t:T})))<1e-10
print('EXACT_CONTROL_GRAMIAN_OK: determinant, derivative, uniqueness-sign certificates, asymptotics, six numerical root checks')
