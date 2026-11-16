"""Exact and independent numerical checks for orthogonal-cap quadrupole concentration.
Run: python verify.py  (requires sympy and numpy).
"""
from functools import lru_cache
import sympy as sp
import numpy as np

c, t = sp.symbols('c t', real=True)
x,y,z = sp.symbols('x y z', real=True)
q = [x*x-z*z, x*x+z*z-2*y*y, x*z, x*y, y*z]
expected_norms = [sp.Rational(4,15),sp.Rational(4,5),sp.Rational(1,15),sp.Rational(1,15),sp.Rational(1,15)]
branches = [
 (1-c)*(57*c**4+57*c**3-13*c**2-13*c+32)/32,
 (1-c)*(27*c**4+27*c**3-23*c**2-23*c+32)/32,
 (1-c)**2*(3*c**3+6*c**2+4*c+2)/2,
 (1-c)**2*(9*c**3+18*c**2+17*c+16)/16,
]

@lru_cache(None)
def moment(a,b,d):
    if a%2 or b%2:
        return sp.Integer(0)
    m,n = a//2,b//2
    az = sp.Rational(sp.factorial(2*m)*sp.factorial(2*n),
                     4**(m+n)*sp.factorial(m)*sp.factorial(n)*sp.factorial(m+n))
    # normalized spherical area measure: (1/2) dt dphi/(2pi)
    return sp.expand(az*sp.integrate(sp.expand(t**d*(1-t*t)**(m+n)),(t,c,1))/2)

def cap_product(u,v,axis):
    w=sp.expand(u*v)
    if axis=='x':
        w=w.xreplace({x:z,z:x})
    return sp.factor(sum(coeff*moment(*powers) for powers,coeff in sp.Poly(w,x,y,z).terms()))

G=sp.zeros(5); H=sp.zeros(5)
for i in range(5):
    for j in range(5):
        v=cap_product(q[i],q[j],'z')+cap_product(q[i],q[j],'x')
        G[i,j]=sp.factor(v)
        H[i,j]=sp.factor(cap_product(q[i],q[j],'z').subs(c,-1))
assert H==sp.diag(*expected_norms), ('unexpected full sphere Gram',H)
assert all(sp.simplify(G[i,j])==0 for i in range(5) for j in range(5) if i!=j),G
assert all(sp.simplify(G[i,i]/H[i,i]-branches[min(i,3)])==0 for i in range(5))
A,B,C,D=branches
assert sp.simplify(A+B+C+2*D-5*(1-c))==0
relations = {
 'A-B':(A-B,5*c*(1-c)*(1+c)*(3*c**2+1)/16),
 'A-C':(A-C,15*c*(1-c)*(1+c)*(7*c**2-3)/32),
 'A-D':(A-D,15*c*(1-c)*(1+c)*(5*c**2-1)/32),
 'B-C':(B-C,5*c*(1-c)*(1+c)*(15*c**2-11)/32),
 'B-D':(B-D,5*c*(1-c)*(1+c)*(9*c**2-5)/32),
 'C-D':(C-D,15*c*(1-c)**2*(1+c)**2/16),
}
for name,(lhs,rhs) in relations.items():
    assert sp.factor(lhs-rhs)==0,name

fn = sp.lambdify((x,y,z),q,'numpy')
for cv in [1/np.sqrt(2),0.73,np.sqrt(5)/3,0.8,np.sqrt(11/15),0.93,0.999]:
    nodes,weights=np.polynomial.legendre.leggauss(48)
    ang=(2*np.arange(128)+1)*np.pi/128
    # direct numerical integration uses two distinct cap orientations
    op=np.zeros((5,5))
    for swap in [False,True]:
        tt=cv+(nodes+1)*(1-cv)/2
        zz=np.broadcast_to(tt[:,None],(48,128)).copy()
        rr=np.sqrt(1-zz**2)
        xx=rr*np.cos(ang)
        yy=rr*np.sin(ang)
        xx=np.broadcast_to(xx,(48,128)); yy=np.broadcast_to(yy,(48,128))
        if swap:xx,zz=zz,xx
        F=np.array(fn(xx,yy,zz)).reshape(5,-1)
        weights_2d=(weights*(1-cv)/4)[:,None]*np.ones((1,128))/128
        op+=(F*weights_2d.reshape(1,-1))@F.T
    lam=np.linalg.eigvalsh(op/np.sqrt(np.outer(np.array(expected_norms,dtype=float),np.array(expected_norms,dtype=float))))
    pred=np.sort([float(b.subs(c,cv)) for b in [A,B,C,D,D]])
    assert np.max(np.abs(lam-pred))<2e-12,(cv,lam,pred)
print('ORTHOGONAL_DUAL_CAP_QUADRUPOLE_PASS exact_gram=25 branch_differences=6 quadrature_radii=7 transitions=5/9,11/15')
