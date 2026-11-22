"""Supplementary numerical and exact checks for anisotropic Gaussian-puff inverse formulas."""
import itertools
import math
import numpy as np
import sympy as sp

def nodes(d):
    E=np.eye(d, dtype=int)
    return np.array([np.zeros(d,dtype=int),*E,*(2*e for e in E),*(E[i]+E[j] for i in range(d) for j in range(i+1,d))],dtype=float)

def Vmat(points):
    d=points.shape[1]
    return np.array([[1.,*x,*(x[i]*x[j] for i in range(d) for j in range(i,d))] for x in points],dtype=float)

def reconstruct(points, observations, age):
    d=points.shape[1]
    coeff=np.linalg.solve(Vmat(points),np.log(observations))
    b=coeff[1:d+1]
    H=np.zeros((d,d))
    k=d+1
    for i in range(d):
        for j in range(i,d):
            H[i,j]=H[j,i]=(-2 if i==j else -1)*coeff[k];k+=1
    center=np.linalg.solve(H,b)
    cov=np.linalg.inv(H)
    mass=np.exp(coeff[0]+center@H@center/2)*((2*np.pi)**(d/2))*np.sqrt(np.linalg.det(cov))
    return center,cov/(2*age),mass,H

def data(points,mu,D,M,age):
    precision=np.linalg.inv(D)
    dif=points-mu
    det=np.linalg.det(D)
    return M*(4*np.pi*age)**(-len(mu)/2)*det**(-.5)*np.exp(-np.einsum('ij,jk,ik->i',dif,precision,dif)/(4*age))

rng=np.random.default_rng(93024)
checks=0
for d in (1,2,3,4):
    p=nodes(d); q=(d+1)*(d+2)//2
    assert p.shape==(q,d)
    v=sp.Matrix([[sp.Integer(int(y)) for y in row] for row in Vmat(p)])
    assert v.det()!=0
    checks+=1
    for _ in range(75):
        B=rng.normal(size=(d,d));D=B@B.T+np.eye(d)*.75
        mu=rng.normal(size=d);M=float(rng.uniform(.3,10));age=float(rng.uniform(.7,4))
        y=data(p,mu,D,M,age)
        mm,DD,MM,H=reconstruct(p,y,age)
        assert np.allclose(mm,mu,atol=1e-8,rtol=1e-8)
        assert np.allclose(DD,D,atol=1e-8,rtol=1e-8)
        assert np.isclose(MM,M,atol=1e-8,rtol=1e-8)
        checks+=3
        # unknown release time: Hessian ratios recovered from two snapshots
        t1=age+5.;t0=5.; t2=t1+float(rng.uniform(.5,3))
        _,_,_,H1=reconstruct(p,data(p,mu,D,M,t1-t0),t1-t0)
        _,_,_,H2=reconstruct(p,data(p,mu,D,M,t2-t0),t2-t0)
        ratio=float(np.trace(H1)/np.trace(H2))
        estimated_t0=(ratio*t1-t2)/(ratio-1)
        assert np.isclose(estimated_t0,t0,atol=1e-8,rtol=1e-8)
        checks+=1
        # one snapshot known clock cannot resolve unknown source time
        newage=age*1.7
        D2=D*age/newage
        assert np.allclose(data(p,mu,D2,M,newage),y,rtol=1e-9,atol=1e-12)
        checks+=1

# Exact rank deficiency and algebraic nonidentification for six planar conic sensors
points=sp.Matrix([[1,0],[-1,0],[0,1],[0,-1],[sp.Rational(3,5),sp.Rational(4,5)],[sp.Rational(3,5),-sp.Rational(4,5)]])
V=sp.Matrix([[1,x,y,x*x,x*y,y*y] for x,y in points.tolist()])
assert V.rank()==5
v=sp.Matrix([-1,0,0,1,0,1]);assert V*v==sp.zeros(6,1)
checks+=2
# Arbitrarily small null-perturbation of a Gaussian log field remains negative definite
base=sp.Matrix([sp.Integer(0),0,0,-1,0,-1]);new=base+sp.Rational(1,10)*v
assert V*base==V*new and new[3]<0 and new[5]<0
checks+=3
print(f'PASS: {checks} checks, 4 exact full-rank constructions, conic nullspace, inversion, release-time alias')
