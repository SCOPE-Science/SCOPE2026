"""Phase 1: Jones-only enumeration/grouping (cheap), then Alexander only on collision members."""
import sys, itertools, random, json, time
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-07/output/artifacts")
from braid_toolkit import (closure_components, n_components, writhe, jones_poly, poly_key,
                            is_alternating_diagram, is_diagram_prime, jones_span, alexander_poly)

def gen_words(s, m):
    syms = [(i, e) for i in range(1, s) for e in (1, -1)]
    if m == 0:
        yield [];
        return
    def rec(cur):
        if len(cur) == m:
            yield list(cur); return
        for sym in syms:
            if cur and cur[-1][0] == sym[0] and cur[-1][1] == -sym[1]:
                continue  # skip immediate RII (non-reduced)
            cur.append(sym)
            yield from rec(cur)
            cur.pop()
    yield from rec([])

def is_knot(s, w):
    return n_components(s, w) == 1

t0 = time.time()
classes = {}  # jones_key -> list of (s, word)
stats = {"total": 0, "knots": 0}
# systematic 3-strand lengths 1..8
for m in range(1, 9):
    n = 0
    for w in gen_words(3, m):
        stats["total"] += 1; n += 1
        if not is_knot(3, w):
            continue
        stats["knots"] += 1
        try:
            jp = jones_poly(3, w)
        except ValueError:
            continue
        classes.setdefault(poly_key(jp), []).append((3, tuple(w), dict(jp)))
    print(f"s=3 m={m}: words={n} knots-so-far={stats['knots']} classes={len(classes)} t={time.time()-t0:.1f}s", flush=True)

# random 3-strand lengths 9..12 + 4-strand lengths 6..12
random.seed(20260907)
def rand_word(s, m):
    while True:
        w = [(random.randint(1, s - 1), random.choice((1, -1))) for _ in range(m)]
        bad = any(w[k][0] == w[k+1][0] and w[k][1] == -w[k+1][1] for k in range(m - 1))
        if not bad:
            return w
N = 0
for (s, m, cnt) in [(3, 9, 1500), (3, 10, 1500), (3, 11, 800), (3, 12, 800), (4, 8, 1200), (4, 9, 1000), (4, 10, 800), (4, 11, 500), (4, 12, 500)]:
    for _ in range(cnt):
        w = rand_word(s, m)
        stats["total"] += 1
        if not is_knot(s, w):
            continue
        stats["knots"] += 1
        try:
            jp = jones_poly(s, w)
        except ValueError:
            continue
        classes.setdefault(poly_key(jp), []).append((s, tuple(w), dict(jp)))
        N += 1
    print(f"random s={s} m={m} x{cnt}: knots-so-far={stats['knots']} classes={len(classes)} t={time.time()-t0:.1f}s", flush=True)

coll = {k: v for k, v in classes.items() if len(v) >= 2}
print(f"TOTAL words={stats['total']} knots={stats['knots']} jones-classes={len(classes)} collision-classes={len(coll)}")
# save collision classes (Jones only)
out = []
for k, v in coll.items():
    out.append({"jones": dict(v[0][2]), "members": [{"s": s, "word": [list(x) for x in w]} for (s, w, _) in v]})
with open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-07/output/artifacts/jones_collisions.json", "w") as f:
    json.dump({"stats": stats, "n_classes": len(out), "classes": out}, f)
print("wrote jones_collisions.json")
# print small summary: class sizes
sizes = sorted([len(v) for v in coll.values()], reverse=True)[:20]
print("top class sizes:", sizes)
