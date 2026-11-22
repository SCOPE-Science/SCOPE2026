#!/usr/bin/env python3
"""Exact standard-library checks of the finite-field rank and zeta formulas."""

def product(a,b,N):
    c=[0]*(N+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=N:c[i+j]+=x*y
    return c

def inv(a,N):
    assert a[0]==1
    b=[1]+[0]*N
    for n in range(1,N+1):b[n]=-sum(a[j]*b[n-j] for j in range(1,n+1))
    return b

def zeta_coefficients(q,N):
    def line(k,sign=1):return [1,sign*k]+[0]*(N-1)
    def powpoly(poly,n):
        out=[1]+[0]*N
        for _ in range(n):out=product(out,poly,N)
        return out
    num=product(powpoly(line(q*q,-1),2),powpoly(line(q*q,1),2),N)
    den=product(powpoly(line(q**3,-1),2),product(line(q**4,-1),product(line(q**4,1),line(q,1),N),N),N)
    z=product(num,inv(den,N),N)
    deriv=[(n+1)*z[n+1] for n in range(N)]+[0]
    logderiv=product(deriv,inv(z,N),N)
    return [logderiv[n-1] for n in range(1,N+1)]

for q in (2,3,4,5,7,9):
    for s,value in enumerate(zeta_coefficients(q,6),1):
        Q=q**s
        want=(2*Q**3-Q) if s%2 else Q*(2*Q**3+2*Q**2-4*Q+1)
        assert value==want,(q,s,value,want)
    irreduc=[1,q*q+q-2,q*q-1,2*(q-1)*(q*q-1)]
    assert sum(irreduc)==2*q**3-q
    split=[1,(q-1)*(5*q+2),(q-1)*(4*q*q+q-5),2*(q-1)*(q**3-3*q+2)]
    assert sum(split)==q*(2*q**3+2*q*q-4*q+1)
    print('EXACT_FORMULAS_PASS q=',q)
print('QUADRATIC_PRELIE_ZETA_VERIFIED')
