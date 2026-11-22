#!/usr/bin/env python3
"""Standalone small-group checks of prescribed associator fibers in Chein doubles.

Only standard Python is required. Uses direct four-case multiplication and
full enumeration of triples; does not assume the seven-sector proof.
"""
from collections import Counter
from itertools import permutations, product


def permutation_group(n, even_only=False):
    els = tuple(permutations(range(n)))
    if even_only:
        def parity(a):
            return sum(a[i] > a[j] for i in range(n) for j in range(i+1,n)) % 2
        els = tuple(a for a in els if parity(a) == 0)
    mul = lambda a,b: tuple(a[b[i]] for i in range(n))
    e = tuple(range(n))
    inv = {a: tuple(a.index(i) for i in range(n)) for a in els}
    return els,mul,inv,e


def cyclic_group(n):
    els=tuple(range(n))
    mul=lambda a,b:(a+b)%n
    inv={a:(-a)%n for a in els}
    return els,mul,inv,0


def dihedral_group(m):
    els=tuple(product(range(m),range(2)))
    def mul(a,b):
        return ((a[0]+(-1 if a[1] else 1)*b[0])%m,(a[1]+b[1])%2)
    inv={a:next(b for b in els if mul(a,b)==(0,0)) for a in els}
    return els,mul,inv,(0,0)


def quaternion_group():
    # signed unit quaternions: (sign, 0/1/2/3) = ±1, ±i, ±j, ±k
    els=tuple(product(range(2),range(4)))
    qmul={(0,0):(0,0)}
    def mul(a,b):
        x,y=a[1],b[1]
        if x==0: return ((a[0]+b[0])%2,y)
        if y==0: return ((a[0]+b[0])%2,x)
        if x==y: return ((a[0]+b[0]+1)%2,0)
        table={(1,2):(0,3),(2,3):(0,1),(3,1):(0,2),
               (2,1):(1,3),(3,2):(1,1),(1,3):(1,2)}
        s,z=table[(x,y)]
        return ((a[0]+b[0]+s)%2,z)
    inv={a:next(b for b in els if mul(a,b)==(0,0)) for a in els}
    return els,mul,inv,(0,0)


def audit(name, group):
    elements,m,iv,e=group
    n=len(elements)
    def chein(a,b):
        x,i=a;y,j=b
        if i==0 and j==0: return (m(x,y),0)
        if i==0 and j==1: return (m(y,x),1)
        if i==1 and j==0: return (m(x,iv[y]),1)
        return (m(iv[y],x),0)
    loop=[(x,i) for x in elements for i in range(2)]
    comm=Counter(m(m(m(iv[x],iv[y]),x),y) for x in elements for y in elements)
    def group_comm(x,y):
        return m(m(m(iv[x],iv[y]),x),y)
    def derived_formula(a,b,c):
        x,i=a; y,j=b; z,k=c
        bits=(i,j,k)
        if bits==(0,0,0): return e
        if bits==(0,0,1): return group_comm(x,y)
        if bits==(0,1,0): return group_comm(x,iv[z])
        if bits==(1,0,0): return group_comm(iv[y],iv[z])
        if bits==(0,1,1):
            t=m(iv[z],y)
            return group_comm(iv[t],iv[x])
        if bits==(1,0,1):
            t=m(iv[z],x)
            return group_comm(iv[t],y)
        if bits==(1,1,0):
            t=m(iv[y],x)
            return group_comm(iv[t],iv[z])
        r=m(x,iv[y]); s=m(z,iv[y]); v=group_comm(s,r)
        return m(m(iv[y],v),y)
    assoc=Counter()
    sectors=Counter()
    for a,b,c in product(loop,repeat=3):
        left=chein(chein(a,b),c)
        right=chein(a,chein(b,c))
        assert left[1]==right[1]
        # Left quotient in the loop: unique d such that d*right=left.
        candidates=[d for d in elements if chein((d,0),right)==left]
        assert len(candidates)==1
        t=candidates[0]
        assert t == derived_formula(a,b,c), (name,a,b,c,t,derived_formula(a,b,c))
        assoc[t]+=1
        sectors[(a[1],b[1],c[1],t)]+=1
    for t in elements:
        want=7*n*comm[t]+(n**3 if t==e else 0)
        assert assoc[t]==want,(name,t,assoc[t],want)
    for bits in product(range(2),repeat=3):
        for t in elements:
            want=(n**3 if bits==(0,0,0) and t==e else
                  0 if bits==(0,0,0) else n*comm[t])
            assert sectors[(*bits,t)]==want,(name,bits,t,sectors[(*bits,t)],want)
    print(name, 'group_order',n,'loop_order',2*n,'triples',8*n**3,
          'group_commuting_pairs',comm[e],
          'identity_associator',assoc[e],
          'nonidentity_values',sum(bool(assoc[t]) for t in elements if t!=e),
          'PASS')

if __name__=='__main__':
    for name,g in (
        ('C2',cyclic_group(2)),('C3',cyclic_group(3)),
        ('D6',dihedral_group(3)),('D8',dihedral_group(4)),
        ('Q8',quaternion_group()),('S3',permutation_group(3)),
        ('A4',permutation_group(4,True)),('S4',permutation_group(4))):
        audit(name,g)
