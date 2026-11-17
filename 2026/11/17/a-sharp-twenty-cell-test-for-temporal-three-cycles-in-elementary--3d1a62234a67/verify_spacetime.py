"""Independent 3-row spacetime column graph, no seven-bit window evaluator."""
import json
from collections import Counter, deque


def minimum_three(rule):
    # A vertex encodes a consecutive pair of time-columns a,b, each in 0..7.
    # Edge (a,b)->(b,c) iff b^1=f(a^0,b^0,c^0),
    # b^2=f(a^1,b^1,c^1), b^0=f(a^2,b^2,c^2).
    edges=[[] for _ in range(64)]
    for a in range(8):
        for b in range(8):
            for c in range(8):
                valid=True
                for t in range(3):
                    pattern=(((a>>t)&1)<<2)|(((b>>t)&1)<<1)|((c>>t)&1)
                    if (rule>>pattern)&1 != ((b>>((t+1)%3))&1):
                        valid=False;break
                if valid:
                    edges[8*a+b].append((8*b+c, (b&1)!=((b>>1)&1)))
    best=None
    for u in range(64):
        for v,mark in edges[u]:
            if not mark:continue
            dist=[-1]*64
            dist[v]=0
            todo=deque([v])
            while todo:
                w=todo.popleft()
                if w==u:break
                for nxt,_ in edges[w]:
                    if dist[nxt]<0:
                        dist[nxt]=dist[w]+1
                        todo.append(nxt)
            if dist[u]>=0:
                candidate=dist[u]+1
                if best is None or candidate<best: best=candidate
    return best


def produce():
    minima=[minimum_three(r) for r in range(256)]
    counts=Counter(minima)
    return {'minimum_ring_length':minima,
            'distribution':{str(k):counts[k] for k in sorted(counts,key=lambda x:(x is None,x or 0))},
            'max_finite_minimum':max(k for k in minima if k is not None),
            'maximizers':[i for i,m in enumerate(minima) if m==max(k for k in minima if k is not None)],
            'number_witnessed_rules':sum(k is not None for k in minima)}

if __name__=='__main__':
    print(json.dumps(produce(),sort_keys=True,separators=(',',':')))
