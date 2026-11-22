"""Independent finite-field checks for the parity theorem.

Usage: python3 verify_sign.py
Standard-library only. Finite samples corroborate, but do not prove, the theorem.
"""
from itertools import product
from math import gcd


def poly_rem(f, g, p):
    r = list(f)
    while len(r) >= len(g):
        c = r[-1] % p
        shift = len(r) - len(g)
        for i, b in enumerate(g):
            r[shift + i] = (r[shift + i] - c * b) % p
        while r and r[-1] == 0:
            r.pop()
    return r


def irreducible_polynomial(p, n):
    for c in product(range(p), repeat=n):
        if c[0] == 0:
            continue
        f = list(c) + [1]
        irreducible = True
        for d in range(1, n // 2 + 1):
            for coeffs in product(range(p), repeat=d):
                if not poly_rem(f, list(coeffs) + [1], p):
                    irreducible = False
                    break
            if not irreducible:
                break
        if irreducible:
            return f
    raise AssertionError("No irreducible modulus")


class Field:
    def __init__(self, p, degree):
        self.p, self.degree = p, degree
        self.size = p ** degree
        self.modulus = irreducible_polynomial(p, degree)
        self.digits = [self.unpack(z) for z in range(self.size)]
        self.plus = [[self.pack([(u + v) % p for u, v in zip(self.digits[a], self.digits[b])])
                      for b in range(self.size)] for a in range(self.size)]
        self.times = [[self._multiply(a, b) for b in range(self.size)] for a in range(self.size)]

    def unpack(self, x):
        out = []
        for _ in range(self.degree):
            out.append(x % self.p)
            x //= self.p
        return out

    def pack(self, a):
        z = 0
        for c in reversed(a):
            z = z * self.p + c
        return z

    def _multiply(self, a, b):
        c = [0] * (2 * self.degree - 1)
        for i, u in enumerate(self.digits[a]):
            for j, v in enumerate(self.digits[b]):
                c[i + j] += u * v
        for k in range(len(c) - 1, self.degree - 1, -1):
            v = c[k] % self.p
            for i in range(self.degree):
                c[k - self.degree + i] -= v * self.modulus[i]
        return self.pack([v % self.p for v in c[:self.degree]])

    def power(self, a, n):
        out = 1
        while n:
            if n & 1:
                out = self.times[out][a]
            a = self.times[a][a]
            n >>= 1
        return out


def signature(perm):
    seen = set()
    cycles = 0
    for x in range(len(perm)):
        if x in seen:
            continue
        cycles += 1
        y = x
        while y not in seen:
            seen.add(y)
            y = perm[y]
    return -1 if (len(perm) - cycles) % 2 else 1


def verify():
    checks = 0
    permutations = 0
    signatures = set()
    for p, s in [(3, 1), (5, 1), (7, 1), (11, 1), (3, 2)]:
        q = p ** s
        E = Field(p, 2 * s)
        size = q * q
        assert E.size == size
        # Field sanity checks, independently of candidate permutations.
        for x in range(1, size):
            assert E.power(x, size - 1) == 1
        ds = [d for d in range(1, 2 * (q + 1) + 1)
              if gcd(d, q + 1) == 2]
        rs = [r for r in range(1, min(size, 27)) if gcd(r, 2 * (q - 1)) == 1]
        field_permutations = 0
        for d in ds:
            pow_d = [E.power(x, d * (q - 1)) for x in range(size)]
            for r in rs:
                pow_r = [E.power(x, r) for x in range(size)]
                for a in range(1, size):
                    perm = [E.times[pow_r[x]][E.plus[pow_d[x]][a]] for x in range(size)]
                    checks += 1
                    if len(set(perm)) != size:
                        continue
                    permutations += 1
                    field_permutations += 1
                    sign = signature(perm)
                    expected = -1 if ((r - 1) // 2) % 2 else 1
                    signatures.add(sign)
                    assert sign == expected, (q, d, r, a, sign, expected)
        print("PASS q=%s; modulus=%s; indices=%s; exponents=%s; permutations=%s" %
              (q, E.modulus, len(ds), len(rs), field_permutations))
    assert permutations > 0
    assert signatures == {-1, 1}
    print("PASS total_parameter_checks=%s; permutation_instances=%s; even_and_odd_seen=true" %
          (checks, permutations))


if __name__ == '__main__':
    verify()
