#!/usr/bin/env python3
"""Self-contained exact finite core for an all-order combinatorial collapse."""
from itertools import combinations

# Ground elements 0,1,2,3,4; the removed Kneser edge is 01--23.
# Each line is (lower face, vertex to adjoin to obtain its unique cofacet).
LOCAL_STEPS = [
    (('01','14','23','34'),'13'),
    (('01','14','23','24'),'12'),
    (('01','04','23','24'),'02'),
    (('01','13','23','34'),'03'),
    (('01','02','04','23'),'03'),
    (('01','04','23','34'),'03'),
    (('01','04','23'),'03'),
    (('01','23','34'),'03'),
    (('01','12','23','24'),'02'),
    (('01','13','14','23'),'12'),
    (('01','14','23'),'12'),
    (('01','23','24'),'02'),
]

def pair_vertices(n):
    return list(combinations(range(n),2))

def face_sets(n, deleted=False):
    vertices=pair_vertices(n)
    adj=[0]*len(vertices)
    for i in range(len(vertices)):
        for j in range(i+1,len(vertices)):
            if not (set(vertices[i]) & set(vertices[j])):
                if deleted and vertices[i]==(0,1) and vertices[j]==(2,3):
                    continue
                adj[i]|=1<<j
                adj[j]|=1<<i
    return {s for s in range(1<<len(vertices))
            if all((adj[i]&s).bit_count()<=1
                   for i in range(len(vertices)) if s&(1<<i))}

def check(n):
    vertices=pair_vertices(n)
    idx={p:i for i,p in enumerate(vertices)}
    old=face_sets(n)
    new=face_sets(n,True)
    fresh=new-old
    assert old<=new
    assert len(fresh)==24*(n-4), (n,len(fresh))
    assert all((s&(1<<idx[0,1])) and (s&(1<<idx[2,3])) for s in fresh)
    # Prove that the new faces partition into 24-face, five-label fibers.
    for s in fresh:
        outside={x for j,p in enumerate(vertices) if s>>j&1 for x in p if x>=4}
        assert len(outside)==1, (n,s,outside)
    core=face_sets(5,True)-face_sets(5)
    assert len(core)==24
    fibers=set()
    for w in range(4,n):
        for s in core:
            mapped=0
            for i,p in enumerate(pair_vertices(5)):
                if s>>i&1:
                    mapped|=1<<idx[tuple(sorted(w if x==4 else x for x in p))]
            assert mapped not in fibers
            fibers.add(mapped)
    assert fibers==fresh
    # Validate elementary simplicial collapses in the specified order.
    # A free lower face is contained in exactly one strict coface, its upper mate.
    current=set(new)
    for w in range(4,n):
        for lower, extra in LOCAL_STEPS:
            lab=lambda x:tuple(sorted(w if int(t)==4 else int(t) for t in x))
            a=sum(1<<idx[lab(x)] for x in lower)
            b=a|(1<<idx[lab(extra)])
            assert a in current and b in current and a not in old and b not in old
            cofaces=[s for s in current if s!=a and s&a==a]
            assert cofaces==[b], (n,w,lower,cofaces)
            current.remove(a);current.remove(b)
    assert current==old
    return len(old),len(new),len(fresh),len(LOCAL_STEPS)*(n-4)

def main():
    for n in (5,6,7):
        a,b,c,d=check(n)
        print(f'n={n}: intact_faces={a}, fault_faces={b}, extra_faces={c}, free_face_pairs={d}: PASS')
    print('UNIVERSAL_5_LABEL_COLLAPSE_CORE_PASS')

if __name__=='__main__':
    main()
