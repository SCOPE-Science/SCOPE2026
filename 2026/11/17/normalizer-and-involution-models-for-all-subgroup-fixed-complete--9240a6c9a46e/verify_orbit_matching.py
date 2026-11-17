"""Exact finite checks for orbit-type matching-complex fixed spaces.
Only finite permutation actions; theoretical classification proved separately.
"""
from itertools import combinations
from collections import Counter
from math import comb, factorial


def closure(generators, degree):
    one=tuple(range(degree)); seen={one}; pending=[one]
    while pending:
        p=pending.pop()
        for g in generators:
            q=tuple(p[g[i]] for i in range(degree))
            if q not in seen: seen.add(q);pending.append(q)
    return sorted(seen)


def perm_from_cycles(n, cycles):
    a=list(range(n))
    for c in cycles:
        for i,x in enumerate(c): a[x]=c[(i+1)%len(c)]
    return tuple(a)


def orbits(points, group):
    unseen=set(points); res=[]
    while unseen:
        x=min(unseen); orb=frozenset(g[x] for g in group)
        assert orb <= unseen
        res.append(orb); unseen-=orb
    return res


def orbit_edges(n, group):
    all_edges={tuple(t) for t in combinations(range(n),2)}
    out=[]
    while all_edges:
        e=min(all_edges)
        o=frozenset(tuple(sorted((g[e[0]],g[e[1]]))) for g in group)
        out.append(o);all_edges-=o
    return out


def matching_edges(edges):
    ends=[v for e in edges for v in e]
    return len(ends)==len(set(ends))


def equivariant_bijections(source, target, group):
    source=sorted(source); target=set(target)
    # Equivariance and transitivity: image of first element determines map
    ans=[]
    for y in sorted(target):
        f={}
        for g in group:
            x=g[source[0]]; z=g[y]
            if x in f and f[x]!=z:break
            f[x]=z
        else:
            if len(f)==len(source) and len(set(f.values()))==len(source) and set(f.values())==target:
                ans.append(f)
    return ans


def find_prediction(n, group):
    vos=orbits(range(n),group)
    result=[]; orbit_type_groups=[]; assigned=set()
    for i, O in enumerate(vos):
        if i in assigned:continue
        typ=[j for j,O2 in enumerate(vos) if equivariant_bijections(O,O2,group)]
        assigned.update(typ); orbit_type_groups.append(typ)
        w=len(equivariant_bijections(O,O,group))
        s=sum(1 for f in equivariant_bijections(O,O,group)
              if all(f[v]!=v and f[f[v]]==v for v in O))
        for j in typ:
            O2=vos[j]
            for f in equivariant_bijections(O2,O2,group):
                if all(f[v]!=v and f[f[v]]==v for v in O2):
                    result.append(frozenset(tuple(sorted((v,f[v]))) for v in O2))
        for j,k in combinations(typ,2):
            for f in equivariant_bijections(vos[j],vos[k],group):
                result.append(frozenset(tuple(sorted((x,y))) for x,y in f.items()))
    return set(result), [(len(typ),len(equivariant_bijections(vos[typ[0]],vos[typ[0]],group)),
        sum(1 for f in equivariant_bijections(vos[typ[0]],vos[typ[0]],group) if all(f[v]!=v and f[f[v]]==v for v in vos[typ[0]]))) for typ in orbit_type_groups]


def fact_coeff(m,w,s):
    p=Counter()
    for j in range(m//2+1):
        match_count=factorial(m)//(2**j*factorial(j)*factorial(m-2*j))
        for v in range(m-2*j+1):
            p[j+v]+=match_count*w**j*comb(m-2*j,v)*s**v
    return p


def conv(p,q):
    z=Counter()
    for i,a in p.items():
        for j,b in q.items(): z[i+j]+=a*b
    return z


def exact_face_counts(eligible, limit=22):
    assert len(eligible)<=limit, len(eligible)
    count=Counter({0:1}); occupied=[{v for e in orb for v in e} for orb in eligible]
    for r in range(1,len(eligible)+1):
        for ix in combinations(range(len(eligible)),r):
            used=set()
            ok=True
            for i in ix:
                if occupied[i] & used:
                    ok=False
                    break
                used.update(occupied[i])
            if ok:
                count[r]+=1
    return count


def case(name, generators):
    n=len(generators[0]); G=closure(generators,n)
    direct=set(orb for orb in orbit_edges(n,G) if matching_edges(orb))
    predicted,types=find_prediction(n,G)
    assert direct==predicted,(name,'edge orbit mismatch',direct^predicted)
    calc=Counter({0:1})
    for m,w,s in types:calc=conv(calc,fact_coeff(m,w,s))
    f=exact_face_counts(sorted(direct,key=lambda orb:sorted(orb)))
    assert {k:v for k,v in calc.items() if v}=={k:v for k,v in f.items() if v},(name,dict(calc),dict(f))
    print(f'{name}: degree={n}, group={len(G)}, types={types}, fixed_vertices={len(direct)}, faces={sum(f.values())}, f={dict(sorted(f.items()))}')
    return len(direct),sum(f.values())


def run():
    # For a regular action, use left multiplication of concrete finite groups.
    # The cases below use explicit generating permutations and their diagonal copies.
    def rep(base, m, extra=0):
        n=len(base[0])*m+extra; b=len(base[0]); out=[]
        for g in base:
            a=list(range(n))
            for j in range(m):
                for i in range(b):a[j*b+i]=j*b+g[i]
            out.append(tuple(a))
        return out
    cyc3=[perm_from_cycles(3,[(0,1,2)])]
    cyc4=[perm_from_cycles(4,[(0,1,2,3)])]
    v4=[perm_from_cycles(4,[(0,1),(2,3)]),perm_from_cycles(4,[(0,2),(1,3)])]
    s3=[perm_from_cycles(6,[(0,1,2),(3,5,4)]),perm_from_cycles(6,[(0,3),(1,4),(2,5)])]
    assert len(closure(s3,6))==6
    cases=[('C3-one',rep(cyc3,1)),('C3-two',rep(cyc3,2)),('C3-three',rep(cyc3,3)),
    ('C4-two',rep(cyc4,2)),('C4-two-fixed',rep(cyc4,2,1)),
    ('V4-one',rep(v4,1)),('V4-two',rep(v4,2)),('V4-three',rep(v4,3)),
    ('S3-one',rep(s3,1)),('S3-two',rep(s3,2)),
    ('S3-two-fixed',rep(s3,2,1)),
    ('S3-two-natural',rep([perm_from_cycles(3,[(0,1,2)]),perm_from_cycles(3,[(1,2)])],2)),
    ('S3-regular-and-natural',[
      tuple(s3[0][i] if i<6 else 6+perm_from_cycles(3,[(0,1,2)])[i-6] for i in range(9)),
      tuple(s3[1][i] if i<6 else 6+perm_from_cycles(3,[(1,2)])[i-6] for i in range(9))]),
    ('C4-disjoint-mixed',[perm_from_cycles(7,[(0,1,2,3),(4,5)])]),
    ('C2-four-two-fixed',[perm_from_cycles(10,[(0,1),(2,3),(4,5),(6,7)])])]
    total=0
    for name,gens in cases:
        _,n=case(name,gens);total+=n
    print(f'ALL_ORBIT_TYPE_MATCHING_CHECKS_PASS cases={len(cases)} enumerated_faces={total}')
if __name__=='__main__':run()
