"""Reproduce finite checks for the signed short binary representation theorem."""

from collections import defaultdict


def direct_signed_counts(limit):
    even = [0] * (limit + 1)
    odd = [0] * (limit + 1)
    # A representation of a positive n <= limit has length d only if
    # 2^(d-2)+1 <= n for d>=2 (the shortness convention).
    d = 1
    while d == 1 or (1 << (d - 2)) + 1 <= limit:
        tail_count = d - 1
        for code in range(3**tail_count):
            t = code
            digits = []
            for _ in range(tail_count):
                digits.append((t % 3) - 1)
                t //= 3
            if d >= 2 and digits[-1] == -1:
                continue
            n = (1 << (d - 1)) + sum(a << j for j, a in enumerate(digits))
            if 1 <= n <= limit:
                counts = odd if sum(a == -1 for a in digits) % 2 else even
                counts[n] += 1
        d += 1
    return [even[n] - odd[n] for n in range(limit + 1)]


def recursive_values(limit):
    g = [0] * (limit + 1)
    if limit:
        g[1] = 1
    for n in range(2, limit + 1):
        g[n] = g[n // 2] if n % 2 == 0 else g[n // 2] - g[n // 2 + 1]
    return g


TRANS = {
    "P": ("I", "Z+"), "I": ("P", "I"),
    "Z+": ("Z-", "N-"), "Z-": ("Z+", "N+"),
    "N+": ("R+", "N+"), "N-": ("R-", "N-"),
    "R+": ("N+", "N-"), "R-": ("N-", "N+"),
}
POS = {"P", "I", "N+", "R+"}
NEG = {"N-", "R-"}


def state(a, b):
    if a == b and a > 0:
        return "P"
    if a > 0 and b == 0:
        return "I"
    if a == 0 and b > 0:
        return "Z+"
    if a == 0 and b < 0:
        return "Z-"
    if a > 0 and b < 0:
        return "N+"
    if a < 0 and b > 0:
        return "N-"
    if 0 < a < b:
        return "R+"
    if b < a < 0:
        return "R-"
    raise AssertionError((a, b))


def main():
    limit = 1300
    independent = direct_signed_counts(limit)
    recursive = recursive_values(limit)
    assert independent == recursive, "representation enumeration disagrees with recurrence"

    Lmax = 16
    g = recursive_values(1 << Lmax)
    states = {"P": 1}
    f0, f1 = 0, 1
    for L in range(1, Lmax + 1):
        N = 1 << L
        pos = sum(a > 0 for a in g[1:N])
        neg = sum(a < 0 for a in g[1:N])
        zeros = sum(a == 0 for a in g[1:N])
        assert pos == (1 << (L - 1))
        assert sum(g[:N]) == L
        assert sum(a * a for a in g[:N]) == (3 ** (L - 1) + 1) // 2
        assert sum(g[n] * g[n + 1] for n in range(N)) == 1
        f0, f1 = f1, f0 + f1  # F_L and F_(L+1)
        assert zeros == f1 - 1
        assert neg == (1 << (L - 1)) - f1
        assert pos + neg + zeros == N - 1
        assert sum(states.get(s, 0) for s in POS) == (1 if L == 1 else 1 << (L - 2))
        assert sum(states.get(s, 0) for s in NEG) == sum(g[n] < 0 for n in range(1 << (L - 1), N))
        for n in range(1 << (L - 1), N):
            path = bin(n)[3:]
            s = "P"
            for digit in path:
                s = TRANS[s][int(digit)]
            assert s == state(g[n], g[n + 1]), (n, s)
        updated = defaultdict(int)
        for s, amount in states.items():
            for nxt in TRANS[s]:
                updated[nxt] += amount
        states = dict(updated)
    print("PASS: independently enumerated short signed representations up to", limit)
    print("PASS: exhaustive eight-state and sign checks through 2^", Lmax, sep="")
    print("PASS: exact signed first, second and adjacent moments through depth", Lmax)


if __name__ == "__main__":
    main()
