#!/usr/bin/env python3
"""Exact (integer Gaussian) check for apex-weighted Boolean 2-shell Gabor projectors.
For integers A,B,D>0 in denominator with g(0)=(A+iB)/D and g(weight2)=1,
we multiply all ambiguity coefficients by D**2 and compare squared moduli.
"""
from math import comb
from collections import Counter
import numpy as np

def pop(x):return x.bit_count()
def formula(n,A,B,D):
    N=1<<n;m=n-2;C=Counter()
    for w in range(n+1):
        k=((n-2*w)**2-n)//2
        C[(A*A+B*B+D*D*k)**2]+=comb(n,w)
    for j in range(m+1):
        t=m-2*j
        for eps in (-1,1):
            C[(2*D*(A+D*eps*t))**2]+=comb(n,2)*comb(m,j)
    C[(2*B*D)**2]+=comb(n,2)*N//2
    C[(2*D*D)**2]+=comb(n,4)*3*N//8
    C[(6*D*D)**2]+=comb(n,4)*N//8
    C[0]+=(N-1-comb(n,2)-comb(n,4))*N+comb(n,4)*N//2
    assert sum(C.values())==N*N,(n,A,B,D,sum(C.values()),N*N)
    return C

def brute(n,A,B,D):
    N=1<<n
    g=[(A,B) if x==0 else ((D,0) if pop(x)==2 else (0,0)) for x in range(N)]
    C=Counter()
    for a in range(N):
        for b in range(N):
            re=im=0
            for x in range(N):
                u,v=g[x]; w,z=g[x^a]
                s=1 if pop(x&b)%2==0 else -1
                re += s*(u*w+v*z)
                im += s*(u*z-v*w)
            C[re*re+im*im]+=1
    return C

def rankformula(n,A,B,D):
    N=1<<n;m=n-2
    z0=sum(comb(n,w) for w in range(n+1) if A*A+B*B+D*D*(((n-2*w)**2-n)//2)==0)
    z2=(N//2 if B==0 else 0)+2*sum(comb(m,j) for j in range(m+1) if A==D*(m-2*j))
    return N-z0+comb(n,2)*(N-z2)+comb(n,4)*N//2

for n in range(4,8):
    for A,B,D in [(0,0,1),(1,0,1),(0,1,1),(1,1,1),(1,2,2),(2,1,2),(n-1,1,1)]:
        f=formula(n,A,B,D)
        b=brute(n,A,B,D)
        assert f==b,(n,(A,B,D),f-b,b-f)
        assert rankformula(n,A,B,D)==(1<<n)**2-f[0]
    print('n',n,'several_parameters_pass')

# Direct independent complex Gram spectrum for one generic case and one resonant case.
for A,B,D in [(1,2,2),(3,1,1),(0,0,1)]:
    n=4;N=1<<n
    g=np.array([complex(A,B)/D if x==0 else (1 if pop(x)==2 else 0) for x in range(N)])
    X=[]
    for a in range(N):
        for b in range(N):
            h=np.array([g[x^a]*(1 if pop(b&x)%2==0 else -1) for x in range(N)])
            X.append(np.outer(h,np.conjugate(h)).ravel())
    P=np.stack(X);Gram=P@P.conj().T
    actual=np.linalg.eigvalsh(Gram)
    wanted=[]
    for val,count in formula(n,A,B,D).items():wanted.extend([N*val/D**4]*count)
    assert np.allclose(actual,sorted(wanted),atol=1e-7,rtol=1e-9),(A,B,D)
    print('direct Gram matches n4',A,B,D)
print('APEX_WEIGHT_TWO_HAMMING_GABOR_EXACT_CHECKS_PASS')
