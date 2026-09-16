"""Script F: where does greedy surplus sit? Locate extra triples (inside V1? crossing? deep?).
Also test random 2-level B variants and 'B_rec + sparse random' max sizes at n=9..14."""
import random, itertools, sys
from math import comb
sys.path.insert(0, 'output/artifacts')
from scriptE2_fast import build_brec, has_C7_bt, brec_dp
B, CH = brec_dp(60)

def greedy_max(E, n, seed=7, trials=60):
    all3 = [t for t in itertools.combinations(range(n), 3) if t not in E]
    rng = random.Random(seed)
    best = (len(E), [])
    for _ in range(trials):
        rng.shuffle(all3)
        cur = set(E)
        for t in all3:
            cur.add(t)
            if has_C7_bt(cur, n, cap=1):
                cur.discard(t)
        if len(cur) > best[0]: best = (len(cur), sorted(set(cur) - set(E)))
    return best

for n in [7, 8, 9]:
    E, depth, blocks = build_brec(n)
    V1 = set(blocks[0])
    size, extras = greedy_max(E, n, trials=30 if n > 8 else 200)
    def kind(t):
        s = sum(1 for v in t if v in V1)
        return f"inV1={s}"
    from collections import Counter
    print(f"n={n} brec={len(E)} max={size} gap={size-len(E)} kinds={dict(Counter(kind(t) for t in extras))}")
    print("  extras:", extras)
