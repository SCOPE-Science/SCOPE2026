"""Exact minimum-maximal-matching exchange enumeration for the Mobius-Kantor graph.
Standalone Python 3 standard-library verifier; every matching is enumerated once.
"""
from collections import Counter,deque
from itertools import combinations

def edge_set():
    n=8
    E=set()
    for i in range(n):
        for a,b in ((i,(i+1)%n),(i,n+i),(n+i,n+(i+3)%n)):
            E.add(tuple(sorted((a,b))))
    return sorted(E)

def compute():
    E=edge_set(); n=16; m=len(E)
    assert m==24 and len(set(E))==24
    edgebits=[(1<<a)|(1<<b) for a,b in E]
    options=[]
    def visit(i,used,chosen):
        if i==m:
            # A matching is maximal iff no graph edge has both ends unmatched.
            if all(used&mask for mask in edgebits):options.append(chosen)
            return
        visit(i+1,used,chosen)
        if not (used&edgebits[i]):visit(i+1,used|edgebits[i],chosen|(1<<i))
    visit(0,0,0)
    size_hist=Counter(t.bit_count() for t in options)
    assert size_hist=={6:176,7:336,8:33},size_hist
    states=sorted(t for t in options if t.bit_count()==6)
    idx={t:i for i,t in enumerate(states)}
    nbh=[set() for t in states]
    for i,t in enumerate(states):
        for a in range(m):
            if not t&(1<<a):continue
            rem=t^(1<<a)
            for b in range(m):
                if rem&(1<<b):continue
                other=rem|(1<<b)
                j=idx.get(other)
                if j is not None and j!=i:
                    # Necessary structural lemma: the replacements share an endpoint.
                    assert edgebits[a]&edgebits[b]
                    nbh[i].add(j)
    assert all(i in nbh[j] for i,row in enumerate(nbh) for j in row)
    nedge=sum(map(len,nbh))//2
    seen=set(); components=[]
    for s in range(len(states)):
        if s in seen:continue
        seen.add(s);q=[s]
        for u in q:
            for v in nbh[u]:
                if v not in seen:seen.add(v);q.append(v)
        components.append(q)
    cycles=[q for q in components if len(q)>1]
    assert len(cycles)==6 and all(len(c)==16 for c in cycles)
    assert all(len(nbh[v])==2 for c in cycles for v in c)
    assert Counter(map(len,components))=={1:80,16:6}
    ecc=Counter()
    for c in cycles:
        for s in c:
            dist={s:0};q=deque([s])
            while q:
                u=q.popleft()
                for v in nbh[u]:
                    if v not in dist:
                        dist[v]=dist[u]+1;q.append(v)
            assert len(dist)==16
            ecc[max(dist.values())]+=1
    assert ecc=={8:96} and nedge==96
    print('GRAPH_VERTICES=16 GRAPH_EDGES=24')
    print('MAXIMAL_MATCHINGS_BY_SIZE='+str(sorted(size_hist.items())))
    print('MINIMUM_MAXIMAL_SIZE=6 MINIMUM_MATCHINGS=176')
    print('SINGLE_EDGE_EXCHANGES=96')
    print('COMPONENTS='+str(sorted(Counter(map(len,components)).items())))
    print('NONTRIVIAL_COMPONENTS_SIX_C16=True')
    print('NONTRIVIAL_ECCENTRICITIES='+str(sorted(ecc.items())))
    print('ALL_EXCHANGES_SHARE_ENDPOINT=True')
    print('VERIFY_OK')
if __name__=='__main__':compute()
