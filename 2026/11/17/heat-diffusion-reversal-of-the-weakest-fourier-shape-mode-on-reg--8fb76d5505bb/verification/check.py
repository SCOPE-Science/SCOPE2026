"""Independent finite-mode and finite-difference checks of circle heat-energy Hessian.
All infinite-frequency statements in the accompanying proof are analytic; these tests are illustrative.
"""
import math
import numpy as np

def energy(t, angles, trunc=300):
    z=np.array(angles)
    n=np.arange(-trunc,trunc+1)
    f=np.exp(1j*np.outer(n,z)).mean(axis=1)
    return float(np.sum(np.exp(-2*t*n*n)*np.abs(f)**2))

def residue_gap(N,t,k,trunc=300):
    n=np.arange(-trunc,trunc+1)
    w=n*n*np.exp(-2*t*n*n)
    return float(np.sum(w[n%N==k])-np.sum(w[n%N==0]))

checks=0
for N in [4,5,6,8,9,13]:
    theta=2*math.pi*np.arange(N)/N
    for t in [.015,.035,.1,.25,.5]:
        n=np.arange(-300,301)
        for k in range(1,N//2+1):
            u=np.cos(2*math.pi*k*np.arange(N)/N)
            eps=.0001
            numerical=(energy(t,theta+eps*u)+energy(t,theta-eps*u)-2*energy(t,theta))/eps**2
            uhat=np.fft.fft(u)
            pred=2/N**2*sum(residue_gap(N,t,j)*abs(uhat[j])**2 for j in range(1,N))
            assert abs(numerical-pred)<5e-5*max(1.,abs(pred)), (N,t,k,numerical,pred)
            checks+=1
    for t in [.005,.007,.01]:
        gaps=np.array([residue_gap(N,t,k) for k in range(1,N)])
        if np.min(gaps)>1e-12:
            assert np.argmin(gaps) in [0,N-2];checks+=1
    for t in [1.,1.5]:
        gaps=np.array([residue_gap(N,t,k) for k in range(1,N)])
        assert np.argmin(gaps) in ([N//2-1] if N%2==0 else [(N-1)//2-1,(N+1)//2-1]);checks+=1
# One representative nondegenerate soft-mode crossing for N=4.
def diff(t):return residue_gap(4,t,1)-residue_gap(4,t,2)
a,b=.20,.8
assert diff(a)<0<diff(b)
for _ in range(50):
    m=(a+b)/2
    if diff(m)>0:b=m
    else:a=m
assert abs(diff((a+b)/2))<1e-12
print('checks_passed',checks+2)
print('representative_N4_crossing_t', format((a+b)/2,'.12f'))
