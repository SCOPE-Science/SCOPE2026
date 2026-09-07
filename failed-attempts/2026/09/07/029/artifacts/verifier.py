#!/usr/bin/env python3
"""Final verifier for gamma_T(11)=5 (stdlib only, deterministic).
Replays: |N|=41, k=2 counting bound, k=3/k=4 canonical exhaustive UNSAT
(translation-fixed to contain (0,0)), and 5-witness full coverage with table.
Builds coverage from explicit line lists (independent of predicate path).
Run: python3 verifier.py  (~1s)
"""
import itertools, time, json, csv, sys, os


N = 11
FULL = (1 << (N*N)) - 1

def mask_from_lines(q):
    r0, c0 = q
    cells = set()
    for c in range(N):
        cells.add((r0, c))
    for r in range(N):
        cells.add((r, c0))
    for t in range(N):
        cells.add(((r0+t) % N, (c0+t) % N))
    for t in range(N):
        cells.add(((r0+t) % N, (c0-t) % N))
    m = 0
    for (r, c) in cells:
        m |= 1 << (r*N+c)
    return m, cells

def line_type(q, cell):
    r0, c0 = q
    r, c = cell
    if r == r0:
        return "row"
    if c == c0:
        return "col"
    if (r-c) % N == (r0-c0) % N:
        return "diag"
    if (r+c) % N == (r0+c0) % N:
        return "antidiag"
    return None

def main():
    t_all = time.time()
    # 1. neighbourhood size
    masks = {}
    for r in range(N):
        for c in range(N):
            m, cells = mask_from_lines((r, c))
            masks[(r, c)] = m
            assert len(cells) == 41, f"|N({r},{c})|={len(cells)} != 41"
    print(f"[1] |N(q)|=41 for all 121 cells: OK")

    # 2. k=2 counting bound
    assert 2*41 < 121
    print(f"[2] k=2 impossible by union bound 2*41=82<121: OK")

    cells = [(r, c) for r in range(N) for c in range(N) if (r, c) != (0, 0)]
    m0 = masks[(0, 0)]

    # 3. k=3 canonical exhaustive: C(120,2)=7140
    t0 = time.time()
    n3 = 0; max3 = 0; best3 = None
    for a, b in itertools.combinations(cells, 2):
        cov = m0 | masks[a] | masks[b]
        if cov == FULL:
            print(f"FAIL: unexpected 3-dominator {(0,0),a,b}")
            sys.exit(1)
        n3 += 1
        pc = bin(cov).count("1")
        if pc > max3:
            max3 = pc; best3 = (a, b)
    assert n3 == 7140, n3
    print(f"[3] k=3 UNSAT: checked {n3} canonical triples containing (0,0), "
          f"0 dominate, max cover {max3}/121 e.g. {((0,0),)+best3} ({time.time()-t0:.2f}s)")

    # 4. k=4 canonical exhaustive: C(120,3)=280840
    t0 = time.time()
    n4 = 0; max4 = 0; best4 = None
    for a, b, c in itertools.combinations(cells, 3):
        cov = m0 | masks[a] | masks[b] | masks[c]
        if cov == FULL:
            print(f"FAIL: unexpected 4-dominator {(0,0),a,b,c}")
            sys.exit(1)
        n4 += 1
        pc = bin(cov).count("1")
        if pc > max4:
            max4 = pc; best4 = (a, b, c)
    assert n4 == 280840, n4
    print(f"[4] k=4 UNSAT: checked {n4} canonical quadruples containing (0,0), "
          f"0 dominate, max cover {max4}/121 e.g. {((0,0),)+best4} ({time.time()-t0:.2f}s)")

    # 5. 5-witness
    W = [(4,3),(10,1),(8,5),(7,2),(6,10)]
    cov = 0
    for q in W:
        cov |= masks[q]
    assert cov == FULL, "5-witness fails to dominate"
    print(f"[5] 5-witness {W} dominates all 121 cells: OK")
    # canonical translation containing (0,0)
    Wc = sorted([((r-4) % N, (c-3) % N) for (r, c) in W])
    assert Wc == [(0,0),(2,7),(3,10),(4,2),(6,9)], Wc
    cov2 = 0
    for q in Wc:
        cov2 |= masks[q]
    assert cov2 == FULL
    print(f"    canonical translate (by -(4,3)): {Wc} also dominates: OK")

    # 6. coverage table (first-hit assignment)
    rows = []
    for r in range(N):
        for c in range(N):
            hit = None
            for i, q in enumerate(W):
                lt = line_type(q, (r, c))
                if lt is not None:
                    hit = (i, q, lt); break
            assert hit is not None
            rows.append((r, c, hit[0], hit[1][0], hit[1][1], hit[2]))
    outdir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(outdir, "coverage_table.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["r","c","queen_index","queen_r","queen_c","line_type"])
        w.writerows(rows)
    print(f"[6] wrote coverage_table.csv ({len(rows)} rows)")
    print(f"ALL CHECKS PASSED in {time.time()-t_all:.2f}s => gamma_T(11)=5")

if __name__ == "__main__":
    main()
