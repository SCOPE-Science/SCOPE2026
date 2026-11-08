#!/usr/bin/env python3
"""Numerical cross-check of exact cyclic spectrogram/autocorrelation assertions.

The analytic proof, not this finite check, covers every prime p>=5.
"""
import cmath, math, numpy as np


def chirp(p):
    n=p*p
    return np.exp((2j*math.pi/n)*(np.arange(n,dtype=np.int64)**3 % n))/math.sqrt(n)


def ambiguity(g):
    n=len(g)
    u=np.arange(n)
    z=np.exp(-2j*math.pi*np.arange(n)/n)
    return np.asarray([np.fft.fft(g*np.conj(np.roll(g,k))) for k in u])


def stft_intensities(g,x):
    n=len(g)
    return np.asarray([np.abs(np.fft.fft(x*np.conj(np.roll(g,a))))**2 for a in range(n)])


def rng_signal(p, classes, seed):
    rng=np.random.default_rng(seed)
    x=np.zeros(p*p,dtype=complex)
    for r in classes:
        x[r::p]=rng.normal(size=p)+1j*rng.normal(size=p)
    return x


def autocorr_blocks(p,x):
    return np.array([[np.vdot(np.roll(x[r::p],h), x[r::p])
        for h in range(1,p)] for r in range(p)])


def check(p):
    n=p*p
    g=chirp(p)
    a=ambiguity(g)
    for k in range(n):
        for ell in range(n):
            target = (1.0 if (k==0 and ell==0) else
                0.0 if k==0 else
                1/p if k%p else
                1/math.sqrt(p) if ell%p==0 else 0.0)
            assert abs(abs(a[k,ell])-target)<2e-9,(p,k,ell,a[k,ell],target)
    # Perfect cyclic autocorrelation in both populated residue blocks.
    x=np.zeros(n,dtype=complex)
    r,s=1,2
    t=np.arange(p,dtype=np.int64)
    ca=np.exp(2j*math.pi*(t*t%p)/p)
    cb=np.exp(2j*math.pi*((2*t*t+t)%p)/p)
    x[r::p]=2*ca
    x[s::p]=3*cb
    assert np.max(np.abs(autocorr_blocks(p,x)))<1e-9
    # Reciprocal scale exchanges the two block energies.
    y=x.copy(); y[r::p]*=1.5; y[s::p]/=1.5
    assert np.linalg.norm(x-y)>1
    X=stft_intensities(g,x);Y=stft_intensities(g,y)
    assert np.max(np.abs(X-Y))<1e-8,(p,np.max(np.abs(X-Y)))
    # Repeated for two unequal-weight spikes (without any chirp algebra).
    z=np.zeros(n,dtype=complex)
    z[1]=2+1j;z[2]=-1+4j
    zr=abs(z[1]);zs=abs(z[2]); w=z.copy();w[1]*=zs/zr;w[2]*=zr/zs
    assert np.max(np.abs(stft_intensities(g,z)-stft_intensities(g,w)))<1e-8
    # Nonperfect block prevents nontrivial reciprocal rescaling.
    u=rng_signal(p,[0,1],seed=p)
    v=u.copy();v[0::p]*=1.2;v[1::p]/=1.2
    assert np.max(np.abs(stft_intensities(g,u)-stft_intensities(g,v)))>1e-4
    # Three-block cross constraints prevent independent rescaling.
    u=rng_signal(p,[0,1,2],seed=p+10)
    v=u.copy();v[0::p]*=1.2;v[1::p]/=1.2
    assert np.max(np.abs(stft_intensities(g,u)-stft_intensities(g,v)))>1e-4
    # Independently verify the crucial double-Fourier normalization/sign identity.
    if p==5:
        f=rng_signal(p,[0,2,3],seed=333)
        V=stft_intensities(g,f)
        omega=np.exp(2j*math.pi/n)
        for u,vv in [(0,0),(0,1),(1,1),(1,3),(5,5),(5,1),(10,15)]:
            left=sum(V[aa,bb]*omega**(bb*u-aa*vv)
                for aa in range(n) for bb in range(n))
            chi=sum(f[j]*np.conj(f[(j-u)%n])*omega**(-vv*j)
                for j in range(n))
            ag=sum(np.conj(g[j])*g[(j-u)%n]*omega**(vv*j)
                for j in range(n))
            assert abs(left-n*chi*ag)<1e-8
    print('PASS p=%d n=%d ambiguity=%d raw_spectrogram_entries=%d' % (p,n,n*n,4*n*n))

for pp in [5,7,11]:check(pp)
print('CHECK_OK prime_squares=3 independent_intensity_tests=12')
