#!/usr/bin/env python3
"""Exhaustive finite-state functional-graph census for two excitable dynamics."""
import itertools, collections, json
from pathlib import Path

PAIRS=list(itertools.combinations(range(5),2)); N=3**len(PAIRS)
NEI=[[j for j,f in enumerate(PAIRS) if i!=j and (e[0] in f or e[1] in f)] for i,e in enumerate(PAIRS)]
POW=[3**i for i in range(10)]
assert len(NEI)==10 and all(len(v)==6 for v in NEI)

def nxt(z,kind):
    a=[z//v%3 for v in POW]; out=0
    for i,c in enumerate(a):
        if kind=='cca':
            d=(c+1)%3 if any(a[j]==(c+1)%3 for j in NEI[i]) else c
        else:
            d=(c+1)%3 if c!=0 else int(any(a[j]==1 for j in NEI[i]))
        out+=POW[i]*d
    return out

def classify(kind):
    succ=[nxt(z,kind) for z in range(N)]
    indeg=[0]*N
    for z in succ: indeg[z]+=1
    q=collections.deque(i for i in range(N) if indeg[i]==0)
    order=[]
    while q:
        a=q.popleft(); order.append(a); indeg[succ[a]]-=1
        if indeg[succ[a]]==0:q.append(succ[a])
    t=[-1]*N;p=[0]*N;cyclelist=[]
    for k in range(N):
        if indeg[k]==0 or t[k]>=0:continue
        path=[]; v=k
        while t[v]<0:
            t[v]=0;path.append(v);v=succ[v]
        assert v==k
        for v in path:p[v]=len(path)
        cyclelist.append((len(path),min(path)))
    for a in reversed(order):
        t[a]=t[succ[a]]+1;p[a]=p[succ[a]]
    assert all(a>=0 for a in t) and len(order)+sum(x for x,_ in cyclelist)==N
    return succ,t,p,cyclelist

def main():
    a=classify('cca'); b=classify('ghm')
    tables=[]
    for name,v in (('cca',a),('ghm',b)):
        hist=collections.Counter(zip(v[1],v[2])); orbits=collections.Counter(k for k,_ in v[3]);
        tables.append((name,sorted([[k[0],k[1],count] for k,count in hist.items()]),sorted([[k,count] for k,count in orbits.items()])))
    assert a[2]==b[2]
    assert tables[0][1]==[[0,1,3],[0,3,30240],[1,1,2916],[1,3,20370],[2,1,480],[2,3,5040]]
    assert tables[1][1]==[[0,1,1],[0,3,30240],[1,1,1023],[1,3,6700],[2,1,1133],[2,3,8470],[3,1,1082],[3,3,8560],[4,1,160],[4,3,1680]]
    assert tables[0][2]==[[1,3],[3,10080]] and tables[1][2]==[[1,1],[3,10080]]
    cyc1={i for i in range(N) if a[1][i]==0 and a[2][i]==3};cyc2={i for i in range(N) if b[1][i]==0 and b[2][i]==3}
    assert cyc1==cyc2 and len(cyc1)==30240
    for i in cyc1:
        assert a[0][i]==b[0][i]
    for i in range(N):
        cond=all(any(((i//POW[j])%3)==(((i//POW[v])%3+1)%3) for j in NEI[v]) for v in range(10))
        assert cond==(i in cyc1)
    obj={'graph':'T(5)=L(K5)','vertex_order':[list(p) for p in PAIRS],'number_of_initial_states':N,
         'cca':{'entry_period_counts':tables[0][1],'primitive_cycles':tables[0][2]},
         'ghm':{'entry_period_counts':tables[1][1],'primitive_cycles':tables[1][2]},
         'pointwise_period_equal':True,'shared_primitive_three_cycle_states':len(cyc1),
         'shared_primitive_three_cycle_transitions':True}
    if __name__=='__main__':
        dest=Path(__file__).resolve().parent.parent/'data'/'census.json'
        if dest.exists():assert json.loads(dest.read_text())==obj
        print('CENSUS_ALL_59049_OK')
    return obj

if __name__=='__main__':main()
