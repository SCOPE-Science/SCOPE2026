#!/usr/bin/env python3
"""Exact finite census of paired BSL semantics for one proposition.
All four teams are represented by bit positions 0,1,2,3.
A family is a four-bit mask; the pair is (support-mask, antisupport-mask).
The language has primitive bot, NE, p, bilateral negation, conjunction,
splitting disjunction and the nonempty-subteam diamond.
No precomputed reachability or count is assumed.
"""
from itertools import product
TEAM_RANGE = tuple(range(4))
ALL = (1 << 4) - 1
def split(a, b):
    out=0
    for s in TEAM_RANGE:
        if a & (1 << s):
            for t in TEAM_RANGE:
                if b & (1 << t):
                    out |= 1 << (s | t)
    return out
def maybe(a):
    return sum(1 << t for t in TEAM_RANGE
               if any(s != 0 and s & ~t == 0 and ((a >> s) & 1)
                      for s in TEAM_RANGE))
def neg(x):
    a,b=x
    return b,a
def conj(x,y):
    a,b=x
    c,d=y
    return a&c,split(b,d)
def disj(x,y):
    a,b=x
    c,d=y
    return split(a,c),b&d
def diamond(x):
    a,b=x
    return maybe(a),b
ATOMS = {
    "bot": (1, 15),    # only empty team supports bottom
    "NE": (14, 1),     # exactly nonempty teams support NE
    "p": (5, 3),       # p true at valuation 1, false at valuation 0
}
# The actual p mask: teams [] and {valuation 1} correspond to indices 0,2 => 5.
# The actual anti-p mask: indices 0,1 => 3.
assert ATOMS["p"] == (5,3)
def close(initial, layer, witnesses, trace=False):
    seen=dict(witnesses)
    for pair,desc in initial.items():
        if pair not in seen: seen[pair]=desc
    while True:
        old=len(seen)
        items=list(seen)
        for x in items:
            y=neg(x)
            if y not in seen:seen[y]=("neg",x)
        for j,x in enumerate(items):
            for y in items[:j+1]:
                for opname,fn in (("and",conj),("or",disj)):
                    z=fn(x,y)
                    if z not in seen: seen[z]=(opname,x,y)
        if len(seen)==old:break
    return seen
def descend_ladder(max_depth=4):
    base={v:("atom",k) for k,v in ATOMS.items()}
    prev={}
    layers=[]
    witnesses_by_depth=[]
    for d in range(max_depth+1):
        starts=dict(base)
        starts.update(prev)
        if d:
            for x in prev:
                y=diamond(x)
                if y not in starts:starts[y]=("diamond",x)
        out=close(starts,d,starts)
        layers.append(set(out))
        witnesses_by_depth.append(out)
        prev=out
        if d>0 and len(layers[-1])==len(layers[-2]):break
    return layers,witnesses_by_depth
LAYERS,WITNESSES=descend_ladder()
assert [len(x) for x in LAYERS]==[39,64,66,66]
F=LAYERS[2]
assert (10,12) in F and (10,12) not in LAYERS[1]
assert diamond(neg(diamond(ATOMS["p"])))==(10,12)
assert F == LAYERS[3]
# Independent upper-bound certificate table, stored explicitly.
TABLE={
 0: (0,1,2,3,4,5,8,10,12,14,15),
 1: (0,8,10,12,14,15),
 2: (0,4,5,8,12),
 3: (0,4,5,8,12),
 4: (0,2,3,8,10),
 5: (0,2,3,8,10),
 8: (0,1,2,3,4,5,8,10,12,14,15),
10: (0,1,4,5,8,12),
12: (0,1,2,3,8,10),
14: (0,1,8),
15: (0,1,8)
}
target={(a,b) for a,B in TABLE.items() for b in B}
assert len(target)==66
assert target==F
assert set(ATOMS.values())<=target
for x in target:
    assert neg(x) in target
    assert diamond(x) in target
    for y in target:
        assert conj(x,y) in target
        assert disj(x,y) in target
# Check upper-bound certificates for each modal-depth layer separately
for d,S in enumerate(LAYERS[:-1]):
    assert set(ATOMS.values())<=S
    for x in S:
        assert neg(x) in S
        for y in S:
            assert conj(x,y) in S
            assert disj(x,y) in S
    if d>0:
        assert {diamond(x) for x in LAYERS[d-1]}<=S
# Verify every enumerated point is semantically a weak ideal (convex, union closed).
def weak_ideal(mask):
    U=[s for s in TEAM_RANGE if (mask>>s)&1]
    return all((mask>>(s|t))&1 for s in U for t in U) and all(
        (mask>>t)&1 for s in U for u in U for t in TEAM_RANGE
        if (s&~t)==0 and (t&~u)==0)
assert all(weak_ideal(a) and weak_ideal(b) for a,b in target)
# Distinct full bilateral pairs and support-only denotations.
assert len({a for a,b in target})==11
assert len({a for a,b in LAYERS[0]})==11
print("BSL_BILATERAL_ONE_ATOM_OK")
print("layer_counts="+str([len(x) for x in LAYERS]))
print("support_only_count=11")
print("depth_two_new="+str(sorted(LAYERS[2]-LAYERS[1])))
print("table="+str(TABLE))
