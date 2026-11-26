"""Exact and independent checks for the four-heading jump-process cumulant theorem.

Requirements: Python 3, SymPy, NumPy, SciPy. Run: python verify.py
"""
import sympy as sp
import numpy as np
from scipy.linalg import expm


def exact_identities():
    a,b,c,v,z,kx,ky=sp.symbols('a b c v z kx ky')
    t,A,B,X,Y=sp.symbols('t A B X Y')
    Q=sp.zeros(4)
    for j in range(4):
        Q[j,j]=-(a+b+c)
        Q[j,(j+1)%4]+=a
        Q[j,(j-1)%4]+=b
        Q[j,(j+2)%4]+=c
    F=sp.expand((z*sp.eye(4)-Q-sp.diag(v*kx,v*ky,-v*kx,-v*ky)).det(method='berkowitz'))
    s=a+b
    h=s+2*c
    H=h**2+(a-b)**2
    expected=z*(z+2*s)*((z+h)**2+(a-b)**2) - v**2*(kx**2+ky**2)*(z+h)*(z+s)+v**4*kx**2*ky**2
    assert sp.factor(F-expected)==0
    series=sp.Poly(expected.subs({kx:t*X,ky:t*Y,z:A*t**2+B*t**4}).expand(),t)
    Av=sp.solve(series.coeff_monomial(t**2),A)[0]
    Bv=sp.factor(sp.solve(series.coeff_monomial(t**4).subs(A,Av),B)[0])
    r,d=sp.symbols('r d',real=True)
    den=(1+2*r)**2+d**2
    Na=(1+2*r)*((3+2*r)*d**2+(1+2*r)**2*(2*r-1))
    Nd=d**4+(4*r**2-1)*d**2+16*r**3+24*r**2+12*r+2
    sub={a:(1+d)/2,b:(1-d)/2,c:r,v:1}
    # Homogeneity permits s=1,v=1 for coefficient algebra.
    normalized_A=sp.factor(Av.subs(sub))
    normalized_B=sp.factor(Bv.subs(sub))
    want_A=(1+2*r)*(X**2+Y**2)/(2*den)
    want_B=(Na*(X**4+Y**4)+ (2*Na-4*(Na+Nd))*X**2*Y**2)/(8*den**3)
    assert sp.factor(normalized_A-want_A)==0
    assert sp.factor(normalized_B-want_B)==0
    # The phase boundary and sign expressions are exact polynomial identities.
    assert sp.factor(Na.subs(r,0))==3*d**2-1
    assert sp.factor(Na.subs(d,0))==(2*r+1)**3*(2*r-1)
    assert sp.factor(Nd.subs(r,0))==d**4-d**2+2
    assert sp.expand(Nd-(d**4-d**2+2)-(4*d**2*r**2+16*r**3+24*r**2+12*r))==0
    return 7


def moment_ode_check(a,b,c,theta):
    v=1.0
    s=a+b
    h=s+2*c
    d=(a-b)/s
    r=c/s
    den=(1+2*r)**2+d**2
    Na=(1+2*r)*((3+2*r)*d**2+(1+2*r)**2*(2*r-1))
    Nd=d**4+(4*r**2-1)*d**2+16*r**3+24*r**2+12*r+2
    predicted=3*v**4/(s**3*den**3)*(Na*np.cos(2*theta)**2-Nd*np.sin(2*theta)**2)
    u=np.array([np.cos(theta),np.sin(theta),-np.cos(theta),-np.sin(theta)])*v
    Q=np.zeros((4,4))
    for j in range(4):
        Q[j,j]=-(s+c)
        Q[j,(j+1)%4]+=a
        Q[j,(j-1)%4]+=b
        Q[j,(j+2)%4]+=c
    H=np.zeros((20,20))
    for n in range(5):
        H[4*n:4*n+4,4*n:4*n+4]=Q.T
        if n:
            H[4*n:4*n+4,4*(n-1):4*n]=n*np.diag(u)
    p0=np.zeros(20)
    p0[:4]=0.25
    def cumulant(t):
        m=expm(H*t)@p0
        return m[16:20].sum()-3*m[8:12].sum()**2
    approximate=(cumulant(160)-cumulant(80))/80.
    assert np.isclose(predicted,approximate,rtol=0.0002,atol=3e-6),(a,b,c,theta,approximate,predicted)
    return 1


def main():
    passes=exact_identities()
    cases=[(1,1,0),(4,1,0),(1,4,0),(1,1,1),(1,1,1.5),
           (2,1,0.3),(3,1,0.9),(1,2,5)]
    for a,b,c in cases:
        for theta in (0.,np.pi/8,np.pi/4):
            passes+=moment_ode_check(float(a),float(b),float(c),theta)
    print('PASS',passes,'symbolic and independent finite-time moment checks')
if __name__=='__main__':main()
