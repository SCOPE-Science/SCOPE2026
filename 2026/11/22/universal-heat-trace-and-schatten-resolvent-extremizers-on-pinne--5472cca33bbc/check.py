#!/usr/bin/env python3
"""Supplementary finite-mask tests for cyclic Dirichlet spectral extremizers.
Requires numpy; the infinite family is proved analytically, not by testing.
"""
import itertools
import math
import numpy as np

checks = 0

def assert_near(a, b, tol=2e-9):
    global checks
    assert abs(a-b) <= tol*(1+abs(a)+abs(b)), (a,b)
    checks += 1

def gaps(mask, N):
    z=sorted(mask)
    return tuple((z[(i+1)%len(z)]-z[i])%N or N for i in range(len(z)))

def spectrum(N, mask, mass):
    seen=set(mask)
    U=[i for i in range(N) if i not in seen]
    if not U:
        return np.array([])
    T=np.zeros((len(U),len(U)))
    idx={v:i for i,v in enumerate(U)}
    for v, i in idx.items():
        T[i,i]=2+mass
        for w in ((v+1)%N,(v-1)%N):
            if w in idx:
                T[i,idx[w]]-=1
    return np.linalg.eigvalsh(T)

def trace_of_block(g, mass):
    if g==1:
        return 0.
    if mass==0:
        return (g*g-1)/6
    theta=math.acosh(1+mass/2)
    return (g/math.tanh(g*theta)-1/math.tanh(theta))/(2*math.sinh(theta))

for N in range(3,11):
    for k in range(1,N+1):
        samples=[]
        for mask in itertools.combinations(range(N),k):
            gs=gaps(mask,N)
            samples.append((mask,gs))
        q,r=divmod(N,k)
        balanced=tuple(sorted((q,)*(k-r)+(q+1,)*r))
        concentrated=tuple(sorted((1,)*(k-1)+(N-k+1,)))
        for mass in (0.,0.5,2.):
            for fun in (lambda x:sum(np.exp(-0.2*x)),lambda x:sum(np.exp(-2.3*x)),lambda x:sum(x**-0.5),lambda x:sum(x**-1),lambda x:sum(x**-2.25)):
                vals=[]
                for mask,gs in samples:
                    eig=spectrum(N,mask,mass)
                    v=float(fun(eig))
                    vals.append(v)
                lo,hi=min(vals),max(vals)
                for (mask,gs),v in zip(samples,vals):
                    if tuple(sorted(gs))==balanced:
                        assert_near(v,lo)
                    elif k not in (1,N):
                        assert v>lo+1e-10, ('minimum uniqueness',N,k,mass,gs,v,lo)
                        checks+=1
                    if tuple(sorted(gs))==concentrated:
                        assert_near(v,hi)
                    elif k not in (1,N):
                        assert v<hi-1e-10, ('maximum uniqueness',N,k,mass,gs,v,hi)
                        checks+=1
            for mask,gs in samples:
                eig=spectrum(N,mask,mass)
                got=float(sum(eig**-1))
                want=sum(trace_of_block(g,mass) for g in gs)
                assert_near(got,want)
print('CYCLE_SPECTRAL_EXTREMAL_CHECK_OK',checks)
