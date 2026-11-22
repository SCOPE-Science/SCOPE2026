#!/usr/bin/env python3
"""Self-contained finite checks for spider independence-complex symmetry formulas.
These are checks, not a replacement for the general equivariant homotopy proof.
"""
from itertools import permutations

def spider_graph(k, ell):
    # central vertex 0, arm (a,j) stored as 1+a*ell+(j-1).
    vertices = 1+k*ell
    edges = set()
    for a in range(k):
        for j in range(1,ell+1):
            v = 1+a*ell+j-1
            u = 0 if j == 1 else v-1
            edges.add(tuple(sorted((u,v))))
    return vertices,edges

def orbit_labels(k, perm):
    seen=set();cycles=[]
    for a in range(k):
        if a not in seen:
            cur=[];i=a
            while i not in seen:
                seen.add(i);cur.append(i);i=perm[i]
            cycles.append(cur)
    return cycles

def orbit_vertex_sets(k,ell,perm):
    cs=orbit_labels(k,perm)
    return [frozenset([0])]+[frozenset(1+a*ell+j for a in c) for c in cs for j in range(ell)]

def orbit_complex_face_counts(k,ell,perm):
    n,edges=spider_graph(k,ell)
    os=orbit_vertex_sets(k,ell,perm)
    ans=[0]*(len(os)+1)
    for mask in range(1<<len(os)):
        S=set().union(*(o for i,o in enumerate(os) if mask>>i&1))
        if all(not(u in S and v in S) for u,v in edges):
            ans[mask.bit_count()]+=1
    return tuple(ans)

def independence_face_counts(k,ell):
    n,edges=spider_graph(k,ell)
    ans=[0]*(n+1)
    for mask in range(1<<n):
        if all(not(mask>>u&1 and mask>>v&1) for u,v in edges):
            ans[mask.bit_count()]+=1
    return tuple(ans)

def chi(counts):
    return 1-sum(((-1)**j)*c for j,c in enumerate(counts))

def expected_chi(k,ell):
    m,r=divmod(ell,3)
    if r==0: return 1
    d=m*k if r==1 else (m+1)*k-1
    return 1+(-1)**d

def path_independence_polynomial(n):
    p0=[1];p1=[1,1]
    if n==0:return p0
    if n==1:return p1
    for v in range(2,n+1):
        q=[0]*max(len(p1),len(p0)+1)
        for i,x in enumerate(p1):q[i]+=x
        for i,x in enumerate(p0):q[i+1]+=x
        p0,p1=p1,q
    return p1

# Direct exhaustive face counts and group orbit complexes.
count=0
for k,ell in [(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(3,5)]:
    direct=independence_face_counts(k,ell)
    assert chi(direct)==expected_chi(k,ell),(k,ell,'underlying Euler')
    for p in permutations(range(k)):
        o=len(orbit_labels(k,p))
        by_orbits=orbit_complex_face_counts(k,ell,p)
        assert by_orbits==independence_face_counts(o,ell),(k,ell,p,'PL orbit model')
        assert chi(by_orbits)==expected_chi(o,ell),(k,ell,p,'fixed Euler')
        if ell%3:
            m,r=divmod(ell,3)
            blockdim=m if r==1 else m+1
            sign=(-1)**(blockdim*(k-o))
            d=m*k if r==1 else (m+1)*k-1
            reduced_lefschetz=chi(by_orbits)-1
            assert reduced_lefschetz==((-1)**d)*sign,(k,ell,p,'orientation character')
        count+=1

# Path reversal quotient Euler for odd paths: a direct Burnside check.
for ell in range(2,60):
    n=2*ell+1
    ambient=chi(path_independence_polynomial(n))
    fixed=chi(path_independence_polynomial(ell+1))
    assert ambient==expected_chi(2,ell)
    assert fixed==expected_chi(1,ell)
    assert (ambient+fixed)%2==0
    # quotient S(U+epsilon V)/C2 = S(U)*RP(dim V-1), or contractible
    quotient_euler=(ambient+fixed)//2
    if ell%3==0:
        expected=1
    else:
        m,r=divmod(ell,3)
        q=m if r==1 else m+1
        # rational reduced Euler of RP^(q-1) is (-1)^(q-1) if q even, else 0
        # and joining S^(m) multiplies reduced Euler by (-1)^(m+1).
        expected=1 + ((-1)**(m+q) if q%2==0 else 0)
    assert quotient_euler==expected,(n,quotient_euler,expected)
print('VERIFY_OK; direct subgroup-orbit complexes:',count,'; odd path widths:',58)
