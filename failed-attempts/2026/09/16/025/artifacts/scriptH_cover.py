"""Script H: PARTITION-COVER lemma test.
For C7-free H, does there EXIST a partition (X,Y) with non-B triples O(n^2)?
Brute-force check on greedy-maximal C7-free graphs at n<=8:
compute min over partitions of |E \ B(X,Y)| and |(B(X,Y)) \ E| structure."""
import itertools, random, sys
from math import comb
sys.path.insert(0, 'output/artifacts')
from scriptE2_fast import build_brec, has_C7_bt, brec_dp
B, CH = brec_dp(60)

def all_partitions(n):
    # representatives under complement: fix 0 in X
    for mask in range(1 << (n-1)):
        X = {0} | {i+1 for i in range(n-1) if mask & (1 << i)}
        Y = set(range(n)) - X
        yield X, Y

def B_edges(X, Y):
    E = set()
    X = sorted(X)
    for i in range(len(X)):
        for j in range(i+1, len(X)):
            for w in Y:
                E.add(tuple(sorted((X[i], X[j], w))))
    return E

def cover_profile(E, n):
    best = None
    for X, Y in all_partitions(n):
        BE = B_edges(X, Y)
        nonB = len(set(E) - BE)
        miss = len(BE - set(E))
        if best is None or nonB < best[0]:
            best = (nonB, miss, X, Y)
    return best

def greedy_instances(E0, n, seeds=(7, 8, 9)):
    out = []
    all3 = [t for t in itertools.combinations(range(n), 3) if t not in E0]
    for s in seeds:
        rng = random.Random(s)
        rng.shuffle(all3)
        cur = set(E0)
        for t in all3:
            cur.add(t)
            if has_C7_bt(cur, n, cap=1):
                cur.discard(t)
        out.append(cur)
    return out

for n in [7, 8]:
    E0, depth, blocks = build_brec(n)
    print(f"== n={n} brec={len(E0)} ==")
    nb, miss, X, Y = cover_profile(E0, n)
    print(f"  B_rec itself: min-nonB={nb} miss={miss} X={sorted(X)} Y={sorted(Y)}")
    for cur in greedy_instances(E0, n):
        nb, miss, X, Y = cover_profile(cur, n)
        print(f"  augmented |E|={len(cur)}: min-nonB={nb} miss={miss} X={sorted(X)} Y={sorted(Y)}")
