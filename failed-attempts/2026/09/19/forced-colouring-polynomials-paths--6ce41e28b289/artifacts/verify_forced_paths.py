from itertools import product
from math import comb


def forces_path(state, lam):
    s = list(state)
    n = len(s)
    for i in range(n - 1):
        if s[i] >= 0 and s[i + 1] >= 0 and s[i] == s[i + 1]:
            return False
    changed = True
    while changed:
        changed = False
        for v in range(n):
            if s[v] >= 0:
                continue
            colours = set()
            if v > 0 and s[v - 1] >= 0:
                colours.add(s[v - 1])
            if v + 1 < n and s[v + 1] >= 0:
                colours.add(s[v + 1])
            if len(colours) == lam - 1:
                missing = set(range(lam)) - colours
                if len(missing) == 1:
                    s[v] = missing.pop()
                    changed = True
    if any(x < 0 for x in s):
        return False
    return all(s[i] != s[i + 1] for i in range(n - 1))


def brute_counts(n, lam=3):
    counts = [0] * (n + 1)
    for state in product(range(-1, lam), repeat=n):
        if forces_path(state, lam):
            counts[sum(x >= 0 for x in state)] += 1
    return counts


def formula_counts(n):
    counts = [0] * (n + 1)
    for j in range((n - 1) // 2 + 1):
        k = n - j
        counts[k] = 3 * (2 ** (n - j - 1)) * comb(n - 1 - j, j)
    return counts


def main():
    checked = 0
    for n in range(2, 9):
        got = brute_counts(n)
        expected = formula_counts(n)
        if got != expected:
            raise AssertionError((n, got, expected))
        checked += 1
    # P_3=K_{1,2}: size-2 and size-3 forcing assignments are 6 and 12.
    assert brute_counts(3) == [0, 0, 6, 12]
    print(f"PASS: exact coefficient formula verified for P_n, 2 <= n <= 8 ({checked} path orders).")
    print("P_3 forcing-domain counts: size 2 -> 6, size 3 -> 12.")


if __name__ == "__main__":
    main()
