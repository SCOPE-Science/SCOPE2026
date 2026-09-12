"""Insertion-encoding state exploration for Av(B) classes.

Model: state = exact set of partial permutations (relative-order profiles)
reachable? We use the standard finite-profile approach: a state's future
depends only on the set of active sites and their distinguishability under
pattern containment. Practical construction: BFS over "slot profiles" where
each state is the isomorphism type of the poset of constraints? Instead we
use direct Myhill-Nerode exploration on insertion words:

We enumerate insertion words w over alphabet {l,m,r,f}-style? The canonical
insertion encoding (Albert-Linton-Ru\u0161kuc): build permutation by inserting
new maximum into slots; word letters: m_i (insert into i-th slot from left,
slot stays / splits). Since slot count is unbounded in general, the encoding
is over infinite alphabet; regular classes are those needing only bounded
slot information.

Practical finite-state test: explore the tree of "configurations" defined as
the set of patterns of length <= L-1=3 present as (not necessarily
consecutive) subsequences together with active-slot equivalence. The classic
Vatter/Albert "insertion-encoding regularity" test: two insertion histories
are equivalent iff their SquareBases/slot-behavior coincide. Implementing the
full test is heavy; we approximate by the profile of all length<=3 pattern
occurrences + number of active sites capped, and check stabilization of the
automaton (no new states after depth D) and that counts from the DFA match
the exact census. If DFA counts match census to n=15, the DFA is at least a
verified counter; full regularity proof needs the indistinguishability check.

Step 1: compute, for each avoider, its "profile": for each subset S of
positions, the pattern? Too big. Use: profile = ( bivincular? ). Simplify:
profile = sorted tuple of patterns (length<=3) occurring + active site
count + for each active site, the set of length-3 patterns it would complete
into a forbidden pattern. Two permutations with the same profile have the
same future under max-insertion (this is a sufficient condition for
regularity when the profile set is finite).

For each live perm q (avoider), active sites = all slots p where inserting
max keeps avoidance. The transition on inserting at p depends only on profile.
State = profile of q. BFS over states via representatives; record transitions
counting multiplicities. Then DFA count check vs census.
"""
import sys
from itertools import combinations

def pat_of(seq):
    order = sorted(range(len(seq)), key=lambda t: seq[t])
    rank = [0]*len(seq)
    for r, t in enumerate(order):
        rank[t] = r+1
    return tuple(rank)

P3 = [tuple(p) for p in set(
    __import__('itertools').permutations([1,2,3]))]

def profile_of(perm, bases):
    s = set()
    n = len(perm)
    for L in (1,2,3):
        for idx in combinations(range(n), L):
            s.add(pat_of([perm[i] for i in idx]))
    s = frozenset(s)
    # active-site signatures
    sigs = []
    for p in range(n+1):
        c = perm[:p] + (n+1,) + perm[p:]  # values: max is n+1? perm values 1..n
        # check avoidance
        bad = any(pat_of([c[i] for i in idx]) in FB
                  for FB in [FBSET] for idx in combinations(range(n+1),4))
        if bad:
            sigs.append(None)
            continue
        # signature: which length<=3 patterns use the new element and would
        # combine (with one more future max) to... approximate by: set of
        # length-3 patterns involving position p
        t = set()
        rest = list(range(n+1)); rest.remove(p)
        for idx in combinations(rest, 2):
            t.add((pat_of([c[p], c[idx[0]], c[idx[1]]] ),
                   pat_of(sorted([c[p], c[idx[0]], c[idx[1]]]))))
        # simpler: full 3-patterns involving p
        u = set()
        for idx in combinations(range(n+1), 3):
            if p in idx:
                u.add(pat_of([c[i] for i in idx]))
        sigs.append(frozenset(u))
    return (s, tuple(sigs))

def build(bases, max_states=4000, max_len=30):
    global FBSET
    FBSET = set(bases)
    start = profile_of((), bases)
    states = {start: 0}
    trans = {}
    reps = [()]
    from collections import deque
    q = deque([()])
    alive_reps = {(): ()}
    while q:
        perm = q.popleft()
        st = states[profile_of(perm, bases)]
        n = len(perm)
        for p in range(n+1):
            c = perm[:p] + (n+1,) + perm[p:]
            if any(pat_of([c[i] for i in idx]) in FBSET
                   for idx in combinations(range(n+1), 4)):
                continue
            pr = profile_of(c, bases)
            if pr not in states:
                if len(states) >= max_states:
                    return states, trans, reps, False, "STATE_LIMIT"
                states[pr] = len(states)
                reps.append(c)
                q.append(c)
            trans.setdefault(st, []).append(states[pr])
        if n >= max_len and q:
            pass
    return states, trans, reps, True, "OK"

def count_from_dfa(states, trans, nmax):
    # words counted with multiplicity = number of insertion words; each perm
    # has a unique insertion word (positions of successive maxima), and each
    # transition sequence corresponds to exactly one perm. So count walks.
    from collections import Counter
    cur = Counter({0: 1})
    counts = [1]  # n=0
    for n in range(1, nmax+1):
        nxt = Counter()
        for st, m in cur.items():
            for t in trans.get(st, []):
                nxt[t] += m
        counts.append(sum(nxt.values()))
        cur = nxt
    return counts

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "A"
    bases = [(4,2,3,1),(3,1,2,4)] if which == "A" else [(4,2,3,1),(3,2,1,4)]
    states, trans, reps, ok, msg = build(bases)
    print(f"class {which}: nstates={len(states)} ok={ok} {msg}")
    counts = count_from_dfa(states, trans, 12)
    print("DFA counts:", counts)
    exact = {"A": [1,1,2,6,22,88,363,1508,6255,25842,106327,435965,1782733],
             "B": [1,1,2,6,22,87,352,1428,5768,23156,92416,367007,1451780]}[which]
    print("exact    :", exact)
    print("match:", counts[:len(exact)] == exact)
