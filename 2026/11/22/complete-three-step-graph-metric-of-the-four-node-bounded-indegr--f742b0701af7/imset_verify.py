"""Exact elementary verification of a finite polytope graph metric.
Usage: python imset_verify.py [imset_certs.json]. Only Python standard library.
"""
from itertools import product, combinations
from collections import Counter, deque
import json, sys, pathlib

def vertices():
    pairs=list(combinations(range(4),2)); triples=list(combinations(range(4),3))
    found={}
    for directions in product((-1,0,1),repeat=6):
        pars=[set() for _ in range(4)]
        for (u,v),direction in zip(pairs,directions):
            if direction==1:pars[v].add(u)
            elif direction==-1:pars[u].add(v)
        if any(len(s)>2 for s in pars):continue
        closure=[set(s) for s in pars]
        for _ in range(4):
            for v in range(4):
                closure[v].update(set().union(*(closure[w] for w in tuple(closure[v]))) if closure[v] else set())
        if any(v in closure[v] for v in range(4)):continue
        q=tuple(int(any(set(S)-{v} <= pars[v] for v in S)) for S in pairs+triples)
        found[q]=found.get(q,0)+1
    assert sum(found.values())==443
    assert len(found)==150
    return list(found)

def verify(certfile):
    V=vertices(); n=len(V); m=len(V[0]); C=json.load(open(certfile,encoding='utf8'))
    assert C['n']==n and C['dimension']==m
    A=[set() for _ in range(n)]; seen=set()
    for i,j,c in C['edges']:
        assert 0<=i<j<n and (i,j) not in seen
        seen.add((i,j)); A[i].add(j); A[j].add(i)
        same=[k for k in range(m) if V[i][k]==V[j][k]]
        diff=[k for k in range(m) if V[i][k]!=V[j][k]]
        assert len(c) in (0,len(diff))
        other=[z for z in range(n) if z not in (i,j) and all(V[z][k]==V[i][k] for k in same)]
        if not c: assert not other
        else:
            assert sum(c)==0
            for z in other:
                assert sum(a*(V[z][k] if V[i][k]==0 else 1-V[z][k]) for a,k in zip(c,diff))<0,(i,j,z)
    for i,j,den,terms in C['nonedges']:
        assert 0<=i<j<n and (i,j) not in seen and den>0
        seen.add((i,j))
        assert len(terms)>0 and sum(num for z,num in terms)==den
        assert all(z not in (i,j) and 0<=z<n and num>0 for z,num in terms)
        for k in range(m):
            assert 2*sum(num*V[z][k] for z,num in terms)==den*(V[i][k]+V[j][k]),(i,j,k)
    assert len(seen)==n*(n-1)//2
    assert len(C['edges'])==2508
    dists=Counter(); diameter=0; ecc=[]
    for source in range(n):
        dist={source:0}; queue=deque([source])
        while queue:
            v=queue.popleft()
            for w in A[v]:
                if w not in dist:
                    dist[w]=dist[v]+1;queue.append(w)
        assert len(dist)==n
        ecc.append(max(dist.values()))
        for j in range(source+1,n):
            dists[dist[j]]+=1;diameter=max(diameter,dist[j])
    assert dists=={1:2508,2:7666,3:1001}
    assert diameter==3
    assert Counter(ecc)=={3:150}
    degrees=Counter(map(len,A))
    assert degrees=={14:3,15:4,16:6,18:1,20:12,25:12,27:12,29:6,30:40,42:12,47:6,49:24,50:12}
    assert sum(k*v for k,v in dists.items())==20843
    print('PASS 150 vertices; 2508 edges; distances (1:2508, 2:7666, 3:1001); diameter 3')
    print('PASS exhaustive exact integer/rational edge and nonedge certificates for all 11175 unordered pairs')
    print('Degree multiplicities:',sorted(Counter(map(len,A)).items()))
if __name__=='__main__':
    certfile=sys.argv[1] if len(sys.argv)>1 else str(pathlib.Path(__file__).with_name('imset_certs.json'))
    verify(certfile)
