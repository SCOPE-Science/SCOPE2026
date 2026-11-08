#!/usr/bin/env python3
"""Exact sign-incidence tests for generic central sections of type-D root polytopes."""
from itertools import combinations, product
from collections import Counter, defaultdict

def roots(d):
    return [tuple((a if k==i else b if k==j else 0) for k in range(d))
            for i,j in combinations(range(d),2) for a,b in product((-1,1),repeat=2)]

def dot(a,b): return sum(x*y for x,y in zip(a,b))

def enumerate_section(d, u):
    R=roots(d)
    assert sorted(map(abs,u),reverse=True)==list(map(abs,u)) and len(set(map(abs,u)))==d
    signed=[dot(u,r) for r in R]
    assert all(s !=0 for s in signed)
    edges=[(p,q) for p in range(len(R)) for q in range(p+1,len(R)) if dot(R[p],R[q])==1]
    crossing=[(p,q) for p,q in edges if signed[p]*signed[q]<0]
    facets=[]
    for i in range(d):
        for e in (-1,1):
            members={j for j,r in enumerate(R) if e*r[i]==1}
            inc={k for k,(p,q) in enumerate(crossing) if p in members and q in members}
            if inc: facets.append((("coord",i,e),inc))
    for signs in product((-1,1),repeat=d):
        members={j for j,r in enumerate(R) if dot(signs,r)==2}
        inc={k for k,(p,q) in enumerate(crossing) if p in members and q in members}
        if inc: facets.append((("signed",signs),inc))
    assert len(crossing)==4*d*(d-1)*(d-2)//3,(d,len(crossing))
    assert len(facets)==2**d+2*d-6,(d,len(facets))
    assert all(len(inc)>=d-1 for _,inc in facets)
    return crossing,facets

def main():
    for d in range(4,8):
        u=[2**(d-i-1) for i in range(d)]
        cross,facets=enumerate_section(d,u)
        print('d',d,'vertices',len(cross),'facets',len(facets),'facet_vertex_spectrum',dict(sorted(Counter(len(inc) for _,inc in facets).items())))
        if d==4:
            quads=[inc for label,inc in facets if len(inc)==4]
            hexes=[inc for label,inc in facets if len(inc)==6]
            assert len(quads)==6 and len(hexes)==12
            # Two section facets meet along an edge exactly when they share two section vertices.
            assert all(len(quads[i]&quads[j])==0 for i in range(6) for j in range(i+1,6))
            links=[]
            for h in hexes:
                touching=[i for i,Q in enumerate(quads) if len(Q&h)==2]
                assert len(touching)==2,touching
                links.append(tuple(touching))
            assert len(set(links))==12
            assert sorted(sum(i in edge for edge in links) for i in range(6))==[4]*6
            incidence=Counter(k for _,face in facets for k in face)
            assert len(incidence)==32 and set(incidence.values())=={3}
            edge_pairs=[(a,b) for a,b in combinations(range(len(facets)),2) if len(facets[a][1]&facets[b][1])==2]
            assert len(edge_pairs)==48
            missing={tuple(pair) for pair in combinations(range(6),2)}-set(links)
            assert len(missing)==3 and len({i for pair in missing for i in pair})==6
            print('d4 hexagon-induced square-links',sorted(links))
        # independent check of sign stability under a new strictly decreasing coordinate vector
        other=[10**(d-i-1) for i in range(d)]
        assert [len(x) for x in (cross,facets)]==[len(x) for x in enumerate_section(d,other)]
    print('D_ROOT_GENERIC_SECTION_EXACT_COUNTS_OK')

if __name__=='__main__': main()
