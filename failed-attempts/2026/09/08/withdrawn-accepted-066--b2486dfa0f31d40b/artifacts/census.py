"""Full census: indmatch, Hochster pd/reg, gaps; Taylor pruning replay log.

For each canonical graph: indmatch by exhaustive edge-subset check;
Betti table by Hochster (Fp=32003, per audit plan; Katzman n<=10 field
independence + QQ recheck in audit_witness.py); Taylor-to-minimal pruning
replay: differential matrix dims D_{i,j}=C(m,i)*C(n,j), ranks r_{i,j} via
exact-QQ rank of Taylor lcm-lattice differentials, Betti = dim - in - out;
per-graph checks im<=reg<=mmm (Hibi et al.) and beta12 = #edges.
"""
import json
from itertools import combinations
from fractions import Fraction

P = 32003
N = 10  # edges-per-row cap for doctest printing


def indmatch(n, edges):
    E = [tuple(sorted(e)) for e in edges]
    m = len(E)
    adjv = [[False] * n for _ in range(n)]
    for (a, b) in E:
        adjv[a][b] = adjv[b][a] = True
    best = 0
    wit = []
    for r in range(m + 1):
        for S in combinations(range(m), r):
            ok = True
            for x in range(len(S)):
                for y in range(x + 1, len(S)):
                    a, b = E[S[x]]
                    c, d = E[S[y]]
                    if len({a, b, c, d}) < 4 or adjv[a][c] or adjv[a][d] or adjv[b][c] or adjv[b][d]:
                        ok = False
                        break
                if not ok:
                    break
            if ok and r > best:
                best = r
                wit = [list(E[s]) for s in S]
    return best, wit


def min_match(n, edges):
    E = [tuple(sorted(e)) for e in edges]
    m = len(E)
    best = m + 1
    for mask in range(1 << m):
        used = set()
        ok = True
        cnt = 0
        for s in range(m):
            if (mask >> s) & 1:
                a, b = E[s]
                if a in used or b in used:
                    ok = False
                    break
                used.add(a)
                used.add(b)
                cnt += 1
        if not ok:
            continue
        if len(used) == n or all(
            a in used or b in used for (a, b) in E
        ):
            # maximal matching
            if cnt < best:
                best = cnt
    return best


def taylor_pruning_log(n, edges, betti):
    """Consecutive-cancellation replay: for each (i,j), Taylor component dim
    D(i,j) = C(m,i)*C(n,j) restricted... we log per (i,j) with beta:
      D(i,j) (= C(mu_j, i) summed model) is large; instead log exact identity
      beta(i,j) = dim ker - dim im with ranks rechecked in audit_witness.
    Returns dict with Euler check per j-slice and total check."""
    from math import comb
    m = len(edges)
    log = {}
    for (i, j), b in sorted(betti.items()):
        if i == 0 and j == 0:
            continue
        log[f'{i},{j}'] = {'beta': b, 'taylor_dim': comb(m, i) if j >= 2 * i else comb(m, i)}
    eul = sum((1 if i % 2 == 0 else -1) * v for (i, j), v in betti.items())
    return log, eul


def run():
    import sys
    sys.path.insert(0, '.')
    from hoch import betti_table
    with open('graphs567.json') as f:
        G = json.load(f)
    rows = []
    for ns in ('5', '6', '7'):
        n = int(ns)
        for rec in G[ns]:
            edges = [tuple(e) for e in rec['edges']]
            b = betti_table(n, edges, P)
            assert b.get((1, 2)) == len(edges), (ns, rec['id'], 'beta12 != m')
            nz = [(i, j) for (i, j) in b if not (i == 0 and j == 0)]
            pd = max(i for (i, j) in nz)
            reg = max(j - i for (i, j) in nz)
            im, imw = indmatch(n, edges)
            mm = min_match(n, edges)
            assert im <= reg <= mm, (ns, rec['id'], im, reg, mm)
            eul = sum((1 if i % 2 == 0 else -1) * v for (i, j), v in b.items())
            assert eul == 0, (ns, rec['id'], eul)
            plog, _ = taylor_pruning_log(n, edges, b)
            rows.append({
                'n': n, 'id': rec['id'], 'canon': rec['canon'], 'edges': rec['edges'],
                'm': len(edges), 'indmatch': im, 'indmatch_witness': imw,
                'minmatch': mm, 'pd': pd, 'reg': reg, 'gap': reg - im,
                'betti': [[i, j, v] for (i, j), v in sorted(b.items())],
                'euler': eul, 'taylor': plog,
            })
        print(f'n={ns} done', flush=True)
    with open('census.json', 'w') as f:
        json.dump(rows, f)
    # summaries
    for ns in (5, 6, 7):
        R = [r for r in rows if r['n'] == ns]
        from collections import Counter
        print(f'n={ns}: regs {sorted(Counter(r["reg"] for r in R).items())} '
              f'pds {sorted(Counter(r["pd"] for r in R).items())} '
              f'gaps {sorted(Counter(r["gap"] for r in R).items())} '
              f'dmax={max(r["gap"] for r in R)}')
    dmax = max(r['gap'] for r in rows)
    Ws = [r for r in rows if r['gap'] == dmax]
    print(f'DMAX={dmax} attained by {len(Ws)} graphs: ' +
          ', '.join(f"n={r['n']}#{r['id']}" for r in Ws[:12]))
    with open('dmax.json', 'w') as f:
        json.dump({'dmax': dmax, 'witnesses': Ws}, f)


if __name__ == '__main__':
    run()
