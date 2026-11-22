#!/usr/bin/env python3
"""Finite diagnostic checks for crossed-parity Fourier sampling; standard library only."""
import cmath, math

def test(M,N,delta,epsilon):
    size=M*N
    rows=[(j,k) for j in range(M) for k in range(N)]
    freqs=[(m,n) for m in range(M) for n in range(N)]
    A=[[cmath.exp(2j*math.pi*(m*(j+delta*(-1)**k)/M+n*(k+epsilon*(-1)**j)/N))/math.sqrt(size)
        for m,n in freqs] for j,k in rows]
    t=math.sin(math.pi*delta)*math.sin(math.pi*epsilon)
    H=[[0j]*size for _ in range(size)]
    s=abs(t)
    max_error=0.0
    for u,(m,n) in enumerate(freqs):
        for v,(mp,np) in enumerate(freqs):
            direct=sum(A[r][u].conjugate()*A[r][v] for r in range(size))
            d=mp-m; e=np-n
            if d==0 and e==0: predicted=1.0
            elif abs(d)==M//2 and abs(e)==N//2:
                predicted=-(1 if d*e>0 else -1)*t
            else: predicted=0.0
            max_error=max(max_error,abs(direct-predicted))
            if u!=v: H[u][v]=predicted
    assert max_error<2e-11,(M,N,delta,epsilon,max_error)
    max_h2=0.0
    for a in range(size):
        for b in range(size):
            z=sum(H[a][c]*H[c][b] for c in range(size))
            max_h2=max(max_h2,abs(z-((s*s) if a==b else 0)))
    assert max_h2<2e-11
    return max_error,max_h2

if __name__=='__main__':
    cases=0
    for M,N in [(2,2),(2,4),(4,6),(6,4),(8,8)]:
        for d,e in [(0,0.0),(0.1,0.23),(-0.37,0.42),(0.5,0.5),(0.8,-0.6)]:
            err,identity=test(M,N,d,e)
            cases+=1
    print(f'PASS: {cases} complete-matrix configurations, matching Gram support, and quadratic identity')
