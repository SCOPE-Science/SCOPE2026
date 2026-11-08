"""Independent phase-pattern range reconstruction, not calling the direct simulator."""
from collections import Counter
from itertools import product
from math import comb

def vertex_range(deg, t_fire, neighbor_phases):
    increments = [sum(phase == t for phase in neighbor_phases)-deg*(t_fire==t) for t in range(3)]
    cumul = 0; lower = 0; upper = 2*deg-1
    for t in range(3):
        if t == t_fire: lower = max(lower, deg-cumul)
        else: upper = min(upper, deg-1-cumul)
        cumul += increments[t]
    if lower > upper: return ()
    return range(lower,upper+1)

def actual_one_fire(n):
    out=Counter()
    for p,q in product(range(3),repeat=2):
        for leafs in product(range(3),repeat=n):
            ranges = [vertex_range(n+1,p,(q,)+leafs), vertex_range(n+1,q,(p,)+leafs)]
            ranges += [vertex_range(2, phase, (p,q)) for phase in leafs]
            if any(not r for r in ranges): continue
            counts=Counter({0:1})
            for r in ranges:
                new=Counter()
                for m,c in counts.items():
                    for a in r: new[m+a] += c
                counts=new
            out.update(counts)
    return out
for n in range(1, 9):
    obs=actual_one_fire(n)
    exp=Counter({2*n+1+j:6*sum(comb(n,k) for k in range(j+1)) for j in range(n)})
    assert obs==exp, (n,obs,exp)
    print(f"n={n} phase_patterns={3**(n+2)} one_fire={sum(obs.values())} support={list(sorted(obs))}")
print('PASS phase reconstruction')
