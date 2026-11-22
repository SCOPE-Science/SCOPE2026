"""Independent Petersen presentation; exact graph SCC and absorption check."""
from itertools import combinations
from collections import Counter
from fractions import Fraction

# Five outer-cycle edges, five inner-star edges, five spokes.
adj=[set() for _ in range(10)]
for i in range(5):
    for u,v in [(i,(i+1)%5),(5+i,5+(i+2)%5),(i,5+i)]:
        adj[u].add(v);adj[v].add(u)
assert all(len(a)==3 for a in adj)
edges=[(i,j) for i in range(10) for j in adj[i] if i<j]
assert len(edges)==15

def E(mask):
    return -sum(1 if ((mask>>i)&1)==((mask>>j)&1) else -1 for i,j in edges)
def outgoing(mask):
    current=E(mask)
    for u,v in edges:
        if bool(mask&(1<<u)) == bool(mask&(1<<v)):continue
        nxt=mask^(1<<u)^(1<<v)
        if E(nxt)<=current: yield nxt
states=[sum(1<<i for i in t) for t in combinations(range(10),5)]
energy_count=Counter(E(s) for s in states)
assert energy_count=={-5:12,-1:120,3:60,7:60},energy_count
expect={-5:{},-1:{-1:4},3:{-5:1,-1:4},7:{-1:2,3:4,7:5}}
for s in states:
    assert Counter(E(t) for t in outgoing(s))==expect[E(s)]
# Equal-energy moves are symmetric; check all equal-energy components independently.
seen=set(); comps=[]
for s in states:
    if s in seen:continue
    stack=[s];comp=set([s]);seen.add(s)
    while stack:
        for t in outgoing(stack.pop()):
            if E(t)==E(s) and t not in seen:
                seen.add(t);comp.add(t);stack.append(t)
    comps.append((E(s),len(comp)))
assert Counter(comps)=={(-5,1):12,(-1,120):1,(3,1):60,(7,60):1},Counter(comps)
# Independent rational first-step equations for the energy levels; tie jumps
# are self-transitions for this harmonic probability, so cancel.
p={-5:Fraction(1),-1:Fraction(0)}
p[3]=(p[-5]+4*p[-1])/5
p[7]=(2*p[-1]+4*p[3])/6
assert p[3]==Fraction(1,5) and p[7]==Fraction(2,15)
q=sum(Fraction(count,252)*p[e] for e,count in energy_count.items())
assert q==Fraction(8,63)
print('PASS: independent outer/inner Petersen labels; expected energy counts',energy_count)
print('PASS: equal-energy components',Counter(comps))
print('PASS: full Markov absorption probability',q)
