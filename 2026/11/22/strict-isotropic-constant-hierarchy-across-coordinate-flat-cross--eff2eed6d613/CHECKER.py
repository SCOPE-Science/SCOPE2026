"""Reproduce exact coordinate-flat section volume, covariance and strict inequalities.
Requires Python 3, SymPy, NumPy and SciPy. This is a finite sanity check;
the all-dimensional proofs are in RESULT.md.
"""
from math import comb, factorial, sqrt
from fractions import Fraction
import numpy as np
from scipy.linalg import null_space
from scipy.spatial import ConvexHull
import sympy as sp


def root_volume(m):
    return sqrt(m)*comb(2*m-2,m-1)/(2**(m-1)*factorial(m-1))


def formula(n,m):
    k=n-m
    d=n-1
    volume=root_volume(m)*2**k*factorial(m-1)/factorial(d)
    yvar=Fraction(2*m-1,(m+1)*n*(n+1))
    zvar=Fraction(2,n*(n+1))
    return volume,float(yvar),float(zvar)


checks=0
# Coarea and simplex Dirichlet integrations, independent of the closed binomial formula.
for m in range(2,17):
    s=sum(Fraction(comb(m,j),factorial(j-1)*factorial(m-j-1)) for j in range(1,m))
    volume_over_sqrt_m=s/Fraction((m-1)*2**(m-1))
    expected=Fraction(comb(2*m-2,m-1),2**(m-1)*factorial(m-1))
    assert volume_over_sqrt_m==expected
    # Integrate the radial squared norm in each sign sector.
    numer=sum(Fraction(comb(m,j),factorial(j-1)*factorial(m-j-1)) *
              (Fraction(2,j+1)+Fraction(2,m-j+1)) for j in range(1,m))
    radial=Fraction(m-1,4*(m+1))*numer/s
    assert radial==Fraction((m-1)*(2*m-1),m*(m+1)**2)
    checks+=2

# Algebraic exact positivity certificates behind the all-dimensional hierarchy.
t=sp.symbols('t',integer=True,positive=True)
f=(2*t-1)/(2*(t+1))
delta=3/((2*t-1)*(t+2))
r2=(t+1)*(2*t-1)**2/(4*t**3)
margin=sp.factor(r2/f - (1+t*delta/(1-(t-1)*delta)))
assert sp.simplify(margin-(t-1)*(t+1)/(2*t**3*(2*t**2+1)))==0
assert sp.factor(1-r2)==(3*t-1)/(4*t**3)
checks+=2

# Independent convex-hull triangulation in orthonormal Euclidean coordinates.
for n in range(3,7):
    for m in range(2,n+1):
        normal=np.r_[np.ones(m), np.zeros(n-m)]
        U=null_space(normal.reshape(1,-1))
        points=[]
        for i in range(m):
            for j in range(m):
                if i!=j:
                    v=np.zeros(n);v[i]=0.5;v[j]=-0.5
                    points.append(v)
        for j in range(m,n):
            v=np.zeros(n);v[j]=1.0
            points.extend((v,-v))
        arr=np.array(points)@U
        d=n-1
        hull=ConvexHull(arr)
        total=0.0
        M=np.zeros((d,d))
        for face in hull.simplices:
            v=arr[face]
            w=abs(np.linalg.det(v))/factorial(d)
            total+=w
            M+=w*(v.T@v+np.outer(v.sum(axis=0),v.sum(axis=0)))/((d+1)*(d+2))
        covariance=M/total
        vtarget,ytarget,ztarget=formula(n,m)
        target=U.T@np.diag(np.r_[np.repeat(ytarget,m),np.repeat(ztarget,n-m)])@U
        assert abs(total-vtarget)<1e-9,(n,m,total,vtarget)
        assert np.max(np.abs(covariance-target))<1e-9,(n,m)
        checks+=2

# Exact rational ratio inequality (never infer all-dimensional truth from the range).
for m in range(2,501):
    mf=Fraction(2*m-1,2*(m+1))
    mp=Fraction(2*m+1,2*(m+2))
    r=Fraction((m+1)*(2*m-1)**2,4*m**3)
    assert mp**m < mf**(m-1)*r
    assert r<1
    checks+=2
print('PASS:',checks,'assertions; Euclidean hull integrations through ambient dimension 6')
