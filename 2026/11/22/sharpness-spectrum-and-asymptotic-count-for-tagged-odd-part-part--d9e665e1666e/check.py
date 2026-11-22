#!/usr/bin/env python3
"""Finite exact checks of tagged-part sharpness and the CM mod-3 support rule."""
from math import isqrt

N = 3600
MOD = 3**12
# Lin's generating function is q times the following eta-quotient product.
exponent = lambda r: -2 + (r % 2 == 0) + 2*(r % 3 == 0) - (r % 6 == 0) + 2*(r % 12 == 0)
coeff = [0]*(N+1)
coeff[0] = 1
for r in range(1,N+1):
    z = exponent(r)
    while z<0:
        for j in range(r,N+1): coeff[j]=(coeff[j]+coeff[j-r])%MOD
        z+=1
    while z>0:
        for j in range(N,r-1,-1): coeff[j]=(coeff[j]-coeff[j-r])%MOD
        z-=1

def v3_mod(x):
    if x % MOD == 0: return 12
    k=0
    while x % 3 == 0: x//=3; k+=1
    return k

def expected(n):
    if n%2==0 or n%3==0:return False
    x=n; p=5
    while p*p<=x:
        if x%p==0:
            e=0
            while x%p==0: x//=p; e+=1
            if p%3==2 and e%2:return False
            if p%3==1 and e%3==2:return False
        p+=2
    if x>1:
        if x%3==1: return True # remaining prime exponent 1
        return False # remaining inert prime exponent 1
    return True

K=N//12
b=[0]*(K+1)
b[0]=1
# f(q)=q * prod_(r>=1)(1-q^(6r))^4
for r in range(6,K+1,6):
    for _ in range(4):
        for j in range(K,r-1,-1):b[j]=(b[j]-b[j-r])%3

checks=0
for n in range(1,K+1):
    s=expected(n)
    assert (b[n-1]%3!=0)==s,("newform_support",n,b[n-1],s)
    for m in range(3):
        index=12*3**m*n
        if index>N:break
        t=coeff[index-1]
        assert t%3**(m+2)==0,("divisibility",m,n,t)
        scaled=(t//3**(m+2))%3
        assert scaled==((-1)**m*b[n-1])%3,("leading_coefficient",m,n,scaled,b[n-1])
        assert (v3_mod(t)==m+2)==s,("exact_valuation",m,n,v3_mod(t),s)
        checks+=1
print(f"TAGGED_3ADIC_SHARPNESS_OK: {checks} exact coefficient checks, {K} CM support checks, up to {N} input degree")
