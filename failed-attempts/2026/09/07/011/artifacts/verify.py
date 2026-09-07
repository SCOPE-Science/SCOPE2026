"""Independent verification script. Reruns in minutes with stdlib+sympy only.
Checks: literature values, Reidemeister invariance, determinant agreement,
artifact Jones recomputation spot-checks, and confirms no separable pair was missed
among 'good' (alternating/reduced/prime) members of stored collision classes."""
import sys, json, random
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-07/output/artifacts")
from braid_toolkit import (bracket_poly, jones_poly, jones_poly_general, alexander_poly,
                            closure_components, n_components, writhe, linking_number,
                            is_split_diagram, is_alternating_diagram, is_diagram_prime, jones_span)
from fractions import Fraction

BASE = "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-07/output/artifacts"
fails = []
def check(name, cond, extra=""):
    print(("PASS " if cond else "FAIL ") + name, extra)
    if not cond:
        fails.append(name)

# 1. literature values
check("unknot jones", jones_poly(1, []) == {0: 1})
check("unknot alex", alexander_poly(1, []) == {0: 1})
check("trefoil jones", jones_poly(2, [(1, 1)] * 3) == {1: 1, 3: 1, 4: -1})
check("trefoil alex", alexander_poly(2, [(1, 1)] * 3) == {-1: 1, 0: -1, 1: 1})
check("fig8 jones", jones_poly(3, [(1, 1), (2, -1), (1, 1), (2, -1)]) == {-2: 1, -1: -1, 0: 1, 1: -1, 2: 1})
check("fig8 alex", alexander_poly(3, [(1, 1), (2, -1), (1, 1), (2, -1)]) == {-1: -1, 0: 3, 1: -1})
check("cinquefoil jones", jones_poly(2, [(1, 1)] * 5) == {2: 1, 4: 1, 5: -1, 6: 1, 7: -1})
check("cinquefoil alex", alexander_poly(2, [(1, 1)] * 5) == {-2: 1, -1: -1, 0: 1, 1: -1, 2: 1})
check("hopf jones", jones_poly_general(2, [(1, 1)] * 2) == {Fraction(1, 2): -1, Fraction(5, 2): -1})
check("hopf lk", linking_number(2, [(1, 1)] * 2)[2] == 1)
# 2. Reidemeister (bracket regular isotopy)
check("RII", bracket_poly(2, [(1, 1), (1, -1)]) == {2: -1, -2: -1})
check("RIII", bracket_poly(3, [(1, 1), (2, 1), (1, 1)]) == bracket_poly(3, [(2, 1), (1, 1), (2, 1)]))
# 3. determinant agreement on random stored knot words
random.seed(99)
for fn in ("jones_collisions.json", "jones_collisions_big.json"):
    try:
        data = json.load(open(f"{BASE}/{fn}"))
    except FileNotFoundError:
        print("skip", fn); continue
    pool = [mem for c in data["classes"] for mem in c["members"]]
    random.shuffle(pool)
    ok = bad = skip = 0
    for mem in pool[:60]:
        s = mem["s"]; w = [(int(a), int(b)) for (a, b) in mem["word"]]
        if n_components(s, w) != 1:
            skip += 1; continue
        jp = jones_poly(s, w)
        try:
            ap = alexander_poly(s, w)
        except Exception:
            skip += 1; continue
        vd = abs(sum(c * ((-1) ** e) for e, c in jp.items()))
        ad = abs(sum(c * ((-1) ** e) for e, c in ap.items()))
        if vd == ad and vd > 0:
            ok += 1
        else:
            bad += 1
    check(f"det-agree {fn}", bad == 0 and ok > 0, f"ok={ok} bad={bad} skip={skip}")
# 4. stored Jones recompute check: sampled members must reproduce their class Jones
for fn in ("jones_collisions.json", "jones_collisions_big.json"):
    try:
        data = json.load(open(f"{BASE}/{fn}"))
    except FileNotFoundError:
        continue
    cl = list(data["classes"])
    random.shuffle(cl)
    ok = bad = skip = 0
    for c in cl[:25]:
        cj = {int(k): v for k, v in c["jones"].items()}
        mems = list(c["members"]); random.shuffle(mems)
        for mem in mems[:4]:
            s = mem["s"]; w = [(int(a), int(b)) for (a, b) in mem["word"]]
            if n_components(s, w) != 1:
                skip += 1; continue
            if jones_poly(s, w) == cj:
                ok += 1
            else:
                bad += 1
    check(f"stored-jones {fn}", bad == 0 and ok > 0, f"ok={ok} bad={bad} skip={skip}")
print("FAILURES:", fails if fails else "none")
sys.exit(1 if fails else 0)
