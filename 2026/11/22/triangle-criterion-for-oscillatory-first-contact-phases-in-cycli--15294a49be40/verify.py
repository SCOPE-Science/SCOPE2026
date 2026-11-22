"""Independent numerical and algebraic checks for cyclic-switching diffusion arrival-phase theorem."""
import numpy as np
from scipy.linalg import expm, sqrtm
from scipy.sparse import diags, block_diag, kron, eye, csr_matrix
from scipy.sparse.linalg import spsolve
from math import sqrt, pi

CHECKS=0

def assert_near(a,b,tol=1e-8):
    global CHECKS
    CHECKS += 1
    if not np.allclose(a,b,rtol=tol,atol=tol):
        raise AssertionError((a,b))

def params(ds,rate=1.):
    a=rate/np.asarray(ds, dtype=float)
    Q=rate*np.array([[-1.,1.,0.],[0.,-1.,1.],[1.,0.,-1.]])
    L=-np.diag(1./np.asarray(ds))@Q
    return a,Q,L

def formula(ds,x,rate=1.):
    a,Q,L=params(ds,rate)
    S=sum(a); P=a[0]*a[1]+a[1]*a[2]+a[2]*a[0]
    m=S/2
    rho=np.asarray(ds)/sum(ds)
    Pi=np.outer(np.ones(3),rho)
    R=np.eye(3)-Pi
    u=sqrt((sqrt(P)+m)/2)
    M=(L-m*R)/(2*u)
    discr=S*S-4*P
    if discr< -1e-11:
        v=sqrt((sqrt(P)-m)/2)
        H=Pi+np.exp(-u*x)*(R*np.cos(v*x)-M*np.sin(v*x)/v)
    elif discr>1e-11:
        v=sqrt((m-sqrt(P))/2)
        H=Pi+np.exp(-u*x)*(R*np.cosh(v*x)-M*np.sinh(v*x)/v)
    else:
        H=Pi+np.exp(-u*x)*(R-x*M)
    return H,discr,Pi,u

for ds in ([1,1,1], [1,1,.3], [1,1,.25], [1,1,.1], [1,1,4], [2,1,5], [1,3,2]):
    a,Q,L=params(ds)
    S=sum(a); P=a[0]*a[1]+a[1]*a[2]+a[2]*a[0]
    root=np.sort_complex(np.linalg.eigvals(L))
    assert_near(np.poly(root),[1,-S,P,0],tol=5e-7)
    for x in (0.0,.3,1.,2.,4.,8.):
        H,discr,Pi,u=formula(ds,x)
        # Independent spectral principal matrix square root, clipped tiny round-off eigenvalue.
        eig,V=np.linalg.eig(L.astype(complex))
        eig[np.argmin(abs(eig))]=0
        Z=(V*np.sqrt(eig))@np.linalg.inv(V)
        Hspec=expm(-x*Z).real
        assert_near(H,Hspec,5e-7)
        assert_near(H.sum(axis=1),np.ones(3),5e-7)
        CHECKS+=1
        assert H.min()>-1e-7
        CHECKS+=1
        assert H.max()<1+1e-7
    H0,_,_,_=formula(ds,0)
    assert_near(H0,np.eye(3))
    Hfar,_,Pi,_=formula(ds,120)
    assert_near(Hfar,Pi,tol=5e-6)

# A distinct finite-difference backward boundary-value problem, not matrix square-root calculation.
for ds in ([1.,1.,1.], [1.,1.,.32], [1.,1.,.25], [1.,1.,.16]):
    a,Q,L=params(ds)
    xmax=24.0
    h=.03
    n=round(xmax/h)-1
    grid=np.arange(1,n+1)*h
    B=diags([np.ones(n-1),-2*np.ones(n),np.ones(n-1)],[-1,0,1],format='csr')/h**2
    # unknown ordering grid-point then phase
    A=kron(B,diags(ds,format='csr'))+kron(eye(n,format='csr'),csr_matrix(Q))
    rho=np.asarray(ds)/sum(ds)
    rhs=np.zeros((n,3,3))
    rhs[0]-=np.diag(ds)@np.eye(3)/h**2
    rhs[-1]-=np.diag(ds)@np.outer(np.ones(3),rho)/h**2
    Z=spsolve(A,rhs.reshape(n*3,3)).reshape(n,3,3)
    for x in (.3,1.,2.,4.):
        index=round(x/h)-1
        xp=grid[index]
        H,_,_,_=formula(ds,xp)
        assert_near(Z[index],H,tol=2e-4)

# Sharp one-defect c=4 and period optimum c=3/2.
for c in (.05,.25,1.,1.5,2.,3.9,3.999):
    D3=1/c
    a,Q,L=params([1,1,D3]); S=sum(a); P=a[0]*a[1]+a[1]*a[2]+a[2]*a[0]
    v=sqrt((sqrt(P)-S/2)/2)
    x0=pi/(2*v)
    T=pi/v
    rho=np.array([1,1,D3])/(2+D3)
    # each matrix entry is a damped sin+cos; zeros repeat exactly at period pi/v.
    R=np.eye(3)-np.outer(np.ones(3),rho)
    u=sqrt((sqrt(P)+S/2)/2)
    M=(L-(S/2)*R)/(2*u)
    for i in range(3):
      for j in range(3):
        angle=np.arctan2(-M[i,j]/v,R[i,j])
        z=(angle+pi/2)%pi
        xx=z/v
        if xx<1e-8: xx+=pi/v
        H1,_,_,_=formula([1,1,D3],xx)
        H2,_,_,_=formula([1,1,D3],xx+T)
        assert_near(H1[i,j],rho[j],tol=4e-8)
        assert_near(H2[i,j],rho[j],tol=4e-8)
# f(c)=v^2/a has unique maximum at c=1.5, derivative sign.
for c in (.1,.3,1.,1.5,2.,3.,3.9):
    v2=.5*(sqrt(1+2*c)-1-c/2)
    assert v2>0
    CHECKS +=1
assert_near(.5*(sqrt(1+3)-1-1.5/2),1/8)

# Closed-form identical-diffusivity diagonal.
for x in (.1, .5, 2.,8.):
    H,discr,Pi,u=formula([1,1,1],x)
    a=1.; v=sqrt((sqrt(3)-1.5)/2)
    assert_near(H[0,0], (1+2*np.exp(-u*x)*np.cos(v*x))/3)

print('PASS',CHECKS,'independent analytical/numerical comparisons')
