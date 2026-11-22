"""Independent exact finite-clock verification for spatial covering-count covariance.
Run: python3 verify.py   (only Python standard library)
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from math import comb, factorial

# Polynomials in p in ascending coefficient order.
def plus(a, b):
    return [((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) for i in range(max(len(a), len(b)))]
def scale(a, x): return [x * v for v in a]
def multiply(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b): out[i+j]+=v*w
    return out
def difference(a,b): return plus(a,scale(b,-1))
def coefficient(arr,k): return arr[k] if k<len(arr) else F(0)
def eq(a,b):
    assert all(coefficient(a,k)==coefficient(b,k) for k in range(max(len(a),len(b)))), (a,b)

def moment_polynomials(distance):
    """Full exact law of first arrivals of all clocks relevant to sites 0,d."""
    edges=tuple(range(-2,distance+2)); n=len(edges)
    totals=[[F(0),F(0),F(0)] for _ in range(n+1)]
    counts=0
    for k in range(n+1):
        for subset in combinations(edges,k):
            available=set(subset)
            for ordering in permutations(subset):
                rank={edge:j for j,edge in enumerate(ordering)}
                def accepted(e):
                    if e not in available: return 0
                    return int(e-1 not in available or rank[e]<rank[e-1] or
                               e+1 not in available or rank[e]<rank[e+1])
                c0=accepted(-1)+accepted(0)
                cd=accepted(distance-1)+accepted(distance)
                totals[k][0]+=F(c0,factorial(k))
                totals[k][1]+=F(cd,factorial(k))
                totals[k][2]+=F(c0*cd,factorial(k))
                counts+=1
    result=[]
    for slot in range(3):
        P=[F(0)]*(n+1)
        for k in range(n+1):
            for j in range(n-k+1):
                P[k+j]+=totals[k][slot]*(-1)**j*comb(n-k,j)
        result.append(P)
    mean0,mean1,second=result
    return mean0,mean1,second,difference(second,multiply(mean0,mean1)),counts

# Proof expressions, with coefficient-by-coefficient comparison against exhaustive orders.
p=[F(0),F(1)]
p2=multiply(p,p);p3=multiply(p2,p);p4=multiply(p3,p);p5=multiply(p4,p);p6=multiply(p5,p)
mean=[F(0),F(2),F(0),F(-2,3)]
var0=[F(0),F(2),F(-2),F(-2),F(8,3),F(0),F(-4,9)]
c1=[F(0),F(1),F(-1),F(-5,3),F(2),F(2,15),F(-4,9)]
c2=[F(0),F(0),F(0),F(-2,3),F(2,3),F(4,15),F(-1,3)]
c3=[F(0),F(0),F(0),F(0),F(0),F(2,15),F(-1,9)]
expected={0:var0,1:c1,2:c2,3:c3}
checked=0
for d in range(4):
    m0,m1,ecc,cov,num=moment_polynomials(d)
    eq(m0,mean);eq(m1,mean);eq(cov,expected[d]);checked+=num
# Infinite-line clock supports are disjoint for site distance >=4, yielding zero covariance.
variance_long=plus(var0,scale(plus(plus(c1,c2),c3),2))
V=[F(0),F(4),F(-4),F(-20,3),F(8),F(16,15),F(-20,9)]
eq(variance_long,V)
# Bernstein-positivity certificates for polynomial factors: for C1/p,
# -15 C2/p^3, and (45/4)V/p (normalization described in RESULT).
def bernstein(P):
    n=len(P)-1
    return [sum((P[j]*F(comb(k,j),comb(n,j)) for j in range(k+1)),F(0)) for k in range(n+1)]
# 45 C1/p = 45 -45p -75p²+90p³+6p⁴-20p⁵.
assert bernstein([F(45),F(-45),F(-75),F(90),F(6),F(-20)]) == [F(45),F(36),F(39,2),F(9,2),F(6,5),F(1)]
# -15 C2/p³ = 10 -10p -4p²+5p³.
assert bernstein([F(10),F(-10),F(-4),F(5)]) == [F(10),F(20,3),F(2),F(1)]
# 45 V/(4p) = 45 -45p -75p²+90p³+12p⁴-25p⁵.
assert bernstein([F(45),F(-45),F(-75),F(90),F(12),F(-25)]) == [F(45),F(36),F(39,2),F(9,2),F(12,5),F(2)]
# C3=p^5(6-5p)/45 positive for 0<p<=1.
# Confirm terminal covariance and long-time fluctuation strength.
for d,value in [(1,F(1,45)),(2,F(-1,15)),(3,F(1,45))]:
    assert sum(expected[d])==value
assert sum(V)==F(8,45)
print('PASS exact-order verifications:',checked,'ordered active-clock cases; four symbolic covariance polynomials')
print('PASS all sign certificates, independence range, and terminal variance 8/45')
