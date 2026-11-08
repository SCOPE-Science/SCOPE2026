"""Exact, standalone checks for the common-fugacity K_{3,n} forest theorem.
Run: python3 verify.py. Requires only the Python standard library.
"""
from fractions import Fraction
from itertools import combinations

# Polynomial in b (fugacity) and h=n-1, stored as (b-degree,h-degree):integer.
def const(v): return {} if v == 0 else {(0, 0): int(v)}
def variable(k): return {(1, 0) if k == 'b' else (0, 1): 1}
def add(*terms):
    z = {}
    for term in terms:
        for power, coefficient in term.items():
            z[power] = z.get(power, 0) + coefficient
            if not z[power]: del z[power]
    return z
def neg(z): return {k:-v for k,v in z.items()}
def sub(a,b): return add(a,neg(b))
def mul(*terms):
    z=const(1)
    for term in terms:
        out={}
        for (i,j),v in z.items():
            for (k,l),w in term.items():
                ij=(i+k,j+l); out[ij]=out.get(ij,0)+v*w
        z={k:v for k,v in out.items() if v}
    return z
def power(a,k):
    result=const(1)
    for _ in range(k):result=mul(result,a)
    return result
def scale(z,s):return {k:v*s for k,v in z.items() if v*s}
b,h=variable('b'),variable('h')
one=const(1)
n=add(h,one)
A=add(one,scale(b,3)); B=add(scale(power(b,2),3),power(b,3))
b4=power(b,4)
Z=add(power(A,2),mul(n,B,A),scale(mul(n,h,b4),3))
E=add(mul(b,add(power(A,2),mul(h,B,A),scale(mul(h,sub(h,one),b4),3))),
      mul(add(scale(power(b,2),2),power(b,3)),power(A,2)),scale(mul(h,b4,A),4))
Q0=add(mul(power(b,2),add(power(A,2),mul(sub(h,one),B,A),
                                  scale(mul(sub(h,one),sub(h,const(2)),b4),3))),
       scale(mul(b,add(mul(add(scale(power(b,2),2),power(b,3)),power(A,2)),
                            scale(mul(sub(h,one),b4,A),4))),2))
QR=mul(power(A,2),add(mul(power(b,2),add(one,b),A),scale(mul(h,b4),2)))
QL=add(Q0,scale(mul(b4,power(A,2)),2))
QD=add(Q0,scale(mul(b4,power(A,2)),3))

def poly(coeffs):
    return {(i,j):c for i,hs in enumerate(coeffs) for j,c in enumerate(hs) if c}
PR=poly([[1],[12],[52,6],[98,46],[75,106,12],[18,66,48],[0,9,18,9]])
PL=poly([[1],[12],[54,5],[118,36],[135,90,5],[78,96,18],[18,36,18]])
PD=poly([[1],[12],[51,7],[100,44],[99,87,7],[48,66,18],[9,18,9]])
for Q,mult,P in [(QR,mul(b4,h),PR),(QL,scale(b4,2),PL),(QD,b4,PD)]:
    assert sub(sub(power(E,2),mul(Q,Z)),mul(mult,P)) == {}
    assert P and all(v>0 for v in P.values())
print('PASS: three bivariate polynomial identities and coefficient positivity.')

def formula(N,t):
    a=1+3*t; c=3*t*t+t**3
    z=a*a+N*c*a+3*N*(N-1)*t**4
    e=t*(a*a+(N-1)*c*a+3*(N-1)*(N-2)*t**4)+(2*t*t+t**3)*a*a+4*(N-1)*t**4*a
    q0=t*t*(a*a+(N-2)*c*a+3*(N-2)*(N-3)*t**4)+2*t*((2*t*t+t**3)*a*a+4*(N-2)*t**4*a)
    return z*a**(N-2),e/(a*z),t*t*(1+t)*a/z+2*(N-1)*t**4/z,(q0+2*t**4*a*a)/(a*a*z),(q0+3*t**4*a*a)/(a*a*z)

def brute(N,t):
    edges=[(i,3+j) for j in range(N) for i in range(3)]
    Z=Fraction(0); singles=Fraction(0); qr=Fraction(0);ql=Fraction(0);qd=Fraction(0)
    for mask in range(1<<len(edges)):
        parent=list(range(N+3))
        def root(x):
            while parent[x]!=x:x=parent[x]
            return x
        ok=True
        for k,(u,v) in enumerate(edges):
            if mask>>k&1:
                x,y=root(u),root(v)
                if x==y:ok=False;break
                parent[x]=y
        if not ok:continue
        w=t**mask.bit_count()
        Z+=w
        if mask&1: singles+=w
        if mask&3==3:qr+=w
        if mask&9==9:ql+=w
        if mask&17==17:qd+=w
    return Z,singles/Z,qr/Z,ql/Z,qd/Z
checks=0
for N in (2,3,4,5):
    for t in (Fraction(1,2),Fraction(1),Fraction(2)):
        assert formula(N,t)==brute(N,t),(N,t)
        checks+=5
print(f'PASS: {checks} independently enumerated exact rational weighted-forest identities.')
print('WARNING: finite enumeration is a check, not the proof for arbitrary sizes.')
