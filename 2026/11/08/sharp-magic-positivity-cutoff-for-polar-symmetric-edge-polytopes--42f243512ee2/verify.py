#!/usr/bin/env python3
"""Exact checks for the K(3,q) polar graph-polytope Ehrhart count and magic signs."""
from fractions import Fraction as F
from math import comb

def poly_add(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    return c

def poly_mul_linear(a,c0,c1):
    out=[F(0)]*(len(a)+1)
    for i,x in enumerate(a):out[i]+=x*c0;out[i+1]+=x*c1
    return out

def ehrhart_value(q,t):
    return (2*t+1)**q+6*sum(r*(2*t+1-r)**q for r in range(1,2*t+1))

def ehrhart_polynomial(q):
    d=q+2
    vals=[F(ehrhart_value(q,t)) for t in range(d+1)]
    differences=[]
    while vals:
        differences.append(vals[0]);vals=[vals[j+1]-vals[j] for j in range(len(vals)-1)]
    coeff=[F(0)]
    basis=[F(1)]
    for k,delta in enumerate(differences):
        coeff=poly_add(coeff,[delta*v for v in basis])
        basis=[a/F(k+1) for a in poly_mul_linear(basis,F(-k),F(1))]
    return coeff+[F(0)]*(d+1-len(coeff))

def magic_coefficients(q):
    d=q+2
    mon=ehrhart_polynomial(q)
    return [sum(((-1)**(i-k))*F(comb(d-k,i-k))*mon[k] for k in range(i+1)) for i in range(d+1)]

def bernoulli(u):
    B=[F(1)]
    for m in range(1,u+1):B.append(-sum(F(comb(m+1,k))*B[k] for k in range(m))/F(m+1))
    return B

def direct_count(q,t):
    s=0
    for x in range(-2*t,2*t+1):
        for y in range(-2*t,2*t+1):
            r=max(0,x,y)-min(0,x,y)
            if r<=2*t:s+=(2*t+1-r)**q
    return s

def main():
    checks=0
    for q in range(1,17):
        co=magic_coefficients(q)
        d=q+2
        assert all(co[i]==co[d-i] for i in range(d+1));checks+=d+1
        assert co[0]==co[-1]==1;checks+=2
        for t in range(0,4):
            lhs=ehrhart_value(q,t)
            rhs=sum(co[i]*t**i*(t+1)**(d-i) for i in range(d+1))
            assert lhs==rhs;checks+=1
            assert lhs==direct_count(q,t);checks+=1
        if q<=6:assert all(c>0 for c in co)
        elif q<=16:assert min(co)<0
        checks+=1
    B=bernoulli(44)
    for q in range(3,41):
        a1=F(q-2)+12*(B[q]-B[q+1])
        a2=F(q*q-5*q+2,2)+12*q*B[q-1]-24*q*B[q]+12*(q+1)*B[q+1]
        # independent expression for q>=3 via Bernoulli vs polynomial coefficients
        if q<=16:
            co=magic_coefficients(q)
            assert a1==co[1] and a2==co[2]
            checks+=2
    negative_witness={7:3,8:3,9:4,10:4,11:5,12:3}
    for q,i in negative_witness.items():
        c=magic_coefficients(q)[i]
        assert c<0;checks+=1
    # Exact baseline |B_{2m}| >= (2m)/12 for every even 14<=2m<=44
    for r in range(14,45,2):
        assert abs(B[r])>=F(r,12);checks+=1
    print('EXACT_CHECKS_OK',checks)
    for q in range(1,13):
        co=magic_coefficients(q)
        print('q=',q,'magic=',','.join(str(x) for x in co))

if __name__=='__main__':main()
