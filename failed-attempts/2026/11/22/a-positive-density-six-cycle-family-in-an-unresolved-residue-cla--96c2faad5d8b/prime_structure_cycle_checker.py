#!/usr/bin/env python3
"""Exact algebraic checks for a finite-field structure-graph six-cycle theorem.

Standard Python only; the infinitude/density argument uses Chebotarev's
mathematical theorem and is not replaced by finite computation.
"""
from fractions import Fraction

P = [3, -6, 9, -10, 8, -4, 1]  # coefficients in increasing order


def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:
        a.pop()
    return a

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)

def sub(a,b):
    c=[0]*max(len(a),len(b))
    for i in range(len(c)):
        c[i]=(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0)
    return trim(c)

def compose(a,b):
    c=[0]
    for x in reversed(a):
        c=mul(c,b)
        c[0]+=x
    return trim(c)

def derivative(a):return [i*a[i] for i in range(1,len(a))]

def rem(a,b,p):
    a=trim([x%p for x in a]);b=trim([x%p for x in b])
    assert b!=[0]
    while len(a)>=len(b) and a!=[0]:
        coef=a[-1]*pow(b[-1],-1,p)%p
        shift=len(a)-len(b)
        for j in range(len(b)):a[j+shift]=(a[j+shift]-coef*b[j])%p
        a=trim(a)
    return a

def prodmod(a,b,mod,p):return rem(mul(a,b),mod,p)

def powmod(a,n,mod,p):
    ans=[1]
    while n:
        if n&1:ans=prodmod(ans,a,mod,p)
        a=prodmod(a,a,mod,p);n//=2
    return ans

def gcdmod(a,b,p):
    a=trim([x%p for x in a])
    b=trim([x%p for x in b])
    while b!=[0]:a,b=b,rem(a,b,p)
    return trim([x*pow(a[-1],-1,p)%p for x in a])

def determinant(matrix):
    # Exact rational Gaussian elimination avoids coefficient roundoff.
    a=[[Fraction(v) for v in row] for row in matrix]
    n=len(a);sign=1;value=Fraction(1)
    for i in range(n):
        j=next((j for j in range(i,n) if a[j][i]),None)
        if j is None:return 0
        if j!=i:a[i],a[j]=a[j],a[i];sign=-sign
        pivot=a[i][i];value*=pivot
        for k in range(i+1,n):
            factor=a[k][i]/pivot
            if factor:
                for m in range(i+1,n):a[k][m]-=factor*a[i][m]
                a[k][i]=0
    result=sign*value
    assert result.denominator==1
    return int(result)

def resultant(a,b):
    # Sylvester determinant with descending-order coefficients.
    m=len(a)-1;n=len(b)-1;A=list(reversed(a));B=list(reversed(b))
    rows=[]
    for i in range(n):rows.append([0]*i+A+[0]*(n-i-1))
    for i in range(m):rows.append([0]*i+B+[0]*(m-i-1))
    return determinant(rows)

def evaluate(a,x,p=None):
    v=0
    for z in reversed(a):v=v*x+z
    return v if p is None else v%p

# Integer polynomial identity g^3(X)-X=-X^2 P(X).
g=[0,1,-1];g3=compose(g,compose(g,g))
assert sub(g3,[0,1])==mul([0,0,-1],P)
assert -resultant(P,derivative(P))==-41472  # monic degree-six discriminant
assert resultant(P,[2,-2,1])==1

# Exact, complete finite-field irreducibility test for degree 6 modulo 5.
# Rabin test uses irreducibility iff X^(5^6)=X and gcd(F,X^(5^(6/r))-X)=1 for primes r|6.
x=[0,1]
assert powmod(x,5**6,P,5)==x
for k in (2,3):
    z=sub(powmod(x,5**k,P,5),x)
    assert gcdmod(P,z,5)==[1]

# Modulo 11: exactly three rational roots and irreducible cubic factor.
assert sorted([i for i in range(11) if evaluate(P,i,11)==0])==[2,5,9]
C=[4,6,1,1]
assert all(evaluate(C,i,11)!=0 for i in range(11))  # cubic irreducibility
factors=[1]
for r in (2,5,9):factors=mul(factors,[-r,1])
factors=mul(factors,C)
assert all((a-b)%11==0 for a,b in zip(P,factors)) and len(factors)==7

# Explicit primitive six-cycles in four primes from the target class.
for p in (43,67,139,163):
    assert p%24==19
    roots=[y for y in range(p) if evaluate(P,y,p)==0]
    assert roots
    for y in roots:
        states=[];point=(-1%p,y)
        for i in range(6):
            assert point not in states
            states.append(point)
            a,b=point;point=((a+b)%p,(a*b)%p)
        assert point==states[0]
for p in (19,211,283):
    assert p%24==19
    assert not any(evaluate(P,y,p)==0 for y in range(p))

# Group-theoretic finite count: within C3xC3 there are 5 elements
# fixing at least one root of its two disjoint orbits of size 3.
assert [sum(int(a==0)+int(b==0)==k for a in range(3) for b in range(3)) for k in (0,1,2)]==[4,4,1]
assert sum(a==0 or b==0 for a in range(3) for b in range(3))==5
assert 18*8//2==72
print('PRIME_STRUCTURE_GRAPH_DENSITY_CERTIFICATE_OK')
