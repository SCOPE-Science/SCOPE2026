"""Independent finite checks for local equal-consecutive-triangle-area polygons.
All code and examples are self-contained; no external data is required.
"""
import numpy as np
from scipy.optimize import root


def areas(theta, amplitude, k):
    r = 1+amplitude*np.cos(k*theta + .27)
    p = np.column_stack((r*np.cos(theta),r*np.sin(theta)))
    a=np.roll(p,-1,axis=0)-p
    b=np.roll(p,-2,axis=0)-np.roll(p,-1,axis=0)
    return a[:,0]*b[:,1]-a[:,1]*b[:,0]


def check(n, alpha, amplitude, k):
    base=alpha+2*np.pi*np.arange(n)/n
    def residual(u):
        theta=base.copy();theta[1:]+=u
        f=areas(theta,amplitude,k)
        return f[:-1]-f[-1]
    sol=root(residual,np.zeros(n-1),tol=1e-12)
    theta=base.copy();theta[1:]+=sol.x
    err=max(abs(residual(sol.x)))
    gaps=np.diff(np.r_[theta,theta[0]+2*np.pi]);assert min(gaps)>0
    assert err<2e-11,(n,k,alpha,amplitude,err)
    assert np.all(np.isfinite(sol.x))
    return np.max(np.abs(sol.x)),err


if __name__=='__main__':
    checks=0
    for n in (5,7,9,11,15):
        c=np.cos(2*np.pi/n)-np.cos(4*np.pi/n)
        J=np.zeros((n-1,n-1))
        for i in range(n-1):
            # c*(u_{i+2}-u_i - u_1+u_{n-1}) for the reference row i=n-1
            for j,coef in [( (i+2)%n,1),(i,-1),(1,-1),(n-1,1)]:
                if j!=0:J[i,j-1]+=c*coef
        assert np.linalg.svd(J,compute_uv=False).min()>1e-3
        checks+=1
        for k in (1,2,3,4,n//2+1,n+1):
            for alpha in (0.0,.19,1.0):
                for amp in (.0001,.001,.007):
                    check(n,alpha,amp,k);checks+=1
    # Test first variation against implicit angular response.
    for n in (5,7,9):
        alpha=.23;k=4;a=1e-6
        base=alpha+2*np.pi*np.arange(n)/n
        f=np.cos(k*base+.27)
        d=2*np.pi/n
        c=np.cos(d)-np.cos(2*d)
        G=(np.sin(d)-np.sin(2*d))*(f+np.roll(f,-2))+2*np.sin(d)*np.roll(f,-1)
        h=(G.mean()-G)/c
        u=np.zeros(n);cur=0
        for _ in range(n-1):
            nxt=(cur+2)%n;u[nxt]=u[cur]+h[cur];cur=nxt
        assert np.max(np.abs(c*(np.roll(u,-2)-u)+G-G.mean()))<1e-9
        theta=base.copy();theta[1:]+=a*u[1:]
        err=max(abs(areas(theta,a,k)-areas(theta,a,k).mean()))
        assert err<5e-10,err
        checks+=1
    print('PASS:',checks,'numerical tests. These test exact algebra/Jacobian and near-circle examples, not the general theorem.')
