"""Independent exhaustive checks of the Narayana recurrence cycle census.

Run: python3 check.py. Uses only the Python standard library.
"""
from collections import Counter


def matmul(a, b):
    return [[sum(a[i][h] * b[h][j] for h in range(3)) for j in range(3)] for i in range(3)]


def determinant(m):
    a, b, c = m[0]
    d, e, f = m[1]
    g, h, i = m[2]
    return a * (e*i-f*h) - b * (d*i-f*g) + c * (d*h-e*g)


def check_matrix():
    m = [[1, 0, 1], [1, 0, 0], [0, 1, 0]]
    a = [[int(i == j) for j in range(3)] for i in range(3)]
    for _ in range(8):
        a = matmul(a, m)
    b = [[(a[i][j]-int(i == j))//3 for j in range(3)] for i in range(3)]
    assert all((a[i][j]-int(i == j)) % 3 == 0 for i in range(3) for j in range(3))
    assert b == [[4,2,3],[3,1,2],[2,1,1]]
    assert determinant(m) == determinant(b) == 1


def exhaustive(k):
    modulus = 3**k
    visited = set()
    periods = Counter()
    for a in range(modulus):
        for b in range(modulus):
            for c in range(modulus):
                start = (a,b,c)
                if start in visited:
                    continue
                v = start
                length = 0
                while True:
                    assert v not in visited
                    visited.add(v)
                    length += 1
                    v = ((v[0]+v[2]) % modulus, v[0], v[1])
                    if v == start:
                        break
                periods[length] += 1
    expected = Counter({1: 1})
    for r in range(k):
        expected[2*3**r] = 1
        expected[8*3**r] = (13*9**r-1)//4
    assert periods == expected, (k, periods, expected)
    assert sum(period*count for period,count in periods.items()) == modulus**3
    print('k=', k, 'states=', modulus**3, 'cycles=', sum(periods.values()),
          'lengths=', dict(sorted(periods.items())))


if __name__ == '__main__':
    check_matrix()
    for k in range(1,5):
        exhaustive(k)
    print('PASS: complete enumeration for k=1,2,3,4 and exact matrix identity')
