"""Finite-state and symbolic checks for the balanced source-pinned contact process.

Run: python verify.py
Requires: Python 3, numpy, scipy, sympy.
The infinite-size theorem relies on the accompanying analytical proof.
"""
import math
import numpy as np
import sympy as sp
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve


def analytic_mean(c):
    return 2*c + 2*math.exp(-c*c)/(math.sqrt(math.pi)*(1+math.erf(c)))


def finite_stationary(n,c):
    a=1+c/math.sqrt(n)
    assert n>=2 and a>0
    lam=a/n
    width=n+1
    size=n*width
    q=lil_matrix((size,size),dtype=float)
    ident=lambda x,y:x*width+y
    X=np.repeat(np.arange(n),width)
    Y=np.tile(np.arange(width),n)
    for x in range(n):
        for y in range(width):
            k=ident(x,y)
            transitions=[]
            if x<n-1: transitions.append((x+1,y,lam*y*(n-1-x)))
            if x>0: transitions.append((x-1,y,float(x)))
            if y<n: transitions.append((x,y+1,lam*(x+1)*(n-y)))
            if y>0: transitions.append((x,y-1,float(y)))
            for xx,yy,rate in transitions:
                q[k,ident(xx,yy)]=rate
                q[k,k]-=rate
    assert np.max(np.abs(np.asarray(q.sum(axis=1))))<1e-11
    mat=q.transpose().tolil()
    rhs=np.zeros(size)
    mat[-1,:]=1.0
    rhs[-1]=1.0
    pi=spsolve(mat.tocsc(),rhs)
    assert abs(float(pi.sum())-1)<1e-11
    assert pi.min()>-1e-11
    s=X+Y
    d=X-Y
    b=lam*(Y*(n-1-X)+(X+1)*(n-Y))
    total=b+s
    # Three independently calculated generator balances.
    assert abs(float(pi@(b-s)))<2e-9
    assert abs(float(pi@d)+a/(1+a))<2e-9
    assert abs(float(pi@(-2*(1+a)*d*d-2*a*d+total)))<2e-8
    mean=float(pi@s)/math.sqrt(n)
    return mean


def exact_identities():
    x,y,n,l=sp.symbols('x y n l')
    s=x+y;d=x-y;a=n*l
    birth=l*(y*(n-1-x)+(x+1)*(n-y))
    assert sp.expand(birth-a*(s+1)+l*((s-d)+(s*s-d*d)/2))==0
    ddrift=l*y*(n-1-x)-x-l*(x+1)*(n-y)+y
    assert sp.expand(ddrift+(1+a)*d+a)==0
    for c in [-1.0,0.0,1.0]:
        Z=math.sqrt(math.pi)*math.exp(c*c)*(1+math.erf(c))
        from scipy.integrate import quad
        z2=quad(lambda w: math.exp(c*w-w*w/4),0,math.inf)[0]
        m2=quad(lambda w:w*math.exp(c*w-w*w/4),0,math.inf)[0]/z2
        assert abs(Z-z2)<1e-8
        assert abs(analytic_mean(c)-m2)<1e-8
    return 5


def main():
    checks=exact_identities()
    for c in [-1.,0.,1.]:
        means=[]
        for n in [6,12,24,48]:
            means.append(finite_stationary(n,c))
            checks+=4
        target=analytic_mean(c)
        assert all(means[i]<means[i+1] for i in range(len(means)-1))
        assert all(x<target for x in means)
        checks+=2
        print(f'c={c:+.0f}: meanW for n=6,12,24,48: {means}; limit={target:.12f}')
    print(f'PASS: {checks} symbolic, finite generator/balance, and analytic-normalization assertions')

if __name__=='__main__':
    main()
