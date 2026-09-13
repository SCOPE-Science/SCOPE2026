"""Compositional + random search for even-hole-free G with chi > max(3, ceil(3w/2)).

Only EHF-guaranteed constructions (clique-blowups, joins with cliques) plus
EHF-filtered random graphs. Every candidate is independently EHF-verified.
"""
import itertools, random, sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1499/output/artifacts')
from tools import from_edges, max_clique_size, chromatic_number, greedy_upper
from screen import chordless_holes
import networkx as nx


def check(masks, n, tag):
    even, total = chordless_holes(masks, n, cap_even=1, cap_total=10**9)
    ehf = (len(even) == 0)
    w = max_clique_size(masks, n)
    if n <= 15:
        chi = chromatic_number(masks, n)
    else:
        chi = greedy_upper(masks, n)
    bound = max(3, -(-3 * w // 2))
    viol = ehf and isinstance(chi, int) and chi > bound
    print("%-34s n=%-3d EHF=%-5s w=%d chi=%s bound=%d %s" %
          (tag, n, ehf, w, chi, bound, "*** VIOLATION ***" if viol else ""), flush=True)
    return viol, (tag, n, ehf, w, chi, bound)


def blowup(base_edges, base_n, sizes):
    E = []
    groups = []
    v = 0
    for i, t in enumerate(sizes):
        groups.append(list(range(v, v + t)))
        v += t
    n = v
    for i in range(base_n):
        for j in range(i + 1, base_n):
            if (i, j) in base_edges or (j, i) in base_edges:
                for u in groups[i]:
                    for w_ in groups[j]:
                        E.append((u, w_))
    for g in groups:
        for u in g:
            for w_ in g:
                if u < w_:
                    E.append((u, w_))
    return n, E


def cyc(n):
    return [(i, (i + 1) % n) for i in range(n)]


def main():
    random.seed(77)
    viols = []
    results = []

    def run(masks, n, tag):
        v, row = check(masks, n, tag)
        results.append(row)
        if v:
            viols.append(row)

    # A. clique blowups of odd holes
    for k in [5, 7, 9]:
        be = set(cyc(k)) | set((j, i) for (i, j) in cyc(k))
        # uniform
        for t in [1, 2, 3]:
            n, E = blowup(be, k, [t] * k)
            if n <= 16:
                run(from_edges(n, E), n, "C%d-blowup t=%d" % (k, t))
        # non-uniform samples
        for trial in range(6):
            sizes = [random.randint(1, 4) for _ in range(k)]
            n, E = blowup(be, k, sizes)
            if n <= 16:
                run(from_edges(n, E), n, "C%d-blowup %s" % (k, sizes))
    # B. odd wheels + blown rims/hubs
    for k in [5, 7]:
        # wheel: rim Ck + hub
        rim = cyc(k)
        for t in [1, 2]:
            sizes = [t] * k + [1]
            be = set(rim) | set((j, i) for (i, j) in rim)
            be2 = set(be) | set((i, k) for i in range(k)) | set((k, i) for i in range(k))
            n, E = blowup(be2, k + 1, sizes)
            if n <= 16:
                run(from_edges(n, E), n, "wheel%d rim-t=%d" % (k, t))
        # hub blown up by clique Kt (join with clique: EHF-preserving)
        for t in [2, 3]:
            sizes = [1] * k + [t]
            be2 = set(rim) | set((j, i) for (i, j) in rim)
            be2 = be2 | set((i, k) for i in range(k)) | set((k, i) for i in range(k))
            n, E = blowup(be2, k + 1, sizes)
            if n <= 16:
                run(from_edges(n, E), n, "wheel%d hub-K%d" % (k, t))
    # C. Kt join Ck (EHF-preserving: join with a clique preserves EHF)
    for k in [5, 7]:
        for t in [1, 2, 3]:
            n = t + k
            E = [(i, j) for i in range(t) for j in range(i + 1, t)]
            E += [(t + i, t + ((i + 1) % k)) for i in range(k)]
            E += [(i, t + j) for i in range(t) for j in range(k)]
            m = from_edges(n, E)
            if n <= 16:
                run(m, n, "K%d join C%d" % (t, k))
    # D. random graphs filtered by EHF (bounded sweep), n<=12
    tried = ehf_count = 0
    for trial in range(400):
        n = random.choice([10, 11, 12])
        p = random.choice([0.25, 0.35, 0.45, 0.55, 0.65])
        E = [(i, j) for i in range(n) for j in range(i + 1, n) if random.random() < p]
        m = from_edges(n, E)
        tried += 1
        even, _ = chordless_holes(m, n, cap_even=1, cap_total=10**9)
        if even:
            continue
        ehf_count += 1
        run(m, n, "rand n=%d p=%.2f t=%d" % (n, p, trial))
    print("random: %d tried, %d EHF" % (tried, ehf_count))
    print("VIOLATIONS: %d" % len(viols))
    with open('/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1499/output/artifacts/search_out.txt', 'w') as f:
        for r in results:
            f.write(repr(r) + "\n")
        f.write("VIOLATIONS=%d\n" % len(viols))


if __name__ == '__main__':
    main()
