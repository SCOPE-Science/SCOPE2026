"""Standalone exact checks for Gaussian-renewal displacement cumulants.
Requires SymPy; run: python verify.py
"""
import sympy as s
r=s.symbols('r',positive=True)
# On one interval of dimensionless duration u, the conditional variance is 2*f(u).
# Map (exponential rate, monomial degree) to coefficient.
f={(0,1):s.Integer(1),(0,0):-s.Rational(3,2),(1,0):s.Integer(2),(2,0):-s.Rational(1,2)}
def mul(a,b):
    out={}
    for (k,i),v in a.items():
        for (j,n),w in b.items():
            out[(k+j,i+n)]=out.get((k+j,i+n),s.Integer(0))+v*w
    return out
def expectation(a):
    return s.factor(sum(v*r*s.factorial(n)/(r+k)**(n+1) for (k,n),v in a.items()))
E=expectation(f)
d=s.factor(r*E)
assert s.simplify(E-2/(r*(r+1)*(r+2)))==0
assert s.simplify(d-2/((r+1)*(r+2)))==0
# Center the reward f(u) by d*u, then renewal rate r E[(f-d*u)^2].
g=f.copy();g[(0,1)]=1-d
v=s.factor(r*expectation(mul(g,g)))
V=8*r*(7*r*r+28*r+27)/((r+1)**3*(r+2)**3*(r+3)*(r+4))
assert s.simplify(v-V)==0
# In physical units: E displacement^2/t=2D/gamma^2*d;
# fourth-cumulant rate = 12 D^2/gamma^5*v.
# Thus excess-kurtosis coefficient (gamma*t)*cum4/Var^2 is 3*v/d^2.
K=s.factor(3*v/d**2)
K_expected=6*r*(7*r*r+28*r+27)/((r+1)*(r+2)*(r+3)*(r+4))
assert s.simplify(K-K_expected)==0
Pabs=35*r**6+406*r**5+1806*r**4+3782*r**3+3487*r**2+600*r-648
Prel=7*r**6+56*r**5+116*r**4-160*r**3-959*r**2-1344*r-648
assert s.simplify(s.diff(v,r)+8*Pabs/((r+1)**4*(r+2)**4*(r+3)**2*(r+4)**2))==0
assert s.simplify(s.diff(K,r)+6*Prel/((r+1)**2*(r+2)**2*(r+3)**2*(r+4)**2))==0
assert Pabs.subs(r,s.Rational(1,4))<0 and Pabs.subs(r,s.Rational(1,3))>0
assert Prel.subs(r,2)<0 and Prel.subs(r,3)>0
ra=[x for x in s.nroots(Pabs,maxsteps=200) if abs(s.im(x))<1e-10 and s.re(x)>0]
rr=[x for x in s.nroots(Prel,maxsteps=200) if abs(s.im(x))<1e-10 and s.re(x)>0]
assert len(ra)==len(rr)==1
assert abs(float(s.re(ra[0]))-0.309107144259572)<1e-11
assert abs(float(s.re(rr[0]))-2.55653661983339)<1e-11
# Independent Markov-generator/short-time Laplace moment hierarchy,
# normalized gamma=D=1. Laplace variable s0 and reset rate r0.
s0=s.symbols('s0', positive=True)
for r0 in [s.Rational(1,2),s.Integer(1),s.Integer(3)]:
    m={(0,0):1/s0}
    # E[x^i v^j] obeys 1/s0-Laplace generator identity.
    for degree in range(1,5):
        for i in range(degree+1):
            j=degree-i
            forcing=(i*m.get((i-1,j+1),0) if i else 0)+(j*(j-1)*m.get((i,j-2),0) if j>=2 else 0)
            m[(i,j)]=forcing/(s0+j+(r0 if j>0 else 0))
    v2=s.factor(s0*s0*m[(2,0)])
    v4=s.factor(s0**3*m[(4,0)])
    c2=s.limit(v2,s0,0)
    c2offset=s.limit(s.diff(v2,s0),s0,0)
    fourthlinear=s.limit(s.diff(v4,s0),s0,0)
    c4=s.factor(fourthlinear-6*c2*c2offset)
    assert s.simplify(c2-4/((r0+1)*(r0+2)))==0
    expected=96*r0*(7*r0**2+28*r0+27)/((r0+1)**3*(r0+2)**3*(r0+3)*(r0+4))
    assert s.simplify(c4-expected)==0
print('PASS: exponential-reward moments, variance-to-cumulant scaling, exact derivatives, unique-root brackets, and independent generator-Laplace tests')
print('absolute-optimum:',ra[0], 'relative-optimum:',rr[0])
