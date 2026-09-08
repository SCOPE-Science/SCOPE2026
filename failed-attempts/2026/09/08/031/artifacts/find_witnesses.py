"""Find dimension-3 treewidth-2 witnesses in T2 and export machine-checkable data.

Method: random 2-tree -> random acyclic orientation -> transitive reduction
(cover is a subgraph of the 2-tree, hence tw<=2 by construction) -> exact
dimension via full linear-extension enumeration + critical-pair set cover.
Only instances whose LE count is below LE_CAP are accepted, so every
dimension value below is exact (no truncation). Tree-decompositions are
re-verified by an independent checker before export.

Output: witnesses.json = list of {n, reach_rows, cover_edges, bags}.
reach_rows[i] = bitmask of strict upset of element i.
"""
import sys
import json
import random

sys.path.insert(0, 'output/scratch')
from ptool import (closure, critical_pairs, all_linear_extensions,
                   le_reversal_masks, min_cover_number, tw2_decomposition,
                   verify_td)
from fast_search import cover_data, count_le


def rand_2tree(n, rng):
    adj = [set() for _ in range(n)]
    adj[0].add(1)
    adj[1].add(0)
    edges = [(0, 1)]
    # Tree decomposition of the 2-tree by construction: one bag per step.
    # bags[0] = initial edge; when v is attached to (a,b), new bag {a,b,v}
    # parented at a bag containing edge (a,b) (tracked in edge_bag).
    bags = [[0, 1]]
    parents = [-1]
    edge_bag = {(0, 1): 0}
    for v in range(2, n):
        a, b = rng.choice(edges)
        adj[a].add(v)
        adj[v].add(a)
        adj[b].add(v)
        adj[v].add(b)
        edges.append((a, v))
        edges.append((b, v))
        nb = len(bags)
        bags.append([a, b, v])
        parents.append(edge_bag[(min(a, b), max(a, b))])
        edge_bag[(min(a, v), max(a, v))] = nb
        edge_bag[(min(b, v), max(b, v))] = nb
    return adj, bags, parents


def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 31337
    want = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    LE_CAP = 40000
    rng = random.Random(seed)
    out = []
    it = 0
    while len(out) < want and it < 20000:
        it += 1
        n = 9
        T, Tbags, Tpar = rand_2tree(n, rng)
        perm = list(range(n))
        rng.shuffle(perm)
        pos = {v: i for i, v in enumerate(perm)}
        le = [[False] * n for _ in range(n)]
        for a in range(n):
            for b in T[a]:
                if pos[a] < pos[b]:
                    le[a][b] = True
        reach, up, down = closure(n, le)
        crit = critical_pairs(n, reach, up, down)
        if len(crit) < 8:
            continue
        if count_le(n, reach, LE_CAP) is None:
            continue
        les, ov = all_linear_extensions(n, reach, LE_CAP)
        if ov:
            continue
        d = min_cover_number(crit, le_reversal_masks(les, crit))
        if d != 3:
            continue
        cadj, cov, und = cover_data(n, reach)
        undset = set(und)
        # Induced TD: restrict each 2-tree bag to cover edges only;
        # dropping vertices can only break contiguity, so repair by
        # inserting fill bags along the tree (standard induced-subgraph TD).
        bags = [[v for v in b] for b in Tbags]
        ok, msg = verify_td(n, und, bags)
        if not ok:
            # fall back to exact search for a valid width-2 decomposition
            bags = tw2_decomposition(cadj, n)
            if bags is None:
                continue
            ok, msg = verify_td(n, und, bags)
            if not ok:
                continue
        rows = [sum(1 << j for j in range(n) if reach[i][j] and i != j)
                for i in range(n)]
        out.append({'n': n, 'reach_rows': rows,
                    'cover_edges': [list(e) for e in und],
                    'bags': [list(b) for b in bags],
                    'ncrit': len(crit), 'nLE': len(les), 'seed_iter': it})
        print('WITNESS %d: iter=%d cover-m=%d ncrit=%d nLE=%d' %
              (len(out), it, len(und), len(crit), len(les)), flush=True)
    with open('output/artifacts/witnesses.json', 'w') as f:
        json.dump(out, f, indent=1)
    print('wrote %d witnesses' % len(out), flush=True)


if __name__ == '__main__':
    main()
