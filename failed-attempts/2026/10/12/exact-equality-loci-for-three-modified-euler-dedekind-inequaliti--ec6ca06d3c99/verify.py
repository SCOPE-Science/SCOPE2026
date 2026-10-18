#!/usr/bin/env python3
from math import prod

LIMIT = 50000

def factor(n):
    out=[]
    d=2
    while d*d<=n:
        if n%d==0:
            a=0
            while n%d==0:
                n//=d; a+=1
            out.append((d,a))
        d += 1 if d==2 else 2
    if n>1:
        out.append((n,1))
    return out

def vals(n):
    fs=factor(n)
    Phi=prod(p**a-1 for p,a in fs)
    Psi=prod(p**a+1 for p,a in fs)
    phi=prod(p**(a-1)*(p-1) for p,a in fs)
    psi=prod(p**(a-1)*(p+1) for p,a in fs)
    squarefree=all(a==1 for _,a in fs)
    prime_power=(len(fs)==1)
    return Phi,Psi,phi,psi,squarefree,prime_power

checks=0
for n in range(2,LIMIT+1):
    Phi,Psi,phi,psi,squarefree,prime_power=vals(n)
    e1=(psi-Psi+phi-Phi==0)
    e2=(Phi+Psi==2*n)
    e3=(Phi*Psi==phi*psi)
    assert e1 == (squarefree or prime_power), (n,'E1')
    assert e2 == prime_power, (n,'E2')
    assert e3 == squarefree, (n,'E3')
    checks += 3
print(f"VERIFY_OK n_max={LIMIT} equality_checks={checks}")
