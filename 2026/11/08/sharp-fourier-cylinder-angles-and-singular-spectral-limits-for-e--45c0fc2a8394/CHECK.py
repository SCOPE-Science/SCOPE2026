"""Reproducibility checks for canonical Fourier/cylinder principal angles.
Run: python CHECK.py (requires NumPy). Finite checks supplement, not replace, proof.
"""
import math
import numpy as np

count = 0

def test(condition, explanation):
    global count
    assert bool(condition), explanation
    count += 1

def digit_set(base, level):
    return np.array([(base/4.0)*sum(((k>>j)&1)*base**j for j in range(level)) for k in range(2**level)], dtype=float)

def prefixes(base, level):
    return np.array([sum((1 if (k>>j)&1 else -1)*base**(-j-1) for j in range(level)) for k in range(2**level)], dtype=float)

def mhat(base, t, terms=18):
    result = np.ones_like(np.asarray(t,dtype=float))
    for j in range(1,terms+1):
        result = result*np.cos(2*math.pi*np.asarray(t)/base**j)
    return result

for b in (4,6,8,10,12):
    tau=b/(4*(b-1))
    beta=float(mhat(b,tau))
    test(0<beta<1,'beta interval')
    previous=1.
    for m in range(1,6):
        n=2**m
        lam=digit_set(b,m)
        pref=prefixes(b,m)
        t=lam/b**m
        B=np.exp(-2j*math.pi*lam[:,None]*pref[None,:])/math.sqrt(n)
        vals=mhat(b,t)
        K=vals[:,None]*B
        # independent columns are level-m normalized cylinder indicators
        singular=np.linalg.svd(K,compute_uv=False)
        test(np.max(np.abs(B@B.conj().T-np.eye(n)))<5e-10,'prefix Hadamard unitarity')
        test(np.max(np.abs(np.sort(singular)-np.sort(vals)))<5e-10,'singular values')
        test(abs(np.min(vals)-float(mhat(b,tau*(1-b**(-m)))))<1e-11,'exact minimum')
        test(abs(np.max(vals)-1)<1e-12,'max = 1')
        test(beta < min(vals) < previous,'strict monotone levels')
        previous=min(vals)
        # Orthogonality via exact leading-digit parity, independent of floating point.
        i_lam=[sum(((k>>j)&1)*b**j for j in range(m)) for k in range(n)]
        for k in range(n):
            for l in range(k):
                diff=i_lam[k]-i_lam[l]
                j=0
                while diff%b==0:
                    diff//=b; j+=1
                # This is the integer argument inside cos(pi * odd / 2).
                test(diff%2 != 0,'odd leading difference gives exact zero cosine factor')
        # finite cylinder quadrature via genuinely sampled residual sign digits
        if m<=3 and b in (4,6):
            for idx in (0,n-1):
                a=lam[idx]
                tail_depth=10
                tail=np.array([sum((1 if (kk>>j)&1 else -1)*b**(-m-j-1) for j in range(tail_depth)) for kk in range(2**tail_depth)])
                # average on cylinder, no direct use of Fourier product
                observed=np.exp(-2j*math.pi*a*(pref[0]+tail)).mean()/math.sqrt(n)
                predicted=K[idx,0]
                test(abs(observed-predicted)<1e-9,'direct cylinder quadrature')
        # Test coupling inequality for two 1-Lipschitz functions.
        if m<=4:
            full=[]
            for idx in range(2**(m+4)):
                full.append((b/4.0)*sum(((idx>>j)&1)*b**(-j-1) for j in range(m+4)))
            sample=mhat(b,np.array(full))
            for fun in (lambda x:x,lambda x:x*x/2):
                err=abs(np.mean(fun(vals))-np.mean(fun(sample)))
                L=sum((2*math.pi/b**j) for j in range(1,15)) # upper bound on |mhat'| on support
                test(err<=L*tau*b**(-m)+2e-12,'coupling rate')
    test(abs(previous-beta)<0.01,'convergence of extremal angle')

for b in (40,80,160,320):
    beta=float(mhat(b,b/(4*(b-1))))
    scaled=(1-beta)*(b-1)**2
    test(abs(scaled-math.pi**2/8)<0.005,'large-base first-order coefficient')

print('PASS:',count,'deterministic tests; exact formula proved independently in RESULT.md')
