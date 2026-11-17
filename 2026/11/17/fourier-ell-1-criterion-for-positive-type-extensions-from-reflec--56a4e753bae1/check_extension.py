#!/usr/bin/env python3
"""Finite diagnostics for the reflection-coset positive-type extension theorem.

The analytic proof covers every finite abelian group. These calculations test
cyclic examples and reconstruct positive semidefinite full-group kernels.
"""
import itertools
import math
import random
import numpy as np

rng = random.Random(260331)
checks = 0


def group_mul(g, k, n):
    a, t = g
    b, u = k
    return ((a + (-1)**t*b) % n, (t+u)%2)


def group_inverse(g, n):
    a, t = g
    return ((-a if t == 0 else a) % n, t)


def make_phi(f):
    """Construct the global state from reflection values on cyclic H."""
    n=len(f)
    alpha=np.fft.fft(f)/n
    norm1=float(np.sum(np.abs(alpha)))
    if norm1>1+1e-10:
        raise ValueError('Fourier l1 obstruction')
    chars=[]
    blocks=[]
    for j in range(n):
        if 2*j % n == 0:
            assert abs(alpha[j].imag)<1e-10
            chars.append((j,float(alpha[j].real)))
        elif j < (n-j)%n:
            blocks.append((j,complex(alpha[j])))
    rest=1-norm1
    assert rest >= -1e-10

    def phi(h,t):
        value=rest*(1 if t==0 else 0)
        for j,c in chars:
            value+=abs(c)*np.exp(2j*math.pi*j*h/n)*(1 if t==0 else (1 if c>=0 else -1))
        for j,c in blocks:
            w=2*abs(c)
            z=complex(c).conjugate()/abs(c) if abs(c) else 1
            rho=np.array([[1,z],[z.conjugate(),1]],dtype=complex)/2
            chi=np.exp(2j*math.pi*j*h/n)
            pi=np.diag([chi,chi.conjugate()])
            if t:
                pi=pi@np.array([[0,1],[1,0]])
            value+=w*np.trace(rho@pi)
        return complex(value)
    return phi

for n in (1,2,3,4,5,6,7,8,12):
    groups=list(itertools.product(range(n),range(2)))
    for _ in range(35):
        vals=np.array([rng.uniform(-1,1) for i in range(n)])
        alpha=np.fft.fft(vals)/n
        norm1=float(np.sum(np.abs(alpha)))
        if norm1>1:
            vals=vals/(norm1*(1+rng.random()))
        phi=make_phi(vals)
        assert abs(phi(0,0)-1)<1e-10
        checks+=1
        for i in range(n):
            assert abs(phi(i,1)-vals[i])<1e-10
            checks+=1
        # Full normalized positive-type condition on the entire group.
        gram=np.array([[phi(*group_mul(group_inverse(g,n),k,n)) for k in groups] for g in groups],dtype=complex)
        assert np.max(np.abs(gram-gram.conjugate().T))<1e-10
        assert np.linalg.eigvalsh(gram).min()>=-1e-9
        checks+=2
    if n>=3:
        vals=np.ones(n)
        vals[-1]=-1
        norm1=float(np.abs(np.fft.fft(vals)/n).sum())
        assert abs(norm1-(3-4/n))<1e-10 and norm1>1
        checks+=1
    if n in (1,2):
        for vals in itertools.product((-1,1),repeat=n):
            assert sum(abs(np.fft.fft(vals)/n))<=1+1e-10
            checks+=1
print(f'PASS {checks} finite diagnostics; universal theorem uses the analytic proof')
