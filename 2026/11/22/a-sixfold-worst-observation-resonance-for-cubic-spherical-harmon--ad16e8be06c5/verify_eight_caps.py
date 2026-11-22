"""Standalone reproducibility checks for cubic-harmonic concentration on eight cubical caps.
Uses only numpy and sympy. All functions and cap domains are explicitly defined.
"""
import itertools
import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss

z=sp.symbols('z',real=True)
t=sp.symbols('t',real=True)
q=sp.sqrt(1-t*t)
c,h=sp.symbols('c h',real=True)
x=t/sp.sqrt(3)+q*(c/sp.sqrt(2)+h/sp.sqrt(6))
y=t/sp.sqrt(3)+q*(-c/sp.sqrt(2)+h/sp.sqrt(6))
w=t/sp.sqrt(3)-q*(2*h/sp.sqrt(6))
F=[x*y*w,x*(y*y-w*w),x*(5*x*x-3)]
expected_p=[(24*t**6-27*t**4+6*t**2+1)/108,(1-t*t)*(12*t**4-5*t*t+1)/18,(300*t**6-495*t**4+210*t*t+17)/54]
expected_norm=[sp.Rational(1,105),sp.Rational(4,105),sp.Rational(4,7)]
expected_lambda=[]

def angular_avg(poly):
    p=sp.Poly(sp.expand(poly),c,h)
    out=sp.Integer(0)
    for (i,j),a in p.terms():
        if i%2 or j%2: continue
        i//=2;j//=2
        moment=(sp.factorial(2*i)*sp.factorial(2*j))/ (4**(i+j)*sp.factorial(i)*sp.factorial(j)*sp.factorial(i+j))
        out+=a*moment
    return sp.factor(out)

for k,f in enumerate(F):
    p=angular_avg(f*f)
    assert sp.simplify(p-expected_p[k])==0, (k,'moment')
    norm=sp.integrate(p,(t,-1,1))/2
    assert norm==expected_norm[k], (k,'normalization')
    expected_lambda.append(sp.factor(4*sp.integrate(p,(t,z,1))/norm))

A,B,C=expected_lambda
assert sp.simplify(A-B-35*z*(1-z*z)*(12*z**4-9*z*z+1)/18)==0
assert sp.simplify(A-C-7*z*(1-z*z)*(60*z**4-3*z*z-13)/54)==0
assert sp.simplify(B-C+14*z*(1-z*z)*(30*z**4-33*z*z+7)/27)==0
zstar=sp.sqrt((33+sp.sqrt(249))/60)
assert sp.simplify((30*z**4-33*z*z+7).subs(z,zstar))==0
assert sp.simplify(zstar*zstar-sp.Rational(2,3))>0
assert sp.simplify(zstar*zstar-1)<0
assert sp.limit((1-z)*A/B,z,1)==sp.Rational(1,3)

# Independent numerical Galerkin construction in all seven cubic harmonic sectors.
def basis(x):
    a,b,c=x[...,0],x[...,1],x[...,2]
    return np.stack([a*b*c,a*(b*b-c*c),b*(c*c-a*a),c*(a*a-b*b),
                     a*(5*a*a-3),b*(5*b*b-3),c*(5*c*c-3)],axis=-1)

norm=np.array([1/105]+[4/105]*3+[4/7]*3)
V=np.array(list(itertools.product([-1.,1.],repeat=3)),dtype=float)/np.sqrt(3)
for cutoff in [np.sqrt(2/3),.85,.90,float(zstar),.94,.99]:
    nodes,ww=leggauss(14)
    tt=(1+cutoff)/2+(1-cutoff)*nodes/2
    wt=(1-cutoff)*ww/2
    phi=2*np.pi*np.arange(32)/32
    cp=np.cos(phi);sp_ =np.sin(phi)
    G=np.zeros((7,7))
    for v in V:
        ee=np.array([v[1],-v[0],0.])/np.sqrt(v[0]**2+v[1]**2)
        ff=np.cross(v,ee)
        P=(tt[:,None,None]*v[None,None,:]+
           np.sqrt(1-tt**2)[:,None,None]*(cp[None,:,None]*ee[None,None,:]+sp_[None,:,None]*ff[None,None,:]))
        Y=basis(P)/np.sqrt(norm)
        G+=np.einsum('tpa,tpb,t->ab',Y,Y,wt)/ (2*32)
    diag=np.array([float(A.subs(z,cutoff))]+[float(B.subs(z,cutoff))]*3+[float(C.subs(z,cutoff))]*3)
    assert np.max(np.abs(G-np.diag(diag)))<5e-12,(cutoff,np.max(np.abs(G-np.diag(diag))))
    assert abs(np.trace(G)-7*4*(1-cutoff))<4e-12,(cutoff,'trace')
print('PASS symbolic identities, normalizations, sharp transition, and six independent 7x7 Galerkin checks')
print('transition',sp.N(zstar,17))
print('eigenvalue formulas',*[str(x) for x in expected_lambda],sep='\n')
