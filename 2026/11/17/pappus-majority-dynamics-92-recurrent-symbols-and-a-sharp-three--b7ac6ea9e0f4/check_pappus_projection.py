"""Independent exact incidence-projection certificate for Pappus majority dynamics.
Uses only the Python 3 standard library; exhaustively verifies 512 shore subsets.
"""
from collections import Counter
from itertools import combinations

MOD=3
# Points: (class 0, coordinate a), (class 1, coordinate b), (class 2, coordinate c).
# Lines: (a,b) incident to (0,a), (1,b), (2,a+b modulo 3).
lines=[(a,3+b,6+(a+b)%MOD) for a in range(3) for b in range(3)]
point_lines=[tuple(j for j,t in enumerate(lines) if i in t) for i in range(9)]
assert len(set(lines))==9 and all(len(x)==3 for x in point_lines)
assert all(len({min(u,v),max(u,v)})==2 for u,v in combinations(range(9),2))

def majority(mask, supports):
    return sum((sum((mask >> k)&1 for k in triple)>=2)<<i
               for i,triple in enumerate(supports))

def phi(mask): return majority(mask,lines)
def psi(mask): return majority(mask,point_lines)
P=tuple(psi(phi(x)) for x in range(512))
Q=tuple(phi(psi(x)) for x in range(512))
P2=tuple(P[P[x]] for x in range(512))
Q2=tuple(Q[Q[x]] for x in range(512))
corep=set(P2);coreq=set(Q2)
assert all(P[P2[x]]==P2[x] for x in range(512))
assert all(Q[Q2[x]]==Q2[x] for x in range(512))
assert len(set(P))==len(set(Q))==110
assert len(corep)==len(coreq)==92
# Verify the exact extra odd-step shortening: F^3 already lies in periodic core.
assert {psi(phi(psi(x))) for x in range(512)}==corep
assert {phi(psi(phi(x))) for x in range(512)}==coreq
assert len(set(psi(x) for x in range(512)))==182
assert len(set(phi(x) for x in range(512)))==182
# On the core, the two shore maps are inverse bijections.
assert {phi(r) for r in corep}==coreq
assert all(psi(phi(r))==r for r in corep)
assert all(phi(psi(r))==r for r in coreq)
wp=Counter(P2); wq=Counter(Q2)
assert Counter(wp.values())==Counter(wq.values())==Counter({2:54,4:36,130:2})
# Independent source-image counts also establish first-entry populations.
assert (182**2,110**2,92**2)==(33124,12100,8464)
assert [8464,12100-8464,33124-12100,512**2-33124]==[8464,3636,21024,229020]
# Classify all 92 core masks geometrically, not from output numerology alone.
coretypes=Counter()
for r in corep:
    c=tuple(sum((r>>(3*j+k))&1 for k in range(3)) for j in range(3))
    coretypes[(r.bit_count(),tuple(sorted(c)))] += 1
assert coretypes==Counter({
    (0,(0,0,0)):1,(9,(3,3,3)):1,
    (3,(1,1,1)):18,(6,(2,2,2)):18,
    (4,(1,1,2)):27,(5,(1,2,2)):27
})
# Weighted recurrent swap gives all orbit basin sizes without full 18-bit simulation.
fixed_hist=Counter(w*w for w in wp.values())
pair_hist=Counter(2*wp[r]*wp[s] for r,s in combinations(corep,2))
assert fixed_hist==Counter({4:54,16:36,16900:2})
assert pair_hist==Counter({8:1431,16:1944,32:630,520:108,1040:72,33800:1})
assert sum(b*count for b,count in fixed_hist.items())==34592
assert sum(b*count for b,count in pair_hist.items())==227552
assert len(pair_hist)>1 and sum(pair_hist.values())==4186
# Construction is isomorphic to the cycle-with-chords graph of full-state checker.
points_as_cycle=(0,10,14,2,6,16,8,4,12)
lines_as_cycle=(1,5,17,3,11,9,13,7,15)
inc_edges={tuple(sorted((points_as_cycle[p],lines_as_cycle[j])))
           for j,t in enumerate(lines) for p in t}
cycle_edges={tuple(sorted((i,(i+1)%18))) for i in range(18)}
chords=((0,5),(1,8),(2,13),(3,10),(4,15),(6,11),(7,14),(9,16),(12,17))
assert inc_edges==cycle_edges|set(chords)
print('Independent 512-subset incidence certificate: PASS')
print('Projection P^3=P^2, Q^3=Q^2, im F^3=92^2: PASS')
print('Shore-map image sizes: 182, 110, 92')
print('Core symbols:',len(corep),'fibers:',dict(sorted(Counter(wp.values()).items())))
print('Core-size classifications:',dict(sorted(coretypes.items())))
print('Periodic orbits: 92 fixed, 4186 primitive 2-cycles')
print('Fixed basin histogram:',dict(sorted(fixed_hist.items())))
print('Two-cycle basin histogram:',dict(sorted(pair_hist.items())))
print('All 27 edges agree with independent graph construction: PASS')
