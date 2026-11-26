"""Exact arithmetic checks for the genus-four curve Y^2=X^10-1 over F_11.
No external libraries. F_121 is represented as F_11[i] with i^2=-1.
"""
from itertools import product
P = 11
K = [(a,b) for a in range(P) for b in range(P)]
Z = (0,0)
ONE = (1,0)

def add(x,y): return ((x[0]+y[0]) % P, (x[1]+y[1]) % P)
def neg(x): return ((-x[0]) % P, (-x[1]) % P)
def sub(x,y): return add(x,neg(y))
def mul(x,y): return ((x[0]*y[0]-x[1]*y[1]) % P,
                      (x[0]*y[1]+x[1]*y[0]) % P)
def power(x,n):
    y=ONE
    while n:
        if n&1: y=mul(y,x)
        x=mul(x,x); n//=2
    return y

def count(exponent,twist=1,quadratic=False):
    field=K if quadratic else [(a,0) for a in range(P)]
    squares={mul(x,x) for x in field}
    num_infinity=2 if exponent%2==0 else 1
    answer=num_infinity
    for x in field:
        v=mul((twist%P,0), sub(power(x,exponent),ONE))
        answer += 1 if v==Z else (2 if v in squares else 0)
    return answer

assert count(5,1,False)==16
assert count(5,1,True)==118
assert count(5,-1,False)==8
assert count(5,-1,True)==118
assert count(10,1,False)==12
assert count(10,1,True)==114
s1=12-count(5,1,False)
s2=122-count(5,1,True)
a2=(s1*s1-s2)//2
assert (s1,s2,a2)==(-4,4,6)
A=[1,-s1,a2,-11*s1,121]
B=[(-1)**j*c for j,c in enumerate(A)]
assert A==[1,4,6,44,121]
assert B==[1,-4,6,-44,121]
assert sum(A)==176 and sum(B)==80
assert sum(A)*sum(B)==14080

def mod_divides(f,g,p=3):
    a=[v%p for v in f]
    b=[v%p for v in g]
    while len(a)>=len(b):
        top=a[-1]*pow(b[-1],-1,p)%p
        off=len(a)-len(b)
        for j in range(len(b)):
            a[off+j]=(a[off+j]-top*b[j])%p
        while a and a[-1]==0:a.pop()
    return not a

# A monic quartic is irreducible if it has no monic factor of degree 1 or 2.
for coeffs in product(range(3),repeat=2):
    assert not mod_divides(A,[coeffs[0],coeffs[1],1])
for coeffs in product(range(3),repeat=1):
    assert not mod_divides(A,[coeffs[0],1])
assert (a2 % 11) != 0
print('ACCOLA_MACLACHLAN_F11_DESCENT_OK',
      'quotient_counts=(16,118),(8,118)',
      'source_counts=(12,114)',
      'Jacobian_order=14080',
      'irreducible_quartic_factors=2')
