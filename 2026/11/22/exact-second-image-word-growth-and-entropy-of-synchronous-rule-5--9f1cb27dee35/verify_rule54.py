#!/usr/bin/env python3
"""Exact, standard-library certificate for the second spatial image of Rule 54."""
from collections import deque
from fractions import Fraction

# Rule 54 uses neighborhood 000 for bit 0 of its truth-table integer.
def f(a,b,c): return (54 >> (4*a + 2*b + c)) & 1

def f2(s):
    assert len(s) == 5
    return f(*(f(*s[j:j+3]) for j in range(3)))

# Labeled edges of the 4-bit de Bruijn graph; a fifth input bit completes one output.
edge = [[0,0] for _ in range(16)]
for u in range(16):
    bits = tuple((u>>shift)&1 for shift in (3,2,1,0))
    for b in (0,1):
        symbol = f2(bits+(b,))
        edge[u][symbol] |= 1 << ((2*u+b) % 16)

def nxt(S, symbol):
    T = 0
    for u in range(16):
        if (S>>u)&1:
            T |= edge[u][symbol]
    return T

# Saturate all subset states, including the rejecting empty set.
full = (1<<16)-1
reachable = {full}
queue = deque([full])
while queue:
    S = queue.popleft()
    for a in (0,1):
        R = nxt(S,a)
        if R not in reachable:
            reachable.add(R); queue.append(R)
assert len(reachable) == 39 and 0 in reachable

# Proposed 18-state deterministic automaton, with state 0 rejecting,
# state 17 initial; all other states accepting.
tr = (
  (0,0),(0,9),(14,0),(2,1),(2,11),(2,12),(6,3),(8,3),(16,3),
  (7,4),(8,5),(6,10),(7,13),(8,13),(15,6),(15,9),(16,10),(16,13)
)
assert len(tr) == 18 and tr[0] == (0,0)

# Exact automata-equivalence check, all reachable pairs; this is finite,
# unlike testing output words only up to a prescribed length.
seen = {(full,17)}
queue = deque(seen)
while queue:
    S,q = queue.popleft()
    assert (S == 0) == (q == 0)
    for a in (0,1):
        pair = (nxt(S,a),tr[q][a])
        if pair not in seen:
            seen.add(pair); queue.append(pair)
assert len(seen) == 39
assert {S for S,q in seen} == reachable
assert set(q for S,q in seen) == set(range(18))

# Transfer matrix represented by its action on column vectors.
def action(v): return [v[u]+v[w] for u,w in tr]
v0 = [0] + [1]*17
powers = [v0]
for _ in range(15): powers.append(action(powers[-1]))

# Monic P(t) = t^15-4t^14+...-4t+1, ascending coefficients.
pa = (1,-4,5,-2,-4,8,-4,-2,6,-5,2,2,-5,6,-4,1)
assert len(pa) == 16
# Exact P(M) v0 = 0: implies recurrence at ALL word lengths.
assert all(sum(pa[k]*powers[k][i] for k in range(16)) == 0
           for i in range(18))
counts = [powers[i][17] for i in range(16)]
assert counts[:16] == [1,2,4,8,16,29,53,100,187,344,635,1172,2155,3959,7271,13336]
# D(z)=z^15 P(1/z); C(z)=N(z)/D(z).
d = tuple(reversed(pa))
ncoef = [sum(d[j]*counts[i-j] for j in range(i+1)) for i in range(15)]
assert ncoef == [1,-2,2,-1,0,-1,0,2,-2,-3,5,-2,-2,3,0]

# Independent brute-force all finite input blocks for short output lengths.
for n in range(1,10):
    outputs = set()
    for a in range(1 << (n+4)):
        b = [(a>>i)&1 for i in range(n+4)]
        outputs.add(tuple(f2(tuple(b[i:i+5])) for i in range(n)))
    assert len(outputs) == counts[n]

# The 16 nonempty recurrent states 1,...,16 form one strongly
# connected directed component (rejecting edges omitted).
def reach(seed, backwards=False):
    adj={i:set() for i in range(1,17)}
    for i in range(1,17):
        for j in tr[i]:
            if 1<=j<=16:
                adj[j if backwards else i].add(i if backwards else j)
    seen={seed}; todo=[seed]
    while todo:
        for u in adj[todo.pop()]:
            if u not in seen:seen.add(u);todo.append(u)
    return seen
assert reach(1)==set(range(1,17))
assert reach(1,True)==set(range(1,17))
assert tr[6][0] == 6  # aperiodic loop

# Exact characteristic polynomial of the internal 16-state component.
# Faddeev--LeVerrier over integers, with division checked at each step.
K=[[0]*16 for _ in range(16)]
for i in range(1,17):
    for j in tr[i]:
        if 1 <= j <= 16: K[i-1][j-1] += 1
B=[[int(i==j) for j in range(16)] for i in range(16)]
char=[1]
for k in range(1,17):
    C=[[sum(K[i][t]*B[t][j] for t in range(16))
        for j in range(16)] for i in range(16)]
    trace=sum(C[i][i] for i in range(16))
    assert trace % k == 0
    ck= -trace//k
    char.append(ck)
    B=[[C[i][j]+(ck if i==j else 0) for j in range(16)]
       for i in range(16)]
assert char == list(reversed(pa)) + [0]

# Perron root bounds by Collatz--Wielandt on a strictly positive vector.
w=[0]+[1]*16
for _ in range(80):
    w=[0]+[sum(w[j] for j in tr[i] if j) for i in range(1,17)]
Aw=[0]+[sum(w[j] for j in tr[i] if j) for i in range(1,17)]
assert all(w[i] > 0 for i in range(1,17))
lo,hi=Fraction(1827684,1000000),Fraction(1827685,1000000)
assert all(lo*w[i] < Aw[i] < hi*w[i] for i in range(1,17))
print('PASS: 39 exact subset states, 18-state DFA, all-word recurrence,')
print('      generating function, nine exhaustive lengths and Perron bounds.')
print('First counts:',counts[:16]);print('D(z) ascending:',d)
print('N(z) ascending:',ncoef)
print('Perron root in (1.827684, 1.827685).')
