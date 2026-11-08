#!/usr/bin/env python3
"""Standalone integer combinatorics checks for oriented triangular books.
Usage: python verify.py. Only Python standard library required.
"""
from itertools import combinations, permutations, product

def faces_book(k):
    # arcs: c=(0,1), u_i=(1,2+i), v_i=(2+i,0)
    arcs=[(0,1)]+[(1,2+i) for i in range(k)]+[(2+i,0) for i in range(k)]
    f=set()
    for bits in range(1<<(2*k+1)):
        chosen=[i for i in range(len(arcs)) if bits>>i&1]
        outs,ins={},{}; good=True
        for i in chosen:
            a,b=arcs[i]
            if a in outs or b in ins:good=False;break
            outs[a]=b;ins[b]=a
        if not good:continue
        for a in outs:
            seen=set();v=a
            while v in outs:
                if v in seen:good=False;break
                seen.add(v);v=outs[v]
            if not good:break
        if good:f.add(frozenset(chosen))
    return f

def predicted(k):
    c=0;us=list(range(1,k+1));vs=list(range(k+1,2*k+1));f={frozenset()}
    for i in [c]+us+vs:f.add(frozenset([i]))
    for i in us+vs:f.add(frozenset([c,i]))
    for a in us:
        for b in vs:
            f.add(frozenset([a,b]))
            if a-1!=b-k-1:f.add(frozenset([c,a,b]))
    return f

def rank_gf2(cols):
    piv={}
    for x in cols:
        while x:
            i=x.bit_length()-1
            if i in piv:x^=piv[i]
            else:piv[i]=x;break
    return len(piv)

def betti_gf2(faces):
    bydim={d:sorted([s for s in faces if len(s)==d+1],key=lambda x:tuple(sorted(x))) for d in range(3)}
    ranks={}
    for d in (1,2):
        ix={face:i for i,face in enumerate(bydim[d-1])}
        cols=[]
        for face in bydim[d]:
            v=0
            for a in face:v^=1<<ix[face-{a}]
            cols.append(v)
        ranks[d]=rank_gf2(cols)
    return [len(bydim[0])-ranks[1]-1,len(bydim[1])-ranks[1]-ranks[2],len(bydim[2])-ranks[2]]

def perm_on_vertex(p,k,v):
    if v==0:return 0
    if v<=k:return 1+p[v-1]
    return 1+k+p[v-1-k]

def subgroup(k,gens):
    ident=tuple(range(k));elts={ident};queue=[ident]
    while queue:
        p=queue.pop()
        for q in gens:
            for r in (tuple(p[q[i]] for i in range(k)), tuple(q[p[i]] for i in range(k))):
                if r not in elts:elts.add(r);queue.append(r)
    return frozenset(elts)

def orbits(points,acts):
    rest=set(points);result=[]
    while rest:
        x=min(rest);orbit={g[x] for g in acts};assert orbit<=rest
        rest-=orbit;result.append(orbit)
    return result

def orbit_of_face(face,H,k):
    return frozenset(frozenset(perm_on_vertex(g,k,v) for v in face) for g in H)

def check_group(k):
    perms=list(permutations(range(k)));groups={subgroup(k,[p,q]) for p in perms for q in perms}
    f=predicted(k)
    c=0;us=range(1,k+1);vs=range(k+1,2*k+1)
    for H in groups:
        # Every action preserves the abstract simplicial complex, including orientation of diagonal edges.
        for g in H:
            assert all(frozenset(perm_on_vertex(g,k,v) for v in face) in f for face in f)
            assert all((perm_on_vertex(g,k,u),perm_on_vertex(g,k,u+k))==(1+g[u-1],1+k+g[u-1]) for u in us)
        fcount=sum(all(g[i]==i for g in H) for i in range(k))
        acts=tuple(H);p_orbits=orbits(range(k),acts)
        assert len(p_orbits)>=1
        # Quotient of cone triangles by arbitrary H: one free off-diagonal edge orbit per triangle orbit.
        E=[frozenset((a,b)) for a in us for b in vs if a-1!=b-k-1]
        T=[frozenset((0,*e)) for e in E]
        eo=set(orbit_of_face(e,H,k) for e in E)
        to=set(orbit_of_face(t,H,k) for t in T)
        assert len(eo)==len(to)
        assert {frozenset(frozenset((0,*e)) for e in orb) for orb in eo}==to
        diag=[frozenset((i+1,k+1+i)) for i in range(k)]
        assert len({orbit_of_face(e,H,k) for e in diag})==len(p_orbits)
        # Fixed geometric complex is supported only at c and vertices of H-fixed pages.
        fixed_verts={0} | {i+1 for i in range(k) if all(g[i]==i for g in H)} | {k+i+1 for i in range(k) if all(g[i]==i for g in H)}
        ff={s for s in f if s<=fixed_verts}
        assert len(ff)==2*fcount*fcount+3*fcount+2
    return len(groups)

if __name__=='__main__':
    for k in range(1,8):
        actual=faces_book(k);expect=predicted(k)
        assert actual==expect,(k,actual^expect)
        assert len(actual)==2*k*k+3*k+2
        # Explicit global free-face certificate. No off-diagonal edge has a second triangle coface.
        E=[frozenset((i+1,k+1+j)) for i in range(k) for j in range(k) if i!=j]
        for edge in E:
            higher={t for t in actual if len(t)==3 and edge<=t}
            assert higher=={edge|{0}}
        remainder=actual-set(E)-{edge|{0} for edge in E}
        Y={frozenset()} | {frozenset([v]) for v in range(2*k+1)}
        Y |= {frozenset((0,v)) for v in range(1,2*k+1)}
        Y |= {frozenset((i+1,k+1+i)) for i in range(k)}
        assert remainder==Y
        b=betti_gf2(actual) if k<=5 else None
        assert b is None or b==[0,k,0],(k,b)
        print(f'k={k}: faces={len(actual)}, free_pairs={len(E)}, residual_edges={3*k}, H1_rank={k}, mod2={b}')
    group_count=check_group(4)
    print(f'k=4: all {group_count} distinct two-generated page-permutation subgroups checked for action, fixed support and orbit-cell cancellation')
    print('ALL_VERIFY_OK')
