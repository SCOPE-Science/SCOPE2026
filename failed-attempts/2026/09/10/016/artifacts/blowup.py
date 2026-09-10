"""Counterexample hunt: clique blow-ups of C5/C8 (preserve claw-free, often
preserve nu) + line graphs with nu=2. Look for reg > 2*nu."""
import sys
sys.path.insert(0, 'output/artifacts')
from clawreg import adj_from_edges, has_claw, induced_matching_number, reg_SI_modp


def blowup(base_n, base_edges, sizes):
    # sizes[v] = clique size replacing v; join cliques iff base edge
    n = sum(sizes)
    blocks = []
    s = 0
    for v in range(base_n):
        blocks.append(list(range(s, s + sizes[v])))
        s += sizes[v]
    be = set()
    for (a, b) in base_edges:
        be.add((min(a, b), max(a, b)))
    edges = []
    for v in range(base_n):
        B = blocks[v]
        for i in range(len(B)):
            for j in range(i + 1, len(B)):
                edges.append((B[i], B[j]))
        for w in range(v + 1, base_n):
            if (v, w) in be:
                for a in B:
                    for b in blocks[w]:
                        edges.append((min(a, b), max(a, b)))
    return n, adj_from_edges(n, edges)


def cycle_edges(n):
    return [(i, (i + 1) % n) for i in range(n)]


if __name__ == "__main__":
    tests = []
    # C5 blow-ups
    for sizes in [(2, 1, 1, 1, 1), (3, 1, 1, 1, 1), (4, 1, 1, 1, 1),
                  (2, 2, 1, 1, 1), (3, 3, 1, 1, 1), (2, 2, 2, 1, 1),
                  (2, 2, 2, 2, 2), (3, 3, 3, 3, 3), (5, 1, 1, 1, 1)]:
        tests.append(("C5" + str(sizes), 5, cycle_edges(5), sizes))
    # C8 blow-ups
    for sizes in [(2, 1, 1, 1, 1, 1, 1, 1), (3, 1, 1, 1, 1, 1, 1, 1),
                  (2, 2, 2, 2, 1, 1, 1, 1), (4, 1, 1, 1, 1, 1, 1, 1)]:
        tests.append(("C8" + str(sizes), 8, cycle_edges(8), sizes))
    for (tag, bn, be, sizes) in tests:
        n, adj = blowup(bn, be, sizes)
        claw = has_claw(n, adj)
        nu = induced_matching_number(n, adj)
        reg = reg_SI_modp(n, adj)
        flag = " <-- INTEREST" if reg > 2 * nu else ""
        print("%s n=%d clawfree=%s nu=%d reg=%d 2nu=%d%s" % (tag, n, (not claw), nu, reg, 2 * nu, flag))
