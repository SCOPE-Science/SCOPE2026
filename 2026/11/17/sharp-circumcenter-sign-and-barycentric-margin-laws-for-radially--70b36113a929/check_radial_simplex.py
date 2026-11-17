"""Independent numerical checks for radially scaled regular-simplex circumcenters."""
import numpy as np


def predicted(r):
    d = len(r)-1
    w = 1/np.asarray(r, dtype=float)
    U = np.sum(w)
    V = np.dot(w,w)
    B = np.sum(r)
    mu = B/U
    kappa = ((d+1)*(2-d)+d*mu*V)/U
    return (d + kappa*w - d*mu*w*w)/(2*(d+1))


def direct(r):
    n = len(r)
    d = n-1
    centering = np.eye(n)[:,:d] - np.ones((n,d))/n
    Q, _ = np.linalg.qr(centering)
    vertices = (Q.T @ np.diag(r))*np.sqrt(n/d)
    A = 2*(vertices[:,1:]-vertices[:,[0]]).T
    b = np.sum(vertices[:,1:]**2,axis=0)-np.sum(vertices[:,[0]]**2)
    center = np.linalg.solve(A,b)
    lam = np.linalg.solve(np.vstack((vertices,np.ones(n))),np.append(center,1.0))
    return lam,vertices,center


def verify():
    rng = np.random.default_rng(20261108)
    max_err=0
    count=0
    for d in range(2,9):
        for _ in range(1500):
            r=np.exp(rng.uniform(-2,2,size=d+1))
            f=predicted(r)
            actual,verts,c=direct(r)
            err=float(np.max(np.abs(f-actual)))
            max_err=max(max_err,err)
            assert err<2e-10, (d,r,err)
            assert abs(np.sum(f)-1)<1e-11
            assert np.max(abs(np.linalg.norm(verts-c[:,None],axis=0)**2-np.linalg.norm(verts-c[:,None],axis=0)[0]**2))<2e-8
            sorted_lam=f[np.argsort(r)]
            assert np.all(np.diff((sorted_lam<(-1e-10)).astype(int)) <=0), (d,r,f)
            assert sorted_lam[-2] > 1/(2*d)-1e-12,(d,r,sorted_lam)
            count+=1
        for k in range(1,d):
            r=np.r_[np.ones(k),np.full(d+1-k,1e6)]
            f=predicted(r)
            assert np.sum(f<0)==k,(d,k,f)
            lim=((d+2)*k-d*(d+1))/(2*k*k)
            assert abs(f[0]-lim)<0.01,(d,k,f[0],lim)
        r=np.r_[np.full(d,1.0), 1e8]
        f=predicted(r)
        assert abs(f[0] - 1/(2*d)) < 1e-6,(d,f)
    # Independently sample the sharp fixed-ratio inequality at many aspect ratios.
    tested = 0
    for d in range(2, 9):
        for _ in range(10000):
            r = np.exp(rng.uniform(-3, 3, d+1))
            indices = np.argsort(-r)
            x = r[indices[1]] / r[indices[0]]
            lower = (1/(2*d) + (d-1)*(d+1)*x*x/(2*d*(d+x)**2))
            actual = predicted(r)[indices[1]]
            assert actual >= lower - 3e-12, (d, r, actual, lower)
            tested += 1
        for x in [0.0001, 0.01, 0.1, 0.25, 0.75, 1.0]:
            r = np.r_[1/x, np.ones(d)]
            lower = (1/(2*d) + (d-1)*(d+1)*x*x/(2*d*(d+x)**2))
            assert abs(predicted(r)[1] - lower) < 1e-10, (d,x)
    print('RADIAL_SIMPLEX_PREFIX_SHARP_BOUND_OK', count, tested,
          'max_linear_algebra_error', f'{max_err:.3e}')

if __name__=='__main__':
    verify()
