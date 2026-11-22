"""Exact exhaustive finite check for the 16-point weighted-square product.
The proof of the continuous parameter statement is in RESULT.md.
No numerical approximations or external packages are used.
"""
from itertools import combinations, product
from collections import Counter

# A and B are long-edge and short-edge two-bit blocks, respectively.
Q = tuple(product((0, 1), repeat=2))
V = tuple(product(Q,Q))


def balls(case):
    M=[]
    for A,B in V:
        mask=0
        for j,(C,D) in enumerate(V):
            diffA=[i for i in range(2) if A[i]!=C[i]]
            diffB=[i for i in range(2) if B[i]!=D[i]]
            if case=='asymmetric':
                covered=(len(diffA)==0 or
                  (len(diffA)==1 and diffA[0] not in diffB))
            else:
                covered=all(not(A[i]!=C[i] and B[i]!=D[i])
                            for i in range(2))
            if covered: mask|=1<<j
        M.append(mask)
    return M


def find_covers(M,k):
    return [c for c in combinations(range(16),k)
            if (sum(0 for x in []) or
                __import__('functools').reduce(int.__or__,(M[i] for i in c),0))
                ==(1<<16)-1]

A=balls('asymmetric')
S=balls('symmetric')
assert {m.bit_count() for m in A}=={8}
assert {m.bit_count() for m in S}=={9}
assert not find_covers(A,1) and not find_covers(A,2)
assert not find_covers(S,1) and not find_covers(S,2)
ca=find_covers(A,3);cs=find_covers(S,3)
assert len(ca)==32,(len(ca),ca)
assert len(cs)==96,(len(cs),cs)

# Show all asymmetric equality triples have opposite long-bit fibers,
# with two antipodal short-bit labels in the doubled fiber.
for triple in ca:
    d=Counter(V[i][0] for i in triple)
    assert sorted(d.values())==[1,2]
    A2=next(a for a,n in d.items() if n==2)
    A1=next(a for a,n in d.items() if n==1)
    assert all(A2[i]!=A1[i] for i in range(2))
    B2=[V[i][1] for i in triple if V[i][0]==A2]
    assert all(B2[0][i]!=B2[1][i] for i in range(2))

# Equality classification for the equal-edge square, under all
# isometries of the two C4 factors and their exchange.
perms=set()
for flips in product((0,1),repeat=4):
    for swap0,swap1,swapXY in product((0,1),repeat=3):
        def image_vertex(z):
            a,b=z
            xx=[a[0],b[0]];yy=[a[1],b[1]]
            if swap0: xx=xx[::-1]
            if swap1: yy=yy[::-1]
            if swapXY: xx,yy=yy,xx
            xx=[xx[0]^flips[0],xx[1]^flips[1]]
            yy=[yy[0]^flips[2],yy[1]^flips[3]]
            return (tuple((xx[0],yy[0])),tuple((xx[1],yy[1])))
        perms.add(tuple(V.index(image_vertex(v)) for v in V))
assert len(perms)==128
remaining=set(cs);sizes=[];reps=[]
while remaining:
    c=min(remaining)
    orb={tuple(sorted(P[i] for i in c)) for P in perms}
    assert orb <= set(cs)
    sizes.append(len(orb));reps.append(c)
    remaining-=orb
assert sorted(sizes)==[32,64],(sizes,reps)

# At radii strictly below R, the universal six-site upper envelope has
# at most 14 covered sites for any three centers.
E=[]
for a,b in V:
    bitmask=0
    for j,(c,d) in enumerate(V):
        dif=[k for k in range(2) if a[k]!=c[k]]
        if len(dif)==0 or (len(dif)==1 and b==d):bitmask|=1<<j
    E.append(bitmask)
assert {m.bit_count() for m in E}=={6}
assert max((E[i]|E[j]|E[k]).bit_count()
           for i,j,k in combinations(range(16),3))==14
print('PASS: 560 triples exhausted; optimal counts 32/96; equal case orbits 32+64; 2-center noncoverage; universal strict-radius envelope max 14.')
