"""Exact finite checks for the perfect-matching edge-deletion theorem.
Standard-library Python 3. No external data or dependencies.
"""
from collections import Counter
from itertools import combinations
import heapq


def perfect_matchings(n, removed_spoke=True):
    """Edge-indexed perfect matchings of the 2n-cycle with antipodal chords."""
    nn=2*n
    edges={tuple(sorted((i,(i+1)%nn))) for i in range(nn)}
    edges.update((i,i+n) for i in range(n) if not removed_spoke or i!=0)
    edges=tuple(sorted(edges))
    adj={i:[] for i in range(nn)}
    for j,(a,b) in enumerate(edges):
        adj[a].append((j,b));adj[b].append((j,a))
    def rec(avail):
        if not avail:
            yield frozenset();return
        a=min(avail)
        for e,b in adj[a]:
            if b in avail:
                for tail in rec(avail-{a,b}):
                    yield tail | {e}
    return edges, set(rec(set(range(nn))))


def ladder_pm(n,edge_lookup,start,end):
    """Perfect tilings of n-step strip columns [start,end] inclusive."""
    vertices=set(range(start,end+1))|set(range(start+n,end+n+1))
    adj={a:[] for a in vertices}
    for e,(a,b) in enumerate(edge_lookup):
        if a in vertices and b in vertices:
            adj[a].append((e,b));adj[b].append((e,a))
    def rec(avail):
        if not avail:
            yield frozenset();return
        a=min(avail)
        for e,b in adj[a]:
            if b in avail:
                for rest in rec(avail-{a,b}):
                    yield rest|{e}
    return set(rec(vertices))


def maximal(sets):
    return {s for s in sets if not any(s<t for t in sets)}


def allfaces(facets):
    allf={0}
    for f in facets:
        subs=[0]
        for e in f:
            subs += [s|(1<<e) for s in subs]
        allf.update(subs)
    return allf


def collapse_to_vertex(faces):
    """Greedy elementary simplicial collapses, checking unique cofaces."""
    live=set(faces)-{0}
    nb=max(live).bit_length()
    count={}
    for face in live:
        for b in range(face.bit_length()):
            if face>>b&1:
                sub=face^(1<<b)
                if sub:count[sub]=count.get(sub,0)+1
    free=[f for f in count if count[f]==1]
    heapq.heapify(free)
    pairs=0
    while free:
        f=heapq.heappop(free)
        if f not in live or count.get(f,0)!=1:continue
        cofaces=[f|(1<<i) for i in range(nb)
                 if not f>>i&1 and f|(1<<i) in live]
        assert len(cofaces)==1,(f,cofaces)
        g=cofaces[0]
        live.remove(f);live.remove(g);pairs+=1
        for h in (f,g):
            for i in range(h.bit_length()):
                if h>>i&1:
                    sub=h^(1<<i)
                    if sub in live:
                        count[sub]-=1
                        if count[sub]==1:heapq.heappush(free,sub)
    return live,pairs


def run():
    for n in (4,6,8,10,12):
        edges,pm=perfect_matchings(n)
        lookup={e:i for i,e in enumerate(edges)}
        front=(lookup[(0,1)],lookup[(n,n+1)])
        twist=(lookup[(0,2*n-1)],lookup[(n-1,n)])
        AA={f for f in pm if set(front)<=f}
        BB={f for f in pm if set(twist)<=f}
        assert AA and BB and AA.isdisjoint(BB)
        assert AA|BB==pm,(n,len(pm),len(AA|BB))
        assert all(front[0] in f if front[1] in f else front[1] not in f for f in pm)
        inner=ladder_pm(n,edges,2,n-2)
        overlap=maximal({f&g for f in AA for g in BB})
        assert overlap==inner,(n,len(overlap),len(inner),len(overlap^inner))
        # Independently test the two join decompositions.
        left=ladder_pm(n,edges,2,n-1)
        right=ladder_pm(n,edges,1,n-2)
        assert AA=={f|set(front) for f in left}
        assert BB=={f|set(twist) for f in right}
        assert len(inner)>0
        print('n=%d perfect_matchings=%d A=%d B=%d overlap_facets=%d'%(
            n,len(pm),len(AA),len(BB),len(inner)))
        if n<=10:
            ff=allfaces(pm)
            remain,pairs=collapse_to_vertex(ff)
            assert len(remain)==1 and next(iter(remain)).bit_count()==1
            assert 2*pairs+2==len(ff), (n,len(ff),pairs)
            print('  verified elementary collapses=%d; nonempty faces=%d; endpoint=one vertex'%(pairs,len(ff)-1))
    print('DEFECTIVE_MOBIUS_PERFECT_MATCHING_PASS')

if __name__=='__main__':run()
