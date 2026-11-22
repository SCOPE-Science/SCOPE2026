"""Exact finite enumeration for alternating-permutation single-deletion codes."""
from itertools import permutations, combinations
from collections import Counter

N = 6
words = [p for p in permutations(range(1, N+1)) if all((p[i] < p[i+1]) == (i % 2 == 0) for i in range(N-1))]
assert len(words) == 61

def rank_deck(p):
    result = set()
    for k in range(N):
        t = p[:k] + p[k+1:]
        result.add(tuple(1+sum(y < x for y in t) for x in t))
    return result

decks = [rank_deck(p) for p in words]
allmask = (1 << len(words)) - 1
adj = [allmask ^ (1 << k) for k in range(len(words))]
conflict_edges = 0
for a,b in combinations(range(len(words)), 2):
    if not decks[a].isdisjoint(decks[b]):
        conflict_edges += 1
        adj[a] &= ~(1 << b)
        adj[b] &= ~(1 << a)
assert conflict_edges == 480

# Bron-Kerbosch maximal-clique enumeration with pivoting on the
# compatibility graph, exact integer bitsets, no pruning by conjectured size.
hist = Counter()
maximum = []

def vertices(bits):
    while bits:
        low = bits & -bits
        yield low.bit_length()-1
        bits ^= low

def maximal_cliques(selected, potential, used):
    if not (potential | used):
        hist[len(selected)] += 1
        if len(selected) >= 11:
            maximum.append(tuple(sorted(selected)))
        return
    union = potential | used
    pivot = max(vertices(union), key=lambda v:(potential & adj[v]).bit_count())
    choices = potential & ~adj[pivot]
    while choices:
        low = choices & -choices
        v = low.bit_length()-1
        maximal_cliques(selected + (v,), potential & adj[v], used & adj[v])
        potential &= ~low
        used |= low
        choices &= ~low

maximal_cliques((),allmask,0)
assert hist == {6:777, 7:10498, 8:16495, 9:5033, 10:393, 11:6}, hist
assert len(maximum) == 6 and len(set(maximum)) == 6
# A valid code is a clique. Every clique extends to a maximal clique;
# therefore the full enumeration rules out any size >= 12.
expect = [
"132546 153426 153624 162534 342516 351426 351624 354612 362514 561324 563412",
"132546 153426 153624 162534 342615 351426 351624 354612 362415 561324 563412",
"132546 153426 153624 231645 263415 351426 351624 354612 362514 561324 563412",
"132546 153426 153624 261534 263415 342615 351426 351624 354612 561324 563412",
"132546 153426 153624 261534 263514 342516 351426 351624 354612 561324 563412",
"132645 153426 153624 231546 263415 351426 351624 354612 362514 561324 563412",
]
formatted = {' '.join(''.join(map(str,words[i])) for i in m) for m in maximum}
assert formatted == set(expect), (formatted-set(expect),set(expect)-formatted)
for chosen in maximum:
    assert all(decks[a].isdisjoint(decks[b]) for a,b in combinations(chosen,2))
common = set(maximum[0]).intersection(*map(set,maximum[1:]))
assert sorted(''.join(map(str,words[i])) for i in common) == ['153426','153624','351426','351624','354612','561324','563412']

# An exact involution preserving the source class and its deletion collisions:
# reverse the positions while complementing all symbol values.
def rc(p): return tuple(7-x for x in p[::-1])
word_ids = {p:i for i,p in enumerate(words)}
code_set = {frozenset(m) for m in maximum}
fixed = sum(frozenset(word_ids[rc(words[i])] for i in m) == frozenset(m) for m in maximum)
assert fixed == 4
assert all(frozenset(word_ids[rc(words[i])] for i in m) in code_set for m in maximum)

# Independent graph check by building all eligible sources through insertion
# into each possible standardized five-symbol output.
from collections import defaultdict
parents = defaultdict(set)
for p in permutations(range(1,6)):
    for pos in range(6):
        for value in range(1,7):
            lifted = tuple(x+int(x>=value) for x in p)
            lifted = lifted[:pos]+(value,)+lifted[pos:]
            if lifted in word_ids: parents[p].add(word_ids[lifted])
comp = set()
for ids in parents.values():
    comp.update(combinations(sorted(ids),2))
assert len(comp) == conflict_edges
assert all(not (adj[a] & (1<<b)) for a,b in comp)
print('VERIFY_OK; sources=61; conflict_edges=480; maximal_clique_histogram='+str(sorted(hist.items()))+'; opt=11; equality_cases=6; common=7; fixed_under_reverse_complement=4')
