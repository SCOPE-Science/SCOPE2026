#!/usr/bin/env python3
"""Exact finite diagnostics for odd-part overpartition internal congruences."""
from math import isqrt

def odd_part_overpartition(N):
    a=[0]*(N+1); a[0]=1
    for d in range(1,N+1,2):
        # (1-q^d)^(-1) then (1+q^d); fresh arrays not required.
        for n in range(d,N+1):
            a[n]+=a[n-d]
        for n in range(N,d-1,-1):
            a[n]+=a[n-d]
    return a

def multiply(a,b,N,mod):
    out=[0]*(N+1)
    for j,c in enumerate(a):
        if not c: continue
        for k in range(N-j+1):
            out[j+k]=(out[j+k]+c*b[k])%mod
    return out

def polyadd(a,b):
    c=[0]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]+=v
    for i,v in enumerate(b):c[i]+=v
    while len(c)>1 and c[-1]==0:c.pop()
    return c

def polyn(a,t):return [t*v for v in a]

def polyp(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):c[i+j]+=v*w
    return c

def chebs(N):
    T=[[1],[0,1]]
    V=[[1],[0,2]]
    for j in range(2,N+1):
        T.append(polyadd(polyn(polyp([0,1],T[-1]),2),polyn(T[-2],-1)))
        V.append(polyadd(polyn(polyp([0,1],V[-1]),2),polyn(V[-2],-1)))
    return T[:N+1],V[:N+1]

def theta_poly(f,T):
    z=[0]
    for j,v in enumerate(f):
        z=polyadd(z,polyn(polyadd(T[2*j+2],polyn(T[2*j],-1)),v))
    # quotient by (x-1), coefficients use synthetic division
    out=[0]*(len(z)-1)
    v=0
    for i in range(len(z)-1,0,-1):
        v+=z[i];out[i-1]=v
    assert sum(z)==0
    while len(out)>1 and out[-1]==0:out.pop()
    return out

T,V=chebs(52)
for j in range(0,11):
    # theta((x+1)x^j) = 8*x^2*(x+1)*V_j(2x^2-1)
    w=[0]*j+[1,1]
    x2=[-1,0,2]
    p=[1]
    v=[0]
    for coeff in V[j]:
        v=polyadd(v,polyn(p,coeff));p=polyp(p,x2)
    rhs=polyn(polyp([0,0,1,1],v),8)
    assert theta_poly(w,T)==rhs,(j,theta_poly(w,T),rhs)
print('CHEBYSHEV_OPERATOR_IDENTITY_OK j=0..10')
for m in range(2,43,4):
    P1=T[m//2]
    # S(P1)
    P2=[0]
    for j,c in enumerate(P1):P2=polyadd(P2,polyn(T[2*j],c))
    diff=polyadd(P2,polyn(P1,-1))
    R2=[0]*(len(diff)-1)
    acc=0
    for j in range(len(diff)-1,0,-1): acc+=diff[j];R2[j-1]=acc
    assert sum(diff)==0
    assert all((R2[j]-(1 if j==0 else 2 if j==1 else 0))%4==0 for j in range(len(R2)))
print('TWICE_ODD_START_POLYNOMIAL_OK m=2..42 step4')
N=416
mod=1<<20
A=[x%mod for x in odd_part_overpartition(N)]
for m in [2,6,10,14]:
    P=[0]*(N+1);P[0]=1
    for _ in range(m):P=multiply(P,A,N,mod)
    for i in [3,4,5]:
        checked=0
        for n in range(0,min(13,N//(2**i))+1):
            diff=(P[n*(2**i)]-P[n*(2**(i-1))])% (1<<(3*i-3))
            odd_square=int(isqrt(n))**2==n and isqrt(n)%2==1
            expected=(1<<(3*i-4)) if odd_square else 0
            assert diff==expected,(m,i,n,diff,expected)
            checked+=1
        print('EULER_PRODUCT_CONGRUENCE_OK m=%d i=%d indices=%d'%(m,i,checked))
print('VERIFY_OK exact_finite_checks=True infinite_proof_in_RESULT=True independent_audit=False')
