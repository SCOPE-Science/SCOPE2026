"""Reproducible arithmetic and symbolic checks for a ridge-angle theorem.

Dependencies: Python 3, SymPy. No external data or downloads.
"""
import math
from math import factorial
import sympy as sp
from sympy.functions.combinatorial.numbers import stirling

# Independent Euclidean vector check against the analytic cosine.
for n in range(3, 10):
    total = 0
    sum_angles = 0.0
    sum_sq = 0.0
    for a in range(1, n-1):
        for b in range(1, n-a):
            c = n-a-b
            A = set(range(a))
            AB = set(range(a+b))
            v = [(int(i in A)-a/n) for i in range(n)]
            w = [(int(i in AB)-(a+b)/n) for i in range(n)]
            cos_by_vectors = sum(p*q for p,q in zip(v,w)) / (
                math.sqrt(sum(p*p for p in v)*sum(q*q for q in w)))
            cos_by_formula = math.sqrt(a*c/((a+b)*(b+c)))
            assert abs(cos_by_vectors - cos_by_formula) < 3e-14
            angle = math.pi-math.acos(cos_by_vectors)
            m = factorial(n)//(factorial(a)*factorial(b)*factorial(c))
            total += m
            sum_angles += m*angle
            sum_sq += m*(angle-2*math.pi/3)**2
            cyclic = sum(math.pi-math.acos(math.sqrt(
                i*k/((i+j)*(j+k)))) for i,j,k in
                [(a,b,c),(b,c,a),(c,a,b)])
            assert abs(cyclic-2*math.pi) < 3e-14
    assert total == 3**n - 3*2**n + 3
    assert abs(sum_angles/total - 2*math.pi/3) < 3e-13
    if n == 3:
        assert abs(sum_sq/total) < 1e-25
    else:
        assert sum_sq > 0

# Derive the Taylor polynomial directly from the geometric angle.
s,t,N=sp.symbols('s t N',real=True)
p=sp.Rational(1,3)+s
q=sp.Rational(1,3)+t
r=1-p-q
f=sp.pi-sp.acos(sp.sqrt(p*r/((p+q)*(q+r))))
def homogeneous(k):
    return sp.expand(sum(sp.diff(f,s,i,t,k-i).subs({s:0,t:0})*
                         s**i*t**(k-i)/(sp.factorial(i)*sp.factorial(k-i))
                         for i in range(k+1)))
L,Q,C=(homogeneous(k) for k in (1,2,3))
assert sp.simplify(L+3*sp.sqrt(3)*t/4)==0
assert sp.simplify(Q+9*sp.sqrt(3)*s*s/8+
                   9*sp.sqrt(3)*s*t/8-9*sp.sqrt(3)*t*t/16)==0
assert sp.simplify(C+27*sp.sqrt(3)*(s*s*t+s*t*t+t**3)/16)==0

# Exact mixed centered-multinomial expectations via factorial moments.
def moment(i,j):
    X,Y=sp.symbols('X Y')
    poly=sp.Poly(sp.expand((X/N-sp.Rational(1,3))**i*
                           (Y/N-sp.Rational(1,3))**j),X,Y)
    ans=0
    for (a,b),coefficient in poly.terms():
        raw=sum(stirling(a,k,kind=2)*stirling(b,l,kind=2)*
                sp.ff(N,k+l)/3**(k+l)
                for k in range(a+1) for l in range(b+1))
        ans+=coefficient*raw
    return sp.factor(ans)
def expect(expr):
    return sp.factor(sum(coefficient*moment(i,j)
                         for (i,j),coefficient in sp.Poly(expr,s,t).terms()))
assert sp.simplify(expect(L*L)-3/(8*N))==0
assert sp.simplify(expect(2*L*Q)+9/(16*N**2))==0
assert sp.simplify(expect(Q*Q+2*L*C)-99*(2*N-1)/(128*N**3))==0
assert sp.simplify(expect(Q))==0
print('PASS: all exact normal, face-count, mean, Taylor and moment checks')
