#!/usr/bin/env python3
"""Exact finite-field check of the leading valuation coefficient in an averaged binomial congruence."""
from math import factorial

def poly_product(p,K,t):
    coeff=[0]*(t+1); coeff[0]=1
    for u in range(1,K+1):
        if u%p == 0:continue
        q=pow(u,-1,p)
        for j in range(t,0,-1):coeff[j]=(coeff[j]+q*coeff[j-1])%p
    return coeff

def witness_data(p,t):
    j=t-p+1
    if 1<=j<=p-2:q=j
    elif j==p-1:q=0
    elif j==p:q=1
    else:raise ValueError
    K=p*(p-1)+q
    coeff=poly_product(p,K,t)[j]
    high=1
    for a in range(1,p):high=high*pow(a,-1,p)%p
    lead=high*coeff%p
    target=(pow(factorial(j),-1,p) if j<=p-2 else 1)
    return K,coeff,lead,target*high%p

if __name__=='__main__':
    cases=0
    for p in (5,7,11,13,17,19):
        for t in range(p,2*p):
            K,coeff,lead,expected=witness_data(p,t)
            assert lead==expected and lead!=0,(p,t,K,lead,expected)
            cases+=1
        print('p=',p,':',p,'witnesses checked')
    print('PASS',cases,'parameter pairs')

def direct_averaged_defect_v(p,t,r):
    """Compute G_c(-1) modulo p^(L+1), using all c terms (for manageable test r)."""
    L=2*t-p+1
    K,_,lead,_=witness_data(p,t)
    c=K*p**(r-2)
    assert c<p**r
    modulus=p**(L+1)
    arr=[0]*(t+1);arr[0]=1
    for i in range(1,c+1):
        temp=i;v=0
        while temp%p==0:
            temp//=p;v+=1
        a=(p**(r-v)*pow(temp,-1,modulus))%modulus
        if a==0:continue
        for z in range(t,0,-1):arr[z]=(arr[z]-a*arr[z-1])%modulus
    # G_c(-1) = (-1)^c * (sum of terms at degrees multiple of t)
    # Here modulo p^(L+1), degree >=2t necessarily vanishes.
    actual=arr[t]*((-1)**c)%modulus
    assert actual%p**L==0
    leading=(actual//p**L)%p
    # (-1)^c times (-1)^t times high-product leading; no other factors.
    expected=((-1)**(c+t)*lead)%p
    assert leading==expected,(p,t,r,leading,expected)
    return c,leading

if __name__=='__main__':
    for p,t,r in ((5,6,4),(5,6,5),(5,8,4),(5,9,4),(7,8,4),(7,12,4)):
        c,lc=direct_averaged_defect_v(p,t,r)
        print('direct p,t,r,c,leading:',p,t,r,c,lc)
