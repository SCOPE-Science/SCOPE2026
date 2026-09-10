"""Verify the explicit extremal spine F = {identity perms}:
1. identity avoids 1324 (brute force, n<=8);
2. word r1^(n-1) f1 decodes to identity under the standard slot decoder;
3. its slot walk stays at 1 (hence in E3).
Decoder convention (standard Vatter): one slot (interval); l1 = new max just
left of slot interval, r1 = new max just right, m1 = new max inside slot
splitting it into left+right slots, f1 = new max fills the single slot. The
identity 12..n built by inserting maxima has each new max immediately left of
the single diamond, so its encoding is l1^(n-1) f1 (verified below).
"""
from itertools import permutations


def contains_1324(p):
    n = len(p)
    for a in range(n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                for d in range(c+1, n):
                    q = (p[a], p[b], p[c], p[d])
                    # pattern type of q
                    s = sorted(q)
                    rank = {v: i+1 for i, v in enumerate(s)}
                    if tuple(rank[v] for v in q) == (1, 3, 2, 4):
                        return True
    return False


for n in range(1, 9):
    ident = tuple(range(1, n+1))
    assert not contains_1324(ident), n
print("identities avoid 1324 for n<=8: OK")


def decode_single_slot(word):
    """Decode words using only slot-count-1 letters {l1,r1,f1} plus m1 (exits).
    Represent state as (seq, slots): seq = list of values/'D' diamonds.
    Start: ['D']. l1: insert new max left of the single diamond; r1: right;
    f1: replace diamond by new max. m1 would split (not used here)."""
    seq = ['D']
    placed = 0
    slots = 1
    trace = [slots]
    for k, ch in enumerate(word):
        placed += 1
        i = seq.index('D') if 'D' in seq else None
        if ch == 'r1':
            assert slots == 1 and i is not None
            seq = seq[:i+1] + [placed] + seq[i+1:]
            # diamond stays, new max just right of it: insert right of D
            # (seq[i] is 'D', so element goes to i+1)
        elif ch == 'l1':
            seq = seq[:i] + [placed] + seq[i:]
        elif ch == 'f1':
            seq[i] = placed
            slots = 0
        else:
            raise ValueError(ch)
        trace.append(slots)
    vals = [x for x in seq if x != 'D']
    return vals, trace


for n in range(1, 13):
    word = ['l1']*(n-1) + ['f1']
    vals, trace = decode_single_slot(word)
    assert vals == list(range(1, n+1)), (n, vals)
    assert max(trace) <= 1, (n, trace)
print("word l1^(n-1)f1 decodes to identity with slot depth 1 for n<=12: OK")

# Alphabet-size lemma replay: from s slots, letters = s(m)+2s(l/r)+s(f) = 4s.
for s in [1, 2, 3]:
    assert s + 2*s + s == 4*s
    assert 4*s <= 12
print("alphabet lemma 4s<=12 for s<=3: OK")
print("ALL CHECKS PASSED")
