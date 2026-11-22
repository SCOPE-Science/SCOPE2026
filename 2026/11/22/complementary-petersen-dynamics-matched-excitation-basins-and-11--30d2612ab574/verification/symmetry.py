#!/usr/bin/env python3
"""Complete orbit count under all permutations of five underlying points."""
import itertools,collections,json
from pathlib import Path
from census import classify, PAIRS, NEI, POW

def main():
    successor,time,period,cycles=classify('ghm')
    reps={r for p,r in cycles if p==3}
    assert len(reps)==10080
    pind={x:i for i,x in enumerate(PAIRS)}
    actions=[]
    for p in itertools.permutations(range(5)):
        action=tuple(pind[tuple(sorted((p[x],p[y])))] for x,y in PAIRS)
        for v in range(10):
            assert {action[w] for w in NEI[v]}==set(NEI[action[v]])
        actions.append(action)
    assert len(set(actions))==120
    def move(s,action):
        out=0
        for i in range(10):out+=(s//POW[i]%3)*POW[action[i]]
        return out
    seen=set(); multiplicity=collections.Counter(); cls=[]
    for r in sorted(reps):
        if r in seen:continue
        group=set()
        for a in actions:
            q=move(r,a)
            q2=successor[q];q3=successor[q2]
            assert successor[q3]==q
            group.add(min(q,q2,q3))
        assert group <= reps
        assert group.isdisjoint(seen)
        seen |= group
        multiplicity[len(group)]+=1;cls.append((min(group),len(group)))
    assert seen==reps and len(cls)==118
    assert multiplicity=={120:57,60:49,30:7,20:3,15:2}
    obj={'graph':'T(5)=L(K5)','automorphism_group':'S5','automorphism_order':120,
         'spatial_orbits_of_primitive_temporal_three_cycles':118,
         'orbit_size_distribution':[[k,multiplicity[k]] for k in sorted(multiplicity)],
         'canonical_orbit_representatives':[[a,b] for a,b in cls]}
    dest=Path(__file__).resolve().parent.parent/'data'/'symmetry.json'
    if dest.exists():assert json.loads(dest.read_text())==obj
    print('SYMMETRY_ALL_10080_OK')
    return obj
if __name__=='__main__':main()
