"""Exhaustive exact stability census on the twelve-vertex icosahedron."""
from collections import Counter
from itertools import combinations, product

# (a,b) represents a+b*phi in Z[phi], with phi**2=phi+1.
verts = [tuple(v[j:]+v[:j]) for a,b,j in product((-1,1),(-1,1),range(3))
         for v in [[(0,0),(a,0),(0,b)]]]

def sqdist(v,w):
    x=y=0
    for (r,s),(t,u) in zip(v,w):
        e,f=r-t,s-u
        x+=e*e+f*f
        y+=2*e*f+f*f
    return x,y

E = {(i,j) for i,j in combinations(range(12),2) if sqdist(verts[i],verts[j])==(4,0)}
N = [{v for v in range(12) if tuple(sorted((i,v))) in E} for i in range(12)]
assert len(E)==30 and {len(a) for a in N}=={5}

def connected(S):
    seen={min(S)}
    for _ in S:
        seen |= set().union(*(N[i]&S for i in seen))
    return seen==S

antipodes = {(i,j) for i,j in combinations(range(12),2)
             if all(a+b==c+d==0 for (a,c),(b,d) in zip(verts[i],verts[j]))}
assert len(antipodes)==6
for i,j in antipodes:
    assert N[i].isdisjoint(N[j]) and N[i]|N[j]==set(range(12))-{i,j}

MB = []
for x in range(4096):
    spins = [1-2*((x>>v)&1) for v in range(12)]
    MB.append((sum(spins),sum(spins[i]*spins[j] for i,j in E)))

expected_weak = [
    {(0,-10):72,(0,-6):20},
    {(0,-10):72,(0,-6):50,(2,-8):120,(2,-4):120,(4,-6):30,(4,-2):15},
    {(4,-6):30,(4,-2):15},
    {(4,-6):30,(4,-2):75,(6,0):20,(6,4):60,(8,10):6},
    {(6,0):20,(8,10):6},
    {(6,0):20,(8,10):36,(10,20):12,(12,30):1},
    {(12,30):1},
]
expected_ground = [72,222,30,50,20,69,1]
expected_excited = [20,0,15,0,6,0,0]
geometries=Counter()
for h in range(7):
    energy = [b-h*m for m,b in MB]
    emin = min(energy)
    weak,strict=Counter(),Counter()
    excited=0
    for x,value in enumerate(energy):
        next_energy = min(energy[x^(1<<i)] for i in range(12))
        if next_energy>=value:
            weak[MB[x]]+=1
        if next_energy<=value:
            continue
        strict[MB[x]]+=1
        if value==emin:
            continue
        excited+=1
        D={i for i in range(12) if (x>>i)&1}
        U=set(range(12))-D
        if h==0:
            assert MB[x]==(0,-6) and len(D)==6
            assert all(len(N[i]&S)==2 for S in (D,U) for i in S)
            geometries[connected(D),connected(U)]+=1
        elif h==2:
            assert MB[x]==(4,-2) and len(D)==4
            assert all(len(N[i]&D)==1 for i in D)
            assert all(len(N[i]&D)==2 for i in U)
        elif h==4:
            assert MB[x]==(8,10) and tuple(sorted(D)) in antipodes
        else:
            raise AssertionError((h,x))
    assert weak==expected_weak[h]
    assert strict==(weak if h%2==0 else Counter())
    assert energy.count(emin)==expected_ground[h]
    assert excited==expected_excited[h]
    print(h, 'weak',sum(weak.values()),'strict',sum(strict.values()),'ground',energy.count(emin),'strict excited',excited)
assert geometries=={(True,False):10,(False,True):10}

outside=Counter()
for D in map(set,combinations(range(12),4)):
    if all(len(N[i]&D)==1 for i in D):
        outside[tuple(sorted(len(N[i]&D) for i in set(range(12))-D))]+=1
assert outside=={(1,1,2,2,2,2,3,3):60,(2,2,2,2,2,2,2,2):15}
print('PASS: complete flip census, complementary cycle/triangles, 15 two-edge supports, 6 antipodal pairs')
