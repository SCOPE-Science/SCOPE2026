#!/usr/bin/env python3
"""High-precision checks of two-term asymptotics for Veronese Fourier norms."""
from decimal import Decimal as D, getcontext
from math import prod
from check_veronese import rank_count
getcontext().prec=75

def high_precision_norm(q,n):
    qd=D(q);root=qd.sqrt();num=D(0)
    for r in range(n+1):
        ct=D(rank_count(q,n,r))
        if r%2==0:
            s=r//2
            mag=(qd**(n-s)+qd**(-s))
        elif q%4==1:
            mag=qd**(n-r//2)/root
        else:
            mag=(D(1)+qd**(2*n-r)).sqrt()
        num+=ct*mag
    return num/(2*qd**(n*(n+1)//2))

def constants(q,cutoff=65):
    Q=D(1)/D(q);sq=Q.sqrt()
    a=prod(1-Q**(2*j-1) for j in range(1,cutoff+1))
    C=a*prod(1+Q**j/sq for j in range(1,cutoff+1))
    P=[D(1)]
    for d in range(1,cutoff+1):P.append(P[-1]*(1-Q**d))
    w=[a*Q**(d*(d+1)//2)/P[d] for d in range(cutoff+1)]
    B=[]
    for epsilon in range(2):
        T=D(0);Ev=D(0);Ov=D(0)
        for d in range(cutoff+1):
            wd=w[d]
            root_d=Q**(d//2)*(sq if d%2 else D(1))
            A=Q**((epsilon-d)%2)/(1-Q**2)
            T+=wd/root_d*Q**(1-d)*(A-(1-Q**d)/(1-Q))
            if (epsilon-d)%2==0: Ev+=wd/root_d/D(2)
            elif q%4==3: Ov+=wd*root_d/D(4)
        B.append(T/D(2)+Ev+Ov)
    return C,B

for q in (3,5,7):
    C,B=constants(q)
    print('q',q,'C',str(C)[:27], 'B0',str(B[0])[:27], 'B1',str(B[1])[:27])
    for n in range(4,17):
        norm=high_precision_norm(q,n)
        scale=D(q)**(n//2)*(D(q).sqrt() if n%2 else 1)
        res=(norm-C*scale/D(2))*scale
        error=abs(res-B[n%2]);
        assert error < D(6)*D(q)**(-n), (q,n,error,res,B[n%2])
    print('TWO_TERM_ASYMPTOTIC_CHECK_PASS')
