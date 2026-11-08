"""Independent finite-field reconstruction of rank-one associative Nijenhuis equations.
Only standard Python is required. Run: python kronecker_nijenhuis_check.py
"""
from itertools import product


def F(q):
    if q in (2, 3):
        return lambda a, b: (a + b) % q, lambda a, b: (a * b) % q
    if q == 4:
        def mul(a, b):
            out = 0
            for i in range(2):
                if (a >> i) & 1:
                    for j in range(2):
                        if (b >> j) & 1:
                            out ^= (1 << (i + j))
            if out & 4:
                out ^= 7  # X^2 + X + 1
            return out
        return lambda a, b: a ^ b, mul
    raise ValueError(q)


def check(m, q):
    add, times = F(q)
    d = m + 2
    zero = (0,) * d
    def mult(a, b):
        return (times(a[0], b[0]), times(a[1], b[1])) + tuple(add(times(a[0], b[i]), times(a[i], b[1])) for i in range(2, d))
    def scal(c, a):
        return tuple(times(c, v) for v in a)
    def plus(a, b):
        return tuple(add(x, y) for x, y in zip(a, b))
    units = [tuple(int(i == j) for i in range(d)) for j in range(d)]
    nonzero = list(range(1, q))
    # Determine rank-one tensor a \otimes phi uniquely: first nonzero a entry normalized to 1.
    inv = {c: next(x for x in nonzero if times(c, x) == 1) for c in nonzero}
    projective = []
    for a in product(range(q), repeat=d):
        if a == zero:
            continue
        c = next(x for x in a if x)
        if c == 1:
            projective.append(a)
    branches = [0, 0, 0, 0]
    count = 0
    mismatch = 0
    for a in projective:
        # Types from coordinate description, independent of operator equations.
        if a[0] == a[1] == 0:
            branch = 0
        elif a[0] and not a[1]:
            branch = 1
        elif a[1] and not a[0]:
            branch = 2
        elif a[0] and a[0] == a[1] and all(x == 0 for x in a[2:]):
            branch = 3
        else:
            branch = -1
        ab = [[mult(a, u) for u in units], [mult(u, a) for u in units]]
        aa = mult(a, a)
        for phi in product(range(q), repeat=d):
            if phi == zero:
                continue
            # Literal original Nijenhuis identity on all basis pairs:
            # P(x)P(y)=P(P(x)y+xP(y)-P(xy)).
            OK = True
            for i in range(d):
                for j in range(d):
                    left = scal(times(phi[i], phi[j]), aa)
                    # scalar terms of P(P(e_i)e_j + e_i P(e_j) - P(e_i e_j))
                    t1 = 0
                    t2 = 0
                    t3 = 0
                    for h in range(d):
                        t1 = add(t1, times(phi[h], ab[0][j][h]))
                        t2 = add(t2, times(phi[h], ab[1][i][h]))
                        t3 = add(t3, times(phi[h], mult(units[i], units[j])[h]))
                    # subtract == add in characteristic 2, else negate
                    phi_a = 0
                    for h in range(d):
                        phi_a = add(phi_a, times(phi[h], a[h]))
                    term = times(phi_a, t3)
                    rhs_coeff = add(add(times(phi[i], t1), times(phi[j], t2)), (-term) % q if q != 4 else term)
                    right = scal(rhs_coeff, a)
                    if left != right:
                        OK = False
                        break
                if not OK:
                    break
            # Expected branch conditions derived from 7-component theorem.
            if branch == 0:
                predicted = (sum(times(phi[2+h], a[2+h]) for h in range(m)) % q == 0 if q != 4 else _dot4(phi[2:], a[2:])) or (add(phi[0], phi[1]) == 0)
            elif branch in (1, 2):
                predicted = (add(phi[0], phi[1]) == 0) or (all(phi[h] == 0 for h in range(d) if h != (branch-1)))
            elif branch == 3:
                predicted = (all(phi[h] == 0 for h in range(d) if h != 0) or all(phi[h] == 0 for h in range(d) if h != 1))
            else:
                predicted = False
            if predicted != OK:
                mismatch += 1
                raise AssertionError((m, q, a, phi, predicted, OK))
            if OK:
                count += 1
                branches[branch] += 1
    lines = (q**m - 1) // (q - 1)
    predicted_nonzero = lines * (2*q**(m+1)-q**m-1) + 2*q**m*(q**(m+1)+q-2) + 2*(q-1)
    assert count == predicted_nonzero, (count, predicted_nonzero)
    print(f"m={m} q={q} all_rank_one_nonzero={count} predicted={predicted_nonzero} branches={branches} MATCH")


def _dot4(x, y):
    _, mul = F(4)
    v = 0
    for a, b in zip(x, y):
        v ^= mul(a, b)
    return v == 0


if __name__ == '__main__':
    for case in [(2,2),(2,3),(3,2),(2,4)]:
        check(*case)
    print('KRONECKER_RANK_ONE_NIJENHUIS_ORIGINAL_EQUATION_OK')
