#!/usr/bin/env python3
"""Direct base-three transition and full functional graph classification for two small Paley graphs."""
from collections import Counter,defaultdict

def graph(q):
    if q==5:
        return [[j for j in range(q) if j!=i and (j-i)%q in (1,4)] for i in range(q)]
    if q==9:
        return [[j for j in range(9) if i!=j and (i//3==j//3 or i%3==j%3)] for i in range(9)]
    raise ValueError(q)

def update(k,g,q):
    a=[];x=k
    for i in range(q):
        a.append(x%3);x//=3
    b=[]
    for i,ns in enumerate(g):
        if a[i]==1:b.append(2)
        elif a[i]==2:b.append(0)
        else:b.append(int(sum(a[j]==1 for j in ns)>=len(ns)//2))
    return sum(v*3**i for i,v in enumerate(b))

def classify(q):
    N=3**q;g=graph(q);edge=sum(len(v) for v in g)//2
    assert edge==q*(q-1)//4
    trans=[update(i,g,q) for i in range(N)]
    done=bytearray(N);depth=[0]*N;period=[0]*N;root=[-1]*N;cycs=[]
    for r in range(N):
        if done[r]:continue
        seq=[];pos={};v=r
        while not done[v] and v not in pos:
            pos[v]=len(seq);seq.append(v);v=trans[v]
        if v in pos:
            j=pos[v];p=len(seq)-j;rr=min(seq[j:]);cycs.append((rr,p))
            for w in seq[j:]:done[w]=1;period[w]=p;root[w]=rr
            seq=seq[:j]
        for w in seq[::-1]:
            done[w]=1;depth[w]=depth[trans[w]]+1;period[w]=period[trans[w]];root[w]=root[trans[w]]
    count=Counter((depth[i],period[i]) for i in range(N))
    basins=Counter(root)
    print('q',q,'states',N,'cycles',dict(sorted(Counter(p for _,p in cycs).items())),
          'max_depth',max(depth),'entry_period',sorted((list(k),v) for k,v in count.items()),
          'cycle_basin',sorted((r,p,basins[r]) for r,p in cycs))
    if q==5:
        assert Counter(p for _,p in cycs)=={1:1,5:2}
        assert Counter(basins.values())=={153:1,45:2}
        assert max(depth)==4
        assert [sum(count[d,p] for p in (1,5)) for d in range(5)]==[11,61,91,50,30]
    else:
        assert Counter(p for _,p in cycs)=={1:1,3:4}
        assert Counter(basins.values())=={19671:1,3:4}
        assert max(depth)==5
        assert [sum(count[d,p] for p in (1,3)) for d in range(6)]==[13,511,5641,9990,3438,90]
    return count

if __name__=='__main__':
    classify(5);classify(9)
    print('FORWARD_OK')
