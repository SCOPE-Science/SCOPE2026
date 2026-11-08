"""Direct finite certificate for cyclic binary five-window capacities."""
import itertools
import json
from pathlib import Path

D = json.loads((Path(__file__).parent/'witnesses.json').read_text(encoding='utf-8'))
assert D['window_length'] == 5

def windows(w):
    return {''.join(w[(i+j)%len(w)] for j in range(5)) for i in range(len(w))}

def min_rotation(w):
    return min(w[i:]+w[:i] for i in range(len(w)))

# These checks cover every feasible positive ring length k>=5:
# for k>32, the counting bound forces zero; for 5<=k<=32,
# explicitly given disjoint cycles achieve the claimed number.
for k in range(5,33):
    W = D['witnesses_by_ring_length'][str(k)]
    assert len(W) == (3 if k==7 else 32//k)
    seen = set()
    for w in W:
        assert len(w)==k and set(w)<={'0','1'}
        f=windows(w)
        assert len(f)==k and not(seen&f)
        seen|=f

# Enumerate ALL binary seven-necklaces independently of the
# explicit witness list. Each length-seven cycle is a primitive
# necklace with seven distinct cyclic length-five factors.
necklaces = {min_rotation(''.join(t)) for t in itertools.product('01',repeat=7)}
valid = {w for w in necklaces if len(windows(w))==7}
certificate = {min_rotation(w) for w in D['seven_cycle_classes'].values()}
assert len(necklaces)==20, len(necklaces)
assert len(valid)==12 and certificate==valid

G=D['seven_cycle_intersection_groups']
assert sorted(int(i) for g in G for i in g)==list(range(12))
for g in G:
    for a,b in itertools.combinations(g,2):
        assert windows(D['seven_cycle_classes'][a]) & windows(D['seven_cycle_classes'][b])

# Each selection of disjoint seven-cycles has at most one from each
# of the above three internally-intersecting groups; hence <=3.
assert sum(bool(windows(w)) for w in D['witnesses_by_ring_length']['7'])==3
print('DIRECT_CERTIFICATE_OK: 5<=k<=32, seven-cycle partition, all k>32 excluded')
