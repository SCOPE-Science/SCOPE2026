"""Exact certificate for the six-term progression enumerator.

Only Python's standard library is used. A transfer-matrix characteristic
polynomial and its initial coefficients certify the rational generating
function for all nonnegative digit lengths, not merely a finite sample.
"""
from collections import defaultdict, deque
from math import comb

BASE = 7
LENGTH = 6
MISSING = 3
P = [1, -27, 202, -588, 614, 289, -648, -258, 320]
B = [1, -27, 193, -556, 616, 136, -346, -720, 928]
Q = [(B[i] if i < len(B) else 0) - (6 * B[i-1] if i else 0) for i in range(len(B)+1)]


def multiply(a, b):
    out = [0] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def transitions():
    root = (0,)*LENGTH
    seen = {root}
    todo = deque([root])
    rules = {}
    while todo:
        carry = todo.popleft()
        ways = defaultdict(int)
        for a in range(BASE):
            for d in range(BASE):
                next_carry = []
                for j in range(LENGTH):
                    value = a + j*d + carry[j]
                    if value % BASE == MISSING:
                        break
                    next_carry.append(value // BASE)
                if len(next_carry) == LENGTH:
                    state = tuple(next_carry)
                    ways[state] += 1
                    if state not in seen:
                        seen.add(state)
                        todo.append(state)
        rules[carry] = dict(ways)
    states = sorted(seen)
    ids = {state: i for i, state in enumerate(states)}
    matrix = [[0]*len(states) for _ in states]
    for source, ways in rules.items():
        for target, count in ways.items():
            matrix[ids[source]][ids[target]] = count
    return states, ids[root], matrix


def matmul(a, b):
    n = len(a)
    c = [[0]*n for _ in range(n)]
    for i in range(n):
        for k, x in enumerate(a[i]):
            if x:
                for j, y in enumerate(b[k]):
                    c[i][j] += x*y
    return c


def characteristic(a):
    # Faddeev-LeVerrier gives the exact characteristic polynomial.
    n = len(a)
    work = [[int(i == j) for j in range(n)] for i in range(n)]
    coefficients = [1]
    for k in range(1, n+1):
        work = matmul(a, work)
        trace = sum(work[j][j] for j in range(n))
        new, remainder = divmod(-trace, k)
        assert remainder == 0
        coefficients.append(new)
        for j in range(n):
            work[j][j] += new
    assert all(x == 0 for row in work for x in row)  # Cayley-Hamilton
    return coefficients


def sequence(matrix, root, length):
    n = len(matrix)
    vector = [int(i == root) for i in range(n)]
    result = []
    for _ in range(length):
        result.append(vector[root])
        vector = [sum(vector[i]*matrix[i][j] for i in range(n))
                  for j in range(n)]
    return result


def brute(r):
    size = BASE**r
    if r == 0:
        return 0
    allowed = set()
    for n in range(size):
        x = n
        while x and x % BASE != MISSING:
            x //= BASE
        if not x:
            allowed.add(n)
    return sum(all(n+j*d in allowed for j in range(LENGTH))
               for d in range(1, (size-1)//(LENGTH-1)+1)
               for n in allowed if n+(LENGTH-1)*d < size)


def check():
    states, root, matrix = transitions()
    assert len(states) == 24
    assert sum(v != 0 for row in matrix for v in row) == 294
    den = characteristic(matrix)
    f = sequence(matrix, root, 24)
    num = [sum(den[k]*f[j-k] for k in range(j+1))
           for j in range(24)]
    # (sum f_r z^r) = P(z)/((1-6z) B(z)), as an exact identity.
    lhs = multiply(num, Q)
    rhs = multiply(den, P)
    lhs += [0]*(max(len(lhs), len(rhs))-len(lhs))
    rhs += [0]*(max(len(lhs), len(rhs))-len(rhs))
    assert lhs == rhs
    values = sequence(matrix, root, 13)
    expected = [v-BASE**0 if i == 0 else v-6**i
                for i, v in enumerate(values)]
    assert expected[:6] == [0, 0, 9, 265, 5548, 104588]
    for r in range(4):
        assert expected[r] == brute(r)
    # Independent small-index central-trinomial and digit checks.
    for n in range(150):
        coefficient = sum(comb(n,2*j)*comb(2*j,j)
                          for j in range(n//2+1))
        digit_rule = True
        x = n
        while x:
            if x % 7 == 3:
                digit_rule = False
            x //= 7
        assert (coefficient % 7 != 0) == digit_rule
    print('PASS: 24 carry states, exact characteristic identity,')
    print('finite enumeration checks and independent digit checks')
    print('six-term counts for r=0..12:', expected)
    print('complete polynomial identity lengths:', len(den), len(num))


if __name__ == '__main__':
    check()
