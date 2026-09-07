"""Phase 3 (expanded): big random braid search, 4/5/6 strands, lengths 9..12.
Jones-only grouping -> collisions JSON. Alternating prefilter to save time? No:
keep all knots (filter later) to allow full gap table."""
import sys, random, json, time
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-07/output/artifacts")
from braid_toolkit import n_components, jones_poly, poly_key

random.seed(918273645)
def rand_word(s, m):
    while True:
        w = [(random.randint(1, s - 1), random.choice((1, -1))) for _ in range(m)]
        bad = any(w[k][0] == w[k+1][0] and w[k][1] == -w[k+1][1] for k in range(m - 1))
        if not bad:
            return w

plan = [(4, 9, 2500), (4, 10, 2500), (4, 11, 1500), (4, 12, 1500),
        (5, 9, 2000), (5, 10, 2000), (5, 11, 1200), (5, 12, 1200),
        (6, 9, 1200), (6, 10, 1200), (6, 11, 800), (6, 12, 800)]
classes = {}
nk = 0; nw = 0
t0 = time.time()
for (s, m, cnt) in plan:
    for _ in range(cnt):
        w = rand_word(s, m); nw += 1
        if n_components(s, w) != 1:
            continue
        nk += 1
        try:
            jp = jones_poly(s, w)
        except ValueError:
            continue
        classes.setdefault(poly_key(jp), []).append((s, tuple(w), dict(jp)))
    print(f"s={s} m={m} x{cnt}: words={nw} knots={nk} classes={len(classes)} t={time.time()-t0:.1f}s", flush=True)
coll = {k: v for k, v in classes.items() if len(v) >= 2}
out = [{"jones": dict(v[0][2]), "members": [{"s": s, "word": [list(x) for x in w]} for (s, w, _) in v]} for k, v in coll.items()]
with open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-07/output/artifacts/jones_collisions_big.json", "w") as f:
    json.dump({"words": nw, "knots": nk, "n_classes": len(out), "classes": out}, f)
print(f"DONE words={nw} knots={nk} collision-classes={len(out)} t={time.time()-t0:.1f}s")
