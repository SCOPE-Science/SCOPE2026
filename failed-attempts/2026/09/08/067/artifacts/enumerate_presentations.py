#!/usr/bin/env python3
"""Step 1: enumerate canonical representatives of 2-generator 2-relator
presentations <a,b | w1, w2> with |w1|+|w2| <= 8.

Words over {a,b,A,B} (A=a^-1, B=b^-1), cyclically reduced, nonempty.
Canonical form under: 8 signed generator renamings (swap a/b, invert a/b),
cyclic rotation, inversion of each relator, swapping the two relators.
Output: output/artifacts/presentations.csv
"""
import csv, itertools, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "presentations.csv")

INV = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}

def all_cyc_red(length):
    """All cyclically reduced words of given length >= 1 as strings."""
    alpha = ('a', 'b', 'A', 'B')
    if length == 1:
        return list(alpha)
    out = []
    def rec(prefix):
        if len(prefix) == length:
            if prefix[-1] != INV[prefix[0]]:
                out.append(''.join(prefix))
            return
        for g in alpha:
            if g != INV[prefix[-1]]:
                rec(prefix + [g])
    for g in alpha:
        rec([g])
    return out

def rotations(w):
    n = len(w)
    return [w[i:] + w[:i] for i in range(n)]

def invert_word(w):
    return ''.join(INV[g] for g in reversed(w))

def canon_relator(w, m):
    """Canonical form of a single relator under rotation/inversion after renaming map m."""
    mw = ''.join(m(g) for g in w)
    cands = rotations(mw) + rotations(invert_word(mw))
    return min(cands)

def signed_perms():
    """The 8 signed permutations of {a,b}: swap/no-swap x invert-a x invert-b."""
    maps = []
    for swap in (False, True):
        for sa in (False, True):
            for sb in (False, True):
                def m(g, swap=swap, sa=sa, sb=sb):
                    base = {'a': 'b', 'b': 'a', 'A': 'B', 'B': 'A'}[g] if swap else g
                    low = base.lower()
                    inv = (sa if low == 'a' else sb)
                    if inv:
                        base = INV[base]
                    return base
                maps.append(m)
    return maps

MAPS = signed_perms()

def canon_pair(w1, w2):
    best = None
    for m in MAPS:
        c1 = canon_relator(w1, m)
        c2 = canon_relator(w2, m)
        key = (c1, c2) if c1 <= c2 else (c2, c1)
        if best is None or key < best:
            best = key
    return best

def main():
    words = {}  # length -> list
    for L in range(1, 8):
        words[L] = all_cyc_red(L)
        print(f"length {L}: {len(words[L])} cyclically reduced words", flush=True)
    seen = {}
    for L1 in range(1, 8):
        for L2 in range(1, 9 - L1):
            for w1 in words[L1]:
                for w2 in words[L2]:
                    key = canon_pair(w1, w2)
                    if key not in seen:
                        seen[key] = (len(key[0]) + len(key[1]), key)
    reps = sorted(seen.values())
    with open(OUT, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['id', 'w1', 'w2', 'l1', 'l2', 'ltot'])
        for i, (ltot, (c1, c2)) in enumerate(reps):
            w.writerow([i, c1, c2, len(c1), len(c2), ltot])
    print(f"TOTAL canonical representatives: {len(reps)}")

if __name__ == '__main__':
    main()
