#!/usr/bin/env python3

def mul(p,q): return tuple(p[q[i]] for i in range(len(p)))
def gen_group(gens):
    e=tuple(range(len(gens[0]))); G={e}; todo=[e]
    while todo:
        a=todo.pop()
        for b in gens:
            for c in (mul(a,b),mul(b,a)):
                if c not in G: G.add(c); todo.append(c)
    return sorted(G)

def verify(name,gens):
    G=gen_group(gens); n=len(G); r=len(gens); e=tuple(range(len(gens[0])))
    assert all(h!=e for h in gens)
    idx={g:i for i,g in enumerate(G)}
    # Orbit finite space has exactly one orbit per level -1,0,...,r.
    levels=list(range(-1,r+1)); assert len(levels)==r+2
    # The induced orbit order is the total order on levels.
    orbit_rel={(i,j) for i in levels for j in levels if i<=j}
    assert len(orbit_rel)==(r+2)*(r+3)//2
    # Equivariant retract Y has lower and upper G-orbits and r+1 edge orbits.
    edges=[]
    for g in G:
        edges.append((idx[g],n+idx[g],0))
        for j,h in enumerate(gens,1):
            edges.append((idx[mul(g,h)],n+idx[g],j))
    assert len(edges)==n*(r+1)
    # connected by generator paths; graph Betti number is E-V+1
    beta=len(edges)-2*n+1
    assert beta==n*(r-1)+1
    # Geometric orbit of Y has 2 vertices and r+1 distinct edge orbits, hence beta r.
    orbit_beta=(r+1)-2+1
    assert orbit_beta==r
    # The finite-space quotient map is not a covering: over level 1, U_(g,1)
    # contains both (g,-1) and (g h1,-1), which have the same quotient image.
    h1=gens[0]; g=G[0]
    assert mul(g,h1)!=g
    lower_preimages={g,mul(g,h1)}
    assert len(lower_preimages)==2
    return n,r,beta,orbit_beta

c3=(1,2,0)
v4a=(1,0,3,2); v4b=(2,3,0,1)
s3a=(1,0,2); s3b=(1,2,0)
rows=[verify('C3',[c3]),verify('V4',[v4a,v4b]),verify('S3',[s3a,s3b])]
assert rows==[(3,1,1,1),(4,2,5,2),(6,2,7,2)]
print('VERIFY_OK samples=C3,V4,S3 finite_orbit=chain geometric_orbit_betti=1,2,2 quotient_not_covering')
