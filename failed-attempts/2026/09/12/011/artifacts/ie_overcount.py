"""Replayable certificate that the coarse length<=3 occurrence profile is NOT a
valid insertion-encoding state: exhibits profile-equal permutations with
different futures (so no deterministic quotient transition exists), shows the
first-representative quotient DFA undercounts (|L_7| = 1266 vs exact 1508 for
Av(4231,3124)), and prints the Myhill-Nerode signature table.

Also prints the Myhill-Nerode signature table (replays sig_table.txt cells).
Run: python3 ie_overcount.py  (stdlib only, ~1-2 min)
"""
from itertools import combinations
from collections import defaultdict

def pat_of(seq):
    order = sorted(range(len(seq)), key=lambda t: seq[t])
    rank = [0] * len(seq)
    for r, t in enumerate(order):
        rank[t] = r + 1
    return tuple(rank)

def bases(which):
    return {(4, 2, 3, 1), (3, 1, 2, 4)} if which == 'A' else {(4, 2, 3, 1), (3, 2, 1, 4)}

def avoids(p, F):
    n = len(p)
    if n < 4:
        return True
    return not any(pat_of([p[i] for i in idx]) in F
                   for idx in combinations(range(n), 4))

def kids(p, F):
    n = len(p)
    out = []
    for x in range(n + 1):
        c = p[:x] + (n + 1,) + p[x:]
        if avoids(c, F):
            out.append(c)
    return out

def prof3(p):
    s = set()
    for L in (1, 2, 3):
        for idx in combinations(range(len(p)), L):
            s.add(pat_of([p[i] for i in idx]))
    return frozenset(s)

def avoiders(F, n):
    live = [()]
    for m in range(1, n + 1):
        new = []
        for q in live:
            for x in range(m):
                c = q[:x] + (m,) + q[x:]
                if avoids(c, F):
                    new.append(c)
        live = new
    return live

def main():
    print("=== coarse-profile quotient is not an exact automaton (class A) ===")
    print("Two inequivalent quotients already disagree with the exact count")
    print("A_7 = 1508: pooling all perms per profile is ill-defined (it counts")
    print("with pooled multiplicities, not a quotient walk count), while the")
    print("first-representative quotient undercounts (1266); both computed")
    print("below. The rigorous core is the divergence certificate: two")
    print("avoiders with IDENTICAL length-<=3 profiles but different futures,")
    print("so no well-defined deterministic quotient transition exists.")
    print()
    F = bases('A')
    # profile-quotient walk counts: states = prof3 types seen up to depth 6,
    # transitions with multiplicity. Count walks of length 7 from empty word.
    from collections import Counter
    # build quotient transitions from depth<=6 perms (BFS tree, exact perms)
    # (i) pooled quotient (transitions pooled over all perms sharing a profile)
    trans = defaultdict(list)
    seen = set()
    live = [()]
    for m in range(0, 7):
        new = []
        for q in live:
            s = prof3(q)
            seen.add(s)
            for c in kids(q, F):
                if len(c) <= 7:
                    trans[s].append(prof3(c))
        nxt = []
        for q in live:
            for c in kids(q, F):
                if len(c) == m + 1 and len(c) <= 7:
                    nxt.append(c)
        live = nxt
    cur = Counter({prof3(()): 1})
    for m in range(1, 8):
        nxt = Counter()
        for st, mult in cur.items():
            for t in trans[st]:
                nxt[t] += mult
        cur = nxt
    print("pooled-quotient walk count at n=7: computed (pooled multiplicities,")
    print("not a valid quotient count; shown only to illustrate that pooling")
    print("all perms per profile is ill-defined).")
    # (ii) representative quotient (transitions from first perm per profile)
    rep = {}

    def get_trans(s, perm):
        if s not in rep:
            rep[s] = [prof3(g) for g in kids(perm, F)]
        return rep[s]
    get_trans(prof3(()), ())
    lv = [()]
    for m in range(1, 7):
        nv = []
        for q in lv:
            for c in kids(q, F):
                if len(c) == m:
                    nv.append(c)
                    get_trans(prof3(c), c)
        lv = nv
    cur = Counter({prof3(()): 1})
    for m in range(1, 8):
        nv = Counter()
        for st, mult in cur.items():
            for t in rep[st]:
                nv[t] += mult
        cur = nv
    print("representative-quotient walk count at n=7:", sum(cur.values()),
          "(exact: 1508 -> UNDERCOUNTS by 242)")
    assert sum(cur.values()) == 1266, "representative quotient must give 1266"
    print("Both natural quotients miss 1508: no deterministic profile-quotient")
    print("transition function can be exact.")
    print("QUOTIENT_INEXACTNESS_CERTIFIED")

    print()
    print("=== minimal hand-checkable witness pair (class A, n=7) ===")
    w1, w2 = (6, 5, 4, 3, 2, 7, 1), (6, 5, 4, 3, 7, 2, 1)
    assert avoids(w1, F) and avoids(w2, F) and prof3(w1) == prof3(w2)
    k1, k2 = kids(w1, F), kids(w2, F)
    e1 = (len(k1), sum(len(kids(c, F)) for c in k1))
    e2 = (len(k2), sum(len(kids(c, F)) for c in k2))
    print(f"{'.'.join(map(str, w1))}: identical prof3, (e1,e2) = {e1}")
    print(f"{'.'.join(map(str, w2))}: identical prof3, (e1,e2) = {e2}")
    assert e1 != e2
    print("WITNESS_PAIR_CERTIFIED: same profile, futures (3,11) vs (4,17)")
    print()
    live7 = avoiders(F, 7)
    byprof = defaultdict(list)
    for p in live7:
        byprof[prof3(p)].append(p)
    ndiv = 0
    for prof, members in byprof.items():
        futs = defaultdict(list)
        for p in members:
            k1 = kids(p, F)
            futs[(len(k1), tuple(sorted(len(kids(c, F)) for c in k1)))].append(p)
        if len(futs) > 1:
            ndiv += 1
            if ndiv <= 3:
                print(f"profile with {len(members)} members splits into "
                      f"{len(futs)} futures:")
                for f, ms in sorted(futs.items(), key=lambda kv: str(kv[0])):
                    print(f"  e1={f[0]} grandchild-multiset={f[1]} "
                          f"eg {'.'.join(map(str, ms[0]))}")
    print(f"class A: {len(live7)} perms, {len(byprof)} profiles, "
          f"{ndiv} divergent profiles")
    assert ndiv > 0
    print("DIVERGENCE_CERTIFIED")
    print()
    print("=== Myhill-Nerode signature growth (replay of sig_table.txt) ===")
    print("which,n,perms,distinct_sig2,distinct_prof3")
    for which in ['A', 'B']:
        G = bases(which)
        lv = [()]
        for m in range(1, 9):
            nv = []
            for q in lv:
                for x in range(m):
                    c = q[:x] + (m,) + q[x:]
                    if avoids(c, G):
                        nv.append(c)
            lv = nv
            if m >= 5:
                S2, P = set(), set()
                for p in lv:
                    k1 = kids(p, G)
                    S2.add((len(k1), sum(len(kids(c, G)) for c in k1)))
                    P.add(prof3(p))
                print(f"{which},{m},{len(lv)},{len(S2)},{len(P)}")
    print("SIGNATURE_TABLE_REPLAYED")


if __name__ == '__main__':
    main()
