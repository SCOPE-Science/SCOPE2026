#!/usr/bin/env python3
from math import isqrt

CASES = {
    5: {
        "C": 0, "D": 3,
        "root_interval": (3, 4),
        "field_disc": -135,
        "index": 55,
    },
    96: {
        "C": 1, "D": 13,
        "root_interval": (12, 13),
        "field_disc": -2104,
        "index": (2**7)*(3**3)*29,
    },
}

def cubic_eval(coeffs, x):
    # coeffs are [1,a,b,c]
    return ((coeffs[0]*x + coeffs[1])*x + coeffs[2])*x + coeffs[3]

def cubic_discriminant(a,b,c):
    # x^3+a x^2+b x+c
    return a*a*b*b - 4*b*b*b - 4*a*a*a*c - 27*c*c + 18*a*b*c

def square_transform(C,D):
    # If r has x^3-D x^2+C x-1, then r^2 has
    # x^3-B x^2+A x-1 with A=C^2-2D, B=D^2-2C.
    A = C*C - 2*D
    B = D*D - 2*C
    return A,B

def vp(n,p):
    n=abs(n); v=0
    while n and n%p==0:
        n//=p; v+=1
    return v

def index_formula(b):
    # Specialized implementation of the paper's Theorems 3.3 and 3.5,
    # sufficient for the two verified b values.
    a=1
    # p=2
    w=vp(b,2)
    if w:
        bp=b//(2**w)
        if w%2:
            e=(3*w-1)//2
        else:
            e=3*w//2 + (1 if bp%4==3 else 0)
        a*=2**e
    # p=3
    w=vp(b,3)
    if w:
        a*=3**((3*(w+1))//2)
    # odd p>=5 dividing b or b^3-4; trial division is tiny here
    n1=abs(b); n2=abs(b**3-4)
    limit=isqrt(max(n1,n2))+1
    ps=[]
    for p in range(5,limit+1):
        if any(p%q==0 for q in range(2,isqrt(p)+1)):
            continue
        if n1%p==0 or n2%p==0:
            ps.append(p)
    # residual primes > sqrt(original) are irrelevant unless valuation >=2;
    # all relevant p for these two cases are already in ps, except 263 with v=1.
    for p in ps:
        wb=vp(b,p)
        if wb:
            a*=p**((3*wb)//2)
        else:
            v=vp(b**3-4,p)
            a*=p**(v//2)
    return a

for b,d in CASES.items():
    C,D=d["C"],d["D"]
    g=[1,-D,C,-1]
    lo,hi=d["root_interval"]
    assert cubic_eval(g,lo)<0<cubic_eval(g,hi), (b,"root bracket")
    # no rational root for a monic cubic with constant -1
    assert cubic_eval(g,1)!=0 and cubic_eval(g,-1)!=0, (b,"irreducible")

    A,B=square_transform(C,D)
    Q,P=square_transform(A,B)
    assert P == 3*(b*b+b+1), (b,P)
    assert Q == 3*(b+1), (b,Q)

    disc_f=-27*(b**3)*(b**3-4)
    a=index_formula(b)
    assert a == d["index"], (b,a,d["index"])
    assert disc_f == d["field_disc"]*a*a, (b,disc_f,a,d["field_disc"])

    # Fundamental-unit contradiction using Artin's bound.
    # If gamma=u^q with q>=2, |D_K| <= 4*gamma^(3/2)+24.
    # Use gamma<hi and integer upper bounds for sqrt(hi).
    sqrt_hi_upper=isqrt(hi)+1
    rhs_upper=4*hi*sqrt_hi_upper+24
    assert abs(d["field_disc"]) > rhs_upper, (b,abs(d["field_disc"]),rhs_upper)

    disc_g=cubic_discriminant(-D,C,-1)
    assert disc_g<0

print("VERIFY_OK cases=2 exact_fourth_powers=2 fundamental_units=2")
