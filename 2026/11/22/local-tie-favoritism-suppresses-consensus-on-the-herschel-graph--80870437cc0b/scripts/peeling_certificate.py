"""Independent finite-state verifier: edge-defined bitset update and Kahn peeling."""
from collections import Counter, deque
from itertools import combinations
EDGES = ((1,2),(1,4),(1,5),(2,3),(2,6),(2,7),(3,4),(3,8),
         (4,9),(4,10),(5,6),(5,10),(6,11),(7,8),(7,11),(8,9),
         (9,11),(10,11))
N=11; SIZE=1<<N
MASKS=[0]*N
for u,v in EDGES:
    MASKS[u-1]|=1<<(v-1)
    MASKS[v-1]|=1<<(u-1)
assert sorted(m.bit_count() for m in MASKS)==[3]*8+[4]*3

def transition(s,biased):
    out=0
    for i,m in enumerate(MASKS):
        c=(s&m).bit_count(); degree=m.bit_count()
        if (c*2>degree) or (c*2==degree and ((biased>>i)&1 or (s>>i)&1 and not (biased>>i)&1)):
            out|=1<<i
    return out

def census(biased):
    succ=[transition(s,biased) for s in range(SIZE)]
    indeg=[0]*SIZE
    for t in succ: indeg[t]+=1
    q=deque(s for s in range(SIZE) if not indeg[s]); peeled=[]
    while q:
        s=q.popleft();peeled.append(s)
        t=succ[s];indeg[t]-=1
        if indeg[t]==0:q.append(t)
    cycseen=set(); orbitrep={}; period=[0]*SIZE;depth=[0]*SIZE;rep=[-1]*SIZE
    for s in range(SIZE):
        if indeg[s] and s not in cycseen:
            orbit=[];u=s
            while u not in cycseen:
                cycseen.add(u);orbit.append(u);u=succ[u]
            assert u==s
            R=min(orbit)
            orbitrep[R]=orbit
            for t in orbit: period[t]=len(orbit);rep[t]=R
    for s in reversed(peeled):
        t=succ[s];rep[s]=rep[t]; period[s]=period[t];depth[s]=depth[t]+1
    assert all(p in (1,2) for p in period)
    hist=Counter(rep);fs=[r for r in orbitrep if len(orbitrep[r])==1]
    ts=[r for r in orbitrep if len(orbitrep[r])==2]
    return dict(fixed=len(fs),twos=len(ts),max_entry=max(depth),basin0=hist[0],basin1=hist[SIZE-1],fixed_basin=sum(hist[r] for r in fs),fixed_hist=sorted(Counter(hist[r] for r in fs).items()),two_hist=sorted(Counter(hist[r] for r in ts).items()), entries=sorted(Counter(zip(depth,period)).items()))

AUTOS=((10,4,9,11,5,1,3,8,7,6,2), (1,4,3,2,5,10,9,8,7,6,11))
# Each tuple is the image of vertices 1 through 11.
for p in AUTOS:
    assert sorted(p)==list(range(1,12))
    for u,v in EDGES:
        assert (MASKS[p[u-1]-1]>>(p[v-1]-1))&1
assert [p[i-1] for i in (2,4,11)]==[4,2,11]

if __name__=='__main__':
    groups={}
    for k in range(4):
        for B in combinations((2,4,11),k):
            x=sum(1<<(v-1) for v in B)
            c=census(x)
            if k in groups: assert c==groups[k], (B,c,groups[k])
            groups[k]=c
            print(k,B, {a:c[a] for a in ('fixed','twos','max_entry','basin0','basin1','fixed_basin')})
    print('checked all 8 intervention subsets and all 2048 states per subset')
