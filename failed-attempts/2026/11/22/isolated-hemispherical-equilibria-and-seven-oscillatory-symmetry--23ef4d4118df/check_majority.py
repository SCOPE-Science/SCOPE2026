#!/usr/bin/env python3
"""Self-contained exhaustive census of strict-neighbor majority on the icosahedral graph."""
from collections import Counter, defaultdict

N = 12
edges = []
def add(a,b):
    assert a != b
    edges.append(tuple(sorted((a,b))))
for j in range(5):
    add(0,1+j)
    add(11,6+j)
    add(1+j,1+(j+1)%5)
    add(6+j,6+(j+1)%5)
    add(1+j,6+j)
    add(1+j,6+(j-1)%5)
assert len(edges)==30 and len(set(edges))==30
nb=[0]*N
for a,b in edges:
    nb[a]|=1<<b;nb[b]|=1<<a
assert all(m.bit_count()==5 for m in nb)

# The icosahedral full symmetry group is exhaustively recovered by backtracking
# every edge- and nonedge-preserving vertex permutation.
permutations=[]
order=sorted(range(N),key=lambda v: -((nb[v]&nb[0]).bit_count()))
# Fix distinguished source vertex 0 first for faster pruning.
order=[0]+[v for v in order if v!=0]
used=[False]*N
mapping=[-1]*N
def extend(k):
    if k == N:
        permutations.append(tuple(mapping));return
    i=order[k]
    for j in range(N):
        if used[j]:continue
        if all(bool(nb[i]&(1<<v)) == bool(nb[j]&(1<<mapping[v])) for v in order[:k]):
            used[j]=True;mapping[i]=j;extend(k+1);mapping[i]=-1;used[j]=False
extend(0)
assert len(permutations)==120

def transform(s,p):
    return sum(1<<p[i] for i in range(N) if s&(1<<i))

def F(s):
    return sum(1<<v for v in range(N) if (s&nb[v]).bit_count()>=3)
step=tuple(F(s) for s in range(1<<N))
assert all(step[s ^ 4095] == (step[s] ^ 4095) for s in range(4096))
assert all(step[transform(s,p)] == transform(step[s],p) for p in permutations for s in range(4096))

periodic={s for s in range(4096) if step[step[s]]==s}
assert len(periodic)==326
fixed={s for s in periodic if step[s]==s}
assert len(fixed)==14
caps={(1<<v)|nb[v] for v in range(N)}
assert len(caps)==12 and fixed==caps|{0,4095}

canonical={s:min(s,step[s]) for s in periodic}
cycles={canonical[s] for s in periodic}
assert len(cycles)==170
assert sum(1 for s in cycles if step[s]==s)==14
assert sum(1 for s in cycles if step[s]!=s)==156

entrance_counts=Counter(); basin=Counter(); max_time=0
all_class={}
for s in range(4096):
    v=s
    for t in range(6):
        if v in periodic:break
        v=step[v]
    else:raise AssertionError(('no entry',s))
    k=canonical[v];p=1 if step[k]==k else 2
    all_class[s]=(t,p,k)
    entrance_counts[t,p]+=1;basin[k]+=1
    max_time=max(t,max_time)
assert max_time==5
assert sum(entrance_counts.values())==4096
assert all(basin[c]==1 for c in caps)
assert basin[0]==basin[4095]==1586
assert Counter(basin[c] for c in cycles if step[c]!=c)==Counter({4:60,6:60,14:20,2:16})
assert sum(basin[c] for c in cycles if step[c]!=c)==912 # CHECK

classes=defaultdict(list)
seen=set()
for c in sorted(cycles):
    if c in seen:continue
    orbit={min(transform(c,p), transform(step[c],p)) for p in permutations}
    assert orbit<=cycles
    seen|=orbit
    classes[1 if step[c]==c else 2].append((c,len(orbit),tuple(sorted({basin[k] for k in orbit}))))
assert seen==cycles
assert len(classes[1])==3 and len(classes[2])==7

print('edges',','.join('%d-%d'%(a,b) for a,b in sorted(edges)))
print('automorphisms',len(permutations),'periodic_states',len(periodic),'fixed',len(fixed),'cycles',len(cycles))
print('entrance',sorted(entrance_counts.items()))
print('basin_size_distribution_2cycles',sorted(Counter(basin[c] for c in cycles if step[c]!=c).items()))
print('consensus_basins',basin[0],basin[4095], 'cap_basins', [basin[c] for c in sorted(caps)])
print('max_time',max_time,'extremal_starts',sum(1 for x in all_class if all_class[x][0]==max_time))
print('class_fixed',sorted(classes[1]))
print('class_2cycle',sorted(classes[2]))
