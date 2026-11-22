"""Complete integer certificate for local stability of 12-site icosahedral Ising AFM.
Only Python's standard library is needed. Does not use external result tables.
"""
from collections import Counter

N = 12
# Vertex 0 is upper pole, vertex 11 lower pole;
# upper pentagon 1,...,5 and lower pentagon 6,...,10.
EDGES = set()
for i in range(5):
    EDGES.update((tuple(sorted(e)) for e in [
        (0, 1+i), (11, 6+i),
        (1+i, 1+(i+1)%5), (6+i, 6+(i+1)%5),
        (1+i,6+i), (1+i,6+(i-1)%5),
    ]))
EDGES=sorted(EDGES)
assert len(EDGES) == 30
NEIGH = [set() for _ in range(N)]
for i,j in EDGES:
    NEIGH[i].add(j); NEIGH[j].add(i)
assert all(len(s)==5 for s in NEIGH)

EXPECTED={
    0: {(0,-10):72,(0,-6):20},
    1: {(0,-10):72,(0,-6):50,(2,-8):120,(2,-4):120,(4,-6):30,(4,-2):15},
    2: {(4,-6):30,(4,-2):15},
    3: {(4,-6):30,(4,-2):75,(6,0):20,(6,4):60,(8,10):6},
    4: {(6,0):20,(8,10):6},
    5: {(6,0):20,(8,10):36,(10,20):12,(12,30):1},
    6: {(12,30):1},
}

def stats(h):
    c=Counter(); strict=0; energies=[]
    for mask in range(1<<N):
        spins=[1 if (mask>>i)&1 else -1 for i in range(N)]
        magnetization=sum(spins)
        bonds=sum(spins[i]*spins[j] for i,j in EDGES)
        energies.append(bonds-h*magnetization)
        deltas=[2*spins[i]*(h-sum(spins[j] for j in NEIGH[i])) for i in range(N)]
        if all(d>=0 for d in deltas): c[magnetization,bonds]+=1
        if all(d>0 for d in deltas): strict+=1
    min_energy=min(energies)
    ground_count=sum(e==min_energy for e in energies)
    return c,strict,min_energy,ground_count

expected_strict=[92,0,45,0,26,0,1]
expected_ground=[72,222,30,50,20,69,1]
for h in range(7):
    c,strict,mg,ng=stats(h)
    assert c==Counter(EXPECTED[h]),(h,c)
    assert strict==expected_strict[h],(h,strict)
    assert ng==expected_ground[h],(h,ng)
for h,expected in [(0.5,0),(1.5,2),(2.5,2),(3.5,4),(4.5,4),(5.5,6)]:
    c,strict,_,_=stats(h)
    assert c==Counter(EXPECTED[expected]),(h,c)
    assert strict==sum(c.values()), (h,strict)
# Check explicit geometric signatures of all plateau excited states.
for h,energy,mag,num,degree_pattern in [
    (0.5,-6,0,20,(2,2,2,2,2,2)),
    (2.0,-2,4,15,(1,1,1,1)),
    (4.0,10,8,6,(0,0)),
]:
    seen=0
    for mask in range(1<<N):
        s=[1 if (mask>>i)&1 else -1 for i in range(N)]
        m=sum(s);b=sum(s[i]*s[j] for i,j in EDGES)
        if (m,b)!=(mag,energy): continue
        if not all(2*s[i]*(h-sum(s[j] for j in NEIGH[i]))>0 for i in range(N)):continue
        D=[i for i in range(N) if s[i]==-1]
        assert tuple(sorted(len(NEIGH[i].intersection(D)) for i in D))==degree_pattern
        U=set(range(N))-set(D)
        if h==0.5:
            assert all(len(NEIGH[i].intersection(U))==2 for i in U)
        if h==4.0:
            assert all(len(NEIGH[i].intersection(D))==1 for i in U)
        seen+=1
    assert seen==num,(h,seen)
print('ICOSAHEDRON_METASTABILITY_CERTIFIED', 'configs=4096', 'fields=13', 'open_excited=20,15,6', 'weak=92,407,45,191,26,69,1')
