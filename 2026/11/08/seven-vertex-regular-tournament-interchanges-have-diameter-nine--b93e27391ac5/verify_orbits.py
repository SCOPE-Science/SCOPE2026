#!/usr/bin/env python3
"""Exact independent row-constrained enumeration of seven-player regular tournaments."""
from itertools import combinations, permutations
from collections import Counter, deque

N=7
pairs=list(combinations(range(N),2))
bit={xy:i for i,xy in enumerate(pairs)}
triangles=list(combinations(range(N),3))
full=(1<<len(pairs))-1

def regular_masks():
    scores=[0]*N
    def build(i, code):
        if i==N:
            if scores==[3]*N: yield code
            return
        later=range(i+1,N)
        required=3-scores[i]
        if not (0<=required<=N-1-i):return
        for winners in combinations(later,required):
            wins=set(winners)
            losers=[j for j in later if j not in wins]
            if any(scores[j]>=3 for j in losers):continue
            for j in losers:scores[j]+=1
            original=scores[i]; scores[i]=3
            added=sum(1<<bit[i,j] for j in winners)
            yield from build(i+1,code|added)
            scores[i]=original
            for j in losers:scores[j]-=1
    return sorted(set(build(0,0)))

def arc(mask,i,j):
    if i<j:return bool(mask & (1<<bit[i,j]))
    return not bool(mask & (1<<bit[j,i]))

def neighbors(mask):
    for i,j,k in triangles:
        if arc(mask,i,j) and arc(mask,j,k) and arc(mask,k,i) or \
           arc(mask,i,k) and arc(mask,k,j) and arc(mask,j,i):
            yield mask^((1<<bit[i,j])|(1<<bit[i,k])|(1<<bit[j,k]))

def orbit(mask):
    for p in permutations(range(N)):
        t=0
        for a,b in pairs:
            x,y=p[a],p[b]
            if (arc(mask,a,b) if x<y else arc(mask,b,a)):
                u,v=sorted((x,y));t|=1<<bit[u,v]
        yield t

def distances(source,adj):
    q=deque((source,));dist={source:0}
    while q:
        u=q.popleft()
        for v in adj[u]:
            if v not in dist:
                dist[v]=dist[u]+1;q.append(v)
    return dist

def main():
    states=regular_masks()
    assert len(states)==2640
    maskset=set(states)
    adj={m:set(neighbors(m)) for m in states}
    assert all(len(x)==14 for x in adj.values())
    assert all(all(y in maskset and x in adj[y] for y in adj[x]) for x in states)
    assert sum(map(len,adj.values()))//2==18480
    remaining=set(states);classes=[];pair_dist=Counter();d_pairs=0
    while remaining:
        rep=min(remaining)
        members=set(orbit(rep));assert members<=maskset
        remaining-=members
        d=distances(rep,adj);assert len(d)==len(states)
        h=Counter(d.values());ecc=max(h);maxv=[x for x,v in d.items() if v==ecc]
        classes.append((len(members),rep,ecc,h,len(maxv)))
        for length,count in h.items():pair_dist[length]+=len(members)*count
        if len(members)==720:
            assert ecc==9 and maxv==[rep^full]
            d_pairs+=len(members)
    assert sorted(s for s,*_ in classes)==[240,720,1680]
    assert sorted((size,ecc) for size,_,ecc,_,_ in classes)==[(240,8),(720,9),(1680,8)]
    profiles={
        720:[1,14,91,336,721,822,485,147,22,1],
        1680:[1,14,91,340,739,853,483,113,6],
        240:[1,14,91,343,749,871,476,92,3],
    }
    assert all([h[d] for d in range(ecc+1)]==profiles[size] for size,_,ecc,h,_ in classes)
    assert [pair_dist[d]//2 for d in range(1,10)]==[18480,120120,447720,970200,1116960,637440,158880,13320,360]
    assert pair_dist[9]==720
    assert sum(pair_dist.values())==len(states)**2
    print('PYTHON_INDEPENDENT_PASS', len(states),sum(map(len,adj.values()))//2)
    for size,rep,ecc,h,num in classes:
        print('ORBIT',size,rep,'ecc',ecc,'farthest',num,'layers',','.join(map(str,(h[i] for i in range(ecc+1)))))
    print('UNORDERED_DISTANCES',','.join(str(pair_dist[i]//2) for i in range(1,10)))
    print('DIAMETRAL_PAIRS', d_pairs//2)

if __name__=='__main__':main()
