"""Independent finite graph checks for Mycielskian quantum layer transfer.
Run with Python 3, numpy and scipy: python verify.py
"""
import numpy as np
from scipy.linalg import expm, eigvalsh

def adjacency(n,steps):
    a=np.zeros((n,n),dtype=float)
    for i in range(n):
        for k in steps:
            j=(i+k)%n
            if i != j: a[i,j]=a[j,i]=1.
    return a

def mycielski(a):
    n=len(a)
    b=np.zeros((2*n+1,2*n+1))
    b[:n,:n]=a
    b[:n,n:2*n]=a
    b[n:2*n,:n]=a
    b[n:2*n,2*n]=1
    b[2*n,n:2*n]=1
    return b

def quotient(n,r):
    return np.array([[r,r,0],[r,0,np.sqrt(n)],[0,np.sqrt(n),0]],dtype=float)

maxerr=0.
checks=0
for n,steps in [(5,[1]),(6,[1]),(7,[1]),(8,[1]),(9,[1,2]),(10,[1,2]),(12,[1,2])]:
    base=adjacency(n,steps)
    r=int(base.sum(axis=0)[0]);assert all(base.sum(axis=0)==r)
    full=mycielski(base); Q=quotient(n,r)
    for t in (0.1,0.7,2.0):
        f=expm(-1j*t*full)[:n,2*n]
        z=expm(-1j*t*Q)[0,2]
        err=abs(np.vdot(f,f)-abs(z)**2)
        maxerr=max(maxerr,err)
        assert err<2e-12,(n,steps,t,err)
        checks+=1
    lam=eigvalsh(Q)
    chi=lambda x:x**3-r*x*x-(n+r*r)*x+r*n
    assert max(abs(chi(x)) for x in lam)<1e-8

for r in (2,3,4):
    for n in (100,500,2000,8000):
        q=quotient(n,r)
        lam=eigvalsh(q)
        chi_prime=lambda x:3*x*x-2*r*x-(n+r*r)
        c=r*np.sqrt(n)/np.array([chi_prime(x) for x in lam])
        assert c[0]>0 and c[1]<0 and c[2]>0
        assert abs(c.sum())<1e-9
        T=np.pi/np.sqrt(n)
        qprob=abs(sum(c*np.exp(-1j*lam*T)))**2
        ub=4*c[1]**2
        assert qprob<=ub*(1+1e-10)
        assert abs(n*ub-4*r*r)<(1000*r**6)/n
        checks+=1
print('PASS independent full-matrix calculations and spectral inequalities',checks,'cases; maximum full-vs-reduced error',maxerr)
