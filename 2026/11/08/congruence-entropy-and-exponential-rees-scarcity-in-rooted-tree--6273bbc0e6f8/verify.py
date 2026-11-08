"""Finite checks for rooted-tree graph inverse semigroup congruence counts.

Only uses Python's standard library. Exhaustive tests are finite; the
infinite-depth entropy theorem is proved separately by inequalities.
"""
from collections import Counter
from decimal import Decimal, localcontext


def tree_full(b, height):
    nodes = [[]]
    frontier = [0]
    for _ in range(height):
        new = []
        for u in frontier:
            for _ in range(b):
                v = len(nodes)
                nodes.append([])
                nodes[u].append(v)
                new.append(v)
        frontier = new
    return nodes


def wang_polynomial_brute(children):
    """Independently enumerate all hereditary sets and eligible W subsets."""
    n = len(children)
    output = Counter()
    for h in range(1 << n):
        H = {v for v in range(n) if (h >> v) & 1}
        if any(w not in H for v in H for w in children[v]):
            continue
        eligible = [v for v in range(n) if v not in H
                    and sum(w not in H for w in children[v]) == 1]
        for w in range(len(eligible) + 1):
            # Every size-w subset of eligible vertices contributes once.
            from math import comb
            output[(len(H), w)] += comb(len(eligible), w)
    return output


def multiply_poly(a, b):
    c = Counter()
    for (hi, wi), ai in a.items():
        for (hj, wj), bj in b.items():
            c[(hi + hj, wi + wj)] += ai * bj
    return c


def polynomial_rec(children, root=0):
    """Implement the tree decomposition independently of brute bit masks."""
    def recurse(v):
        if not children[v]:
            return Counter({(0, 0): 1, (1, 0): 1}), 1
        pairs = [recurse(w) for w in children[v]]
        polys, sizes = zip(*pairs)
        result = Counter({(1 + sum(sizes), 0): 1})  # entire subtree in H
        all_out = Counter({(0, 0): 1})
        for poly in polys:
            all_out = multiply_poly(all_out, poly)
        result += all_out
        # root outside H and inside W: exactly one child root outside H
        for idx, poly in enumerate(polys):
            curr = Counter({(0, 1): 1})
            for j, (pj, sizej) in enumerate(pairs):
                if j == idx:
                    restricted = Counter(pj)
                    restricted[(sizej, 0)] -= 1
                    if not restricted[(sizej, 0)]:
                        del restricted[(sizej, 0)]
                    curr = multiply_poly(curr, restricted)
                else:
                    curr = multiply_poly(curr, Counter({(sizej, 0): 1}))
            result += curr
        return result, 1 + sum(sizes)
    return recurse(root)[0]


def paths(children):
    edges = [(u, w) for u, out in enumerate(children) for w in out]
    out = []
    def visit(start, at, word):
        out.append((start, at, word))
        for eid, (u, v) in enumerate(edges):
            if u == at:
                visit(start, v, word + (eid,))
    for v in range(len(children)):
        visit(v, v, ())
    return out


def multiplication_table(children):
    plist = paths(children)
    lookup = {(p[0], p[2]): p for p in plist}
    elements = [None] + [(a, b) for a in plist for b in plist if a[1] == b[1]]
    ids = {x: i for i, x in enumerate(elements)}
    def ext(p, tail):
        return lookup[(p[0], p[2] + tail)]
    def mul(x, y):
        if x is None or y is None:
            return None
        a, b = x
        c, d = y
        if b[0] != c[0]:
            return None
        bw, cw = b[2], c[2]
        if len(bw) <= len(cw) and cw[:len(bw)] == bw:
            return (ext(a, cw[len(bw):]), d)
        if len(cw) <= len(bw) and bw[:len(cw)] == cw:
            return (a, ext(d, bw[len(cw):]))
        return None
    return [[ids[mul(x, y)] for y in elements] for x in elements]


def all_partitions(n):
    block = [0] * n
    def recurse(i, largest):
        if i == n:
            yield tuple(block)
            return
        for label in range(largest + 2):
            block[i] = label
            yield from recurse(i + 1, max(label, largest))
    yield from recurse(1, 0)


def congruence_count_direct(children):
    """Test all semigroup equivalence relations, without using Wang pairs."""
    mult = multiplication_table(children)
    n = len(mult)
    assert n <= 10, "only the small direct comparisons are feasible"
    count = 0
    for p in all_partitions(n):
        rep = {}
        valid = True
        for i, label in enumerate(p):
            if label not in rep:
                rep[label] = i
                continue
            j = rep[label]
            if any(p[mult[i][k]] != p[mult[j][k]] or
                   p[mult[k][i]] != p[mult[k][j]] for k in range(n)):
                valid = False
                break
        if valid:
            count += 1
    return count



def entropy_bounds(b, h):
    """Rigorous interval for the asymptotic Rees decay constant."""
    assert b >= 2 and h >= 1
    C = R = 2
    for _ in range(h):
        C = 1 + C ** b + b * (C - 1)
        R = 1 + R ** b
    with localcontext() as ctx:
        ctx.prec = 70
        cc = Decimal(C)
        rr = Decimal(R)
        den = Decimal(b) ** h
        llo = cc.ln() / den
        ulo = rr.ln() / den
        # The logarithmic increments decrease as the recurrences increase.
        lhi = llo + (1 + Decimal(b + 1) * cc ** (1-b)).ln() / ((b-1) * den)
        uhi = ulo + (1 + rr ** (-b)).ln() / ((b-1) * den)
        return llo-uhi, lhi-ulo


def test():
    for b, max_height in ((2, 3), (3, 2)):
        for h in range(max_height + 1):
            tree = tree_full(b, h)
            p1 = wang_polynomial_brute(tree)
            p2 = polynomial_rec(tree)
            assert p1 == p2, (b, h, p1, p2)
            c = sum(p1.values())
            r = sum(coeff for (H, W), coeff in p1.items() if W == 0)
            assert c >= r >= 1
            if h == 0:
                assert c == r == 2
            else:
                parent = tree_full(b, h - 1)
                p = polynomial_rec(parent)
                cprev = sum(p.values())
                rprev = sum(co for (_, ww), co in p.items() if ww == 0)
                assert c == 1 + cprev ** b + b * (cprev - 1)
                assert r == 1 + rprev ** b
            print(f'full_{b}_ary height={h}: vertices={len(tree)}, congruences={c}, Rees={r}')
    for tree, expected in [([[], []], 4), ([[1], []], 4), ([[1, 2], [], []], 7)]:
        direct = congruence_count_direct(tree)
        assert direct == expected == sum(wang_polynomial_brute(tree).values())
        print(f'direct multiplication: {len(tree)} vertices, {direct} congruences')
    for b, h in ((2, 5), (3, 4)):
        low, high = entropy_bounds(b, h)
        assert low > 0 and high-low < Decimal('1e-10')
        print(f'branching={b}, strict entropy-gap interval=[{low}, {high}]')
    print('VERIFY_OK')


if __name__ == '__main__':
    test()
