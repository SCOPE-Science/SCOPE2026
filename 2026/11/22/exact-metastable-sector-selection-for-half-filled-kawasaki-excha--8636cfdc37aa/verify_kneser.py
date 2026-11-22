"""Exact self-contained check of zero-temperature Petersen Kawasaki kinetics."""
from itertools import combinations, permutations
from collections import Counter, deque
from fractions import Fraction

vertices=list(combinations(range(5),2))
edges=[(i,j) for i in range(10) for j in range(i+1,10) if not(set(vertices[i])&set(vertices[j]))]
assert len(edges)==15
states=[sum(1<<i for i in ss) for ss in combinations(range(10),5)]
def internal(state):
    return sum(bool(state&(1<<i)) and bool(state&(1<<j)) for i,j in edges)
def moves(state):
    e=internal(state)
    return [(state^(1<<i)^(1<<j), internal(state^(1<<i)^(1<<j))-e)
            for i,j in edges if bool(state&(1<<i)) != bool(state&(1<<j))]
counts=Counter(internal(s) for s in states)
assert counts=={2:60,3:60,4:120,5:12}, counts
expected={2:{2:5,3:4,4:2},3:{4:4,5:1},4:{4:4},5:{}}
for s in states:
    e=internal(s)
    d=Counter(internal(t) for t,change in moves(s) if change>=0)
    # Allowed rates: internal edge count may only stay fixed or increase.
    allowed=Counter(internal(t) for t,change in moves(s) if change>=0)
    assert allowed==expected[e],(s,e,allowed)

def same_level_component(start):
    seen={start};Q=deque([start]); e=internal(start)
    while Q:
        for t,delta in moves(Q.popleft()):
            if delta==0 and t not in seen:
                seen.add(t);Q.append(t)
    return seen
assert len(same_level_component(next(s for s in states if internal(s)==4)))==120
assert len(same_level_component(next(s for s in states if internal(s)==2)))==60
assert all(not [t for t,delta in moves(s) if delta>=0] for s in states if internal(s)==5)
def induced_connected(state):
    selected={i for i in range(10) if state&(1<<i)}
    reach={min(selected)}
    while True:
        expanded=reach|{v for u,v in edges if u in reach and v in selected}|{u for u,v in edges if v in reach and u in selected}
        if expanded==reach: return len(reach)==len(selected)
        reach=expanded
assert all(induced_connected(s) for s in states if internal(s)==4)

# Reach-ground probability: e=5 => 1; e=4 => 0; e=3 => 1/5;
# e=2 => (4/6)*(1/5)=2/15. Neutral moves do not affect these rates.
p={5:Fraction(1),4:Fraction(0),3:Fraction(1,5),2:Fraction(2,15)}
prob=sum(Fraction(counts[e],252)*p[e] for e in counts)
assert prob==Fraction(8,63)
# Exactly the mean first entrance time to a terminal recurrent class.
means={5:Fraction(0),4:Fraction(0),3:Fraction(1,5),2:Fraction(1,6)+Fraction(4,6)*Fraction(1,5)}
mean=sum(Fraction(counts[e],252)*means[e] for e in counts)
assert mean==Fraction(5,42)
# In a 5-cycle induced subgraph, each of its five vertices has degree two.
for s in states:
    if internal(s)==5:
        assert all(sum(bool(s&(1<<j)) for i,j in edges if i==v)+sum(bool(s&(1<<i)) for i,j in edges if j==v)==2 for v in range(10) if s&(1<<v))
print('PASS: 252 states; energy-level counts',dict(sorted(counts.items())))
print('PASS: exact move counts',expected,'and connected neutral classes')
print('PASS: ground-hit probability',prob,'metastable',1-prob,'mean terminal-sector entry',mean)
