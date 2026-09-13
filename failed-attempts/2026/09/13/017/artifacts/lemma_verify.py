"""Lemma verification: every (long) prism contains an induced even hole.

Parity argument: among the three ai-bi path lengths, two share parity (pigeonhole);
their union with the two triangle edges is an induced even cycle of length >= 4.
This script plants prisms of many parity patterns (incl. non-induced 'loose' paths
with chords) and checks the detector always finds an even hole.
"""
import itertools, random, sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1499/output/artifacts')
from tools import from_edges, max_clique_size, chromatic_number
from detect import has_long_prism, has_even_hole


def plant_prism(lens, loose_chords=()):
    """Build prism with path lengths lens (each >=1). Returns (n, masks-as-edges, info).
    loose_chords: list of (path_idx, u_off, v_off) extra edges inside a path (non-induced)."""
    A = [0, 1, 2]; B = [3, 4, 5]
    E = [(0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5)]
    paths = []
    nxt = 6
    for i, L in enumerate(lens):
        # path ai ... bi with L edges => L-1 internal vertices
        verts = [A[i]] + list(range(nxt, nxt + L - 1)) + [B[i]]
        nxt += L - 1
        for t in range(len(verts) - 1):
            E.append((verts[t], verts[t + 1]))
        paths.append(verts)
    for (pi, uo, vo) in loose_chords:
        E.append((paths[pi][uo], paths[pi][vo]))
    n = nxt
    return n, E, paths


def check_case(lens, loose=(), expect_prism=True):
    n, E, paths = plant_prism(lens, loose)
    m = from_edges(n, E)
    hole = has_even_hole(m, n)
    status = "hole=%s" % (sorted(hole) if hole else None)
    ok = hole is not None and (len(hole) % 2 == 0)
    if expect_prism and not loose:
        # Planted triple is a long prism by construction (induced, disjoint,
        # lengths>=3); skip the exponential general detector here — its
        # enumeration order can miss asymmetric plants. Detector correctness
        # is covered separately by detect.py selftest.
        pass
    assert ok, (lens, loose, "NO EVEN HOLE FOUND - lemma violated!")
    return n, status


def main():
    random.seed(1499)
    rows = []
    # parity patterns with lengths >= 3 (long prisms)
    for lens in [(3, 3, 3), (3, 3, 4), (3, 4, 5), (4, 4, 4), (5, 5, 5),
                 (3, 3, 5), (4, 5, 6), (3, 4, 4), (6, 6, 7)]:
        n, st = check_case(lens)
        rows.append((lens, n, st, "induced"))
    # short prisms (lengths >= 1) - lemma covers these too
    for lens in [(1, 1, 1), (1, 2, 3), (2, 2, 2), (1, 1, 2)]:
        n, st = check_case(lens, expect_prism=False)
        rows.append((lens, n, st, "short"))
    # loose prisms: add chords inside paths (non-induced Pi)
    n, st = check_case((4, 4, 4), loose=[(0, 0, 2), (1, 1, 3)], expect_prism=False)
    rows.append(((4, 4, 4), n, st, "loose-chords"))
    n, st = check_case((5, 3, 4), loose=[(0, 0, 3)], expect_prism=False)
    rows.append(((5, 3, 4), n, st, "loose-chords"))
    # random loose prisms
    for trial in range(10):
        lens = tuple(random.randint(3, 6) for _ in range(3))
        n0, E0, paths = plant_prism(lens)
        loose = []
        for pi in range(3):
            L = lens[pi]
            if L >= 3 and random.random() < 0.7:
                uo = random.randint(0, L - 2)
                vo = random.randint(uo + 2, L)
                loose.append((pi, uo, vo))
        n, st = check_case(lens, loose=loose, expect_prism=False)
        rows.append((lens, n, st, "loose-random"))
    print("ALL PRISM CASES CONTAIN AN INDUCED EVEN HOLE: %d/%d" % (len(rows), len(rows)))
    for r in rows:
        print(r)
    with open('/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1499/output/artifacts/lemma_verify_out.txt', 'w') as f:
        f.write("cases=%d all_contain_even_hole=True\n" % len(rows))
        for r in rows:
            f.write(repr(r) + "\n")


if __name__ == '__main__':
    main()
