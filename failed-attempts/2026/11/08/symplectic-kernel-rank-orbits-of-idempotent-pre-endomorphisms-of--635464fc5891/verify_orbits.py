#!/usr/bin/env python3
"""Independent symplectic-orbit and ternary direct-morphism checks."""
from collections import Counter
from itertools import product

def bil(a,b):
    return ((a&b>>2).bit_count()+(a>>2&b).bit_count())%2

def mul(C,v):
    out=0
    for i,c in enumerate(C):
        if v>>i&1:out^=c
    return out

def rank2(C):
    piv={}
    for c in C:
        x=c
        while x:
            k=x.bit_length()-1
            if k in piv:x^=piv[k]
            else:piv[k]=x;break
    return len(piv)

def ker_restriction(C):
    K=[x for x in range(16) if mul(C,x)==0]
    basis=[]
    for x in K:
        if rank2(basis+[x])>len(basis):basis.append(x)
    R=[sum(bil(basis[i],basis[j])<<j for j in range(len(basis))) for i in range(len(basis))]
    return rank2(R)

P={C for C in product(range(16),repeat=4)
   if all(mul(C,c)==c for c in C)
   and all(not bil(C[i],C[j]) for i in range(4) for j in range(i))}
assert len(P)==361

def conjugate(C,v):
    def T(x): return x^(v if bil(x,v) else 0)
    return tuple(T(mul(C,T(1<<j))) for j in range(4))
remaining=set(P)
orbits=[]
while remaining:
    root=min(remaining)
    Q={root};stack=[root]
    while stack:
        C=stack.pop()
        for v in range(1,16):
            D=conjugate(C,v)
            assert D in P
            if D not in Q:Q.add(D);stack.append(D)
    remaining.difference_update(Q)
    R=rank2(root)
    restriction=ker_restriction(root)
    expected_s=(restriction-2*(2-R))//2
    assert all(rank2(C)==R and ker_restriction(C)==restriction for C in Q)
    orbits.append(((R,expected_s),len(Q)))
assert sorted(orbits)==sorted([((0,0),1),((1,0),120),((2,0),120),((2,1),120)])
print('F2_H5_symplectic_projection_orbits',sorted(orbits))

# Direct enumerate all 3x3 matrices over F3 against both defining identities;
# H3 structure [x,y]=det(x_V,y_V) z.
q=3

def action(A,x):
    return tuple(sum(A[i][j]*x[j] for j in range(3))%q for i in range(3))
def bracket(x,y): return (0,0,(x[0]*y[1]-x[1]*y[0])%q)
def rank(A):
    rows=[list(row) for row in A];r=0
    for j in range(3):
        pivot=next((i for i in range(r,3) if rows[i][j]%q),None)
        if pivot is None:continue
        rows[pivot],rows[r]=rows[r],rows[pivot]
        inv=pow(rows[r][j],-1,q)
        rows[r]=[(t*inv)%q for t in rows[r]]
        for i in range(3):
            if i!=r:
                coeff=rows[i][j]
                rows[i]=[(rows[i][k]-coeff*rows[r][k])%q for k in range(3)]
        r+=1
    return r
hist=Counter()
E=[tuple(int(i==j) for i in range(3)) for j in range(3)]
for flat in product(range(q),repeat=9):
    A=[flat[0:3],flat[3:6],flat[6:9]]
    cols=[action(A,e) for e in E]
    if any(action(A,c)!=c for c in cols):continue
    if any(action(A,bracket(E[i],E[j]))!=bracket(cols[i],cols[j]) for i in range(3) for j in range(i)):
        continue
    hist[rank(A)]+=1
assert hist=={0:1,1:36,3:1},hist
print('F3_H3_direct_full_homomorphism_ranks',dict(hist))
print('VERIFY_OK')
