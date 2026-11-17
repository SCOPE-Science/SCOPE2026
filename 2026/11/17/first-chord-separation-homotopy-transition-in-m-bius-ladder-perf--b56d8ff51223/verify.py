"""Exact certificate for double-chord deletion in small Möbius ladders.
Python 3 standard library. Run from the folder with collapse_certificate.json.
"""
import itertools
import json
from collections import defaultdict
from pathlib import Path


def graph(n, separation):
    vertices = tuple(range(2*n))
    edges = {tuple(sorted((i,(i+1)%(2*n)))) for i in vertices}
    edges.update((i,n+i) for i in range(n) if i not in (0,separation))
    return vertices, tuple(sorted(edges))


def perfect_matchings_by_subsets(vertices, edges):
    result=set()
    for chosen in itertools.combinations(edges,len(vertices)//2):
        used=[v for e in chosen for v in e]
        if len(set(used))==len(vertices):
            result.add(frozenset(chosen))
    return result


def perfect_matchings_by_backtracking(vertices, edges):
    incidence={v:[] for v in vertices}
    for e in edges:
        for v in e: incidence[v].append(e)
    def rec(remaining):
        if not remaining:
            yield frozenset()
            return
        a=min(remaining)
        for e in incidence[a]:
            b=e[1] if e[0]==a else e[0]
            if b in remaining:
                for tail in rec(remaining-{a,b}):
                    yield tail|frozenset((e,))
    return set(rec(set(vertices)))


def all_faces(facets):
    faces={frozenset()}
    for facet in facets:
        ff=tuple(sorted(facet))
        for r in range(1,len(ff)+1):
            for s in itertools.combinations(ff,r):faces.add(frozenset(s))
    return faces


def encode(face):
    return [list(e) for e in sorted(face)]


def decode(obj):
    return frozenset(tuple(e) for e in obj)


def make_certificate(n,separation):
    vertices,edges=graph(n,separation)
    facets=perfect_matchings_by_backtracking(vertices,edges)
    faces=all_faces(facets)
    rem=set(faces)
    pairs=[]
    while True:
        candidates=sorted((f for f in rem if len(f)>=3),key=lambda f:(-len(f),tuple(sorted(f))))
        selected=None
        for coface in candidates:
            for edge in sorted(coface):
                lower=coface-{edge}
                if sum(1 for f in rem if lower < f)==1:
                    selected=(lower,coface)
                    break
            if selected:break
        if selected is None:break
        lower,coface=selected
        rem.remove(lower);rem.remove(coface)
        pairs.append([encode(lower),encode(coface)])
    assert all(len(f)<=2 for f in rem)
    return {'n':n,'separation':separation,'pairs':pairs,
            'end_faces':[encode(f) for f in sorted(rem,key=lambda f:(len(f),tuple(sorted(f))))]}


def graph_betti(faces):
    vertices={next(iter(f)) for f in faces if len(f)==1}
    edges=[f for f in faces if len(f)==2]
    p={v:v for v in vertices}
    def root(x):
        while p[x]!=x:x=p[x]
        return x
    for edge in edges:
        a,b=tuple(edge)
        p[root(a)]=root(b)
    components=len({root(v) for v in vertices})
    return len(vertices),len(edges),components,len(edges)-len(vertices)+components


def replay(cert):
    n,sep=cert['n'],cert['separation']
    vertices,edges=graph(n,sep)
    backtrack=perfect_matchings_by_backtracking(vertices,edges)
    subsets=perfect_matchings_by_subsets(vertices,edges)
    assert backtrack==subsets
    active=all_faces(backtrack)
    original=len(active)
    for lower_js,upper_js in cert['pairs']:
        lo,up=decode(lower_js),decode(upper_js)
        assert len(up)==len(lo)+1 and lo<up
        assert lo in active and up in active
        assert all(not (lo<f) or f==up for f in active if f!=up)
        active.remove(lo); active.remove(up)
    remaining={decode(f) for f in cert['end_faces']}
    assert remaining==active
    assert len(remaining)==original-2*len(cert['pairs'])
    assert max(map(len,remaining))<=2
    v,e,c,b=graph_betti(remaining)
    result={'n':n,'distance':sep,'perfect_matchings':len(backtrack),
            'original_faces_including_empty':original,'verified_collapse_pairs':len(cert['pairs']),
            'final_vertices':v,'final_edges':e,'components':c,'cycle_rank':b}
    print(json.dumps(result,sort_keys=True))
    return result


def main():
    records=json.loads(Path(__file__).with_name('collapse_certificate.json').read_text(encoding='utf-8'))
    assert [(x['n'],x['separation']) for x in records]==[(3,1),(4,1),(4,2),(5,1),(5,2)]
    results=[replay(x) for x in records]
    assert [(r['components'],r['cycle_rank']) for r in results] == [(1,0),(2,0),(2,0),(1,2),(1,0)]
    print('DOUBLE_CHORD_MOBIUS_MATCHING_HOMOTOPY_PASS')

if __name__=='__main__':main()
