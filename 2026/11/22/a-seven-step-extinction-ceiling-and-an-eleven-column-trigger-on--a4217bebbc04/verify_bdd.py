"""Exact ternary reduced ordered decision-diagram certificate for three-row excitation.

Run: python3 verify_bdd.py
Uses only the Python standard library. Every variable has exactly three values
(0 resting, 1 excited, 2 refractory). The diagram is a canonical DAG whose
leaves are Boolean constants, so a root equal to zero is a finite exhaustive
certificate, not a sample of initial states.
"""
from functools import lru_cache
from itertools import product

class TernaryBDD:
    def __init__(self):
        self.nodes = [(-1, 0, 0, 0), (-1, 1, 1, 1)]
        self.unique = {}
        self.apply_cache = {}
        self.not_cache = {}

    def node(self, index, branches):
        if branches[0] == branches[1] == branches[2]:
            return branches[0]
        key = (index,) + tuple(branches)
        if key not in self.unique:
            self.unique[key] = len(self.nodes)
            self.nodes.append(key)
        return self.unique[key]

    def test(self, index, color):
        return self.node(index, tuple(int(v == color) for v in range(3)))

    def negate(self, root):
        if root <= 1:
            return 1 - root
        if root not in self.not_cache:
            index, *child = self.nodes[root]
            self.not_cache[root] = self.node(index, tuple(self.negate(x) for x in child))
        return self.not_cache[root]

    def combine(self, op, left, right):
        if left > right:
            left, right = right, left
        if op == "and":
            if left == 0:
                return 0
            if left == 1 or left == right:
                return right
        else:
            if left == 1:
                return 1
            if left == 0 or left == right:
                return right
        key = (op, left, right)
        if key in self.apply_cache:
            return self.apply_cache[key]
        x = self.nodes[left]
        y = self.nodes[right]
        indices = [self.nodes[k][0] for k in (left, right) if k >= 2]
        i = min(indices)
        a = x[1:] if left >= 2 and x[0] == i else (left,) * 3
        b = y[1:] if right >= 2 and y[0] == i else (right,) * 3
        ans = self.node(i, tuple(self.combine(op, u, v) for u, v in zip(a, b)))
        self.apply_cache[key] = ans
        return ans

    def AND(self, values):
        result = 1
        for x in values:
            result = self.combine("and", result, x)
        return result

    def OR(self, values):
        result = 0
        for x in values:
            result = self.combine("or", result, x)
        return result

    def at_least_two(self, values):
        one, two = 0, 0
        for x in values:
            two = self.combine("or", two, self.combine("and", one, x))
            one = self.combine("or", one, x)
        return two

    def count(self, root, variable_count):
        @lru_cache(None)
        def visit(start, x):
            if x == 0:
                return 0
            if x == 1:
                return 3 ** (variable_count - start)
            index, *children = self.nodes[x]
            return 3 ** (index - start) * sum(visit(index + 1, c) for c in children)
        return visit(0, root)

    def witness(self, root, variable_count):
        if root == 0:
            return None
        colors = [0] * variable_count
        while root > 1:
            i, *children = self.nodes[root]
            color = next(j for j, child in enumerate(children) if child != 0)
            colors[i] = color
            root = children[color]
        return tuple(colors)


def symbolic(n):
    """Return exact roots for existence of at least one excited site at t=0,...,6."""
    bdd = TernaryBDD()
    e = [[[bdd.test(c * 3 + r, 1) for c in range(n)] for r in range(3)]]
    refractory = [[bdd.test(c * 3 + r, 2) for c in range(n)] for r in range(3)]
    roots = []
    for t in range(7):
        if t:
            rows = []
            for r in range(3):
                row = []
                for c in range(n):
                    neighbors = [e[t - 1][rr][cc] for rr, cc in
                                 ((r-1,c), (r+1,c), (r,c-1), (r,c+1))
                                 if 0 <= rr < 3 and 0 <= cc < n]
                    prior_ref = refractory[r][c] if t == 1 else e[t-2][r][c]
                    val = bdd.AND((bdd.negate(e[t-1][r][c]),
                                   bdd.negate(prior_ref),
                                   bdd.at_least_two(neighbors)))
                    row.append(val)
                rows.append(row)
            e.append(rows)
        roots.append(bdd.OR(root for row in e[t] for root in row))
    return bdd, roots, e


def trajectory(initial, n, steps=8):
    state = tuple(initial)
    result = [state]
    for _ in range(steps):
        next_state = []
        for c in range(n):
            for r in range(3):
                idx = c*3+r
                if state[idx] != 0:
                    next_state.append((state[idx] + 1) % 3)
                else:
                    nei = [cc*3+rr for rr, cc in
                           ((r-1,c), (r+1,c), (r,c-1), (r,c+1))
                           if 0 <= rr < 3 and 0 <= cc < n]
                    next_state.append(int(sum(state[j] == 1 for j in nei) >= 2))
        state = tuple(next_state)
        result.append(state)
    return result


def verify():
    expected = (3,3,4,4,5,5,6,6,6,6,7,7,7)
    witness_11 = None
    for n in range(1,14):
        bdd, roots, site_roots = symbolic(n)
        assert roots[6] == 0, (n, "excitation at time 6")
        last = max(t for t, root in enumerate(roots) if root != 0)
        assert last + 2 == expected[n-1], (n, last)
        x = bdd.witness(roots[last], 3*n)
        seq = trajectory(x, n)
        assert any(v == 1 for v in seq[last])
        assert not any(seq[last+2])
        if n <= 3:  # independent direct enumeration of all initial configurations
            for t in range(7):
                direct = sum(any(s == 1 for s in trajectory(x0, n, t)[t])
                             for x0 in product(range(3), repeat=3*n))
                assert direct == bdd.count(roots[t], 3*n), (n, t)
        if n == 11:
            assert bdd.count(roots[5], 33) == 1265544
            assert roots[5] == bdd.OR((site_roots[5][0][5], site_roots[5][2][5]))
            assert site_roots[5][1][5] == 0
            witness_11 = x
        print(f'n={n:2} sharp_extinction={last+2} final_excited_t={last} nodes={len(bdd.nodes)}')
    assert witness_11 is not None
    assert tuple(''.join(str(x) for x in witness_11[c*3:c*3+3])
                 for c in range(11)) == (
                     '001','010','100','000','111','000','121','000','100','010','001')
    print('n=11: 1,265,544 exact seven-step states among 3^33; witness verified')
    print('all finite BDD certificates passed')

if __name__ == '__main__':
    verify()
