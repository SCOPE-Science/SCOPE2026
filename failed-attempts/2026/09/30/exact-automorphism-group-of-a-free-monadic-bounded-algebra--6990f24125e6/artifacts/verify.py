from itertools import permutations
from math import comb, factorial, log


def formula_order(r):
    m = 2 ** r
    ans = 1
    for k in range(m + 1):
        c = comb(m, k)
        ans *= (factorial(m) * factorial(k)) ** c * factorial(c)
    return ans


def build_graph(r):
    m = 2 ** r
    points = []
    marked = set()
    relation = set()
    for mask in range(1 << m):
        block = []
        for i in range(m):
            p = (mask, "u", i)
            points.append(p)
            block.append(p)
        targets = []
        for j in range(m):
            if (mask >> j) & 1:
                p = (mask, "v", j)
                points.append(p)
                block.append(p)
                targets.append(p)
                marked.add(p)
        for x in block:
            for y in targets:
                relation.add((x, y))
    return points, marked, relation


def brute_r1():
    points, marked, relation = build_graph(1)
    index = {p: i for i, p in enumerate(points)}
    rel = {(index[a], index[b]) for a, b in relation}
    marks = [index[p] for p in points if p in marked]
    unmarks = [index[p] for p in points if p not in marked]
    count = 0
    for pm in permutations(marks):
        marked_map = dict(zip(marks, pm))
        for pu in permutations(unmarks):
            perm = list(range(len(points)))
            for a, b in marked_map.items():
                perm[a] = b
            for a, b in zip(unmarks, pu):
                perm[a] = b
            if all((perm[a], perm[b]) in rel for a, b in rel):
                count += 1
    return count


def main():
    for r in range(3):
        m = 2 ** r
        points, marked, relation = build_graph(r)
        expected_points = 3 * m * (2 ** (m - 1))
        assert len(points) == expected_points
        print(f"r={r} m={m} vertices={len(points)} order={formula_order(r)} log_order={log(formula_order(r)):.15f}")
    brute = brute_r1()
    assert brute == formula_order(1) == 64
    print(f"r=1 brute_force_automorphisms={brute}")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
