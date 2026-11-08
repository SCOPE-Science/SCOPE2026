#!/usr/bin/env python3
"""Independent numerical spectral, projector, and capture-law checks.

Uses the normalized symmetric tensor basis, unlike verify_rank.py.
The analytical proof, not floating-point checks, establishes the all-n theorem.
"""
import numpy as np
from math import sqrt


def eta(n, r):
    if n % 2:
        return 1.0
    if r == 0:
        return 1 - 2*(n-1)/n**2
    if r == 1:
        return 1.0
    if r == n//2:
        return 1 - 4*(n-1)/n**2 if n % 4 == 0 else 1.0
    if r % 2 == 0:
        return 1 - (3*n-4)/n**2
    return 1 - 1/n


def projection_spectral(H, R):
    w, V = np.linalg.eigh(H)
    N = len(w)
    P = np.zeros((N,N), complex)
    j = 0
    while j < N:
        k = j+1
        while k < N and abs(w[k]-w[j]) < 1e-7:
            k += 1
        U = V[:,j:k]
        bw, bv = np.linalg.eigh(U.conj().T@R@U)
        Z = U@bv[:,bw<1e-7]
        P += Z@Z.conj().T
        j = k
    return P


def check(n):
    pairs = [(a,b) for a in range(n) for b in range(a,n)]
    N = len(pairs)
    idx = {p:i for i,p in enumerate(pairs)}
    S = np.zeros((n*n,N), complex)
    for j,(a,b) in enumerate(pairs):
        if a==b: S[a*n+b,j]=1
        else: S[a*n+b,j]=S[b*n+a,j]=1/sqrt(2)
    a1 = np.zeros((n,n), float)
    for j in range(n):
        a1[j,(j+1)%n]=a1[(j+1)%n,j]=1
    H=S.conj().T@(np.kron(a1,np.eye(n))+np.kron(np.eye(n),a1))@S
    weights=np.zeros(N)
    for j,(a,b) in enumerate(pairs):
        if a!=b and (a-b)%n in (1,n-1):weights[j]=1+(3*a+b)%7
    R=np.diag(weights)
    P=projection_spectral(H,R)
    Q=np.zeros((N,N),complex)
    if n%2==0:
        m=n//2
        for shift in range(n):
            for j,(a,b) in enumerate(pairs):
                dest=tuple(sorted(((a+shift)%n,(b+shift)%n)))
                Q[idx[dest],j]+=(-1)**shift/n
        ae=np.zeros(N,complex)
        for j in range(n):
            ae[idx[tuple(sorted((j,(j+1)%n)))]]+=(-1)**j/sqrt(n)
        Q-=np.outer(ae,ae.conj())
        for k in range(1,m):
            z=np.exp(2j*np.pi*k*np.arange(n)/n)/sqrt(n)
            y=np.exp(2j*np.pi*(k+m)*np.arange(n)/n)/sqrt(n)
            v=S.conj().T@(np.kron(z,y)+np.kron(y,z))/sqrt(2)
            Q+=np.outer(v,v.conj())
    assert np.max(abs(P-Q))<2e-8, (n,'projector')
    assert np.max(abs(Q@Q-Q))<2e-8, (n,'idempotence')
    assert np.max(abs(H@Q))<2e-8, (n,'stationarity')
    assert np.max(abs(R@Q))<2e-8, (n,'darkness')
    want=0 if n%2 else (n-1 if n%4==0 else n-2)
    assert abs(np.trace(P)-want)<2e-8, (n,'dimension')
    for r in range(n//2+1):
        loc=idx[(0,r)]
        got=1-P[loc,loc].real
        assert abs(got-eta(n,r))<2e-8, (n,r,got,eta(n,r))
    print(f'n={n:2d} dimension={want:2d} distance-resolved_capture=PASS')


if __name__=='__main__':
    for n in range(3,15):check(n)
    print('PASS: exact projector agrees with independent spectral construction')
