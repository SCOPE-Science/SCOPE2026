"""Exhaustive 14-bit synchronous majority dynamics on the rhombic-dodecahedral graph.

Run: python3 verify_direct.py
All counts are for labelled configurations, with even-degree ties retained.
"""
from collections import Counter
from itertools import permutations

N=14
adj=[[] for _ in range(N)]
for v in range(8):
    for axis in range(3):
        f=8+2*axis+((v>>axis)&1)
        adj[v].append(f)
        adj[f].append(v)
assert [len(x) for x in adj]==[3]*8+[4]*6
assert sum(map(len,adj))==48

def step(state):
    result=0
    for v,nb in enumerate(adj):
        n=sum((state>>w)&1 for w in nb)
        bit=(n*2>len(nb)) if 2*n!=len(nb) else bool((state>>v)&1)
        result|=int(bit)<<v
    return result

size=1<<N
F=[step(x) for x in range(size)]
F2=[F[F[x]] for x in range(size)]
recurrent=[x for x in range(size) if F2[x]==x]
fixed=[x for x in recurrent if F[x]==x]
period2=[x for x in recurrent if F[x]!=x]
assert len(fixed)==46 and len(period2)==366
assert all(F[F[x]]==x for x in recurrent)
entry=Counter()
basins=Counter()
cycle_basins=Counter()
for x in range(size):
    y=x
    t=0
    while F2[y]!=y:
        y=F[y]
        t+=1
        assert t<=5
    period=1 if F[y]==y else 2
    entry[(t,period)]+=1
    basins[period]+=1
    cycle_basins[min(y,F[y])]+=1
assert sum(entry.values())==size
assert max(t for t,p in entry)==5
def iterate(x,t):
    for _ in range(t): x=F[x]
    return x
assert all(iterate(x,7)==iterate(x,5) for x in range(size))
assert any(iterate(x,6)!=iterate(x,4) for x in range(size))
assert [entry[(t,1)] for t in range(6)]==[46,2122,3360,2136,1368,192]
assert [entry[(t,2)] for t in range(6)]==[366,4682,1536,480,96,0]
assert basins=={1:9224,2:7160}
fixed_basin_hist=Counter(cycle_basins[x] for x in fixed)
two_basin_hist=Counter(cycle_basins[x] for x in period2 if x<F[x])
assert fixed_basin_hist=={13:12,73:24,74:8,3362:2}
assert two_basin_hist=={2:16,6:12,10:6,14:48,27:48,28:12,78:24,139:16,596:1}

# The full 48-element octahedral symmetry group of the cube/face incidence graph.
autos=[]
for axisperm in permutations(range(3)):
    for flip in range(8):
        sigma=[0]*N
        for v in range(8):
            sigma[v]=sum(((((v>>j)&1)^((flip>>j)&1)))<<axisperm[j] for j in range(3))
        for j in range(3):
            for b in range(2):
                sigma[8+2*j+b]=8+2*axisperm[j]+(b^((flip>>j)&1))
        assert sorted(sigma)==list(range(N))
        assert all(sorted(sigma[j] for j in adj[i])==sorted(adj[sigma[i]]) for i in range(N))
        autos.append(tuple(sigma))
assert len(set(autos))==48

def move(x,sigma):
    return sum(1<<sigma[j] for j in range(N) if (x>>j)&1)

def geometric_classes(phase_reps,as_cycle=False):
    unknown=set(phase_reps)
    answer=[]
    while unknown:
        r=min(unknown)
        members=set()
        for a in autos:
            y=move(r,a)
            members.add(min(y,F[y]) if as_cycle else y)
        assert members <= set(phase_reps)
        unknown-=members
        answer.append((r,len(members)))
    return answer

fg=geometric_classes(fixed)
cycles={min(x,F[x]) for x in period2}
cg=geometric_classes(cycles,True)
assert len(fg)==6 and sorted(n for x,n in fg)==[1,1,8,12,12,12]
assert len(cg)==13 and sum(n for x,n in cg)==183
assert 255 in cycles and cycle_basins[255]==596
print('vertices=14 edges=24 automorphisms=48 states=16384')
print('fixed=46 primitive_two_states=366 primitive_two_orbits=183')
print('geometric_fixed_classes=6 geometric_two_cycle_classes=13')
print('entry_fixed='+','.join(str(entry[(t,1)]) for t in range(6)))
print('entry_two='+','.join(str(entry[(t,2)]) for t in range(6)))
print('basin_fixed=9224 basin_two=7160 sharp_entry=5')
print('fixed_basin_sizes='+str(sorted(fixed_basin_hist.items())))
print('two_cycle_basin_sizes='+str(sorted(two_basin_hist.items())))
print('fixed_symmetry='+str(fg))
print('two_cycle_symmetry='+str(cg))
a=[1868]
for _ in range(7): a.append(F[a[-1]])
assert a[5]==a[7] and a[4]!=a[6]
print('sharp_witness_trajectory='+str(a))
