"""Exact Jones + spans for K0, K1; state circles s_A/s_B; adequacy; Turaev genus.
Convention convA calibrated in cube.py. Also independent writhe/perm checks.
K1 = 16 crossings -> 65536 states, fine.
"""
import sys, json
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-332/output/artifacts")
from cube import count_circles, kauffman_bracket, jones_from_bracket, showV, Kword, writhe, CONV

def perm(word, n):
    p = list(range(n))
    for i, s in word:
        a = i - 1
        p[a], p[a + 1] = p[a + 1], p[a]
    return p

def spanV(V):
    ks = [k for k, c in V.items() if c]
    return (max(ks) - min(ks)) / 4, min(ks) / 4, max(ks) / 4

out = {}
for k in [0, 1]:
    w = Kword(k); n = len(w); wr = writhe(w)
    b = kauffman_bracket(w, 3, CONV)
    V = jones_from_bracket(b, wr)
    # integer-exponent check
    assert all(e % 4 == 0 for e, c in V.items() if c), V
    Vi = {e // 4: c for e, c in V.items() if c}
    sp, lo, hi = spanV(V)
    sA = count_circles(w, 3, tuple(CONV[s] for _, s in w))  # all-A state
    sB = count_circles(w, 3, tuple(1 - CONV[s] for _, s in w))  # all-B state
    det = abs(sum(c * ((-1) ** e) for e, c in Vi.items()))
    out[f"K{k}"] = {"n": n, "writhe": wr, "perm": perm(w, 3),
                    "V": Vi, "span": sp, "lo": lo, "hi": hi,
                    "sA": sA, "sB": sB, "det": det,
                    "gT": (2 + n - sA - sB) // 2 if (2 + n - sA - sB) % 2 == 0 else None,
                    "gTnum": (2 + n - sA - sB) / 2}
    print(f"K{k}: n={n} w={wr} perm={perm(w,3)}")
    print(f"  V(t) = {dict(sorted(Vi.items()))}")
    print(f"  span={sp} lo={lo} hi={hi} det={det} sA={sA} sB={sB} gTnum={(2+n-sA-sB)/2}")

with open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-332/output/artifacts/jones_K0K1.json", "w") as f:
    json.dump(out, f, indent=1)
