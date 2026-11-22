#!/usr/bin/env python3
"""Independent finite subgroup and homomorphism count for dihedral groups."""
from math import gcd, isqrt

def divs(n): return [d for d in range(1,n+1) if n%d==0]
def phi(n): return sum(gcd(i,n)==1 for i in range(1,n+1))
def predicted(n):
    assert n>=3
    even=(n%2==0)
    iso=1+(n+int(even))**2
    iso+=sum(phi(d) for d in divs(n) if d>=3)
    iso+=sum((n//d)**2*d*phi(d) for d in divs(n) if d>=3)
    if even: iso+=6*(n//2)**2
    end=(n+2)**2 if even else n*n+1
    return iso,end

def mul(x,y,n):
    a,b=x; c,d=y
    return ((a+(-c if b else c))%n,b^d)

def inverse(x,n):
    a,b=x
    return ((a if b else -a)%n,b)

def powers(g,n):
    t=(0,0); i=0
    while True:
        t=mul(t,g,n);i+=1
        if t==(0,0):return i

def subgroup(gens,n):
    e=(0,0)
    S={e}
    frontier=list(gens)
    while frontier:
        x=frontier.pop()
        if x in S:continue
        S.add(x)
        for y in tuple(S):
            for z in [mul(x,y,n),mul(y,x,n)]:
                if z not in S:frontier.append(z)
    return frozenset(S)

def compute(n):
    G=[(a,b) for b in (0,1) for a in range(n)]
    groups={frozenset({(0,0)})}
    # Actual subgroup closure by expanding every existing subgroup by each group element
    stack=list(groups)
    while stack:
        H=stack.pop()
        for g in G:
            if g in H:continue
            K=subgroup(tuple(H)+(g,),n)
            if K not in groups:
                groups.add(K);stack.append(K)
    types={}
    for H in groups:
        d=len(H)
        mx=max(powers(g,n) for g in H)
        kind=('cyclic',d) if mx==d else ('dihedral',d//2)
        types[kind]=types.get(kind,0)+1
    PI=0
    for (kind,d),m in types.items():
        automorphisms=phi(d) if kind=='cyclic' else (6 if d==2 else d*phi(d))
        PI+=m*m*automorphisms
    # Homomorphism from presentation by images of two generators
    r=(1,0); s=(0,1); e=(0,0)
    END=0
    for x in G:
        xn=e
        for _ in range(n): xn=mul(xn,x,n)
        if xn!=e:continue
        for y in G:
            if mul(y,y,n)!=e: continue
            if mul(mul(y,x,n),y,n)==inverse(x,n):END+=1
    return PI,END,types

for n in range(3,17):
    direct=compute(n);formula=predicted(n)
    assert direct[:2]==formula,(n,direct[:2],formula)
    assert direct[0]>direct[1]
    print(n,*formula,'subgroup_types',len(direct[2]))
print('DIHEDRAL_PARTIAL_ISOMORPHISM_OK 3..16')
