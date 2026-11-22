"""Independent exact checks for coherent directed multi-theta dichromatic polynomials.

Python 3 standard library only. Run with `python3 verify.py`.
"""
from itertools import combinations_with_replacement, product
from math import prod


def build_digraph(c, ds):
    edges = []
    n = 2
    def append_path(source, target, length):
        nonlocal n
        last = source
        for _ in range(length - 1):
            edges.append((last, n))
            last = n
            n += 1
        edges.append((last, target))
    append_path(1, 0, c)
    for d in ds:
        append_path(0, 1, d + 1)
    return n, edges


def no_monochromatic_cycle(colors, n, edges):
    # Independently detect cycles in the subdigraph of monochromatic arcs.
    indegree = [0] * n
    nexts = [[] for _ in range(n)]
    for u, v in edges:
        if colors[u] == colors[v]:
            nexts[u].append(v)
            indegree[v] += 1
    stack = [v for v in range(n) if not indegree[v]]
    visited = 0
    while stack:
        u = stack.pop()
        visited += 1
        for v in nexts[u]:
            indegree[v] -= 1
            if not indegree[v]:
                stack.append(v)
    return visited == n


def evaluate(c, ds, q):
    d = sum(ds)
    return q ** (c + d + 1) - q ** (d + 1) + q * prod(q ** k - 1 for k in ds)


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def neg(a):
    return tuple(-u for u in a)


def mul(a, b):
    z = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            z[i+j] += u * v
    return trim(z)


def monomial(k, coefficient=1):
    return tuple([0] * k + [coefficient])


def divide_monic(num, den):
    num = list(num)
    degree = len(den) - 1
    out = [0] * max(1, len(num) - degree)
    while len(num) - 1 >= degree and any(num):
        k = len(num) - 1 - degree
        coefficient = num[-1]
        out[k] += coefficient
        for i, x in enumerate(den):
            num[k+i] -= coefficient * x
        num = list(trim(num))
    return trim(out), trim(num)


def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]


def cyclotomics_up_to(n):
    values = {}
    for j in range(1, n+1):
        f = add(monomial(j), (-1,))
        for d in divisors(j)[:-1]:
            f, rem = divide_monic(f, values[d])
            assert rem == (0,), (j, d, rem)
        values[j] = f
    return values


def mobius(k):
    count = 0
    prime = 2
    while prime*prime <= k:
        if k % prime == 0:
            count += 1
            k //= prime
            if k % prime == 0:
                return 0
            while k % prime == 0:
                k //= prime
        prime += 1
    if k > 1:
        count += 1
    return -1 if count % 2 else 1


def check_inverse(c, ds, cyclotomics):
    d = sum(ds)
    p = add(add(monomial(c+d+1), monomial(d+1, -1)),
            mul((0,1), prod_polys([add(monomial(j), (-1,)) for j in ds])))
    assert len(p) == c+d+2 and p[-1] == 1
    derivative_at_one = sum(i * coefficient for i, coefficient in enumerate(p))
    assert derivative_at_one == c
    # Divide by x, then subtract x^d(x^c-1).
    assert p[0] == 0
    f = add(p[1:], neg(add(monomial(c+d), monomial(d, -1))))
    e = {}
    rem = f
    for j in range(1, d+1):
        count = 0
        while True:
            quo, r = divide_monic(rem, cyclotomics[j])
            if r != (0,):
                break
            rem = quo
            count += 1
        e[j] = count
    assert rem in ((1,), (-1,)), (c, ds, rem)
    recovered = []
    for j in range(1, d+1):
        a = sum(mobius(k) * e.get(k*j, 0) for k in range(1, d//j + 1))
        assert a >= 0
        recovered.extend([j] * a)
    assert tuple(sorted(recovered)) == tuple(ds), (c, ds, recovered)
    return p


def prod_polys(polys):
    ans = (1,)
    for poly in polys:
        ans = mul(ans, poly)
    return ans


def p_scaled_at_fraction(c, ds, numerator, denominator):
    # Compute sign of P(x)/x for x=numerator/denominator in (0,1).
    d = sum(ds)
    r = len(ds)
    a = -numerator**d * (denominator**c - numerator**c)
    # The terms below are scaled to a common positive denominator.
    b = (-1)**r * prod(denominator**j-numerator**j for j in ds) * denominator**c
    return a + b


def main():
    cases = 0
    maps = 0
    for r in range(2, 5):
        for c in range(1, 4):
            for ds in combinations_with_replacement(range(1, 4), r):
                n, edges = build_digraph(c, ds)
                if n > 10:
                    continue
                for q in range(1, 4):
                    if q**n > 80000:
                        continue
                    direct = sum(no_monochromatic_cycle(cols, n, edges)
                                 for cols in product(range(q), repeat=n))
                    assert direct == evaluate(c, ds, q), (c, ds, q, direct)
                    cases += 1
                    maps += q**n
    assert cases == 180 and maps == 1161788
    print('DIRECT_ACYCLIC_COLOURING_ENUMERATION', cases, maps, 'PASS')
    polynomials = {}
    count = 0
    for r in range(2, 5):
        for c in range(1, 4):
            for ds in combinations_with_replacement(range(1, 5), r):
                p = check_inverse(c, ds, cyclotomics_up_to(sum(ds)))
                key = (c, ds)
                if p in polynomials and polynomials[p] != key:
                    raise AssertionError((key, polynomials[p]))
                polynomials[p] = key
                count += 1
                if r % 2 == 0:
                    assert p_scaled_at_fraction(c,ds,1,1000)>0
                    assert p_scaled_at_fraction(c,ds,999,1000)<0
                else:
                    assert p_scaled_at_fraction(c,ds,1,1000)<0
                    assert p_scaled_at_fraction(c,ds,999,1000)<0
    print('EXACT_INVERSE_CYCLOTOMIC_RECOVERY',count,'PASS')
    print('RATIONAL_SIGN_BRACKETS',count,'PASS')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
