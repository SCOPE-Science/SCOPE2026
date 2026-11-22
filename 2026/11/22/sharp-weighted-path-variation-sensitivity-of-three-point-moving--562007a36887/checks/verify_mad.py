#!/usr/bin/env python3
"""Finite checks for exact weighted BV modulus of three-point moving MAD.
All tests are secondary; the all-length argument is in RESULT.md.
"""
import math, random
from fractions import Fraction

def median3(a,b,c):
    return sorted((a,b,c))[1]

def mad3(a,b,c):
    m=median3(a,b,c)
    return median3(abs(a-m),abs(b-m),abs(c-m))

def T(x):
    return [mad3(*x[i:i+3]) for i in range(len(x)-2)]

def variation(x,w):
    return sum(w[i]*abs(x[i+1]-x[i]) for i in range(len(x)-1))

def K(w,v):
    n=len(w)+1
    if n==3: return Fraction(0)
    m=n-2
    z=[Fraction(0),*v,Fraction(0)]
    vals=[v[0]/w[0],v[-1]/w[-1]]
    for j in range(2,n-1):
        # j is the input-difference position, 1-based. Two affected windows.
        vals.append((z[j-2]+2*z[j-1]+z[j])/w[j-1])
    return max(vals)

def Kcols(w,v):
    n=len(w)+1
    if n==3: return [Fraction(0),Fraction(0)]
    z=[Fraction(0),*v,Fraction(0)]
    out=[v[0]/w[0]]
    for j in range(2,n-1):out.append((z[j-2]+2*z[j-1]+z[j])/w[j-1])
    out.append(v[-1]/w[-1]);return out

def primitive(d):
    x=[Fraction(0)]
    for z in d: x.append(x[-1]+z)
    return x

def witness(n,j,eps=Fraction(1,100000)):
    """strict differentiable witness for input-difference j (1-based)."""
    d=[Fraction(5) for _ in range(n-1)]
    if j==1:
        d[0]=Fraction(1);d[1]=Fraction(3)
    elif j==n-1:
        d[-2]=Fraction(3);d[-1]=Fraction(1)
    else:
        d[j-2]=Fraction(-3,2)
        d[j-1]=Fraction(1)
        d[j]=Fraction(-3)
    x=primitive(d)
    dd=d[:];dd[j-1]+=eps
    y=primitive(dd)
    return x,y

r=random.Random(30261)
for n in range(3,27):
    for it in range(90):
        x=[r.randrange(-20,21) for _ in range(n)]
        for i in range(n-2):
            a,b,c=x[i:i+3]
            direct=min(abs(a-b),abs(b-c),abs(a-c))
            assert mad3(a,b,c)==direct
        w=[Fraction(r.randrange(1,10)) for _ in range(n-1)]
        v=[Fraction(r.randrange(1,10)) for _ in range(n-3)]
        bound=K(w,v)
        cols=Kcols(w,v)
        for j in range(1,n):
            a,b=witness(n,j)
            ratio=variation([u-v for u,v in zip(T(a),T(b))],v)/variation([u-v for u,v in zip(a,b)],w)
            assert abs(ratio-cols[j-1])<1e-12,(n,j,ratio,cols[j-1])
        y=[r.randrange(-20,21) for _ in range(n)]
        num=variation([u-v for u,v in zip(T(x),T(y))],v)
        den=variation([u-v for u,v in zip(x,y)],w)
        assert den==0 or num<=bound*den,(n,num,den,bound)
print('EXACT_THREE_SAMPLE_MAD_MIN_DISTANCE_IDENTITY_PASS n=3..26')
print('ARBITRARY_POSITIVE_RATIONAL_WEIGHT_COLUMN_WITNESSES_PASS 2160 configs')
print('ARBITRARY_RATIONAL_TWO_INPUT_WEIGHTED_VARIATION_UPPER_PASS 2160 pairs')
for n in range(3,20):
    w=[Fraction(1)]*(n-1);v=[Fraction(1)]*(n-3)
    t=K(w,v)
    assert t==(0 if n==3 else 2 if n==4 else 3 if n==5 else 4)
print('UNWEIGHTED_SHARP_DIMENSION_TRANSITIONS_PASS n=3..19')
print('ALL_MOVING_MAD_WEIGHTED_BV_CHECKS_PASS')
