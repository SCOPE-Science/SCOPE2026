"""Independent GF(2) matrix verification of wheel-wave fixed spaces.
Run: python check_matrix.py. Uses no third-party packages.
This is finite evidence only, not an infinite proof.
"""
from math import gcd, lcm

def bitrank(rows):
    pivots = {}
    for a in rows:
        while a:
            j = a.bit_length() - 1
            if j in pivots:
                a ^= pivots[j]
            else:
                pivots[j] = a
                break
    return len(pivots)

def multiply(a, b):
    out = []
    for row in a:
        z = 0
        while row:
            k = (row & -row).bit_length() - 1
            z ^= b[k]
            row &= row - 1
        out.append(z)
    return out

def power(matrix, exponent):
    identity = [1 << i for i in range(len(matrix))]
    answer = identity
    while exponent:
        if exponent & 1:
            answer = multiply(answer, matrix)
        matrix = multiply(matrix, matrix)
        exponent >>= 1
    return answer

def transition(n):
    m = n + 1
    a = [(1 << m) - 2]
    for j in range(n):
        a.append(1 | (1 << (1+(j-1)%n)) | (1 << (1+(j+1)%n)))
    return [a[i] | (1 << (m+i)) for i in range(m)] + [1 << i for i in range(m)]

def expected_order(n):
    if n % 2:
        return lcm(6, n)
    h = n & -n
    if h == 2:
        return 4*n
    if h == 4:
        return 2*n
    return n

def expected_exponent(n, t):
    s = 0
    z = t
    while z % 2 == 0:
        s += 1
        z //= 2
    b = 1 << s
    d = gcd(n, t)
    if n % 2:
        return 2*(d-1) + (2*min(b,2) if t%3 == 0 else 0)
    h = n & -n
    if h == 2:
        correction = min(b,6)-2*min(b,2)
    elif h == 4:
        correction = min(b,6)+2*min(b,2)-2*min(b,4)
    else:
        correction = min(b,2)
    return 2*d + correction

def divisors(n):
    return [d for d in range(1,n+1) if n % d == 0]

checked = 0
for n in range(3,51):
    m = 2*(n+1)
    tmat = transition(n)
    L = expected_order(n)
    assert power(tmat,L) == [1 << i for i in range(m)]
    for d in divisors(L):
        p = power(tmat,d)
        actual = m - bitrank([p[i] ^ (1 << i) for i in range(m)])
        wanted = expected_exponent(n,d)
        assert actual == wanted, (n,d,actual,wanted)
        if d < L:
            assert actual < m, (n,d,'claimed order not sharp')
        checked += 1
    # Checks not constrained to divisors of the global order.
    for d in (7,11,13,17,19,23,29):
        p = power(tmat,d)
        actual = m-bitrank([p[i]^(1 << i) for i in range(m)])
        wanted = expected_exponent(n,d)
        assert actual == wanted, (n,d,actual,wanted)
        checked += 1
print(f'PASS matrix: {checked} exact fixed-space comparisons; rims 3..50; global order checked for every rim')
