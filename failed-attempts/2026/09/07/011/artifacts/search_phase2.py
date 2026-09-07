"""Phase 2: within Jones-collision classes, prefilter (alternating, span==m, prime),
then Alexander to find distinct-Alexander pairs."""
import sys, json, time
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-07/output/artifacts")
from braid_toolkit import (is_alternating_diagram, is_diagram_prime, jones_span, alexander_poly)

with open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-07/output/artifacts/jones_collisions.json") as f:
    data = json.load(f)

t0 = time.time()
report = []
found = None
# lexicographic order by Jones string then (audit plan: first non-mutant closable class)
def jkey(c):
    return str(sorted(c["jones"].items()))
classes = sorted(data["classes"], key=jkey)
print(f"scanning {len(classes)} collision classes in lexicographic Jones order", flush=True)
for ci, c in enumerate(classes):
    jp = {int(k): v for k, v in c["jones"].items()}
    span = max(jp) - min(jp)
    # prefilter members
    good = []
    for mem in c["members"]:
        s = mem["s"]; w = [(int(a), int(b)) for (a, b) in mem["word"]]
        m = len(w)
        if jones_span(jp) != m:
            continue  # not reduced/minimal -> skip (need span==m for minimality cert)
        if not is_alternating_diagram(s, w):
            continue
        if not is_diagram_prime(s, w):
            continue
        good.append((s, w))
    if len(good) < 2:
        continue
    # Alexander on good members (cap 12 per class for time)
    alex = {}
    for (s, w) in good[:12]:
        try:
            ap = alexander_poly(s, w)
        except Exception as e:
            continue
        alex.setdefault(tuple(sorted(ap.items())), []).append((s, w))
    rep = {"jones": jp, "n_good": len(good),
           "alex_groups": [{"alex": dict(g), "count": len(v)} for g, v in alex.items()]}
    report.append({"class": ci, **rep})
    print(f"class {ci}: jones={sorted(jp.items())} good={len(good)} alex-groups={len(alex)}", flush=True)
    if len(alex) >= 2 and found is None:
        # freeze lexicographically first pair with distinct Alexander
        g = sorted(alex.items(), key=lambda kv: str(kv[0]))
        (s1, w1) = g[0][1][0]; (s2, w2) = g[1][1][0]
        found = {"class": ci, "jones": jp,
                 "A": {"s": s1, "word": w1, "alex": dict(g[0][0])},
                 "B": {"s": s2, "word": w2, "alex": dict(g[1][0])}}
        print("  *** FOUND PAIR ***", flush=True)
        # keep scanning to complete census of good classes? continue for full gap table (bounded)
with open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-07/output/artifacts/phase2_report.json", "w") as f:
    json.dump({"report": report, "found": found}, f, default=str)
print("FOUND:", json.dumps(found, default=str)[:2000] if found else None)
print(f"done t={time.time()-t0:.1f}s")
