"""Reproduce finite tests for a two-channel cyclic rectangular-window frame theorem.

Requires only Python 3.10+ standard library. Run: python3 CHECK.py
Finite tests support, but do not replace, the all-integer analytic proof.
"""
from math import sin, cos, pi, sqrt, isclose
from cmath import exp

COUNT = 0

def check(condition, message):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(message)

def response(m, k):
    """N times the squared unitary DFT of the normalized half-boxcar."""
    N = 2*m
    k %= N
    if k == 0:
        return float(m)
    if k % 2 == 0:
        return 0.0
    return 1.0/(m*sin(pi*k/N)**2)

def spectrum(m, s, a=1.0, b=1.0):
    return [a*response(m,j)+b*response(m,j-s) for j in range(2*m)]

def direct_operator(m, s, a, b):
    """Construct the complete frame operator from all 2N Gabor vectors."""
    N=2*m
    S=[[0j for _ in range(N)] for _ in range(N)]
    for ell,weight in ((0,a),(s,b)):
        for k in range(N):
            vector=[sqrt(weight/m)*exp(2j*pi*ell*j/N) if (j-k)%N < m else 0j for j in range(N)]
            for i in range(N):
                for j in range(N):
                    S[i][j] += vector[i]*vector[j].conjugate()
    return S

def fourier_diagonalize(S):
    N=len(S)
    U=[[exp(-2j*pi*r*k/N)/sqrt(N) for k in range(N)] for r in range(N)]
    temp=[[sum(U[i][k]*S[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
    return [[sum(temp[i][k]*U[j][k].conjugate() for k in range(N)) for j in range(N)] for i in range(N)]

# Exact analytical Fourier representation versus independent geometric DFT.
for m in range(2,83):
    N=2*m
    for k in range(N):
        coeff=sum(exp(-2j*pi*k*j/N) for j in range(m))/sqrt(m*N)
        val=N*(abs(coeff)**2)
        check(abs(val-response(m,k)) < 2e-8, ('Fourier response',m,k,val,response(m,k)))

# Complete unweighted design enumeration, including singular gaps and m=2 exception.
for m in range(2,99):
    N=2*m
    good=[]
    for s in range(1,N):
        values=spectrum(m,s)
        A=min(values); B=max(values)
        if s%2==0 and m>=3:
            check(A < 1e-12, ('even-gap rank obstruction',m,s,A))
            continue
        check(A > 0.0, ('positive frame',m,s))
        good.append((s,B/A,A,B))
        if s%2:
            H=response(m,s)
            check(abs(B-(m+H)) < 1e-8, ('exact top',m,s,B,m+H))
            if m%2 and s==m:
                want=1/(m*cos(pi/m)**2)
            elif m%2:
                want=1/m
            else:
                want=1/(m*cos(pi/(2*m))**2)
            check(abs(A-want)<1e-8, ('exact bottom',m,s,A,want))
        else:
            check(m==2 and s==2 and abs(A-2)<1e-12 and abs(B-2)<1e-12,('exception',m,s))
    best=min(x[1] for x in good)
    winners={s for s,c,_,_ in good if abs(c-best)<1e-8}
    if m==2:
        expected={2}; exact=1.0
    elif m%2:
        expected={m}; exact=(m*m+1)*cos(pi/m)**2
    else:
        expected={m-1,m+1}; exact=m*m*cos(pi/(2*m))**2+1
    check(winners==expected,('optimizing gaps',m,winners,expected))
    check(abs(best-exact)<1e-7,('optimal condition',m,best,exact))

# Independently synthesize frame operators and diagonalize with unitary DFT.
for m in range(2,9):
    for s in range(1,2*m):
        for a,b in ((1.,1.),(.4,1.6),(1.4,.6)):
            V=fourier_diagonalize(direct_operator(m,s,a,b))
            expected=spectrum(m,s,a,b)
            for j in range(2*m):
                for k in range(2*m):
                    target=expected[j] if j==k else 0.
                    check(abs(V[j][k]-target)<2e-10,('direct matrix check',m,s,a,b,j,k,V[j][k],target))

# Allocations symmetric about equality; every strict imbalance worsens conditioning.
for m in range(2,51):
    for s in range(1,2*m):
        E=spectrum(m,s)
        amin=min(E)
        if amin < 1e-12:
            continue
        ratio0=max(E)/amin
        for a in (.1,.25,.5,.75,1.25,1.5,1.75,1.9):
            b=2.-a
            vals=spectrum(m,s,a,b)
            check(min(vals)>0,('positive weights preserve frame',m,s,a))
            check(max(vals)/min(vals)>ratio0+1e-10,('unique equal weighting',m,s,a))
            reverse=spectrum(m,s,b,a)
            check(all(abs(x-y)<1e-11 for x,y in zip(sorted(vals),sorted(reverse))),('weight symmetry',m,s,a))
print(f'PASS {COUNT} independently enumerated finite assertions')
