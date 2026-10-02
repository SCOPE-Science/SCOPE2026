from math import gcd, ceil, log2


def unpack(x, n):
    return [(x >> i) & 1 for i in range(n)]


def pack(a):
    return sum((b & 1) << i for i, b in enumerate(a))


def chi_step(x, n, v):
    a = unpack(x, n)
    return pack([
        a[i] ^ (a[(i + v) % n] & a[(i + 2 * v) % n]) ^ a[(i + 2 * v) % n]
        for i in range(n)
    ])


def chi_back(x, n, v):
    a = unpack(x, n)
    return pack([
        a[i] ^ (a[(i - 2 * v) % n] & a[(i - v) % n]) ^ a[(i - v) % n]
        for i in range(n)
    ])


def blocks(x, n, v):
    d = gcd(n, v)
    ell = n // d
    a = unpack(x, n)
    return [pack([a[(r + t * v) % n] for t in range(ell)]) for r in range(d)]


def reverse_complement(x, ell):
    a = unpack(x, ell)
    return pack([a[(-t) % ell] ^ 1 for t in range(ell)])


def inverse_formula(y, n, v):
    b = unpack(y, n)
    ell = n // gcd(n, v)
    h = (ell - 1) // 2
    out = []
    for i in range(n):
        z = b[i]
        for j in range(1, h + 1):
            term = b[(i - (2 * j - 1) * v) % n]
            for r in range(j, h + 1):
                term &= b[(i - 2 * r * v) % n] ^ 1
            z ^= term
        out.append(z)
    return pack(out)


def inverse_table(fun, n, v):
    inv = [0] * (1 << n)
    seen = set()
    for x in range(1 << n):
        y = fun(x, n, v)
        seen.add(y)
        inv[y] = x
    assert len(seen) == 1 << n
    return inv


def anf_degree(table, n):
    best = 0
    for coord in range(n):
        f = [(table[x] >> coord) & 1 for x in range(1 << n)]
        for i in range(n):
            for mask in range(1 << n):
                if mask & (1 << i):
                    f[mask] ^= f[mask ^ (1 << i)]
        best = max(best, max((m.bit_count() for m, c in enumerate(f) if c), default=0))
    return best


def permutation_order(fun, n, v):
    vals = [fun(x, n, v) for x in range(1 << n)]
    cur = list(range(1 << n))
    order = 0
    while True:
        cur = [vals[cur[x]] for x in range(1 << n)]
        order += 1
        if all(cur[x] == x for x in range(1 << n)):
            return order


def differential_uniformity(fun, n, v):
    vals = [fun(x, n, v) for x in range(1 << n)]
    ans = 0
    for a in range(1, 1 << n):
        count = {}
        for x in range(1 << n):
            b = vals[x] ^ vals[x ^ a]
            count[b] = count.get(b, 0) + 1
        ans = max(ans, max(count.values()))
    return ans


for n, v in [(6, 2), (10, 2), (12, 4)]:
    d = gcd(n, v)
    ell = n // d
    for x in range(1 << n):
        src = blocks(x, n, v)
        assert blocks(chi_step(x, n, v), n, v) == [chi_step(z, ell, 1) for z in src]
        assert blocks(chi_back(x, n, v), n, v) == [
            reverse_complement(
                chi_step(reverse_complement(z, ell), ell, 1), ell
            )
            for z in src
        ]
        assert inverse_formula(chi_step(x, n, v), n, v) == x
    for fun in (chi_step, chi_back):
        fixed = sum(fun(x, n, v) == x for x in range(1 << n))
        assert fixed == 2 ** d
        assert permutation_order(fun, n, v) == 2 ** ceil(log2((ell + 1) / 2))
    if n <= 10:
        for fun in (chi_step, chi_back):
            assert anf_degree(inverse_table(fun, n, v), n) == (ell + 1) // 2
    print(f"n={n}, v={v}: d={d}, ell={ell}, decomposition/order/fixed/inverse checks PASS")

base_du = differential_uniformity(chi_step, 3, 1)
full_du = differential_uniformity(chi_step, 6, 2)
assert full_du == base_du * 2 ** (6 - 3)
print(f"DDT scaling check: delta(chi_3)={base_du}, delta(chi_(6,2))={full_du} PASS")


def general_map(x, n, u, v, w):
    a = unpack(x, n)
    return pack([
        a[(i + u) % n] ^ (a[(i + v) % n] & (a[(i + w) % n] ^ 1))
        for i in range(n)
    ])


def shift_input(x, n, w):
    a = unpack(x, n)
    return pack([a[(i + w) % n] for i in range(n)])


def shift_output(x, n, s):
    a = unpack(x, n)
    return pack([a[(i + s) % n] for i in range(n)])


# Check the two normal forms for all nondegenerate permitted parameter triples in n=6.
n = 6
for w in range(n):
    for delta in (2, 4):
        v = (w + delta) % n
        for branch in ("minus", "twice"):
            u = (w - delta) % n if branch == "minus" else (w + 2 * delta) % n
            for x in range(1 << n):
                z = shift_input(x, n, w)
                lhs = general_map(x, n, u, v, w)
                if branch == "minus":
                    rhs = shift_output(chi_step(z, n, delta), n, -delta)
                else:
                    rhs = shift_output(chi_back(z, n, delta), n, 2 * delta)
                assert lhs == rhs
print("general classified-family normal-form check for n=6 PASS")


def walsh_max(fun, n, v):
    vals = [fun(x, n, v) for x in range(1 << n)]
    best = 0
    for beta in range(1, 1 << n):
        for alpha in range(1 << n):
            s = 0
            for x in range(1 << n):
                bit = ((alpha & x).bit_count() ^ (beta & vals[x]).bit_count()) & 1
                s += -1 if bit else 1
            best = max(best, abs(s))
    return best

base_w = walsh_max(chi_step, 3, 1)
full_w = walsh_max(chi_step, 6, 2)
assert full_w == base_w * 2 ** (6 - 3)
print(f"Walsh scaling check: Lambda(chi_3)={base_w}, Lambda(chi_(6,2))={full_w} PASS")

print("ALL CHECKS PASS")
