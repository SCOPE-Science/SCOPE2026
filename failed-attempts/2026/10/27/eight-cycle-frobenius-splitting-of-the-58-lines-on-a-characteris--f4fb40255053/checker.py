#!/usr/bin/env python3
"""Exact symbolic and small-field checks for the 58-line quartic over F_3.

Run with Python 3; only the standard library is needed. The universal
Frobenius-orbit conclusion follows from the algebraic argument in RESULT.md.
"""
from itertools import product, combinations

# Polynomial ring F3[T,S,a,b,c,d], sparse standard monomial representation.
VARS = ("T", "S", "a", "b", "c", "d")
ZERO = (0,) * len(VARS)

def c(n):
    n %= 3
    return {ZERO: n} if n else {}

def var(i):
    e = list(ZERO)
    e[i] = 1
    return {tuple(e): 1}

def add(*items):
    out = {}
    for item in items:
        for e, x in item.items():
            z = (out.get(e, 0) + x) % 3
            if z: out[e] = z
            else: out.pop(e, None)
    return out

def neg(f):
    return {e: (-x) % 3 for e, x in f.items()}

def mul(f, g):
    out = {}
    for u, a in f.items():
        for v, b in g.items():
            w = tuple(x+y for x, y in zip(u, v))
            z = (out.get(w, 0) + a*b) % 3
            if z: out[w] = z
            else: out.pop(w, None)
    return out

def power(f, n):
    out = c(1)
    for _ in range(n):out = mul(out, f)
    return out

T, S, a, b, cc, d = (var(i) for i in range(6))

def quartic(x):
    x0,x1,x2,x3=x
    return add(mul(power(x1,3),x2), neg(mul(x1,power(x2,3))),
               mul(power(x0,3),x3), neg(mul(x0,power(x3,3))),
               neg(mul(mul(power(x0,2),x1),x2)))

def chart_coefficients(variables):
    f=quartic(variables)
    coeffs=[]
    for k in range(5):
        ck={e[2:]: n for e,n in f.items() if e[:2] == (4-k,k)}
        coeffs.append(ck)
    return coeffs

def param(f):
    return {e[2:]: n for e,n in f.items() if e[:2] == (0,0)}

forms={
    "01": [T,S,add(mul(a,T),mul(cc,S)),add(mul(b,T),mul(d,S))],
    "02": [T,mul(a,T),S,add(mul(b,T),mul(cc,S))],
    "03": [T,mul(a,T),mul(b,T),S],
    "12": [{},T,S,add(mul(a,T),mul(b,S))],
    "13": [{},T,mul(a,T),S],
    "23": [{},{},T,S],
}
expected={
    "01": [add(b,neg(power(b,3))),add(d,neg(power(a,3)),neg(a)),neg(cc),add(a,neg(power(d,3))),add(cc,neg(power(cc,3)))],
    "02": [add(b,neg(power(b,3))),add(power(a,3),neg(a),cc),{},add(neg(a),neg(power(cc,3))),{}],
    "03": [add(mul(power(a,3),b),neg(mul(a,power(b,3))),neg(mul(a,b))),c(1),{},neg(c(1)),{}],
    "12": [{},c(1),{},neg(c(1)),{}],
    "13": [add(a,neg(power(a,3))),{},{},{},{}],
    "23": [{},{},{},{},{}],
}
for key in forms:
    actual=chart_coefficients(forms[key]); wanted=[param(f) for f in expected[key]]
    assert actual==wanted, (key,actual,wanted)
print("PASS: all 30 homogeneous coefficient equations from six Grassmann charts")

# Univariate polynomial Euclidean arithmetic over F3, coefficient order low to high.
def trim(f):
    f=f[:]
    while f and f[-1]%3==0:f.pop()
    return [x%3 for x in f]

def pmul(a,b):
    v=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):v[i+j]=(v[i+j]+x*y)%3
    return trim(v)

def prem(a,b):
    a=trim(a);b=trim(b)
    if not b:raise ZeroDivisionError
    while len(a)>=len(b):
        q=a[-1]*pow(b[-1],-1,3)%3
        shift=len(a)-len(b)
        for i,z in enumerate(b):a[i+shift]=(a[i+shift]-q*z)%3
        a=trim(a)
    return a

def pgcd(a,b):
    while b:a,b=b,prem(a,b)
    return a

def ppowmod(a,n,m):
    res=[1]
    while n:
        if n&1:res=prem(pmul(res,a),m)
        a=prem(pmul(a,a),m);n//=2
    return res

for sg in (-1,+1):
    P=[0,2,0,sg%3,0,0,0,0,0,1]  # t^9 + sg*t^3 - t
    assert len(P)==10
    assert len(pgcd(P,[2,1]))==1
    x=[0,1]
    for n in range(1,9):
        x=ppowmod(x,3,P)
        diff=x[:]
        if len(diff)<2:diff.extend([0]*(2-len(diff)))
        diff[1]=(diff[1]-1)%3
        diff=trim(diff)
        degree=len(pgcd(P,diff))-1
        assert degree==(9 if n==8 else 1), (sg,n,degree)
    print(f"PASS: additive polynomial sign {sg:+d}, one root over F_3^n for 1<=n<8, all nine over F_3^8")

# Unrelated direct projective-line enumeration over F3, with equality of polynomials.
def test_points(q=3):
    count=0
    for i,j in combinations(range(4),2):
        free=[(row,col) for row,p in ((0,i),(1,j)) for col in range(p+1,4) if col not in (i,j)]
        for values in product(range(q),repeat=len(free)):
            u=[0]*4;v=[0]*4;u[i]=v[j]=1
            for (row,col),value in zip(free,values):
                (u if row==0 else v)[col]=value
            def f(t,s):
                x=[(u[k]*t+v[k]*s)%3 for k in range(4)]
                z=(x[1]**3*x[2]-x[1]*x[2]**3+x[0]**3*x[3]-x[0]*x[3]**3-x[0]**2*x[1]*x[2])%3
                return z
            # For a homogeneous quartic over F3, evaluation at all F3 points
            # alone is not conclusive, so reconstruct all five coefficients from the
            # universal sparse polynomial and substitute all four line parameters.
            params=(u[2],u[3],v[2],v[3]) if (i,j)==(0,1) else None
            xforms=[add(mul(c(u[k]),T),mul(c(v[k]),S)) for k in range(4)]
            if not quartic(xforms):count+=1
    assert count==10,count
    print("PASS: independent enumeration of all 130 F3-lines gives exactly 10")
test_points()
print("ALL CHECKS PASSED")
