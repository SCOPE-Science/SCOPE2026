"""Finite-support certificate for optimum power-domination slides on KG(n,2).
Run: python verify_slide_orbits.py (Python 3 standard library)."""
import itertools
import json
from collections import Counter, deque
from math import comb

PATTERNS = {
    (2,2,2): (0,1,2),
    (2,2,1,1): (0,1,6),
    (2,1,1,1,1): (0,1,18),
    (1,1,1,1,1,1): (0,13,22),
}

def count_types(edges, subset):
    c = Counter(v for index in subset for v in edges[index])
    return tuple(sorted(c.values(),reverse=True))

def maximum_direct_matching(src, tgt, bits):
    return max(sum((bits[a] & bits[b]) == 0 for a,b in zip(src,perm))
               for perm in itertools.permutations(tgt))

def verify(n):
    edges=list(itertools.combinations(range(n),2))
    masks=[sum(1 << x for x in e) for e in edges]
    N=len(edges)
    states=[]; by_state={}; reps={}; types=Counter()
    for s in itertools.combinations(range(N),3):
        kind=count_types(edges,s)
        if kind==(3,1,1,1): continue
        by_state[s]=len(states); states.append(s)
        types[kind]+=1; reps.setdefault(kind,s)
    expected={ (2,2,2):comb(n,3), (2,2,1,1):12*comb(n,4),
               (2,1,1,1,1):30*comb(n,5), (1,1,1,1,1,1):15*comb(n,6)}
    assert dict(types)==expected,(n,types,expected)
    assert len(states)==comb(N,3)-n*comb(n-1,3)
    partners=[[j for j in range(N) if not (masks[i]&masks[j])]
              for i in range(N)]
    adj=[]
    degrees={
       (2,2,2):3*comb(n-3,2),
       (2,2,1,1):3*comb(n-3,2)+(n-3),
       (2,1,1,1,1):3*comb(n-3,2)+2*(n-4),
       (1,1,1,1,1,1):3*comb(n-3,2)+3*(n-5)}
    for s in states:
        nbr=[]
        for ix,remove in enumerate(s):
            others=s[:ix]+s[ix+1:]
            for replace in partners[remove]:
                if replace in others: continue
                candidate=tuple(sorted(others+(replace,)))
                dest=by_state.get(candidate)
                if dest is not None:nbr.append(dest)
        assert len(nbr)==degrees[count_types(edges,s)],(n,s,len(nbr))
        adj.append(nbr)
    all_data={}
    for kind,source in reps.items():
        dist=[-1]*len(states);p=by_state[source];dist[p]=0
        queue=deque([p]);hist=Counter({0:1})
        while queue:
            x=queue.popleft()
            for y in adj[x]:
                if dist[y]<0:
                    dist[y]=dist[x]+1
                    hist[dist[y]]+=1
                    queue.append(y)
        assert min(dist)==0
        ecc=max(dist)
        assert ecc==(4 if kind==(2,2,2) else 5),(n,kind,ecc)
        for j,target in enumerate(states):
            if dist[j]!=5: continue
            assert not set(source).intersection(target)
            assert maximum_direct_matching(source,target,masks)<=1,(n,kind,source,target)
        # Reverse implication (each source/target pair with matching obstruction has distance 5)
        for j,target in enumerate(states):
            if set(source).isdisjoint(target):
                deficient=maximum_direct_matching(source,target,masks)<=1
                assert (dist[j]==5)==deficient,(n,kind,source,target,dist[j])
        all_data[str(kind)]={"orbit_size":types[kind],"degree":degrees[kind],
                             "eccentricity":ecc,"distance_histogram":dict(sorted(hist.items()))}
    return {"n":n,"states":len(states),"edges":sum(map(len,adj))//2,
            "types":all_data,"validation":"PASS"}

if __name__=='__main__':
    print(json.dumps({"proof_sizes":[verify(n) for n in range(8,13)],
                      "status":"PASS"},sort_keys=True,separators=(',',':')))
