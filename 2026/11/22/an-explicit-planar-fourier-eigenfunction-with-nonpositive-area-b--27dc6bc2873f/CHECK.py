#!/usr/bin/env python3
"""Exact rational verification of an explicit planar Fourier-sign witness.

Uses Python standard library only. The Fourier-eigenvalue property follows
analytically from the classical Laguerre generating function, not a grid test.
"""
from fractions import Fraction as F
from math import comb, factorial, gcd, lcm

# Polynomials are lists of rational coefficients in increasing degree.
def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def add(a,b):
    out=[F(0) for _ in range(max(len(a),len(b)))]
    for i,x in enumerate(a):out[i]+=x
    for i,x in enumerate(b):out[i]+=x
    return trim(out)

def multiply_constant(a,c): return trim([v*c for v in a])
def derivative(a):return trim([F(i)*a[i] for i in range(1,len(a))] or [F(0)])

def prem(a,b):
    a=trim(a); b=trim(b)
    assert b!=[F(0)]
    while len(a)>=len(b) and a!=[F(0)]:
        k=len(a)-len(b); c=a[-1]/b[-1]
        for j,v in enumerate(b): a[j+k]-=c*v
        a=trim(a)
    return a

def primitive_preserving_sign(a):
    a=trim(a)
    if a==[F(0)]:return a
    den=1
    for v in a:den=lcm(den,v.denominator)
    ints=[int(v*den) for v in a]
    g=0
    for t in ints:g=gcd(g,abs(t))
    return [F(t//g) for t in ints]

def sturm(p):
    seq=[primitive_preserving_sign(p),primitive_preserving_sign(derivative(p))]
    while len(seq[-1])>1:
        r=primitive_preserving_sign(multiply_constant(prem(seq[-2],seq[-1]),-1))
        if r==[F(0)]:break
        seq.append(r)
    return seq

def evaluate(p,x):
    y=F(0)
    for t in p[::-1]:y=y*x+t
    return y

def sign(v):return 1 if v>0 else -1 if v<0 else 0

def signs_at(seq,x=None):
    return [sign(p[-1]) if x is None else sign(evaluate(p,x)) for p in seq]

def variation(ss):
    a=[v for v in ss if v]
    return sum(x!=y for x,y in zip(a,a[1:]))

def laguerre(n):
    return [F((-1)**k*comb(n,k),factorial(k)) for k in range(n+1)]

weights={2:22,4:20,6:-4,8:1}
P=[F(0)]
for j,w in weights.items():
    L=laguerre(j)
    L[0]-=1
    P=add(P,multiply_constant(L,w))
Q=[F(-4354560),F(2217600),F(-376320),F(50400),F(-10752),F(1344),F(-64),F(1)]
assert P==[F(0)]+[v/F(40320) for v in Q], 'exact Laguerre expansion mismatch'
assert P[0]==0 and P[1]<0 and P[-1]>0
S=sturm(Q)
assert len(S)==8 and all(len(S[i])==8-i for i in range(8))
points=[(F(0),'zero',4,'-++-+---'),(F(73,20),'lower',4,'-+--+---'),
        (F(183,50),'upper',3,'++--+---')]
for x,label,count,pattern in points:
    ss=signs_at(S,x)
    string=''.join('+' if v>0 else '-' if v<0 else '0' for v in ss)
    assert variation(ss)==count and string==pattern,(label,string)
ss=signs_at(S,None)
assert variation(ss)==3 and ''.join('+' if v>0 else '-' for v in ss)=='+++--++-'
assert evaluate(Q,F(73,20))<0
assert evaluate(Q,F(183,50))==F(85807489517127,781250000000)>0
# Sturm: exactly one zero on (0,183/50) and none above 183/50.
# Hence a single positive root, lying in (73/20,183/50).
print('CHECK_OK Laguerre_identity=exact Sturm_signs=4,4,3,3 positive_root_count=1 area_upper=183/100')
