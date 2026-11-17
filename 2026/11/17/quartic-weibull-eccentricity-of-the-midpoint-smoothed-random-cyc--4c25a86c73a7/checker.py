"""Numerical diagnostics for the midpoint-envelope eccentricity theorem.
Scientific calculations use only publicly specified geometry and reproducible random numbers.
"""
import numpy as np

def harmonics_from_angles(theta):
    n = theta.shape[-1]
    q = np.exp(2j * np.pi * np.arange(n)/n)
    z = np.exp(1j*theta)
    a = np.mean(z / q, axis=-1)
    b = np.mean(z * q, axis=-1)
    return a,b

def ell_axes(a,b):
    return abs(a)+abs(b), abs(abs(a)-abs(b))

def check_independent_svd():
    rng = np.random.default_rng(9801)
    for n in (3,4,7,20):
        theta = np.sort(rng.uniform(0,2*np.pi,size=n))
        a,b = harmonics_from_angles(theta)
        t = 2*np.pi*np.arange(1000)/1000
        xy = a*np.exp(1j*t)+b*np.exp(-1j*t)
        coeff=np.array([[np.real(a+b),-np.imag(a-b)],
                        [np.imag(a+b),np.real(a-b)]])
        expected=np.linalg.svd(coeff,compute_uv=False)
        assert np.allclose(expected,ell_axes(a,b),rtol=1e-12,atol=1e-12)
        assert np.all(np.isfinite(xy))
    print('FOURIER_ELLIPSE_SVD_IDENTITY_OK')

def check_damped_midpoints():
    rng=np.random.default_rng(614)
    for n,k in ((5,45),(7,120),(12,350)):
        theta=np.sort(rng.uniform(0,2*np.pi,size=n))
        z=np.exp(1j*theta)
        mu=z.mean()
        z=z-mu
        a,b=harmonics_from_angles(theta)
        base=np.arange(n)*2*np.pi/n
        scale=np.cos(np.pi/n)
        for _ in range(k):
            z=(z+np.roll(z,-1))/2/scale
        ell=a*np.exp(1j*(base+k*np.pi/n))+b*np.exp(-1j*(base+k*np.pi/n))
        assert np.max(abs(z-ell))<2e-8, (n,k,np.max(abs(z-ell)))
    print('MIDPOINT_SPECTRAL_ENVELOPE_OK')

def check_statistical_limit():
    rng=np.random.default_rng(210826)
    for n,reps in ((64,8000),(256,10000),(512,8000)):
        batch=200
        ratios=[]; angles=[]
        q=np.exp(2j*np.pi*np.arange(n)/n)
        for _ in range(reps//batch):
            theta=2*np.pi*np.sort(rng.random((batch,n)),axis=1)
            z=np.exp(1j*theta)
            a=(z/q).mean(axis=1)
            b=(z*q).mean(axis=1)
            ratio=np.abs(b)/np.abs(a)
            # sqrt(n) times relative major/minor axis difference
            h=np.sqrt(n)*2*ratio/(1+ratio)
            ratios.append(h)
            angles.append((np.angle(a)+np.angle(b))% (2*np.pi))
        ratios=np.concatenate(ratios)
        angles=np.concatenate(angles)
        for t in (0.5,1.):
            actual=np.mean(ratios<=t)
            target=1-np.exp(-t*t)
            # A generous finite-size tolerance; this is a diagnostic, not a proof.
            assert abs(actual-target)<0.08, (n,t,actual,target)
        # Exact rotation symmetry predicts vanishing orientation Fourier modes.
        assert abs(np.mean(np.exp(1j*angles)))<0.045
        print(f'n={n}, reps={reps}, mean={ratios.mean():.6f}, '
              f'P(H<=1)={np.mean(ratios<=1):.6f}, limit={1-np.exp(-1):.6f}')
    print('MIDPOINT_RANDOM_ELLIPSE_WEIBULL_DIAGNOSTICS_OK')

if __name__ == '__main__':
    check_independent_svd()
    check_damped_midpoints()
    check_statistical_limit()
