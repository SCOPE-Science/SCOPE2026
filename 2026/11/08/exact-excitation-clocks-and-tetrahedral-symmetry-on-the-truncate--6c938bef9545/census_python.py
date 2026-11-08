"""Independent forward-path census for three-state GHM on the truncated tetrahedron.
The vertex set comprises directed arcs of K4. This uses path memoization rather
than indegree pruning; only the Python standard library is required.
"""
from array import array
from collections import Counter
from itertools import permutations
import json

ARCS = [(a,b) for a in range(4) for b in range(4) if a!=b]
INDEX = {x:i for i,x in enumerate(ARCS)}
NEIGH = [[INDEX[(b,a)]] + [INDEX[(a,c)] for c in range(4) if c!=a and c!=b] for a,b in ARCS]
P3=[3**i for i in range(12)]
N=3**12
assert len(ARCS)==12 and len({tuple(sorted((i,j))) for i in range(12) for j in NEIGH[i]})==18

def step(s):
    digs=[]; x=s
    for _ in range(12):
        digs.append(x%3);x//=3
    out=0
    for i,d in enumerate(digs):
        if d==1: z=2
        elif d==2: z=0
        else: z=int(any(digs[j]==1 for j in NEIGH[i]))
        out+=z*P3[i]
    return out

# All paths are explored until they hit an assigned terminal node or repeat.
period=array('i',[0])*N
entry=array('i',[-1])*N
minrep=array('i',[-1])*N
nxt=array('i',[-1])*N
cycles=Counter()
for s in range(N):
    if entry[s]!=-1:continue
    path=[];local={};cur=s
    while entry[cur]==-1 and cur not in local:
        local[cur]=len(path);path.append(cur)
        nxt[cur]=step(cur)
        cur=nxt[cur]
    if entry[cur]==-1:
        start=local[cur];ring=path[start:]
        L=len(ring);r=min(ring)
        cycles[L]+=1
        for z in ring:period[z]=L;entry[z]=0;minrep[z]=r
        path=path[:start]
    for z in reversed(path):
        y=nxt[z]
        period[z]=period[y]
        entry[z]=entry[y]+1

hist=Counter((period[i],entry[i]) for i in range(N))
basin=Counter(period)
max_entry=max(entry)
max_pop=sum(t==max_entry for t in entry)

def transform(s,pi):
    q=0
    for i,(a,b) in enumerate(ARCS):
        q+=(s//P3[i]%3)*P3[INDEX[pi[a],pi[b]]]
    return q

classes={}
for L in (4,6,8):
    # Every periodic state has a canonical temporal representative.
    rs={minrep[i] for i in range(N) if entry[i]==0 and period[i]==L}
    groups=[]
    while rs:
        x=min(rs)
        orbit={minrep[transform(x,pi)] for pi in permutations(range(4))}
        assert orbit<=rs and len(orbit)>0
        rs-=orbit
        profile=[];z=x
        for i in range(L):
            profile.append(sum(z//p%3==1 for p in P3))
            z=nxt[z]
        assert z==x
        profile=min(profile[i:]+profile[:i] for i in range(L))
        # Count excitation occurrences over the whole cycle for each vertex.
        vertex_exc=[0]*12;z=x
        for _ in range(L):
            for i,p in enumerate(P3):vertex_exc[i]+=int((z//p)%3==1)
            z=nxt[z]
        groups.append({'representative':x,'size':len(orbit),'stabilizer':24//len(orbit),
                       'profile':profile,'vertex_excitation_counts':sorted(vertex_exc),
                       'cycle_representatives':sorted(orbit)})
    classes[str(L)]=groups

result={
 'cycle_counts':{str(L):int(c) for L,c in sorted(cycles.items())},
 'basin_counts':{str(L):int(c) for L,c in sorted(basin.items())},
 'max_transient':max_entry,'max_transient_population':max_pop,
 'time_period_counts':[[int(a),int(b),int(n)] for (a,b),n in sorted(hist.items())],
 'long_cycle_orbits':classes,
}
if __name__=='__main__':
    print(json.dumps(result,sort_keys=True,indent=2))
