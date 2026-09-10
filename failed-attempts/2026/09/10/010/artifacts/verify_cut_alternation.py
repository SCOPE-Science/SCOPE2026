"""Alternation-rank cap for the cut formula phi1(x;y):=(y<x). (FIXED: value range
large enough to realize genuine strictly monotone sequences.)
On any order-indiscernible sequence (strictly monotone or constant), the truth
set {i : b_i < c} is an initial segment (increasing), final segment (decreasing),
or all/none (constant): at most 2 blocks, i.e. alternation rank <= 2.
By Kaplan-et-al Prop 2.8 (needs alt>=2k to witness dp-rank>=k), a single cut can
never witness dp-rank>=2 alone.
"""
import itertools

def blocks(truth):
    return 1 + sum(1 for a, b in zip(truth, truth[1:]) if a != b)

def is_oi(b):
    def cmp(x, y):
        return (x > y) - (x < y)
    s = {cmp(b[i], b[i + 1]) for i in range(len(b) - 1)}
    return len(s) == 1

worst = 0
worst_ex = None
n_oi = 0
N = 5  # values 0..4, length 4: realizes strict monotone + constant + stutter types
for b in itertools.product(range(N), repeat=4):
    if not is_oi(b):
        continue
    n_oi += 1
    for c in [-1, 0, 1, 2, 3, 4, 5]:
        t = [(x < c) for x in b]
        if blocks(t) > worst:
            worst = blocks(t)
            worst_ex = (b, c, t)
print(f"OI 4-types over 0..4: {n_oi}, max blocks: {worst}, ex: {worst_ex}")
assert worst <= 2
# exhibit saturating case: increasing seq with cut in middle gives exactly 2 blocks
b, c = (0, 1, 2, 3), 2
print("saturating ex:", b, c, [(x < c) for x in b], "blocks =", blocks([(x < c) for x in b]))
print("CUT_ALTERNATION_CAP_OK")
