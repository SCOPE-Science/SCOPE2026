"""Exact checks for crossing/nesting pair-count law in random chord diagrams.

Uses only Python standard library, with no external data or dependencies.
Run: python3 verify.py
"""
from itertools import permutations
from collections import Counter
from fractions import Fraction
from math import comb, factorial

KINDS = ('X','N','A')

def relation(a, b):
    x,y=sorted(a); u,v=sorted(b)
    if x<u<y<v or u<x<v<y: return 'X'
    if x<u<v<y or u<x<y<v: return 'N'
    return 'A'

def moments_exact(n):
    counts=Counter(); total=0
    def rec(free, chosen):
        nonlocal total
        if not free:
            c={'X':0, 'N':0, 'A':0}
            for i in range(len(chosen)):
                for j in range(i+1,len(chosen)):
                    c[relation(chosen[i],chosen[j])] += 1
            counts[(c['X'], c['N'], c['A'])] += 1
            total+=1
            return
        a=free[0]
        for k in range(1,len(free)):
            b=free[k]
            rec(free[1:k]+free[k+1:], chosen+[(a,b)])
    rec(tuple(range(2*n)),[])
    assert total == factorial(2*n)//(2**n*factorial(n))
    return total,counts

def expected_table(n, stats):
    total,dist=stats
    means=[sum(Fraction(k[i]*num,total) for k,num in dist.items()) for i in range(3)]
    cov=[[sum(Fraction(k[i]*k[j]*num,total) for k,num in dist.items())-means[i]*means[j]
          for j in range(3)] for i in range(3)]
    return means,cov

def predicted(n):
    c=comb(n,2)
    t=comb(n,3) if n>=3 else 0
    diag=Fraction(2*c,9)+Fraction(2*t,15)
    diagA=Fraction(2*c,9)+Fraction(4*t,15)
    covXN=Fraction(-c,9)
    covXA=Fraction(-c,9)-Fraction(2*t,15)
    cov=[[diag,covXN,covXA],[covXN,diag,covXA],[covXA,covXA,diagA]]
    return [Fraction(c,3)]*3,cov

checks=0
words=set(permutations((0,0,1,1,2,2)))
assert len(words)==90
checks += 1
cross=Counter()
for word in words:
    arcs={k:tuple(i for i,x in enumerate(word) if x==k) for k in (0,1,2)}
    cross[(relation(arcs[0],arcs[1]),relation(arcs[0],arcs[2]))]+=1
expected={('X','X'):12,('N','N'):12,('A','A'):14,
          ('X','N'):10,('N','X'):10,
          ('X','A'):8,('A','X'):8,('N','A'):8,('A','N'):8}
assert cross == expected,(cross,expected)
checks+=len(expected)
for n in range(2,8):
    actual=expected_table(n,moments_exact(n))
    want=predicted(n)
    for i in range(3):
        assert actual[0][i] == want[0][i],(n,i,actual,want)
        checks+=1
        for j in range(3):
            assert actual[1][i][j] == want[1][i][j],(n,i,j,actual,want)
            checks+=1
    assert want[1][0][1] == -Fraction(n*(n-1),18)
    assert want[1][0][0] == Fraction(n*(n-1)*(n+3),45)
    assert Fraction(want[1][0][1],want[1][0][0]) == -Fraction(5,2*(n+3))
    checks+=3

# Elementary polynomial moment integrals, implemented with exact rational arithmetic.
# Integration on the domain 0 <= u <= 1, u <= v <= 1; density = 2.
# If P(u,v) = sum coeff * u^i v^j, its expectation =
# sum 2*coeff/[(j+1)*(i+1)] * (1 - (i+1)/(i+j+2)) = 2*coeff /[(i+1)*(i+j+2)].
# (The final simplification is shown explicitly below.)

def add(*polys):
    out=Counter()
    for p in polys:
        for k,v in p.items():out[k]+=v
    return dict((k,v) for k,v in out.items() if v)

def scale(p,k):return {e:c*k for e,c in p.items()}
def mul(p,q):
    t=Counter()
    for (a,b),x in p.items():
        for (c,d),y in q.items():t[(a+c,b+d)]+=x*y
    return dict(t)

def mean(p):
    out=Fraction()
    for (i,j),coef in p.items():
        # integrate dv from u to 1, then du from 0 to 1:
        out += 2*coef*Fraction(1,j+1)*(Fraction(1,i+1)-Fraction(1,i+j+2))
    return out
one={(0,0):Fraction(1)}
u={(1,0):Fraction(1)}
v={(0,1):Fraction(1)}
ell=add(v,scale(u,-1))
gX=add(scale(ell,2),scale(mul(ell,ell),-2),scale(one,-Fraction(1,3)))
gN=add(mul(ell,ell),scale(mul(u,add(one,scale(v,-1))),2),scale(one,-Fraction(1,3)))
for value,exp in [(mean(gX),0),(mean(gN),0),
                  (mean(mul(gX,gX)),Fraction(1,45)),
                  (mean(mul(gN,gN)),Fraction(1,45)),
                  (mean(mul(gX,gN)),0)]:
    assert value==exp,(value,exp)
    checks+=1

print(f'PASS {checks} exact assertions; uniform matchings enumerated through n=7 (135135 at n=7).')
print('3-chord relation table:', dict(sorted(cross.items())))
print('First-projection variances 1/45, 1/45; cross-projection covariance 0.')
