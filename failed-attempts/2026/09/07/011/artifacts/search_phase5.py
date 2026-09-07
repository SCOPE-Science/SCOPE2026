"""Phase 5: 2-component link search. Group non-split 2-comp closures by general Jones;
prefilter alternating + span==m + prime; flag same-Jones different-lk pairs."""
import sys, random, json, time
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-07/output/artifacts")
from braid_toolkit import (n_components, jones_poly_general, linking_number, is_split_diagram,
                            is_alternating_diagram, is_diagram_prime)

random.seed(31337)
def rand_word(s, m):
    while True:
        w = [(random.randint(1, s - 1), random.choice((1, -1))) for _ in range(m)]
        bad = any(w[k][0] == w[k+1][0] and w[k][1] == -w[k+1][1] for k in range(m - 1))
        if not bad:
            return w

def jkey(jp):
    return tuple(sorted(((str(k), v) for k, v in jp.items())))

plan = [(2, 4, 800), (2, 6, 800), (2, 8, 800), (2, 10, 800),
        (3, 5, 1500), (3, 6, 1500), (3, 7, 1500), (3, 8, 1500), (3, 9, 1200), (3, 10, 1200),
        (4, 6, 1500), (4, 7, 1500), (4, 8, 1500), (4, 9, 1200), (4, 10, 1000), (4, 11, 800)]
classes = {}
nl = 0; nw = 0
t0 = time.time()
for (s, m, cnt) in plan:
    for _ in range(cnt):
        w = rand_word(s, m); nw += 1
        if n_components(s, w) != 2:
            continue
        if is_split_diagram(s, w):
            continue
        nl += 1
        try:
            jp = jones_poly_general(s, w)
        except Exception:
            continue
        classes.setdefault(jkey(jp), []).append((s, tuple(w), {str(k): v for k, v in jp.items()}))
    print(f"s={s} m={m} x{cnt}: words={nw} links={nl} classes={len(classes)} t={time.time()-t0:.1f}s", flush=True)

coll = {k: v for k, v in classes.items() if len(v) >= 2}
print(f"TOTAL words={nw} links={nl} collision-classes={len(coll)}")
# analyze: prefilter + lk groups
found = None
rep = []
for ci, (k, v) in enumerate(sorted(coll.items(), key=lambda kv: kv[0])):
    good = []
    for (s, w, js) in v:
        w = list(w); m = len(w)
        jp = {eval(kk): vv for kk, vv in js.items()}
        span = max(jp) - min(jp)
        if span != m:
            continue
        if not is_alternating_diagram(s, w):
            continue
        if is_split_diagram(s, w):
            continue
        if not is_diagram_prime(s, w):
            continue
        nc, _, lk = linking_number(s, w)
        good.append((s, w, str(lk)))
    if len(good) >= 2:
        lks = {}
        for (s, w, lk) in good[:16]:
            lks.setdefault(lk, []).append((s, w))
        rep.append({"jones": v[0][2], "n_good": len(good), "lk_groups": {lk: len(x) for lk, x in lks.items()}})
        print(f"class {ci}: jones={v[0][2]} good={len(good)} lk={ {lk: len(x) for lk, x in lks.items()} }", flush=True)
        if len(lks) >= 2 and found is None:
            g = sorted(lks.items())
            found = {"jones": v[0][2], "A": {"s": g[0][1][0][0], "word": g[0][1][0][1], "lk": g[0][0]},
                     "B": {"s": g[1][1][0][0], "word": g[1][1][0][1], "lk": g[1][0]}}
            print("  *** LINK PAIR FOUND ***", flush=True)
with open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-07/output/artifacts/phase5_report.json", "w") as f:
    json.dump({"words": nw, "links": nl, "n_coll": len(coll), "good_classes": rep, "found": found}, f, default=str)
print("FOUND:", json.dumps(found, default=str)[:1500] if found else None)
print(f"done t={time.time()-t0:.1f}s")
