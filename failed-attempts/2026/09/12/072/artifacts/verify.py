"""Independent verifier for the height-3/complexity-1 certificate.
Reads output/artifacts/certificate.json, recomputes everything from generators.
Usage: python3 output/artifacts/verify.py
"""
import json, sys, os, itertools
here = os.path.dirname(os.path.abspath(__file__))
base = os.path.dirname(os.path.dirname(here)) if False else None
sys.path.insert(0, os.path.join(os.path.dirname(here)))
sys.path.insert(0, os.getcwd())
from toolkit import (compose, identity, monoid_closure, power, is_aperiodic,
                     all_images, skeleton, bricks, check_partition, stabilizer,
                     holonomy_group, holonomy_height, build_wreath)

def main():
    with open(os.path.join(here, "certificate.json")) as f:
        cert = json.load(f)
    n = len(cert["Q"])
    gens = [tuple(g["map"]) for g in cert["generators"]]
    assert n == 7 and len(gens) == 3
    S = monoid_closure(n, gens)
    assert len(S) == cert["monoid_size"] == 53, f"size {len(S)}"
    assert set(tuple(s) for s in cert["monoid_elements"]) == set(S)
    # closure check
    for a in S:
        for g in gens:
            assert compose(a, g) in S and compose(g, a) in S
    # faithfulness: generators distinct, non-identity present
    assert len(set(gens)) == 3
    # non-aperiodicity: stored involution
    a = tuple(cert["involution"])
    assert a in S and a != identity(n) and compose(a, a) == identity(n)
    assert power(a, n, n) != power(a, n + 1, n)
    assert not is_aperiodic(S, n)
    # skeleton + holonomy
    h, levels, images, reps = holonomy_height(S, n)
    assert h == 3, f"height {h}"
    assert h == cert["holonomy_height"]
    orders = sorted([o for _, o, _ in levels])
    assert orders.count(2) == 3 and all(o in (1, 2) for o in orders), orders
    assert len(reps) == len(cert["skeleton"])
    for entry, rep in zip(cert["skeleton"], reps):
        assert tuple(entry["rep"]) == tuple(sorted(rep))
        order, G, part, k = holonomy_group(rep, images, S)
        assert order == entry["holonomy_order"] and k == entry["n_bricks"]
        assert sorted(tuple(g) for g in entry["holonomy_group"]) == G
    # top rep singleton bricks
    top = max(reps, key=len)
    assert set(top) == set(range(n))
    _, _, part, _ = holonomy_group(top, images, S)
    assert all(len(b) == 1 for b in part), "top bricks not singleton"
    # divisor embedding: check each stored wreath cover acts correctly + labels valid
    W = build_wreath()
    Wacts = [x[0] for x in W]
    U2 = {(0, 1), (0, 0), (1, 1)}
    phi = cert["phi"]
    assert sorted(phi) == [1, 2, 3, 4, 5, 6, 7] and len(set(phi)) == 7
    for entry in cert["witness"]:
        s = tuple(entry["map"])
        assert s in gens
        assert len(entry["covers"]) == n
        for row in entry["covers"]:
            q = row["q"]
            w = tuple(row["w_action"])
            assert w in Wacts, "cover not in wreath"
            assert w[phi[q]] == phi[s[q]], f"cover fails at q={q}"
            lab = row["w_label"]
            assert tuple(lab["a"]) in U2 and all(tuple(b) in U2 for b in lab["beta"])
            assert tuple(lab["alpha"]) in [(0, 0), (0, 1), (1, 0), (1, 1)]
            # recompute action from label
            xa, alpha, beta = tuple(lab["a"]), tuple(lab["alpha"]), [tuple(b) for b in lab["beta"]]
            for x in (0, 1):
                for y in (0, 1):
                    for z in (0, 1):
                        t = x * 4 + y * 2 + z
                        t2 = xa[x] * 4 + (y ^ alpha[x]) * 2 + beta[x * 2 + y][z]
                        assert w[t] == t2, "label/action mismatch"
    # word-lift consistency over whole monoid
    covers = {}
    for entry in cert["witness"]:
        gi = [tuple(g["map"]) for g in cert["generators"]].index(tuple(entry["map"]))
        for row in entry["covers"]:
            covers[(gi, row["q"])] = tuple(row["w_action"])
    from collections import deque
    words = {identity(n): ()}
    dq = deque([identity(n)])
    while dq:
        cur = dq.popleft()
        for gi, g in enumerate(gens):
            nxt = compose(cur, g)
            if nxt not in words:
                words[nxt] = words[cur] + (gi,)
                dq.append(nxt)
    assert len(words) == 53
    for s, word in words.items():
        for q in range(n):
            t, qq = phi[q], q
            for gi in word:
                t = covers[(gi, qq)][t]
                qq = gens[gi][qq]
            assert t == phi[s[q]], "word lift fails"
    # U2 aperiodic, C2 group (complexity scaffolding)
    assert is_aperiodic(set(U2) | {(0, 1)}, 2)
    print("ALL CHECKS PASSED: |S|=53, height=3, involution ok, division lifts ok.")

if __name__ == "__main__":
    main()
