#!/usr/bin/env python3
"""Finite checks for the powers-of-two indicator palindromic-length theorem.
Run: python3 verify.py; Python standard library only.
These tests do not replace the all-length mathematical proof.
"""


def is_power_two(v):
    return v > 0 and v & (v - 1) == 0


def characteristic(N):
    return bytes(is_power_two(i) for i in range(N))


def exact_prefix_pal_lengths(word):
    """All palindromes, exact DP via center expansion."""
    n = len(word)
    by_right = [[] for _ in range(n + 1)]
    for c in range(n):
        a = c
        b = c
        while a >= 0 and b < n and word[a] == word[b]:
            by_right[b + 1].append(a)
            a -= 1
            b += 1
        a, b = c, c + 1
        while a >= 0 and b < n and word[a] == word[b]:
            by_right[b + 1].append(a)
            a -= 1
            b += 1
    dp = [0] + [n + 1] * n
    for b in range(1, n + 1):
        dp[b] = min(dp[a] + 1 for a in by_right[b])
    return dp


def independent_dp(word):
    """Independent dynamic palindrome recurrence; only used on small prefixes."""
    N = len(word)
    pal = [[False] * (N + 1) for _ in range(N + 1)]
    d = [0] + [N + 1] * N
    for b in range(1, N + 1):
        for a in range(b - 1, -1, -1):
            pal[a][b] = word[a] == word[b - 1] and (b - a <= 2 or pal[a + 1][b - 1])
            if pal[a][b] and d[a] + 1 < d[b]:
                d[b] = d[a] + 1
    return d


def pairing_endpoints(j):
    e = 0
    for i in range(j + 1):
        e = 3 * 4**i + 1 - e
    return e



def construct_prefix(n):
    """Explicit factorization behind the upper bound, as end-exclusive intervals."""
    if n == 0:
        return []
    if n == 1:
        return [(0, 1)]
    k = (n - 1).bit_length()
    m = k // 2
    pieces = []
    s = 0
    completed = m - 1 if k % 2 == 0 else m
    for j in range(completed):
        e = 3 * 4**j + 1 - s
        pieces.append((s, e))
        s = e
    if k % 2 == 0:
        a = 4**(m - 1)
        E = 3 * a - s + 1
        if n < E:
            t = 3 * a - n + 1
            if s < t:
                pieces.append((s, t))
            pieces.append((t, n))
        else:
            pieces.append((s, E))
            if E < n:
                pieces.append((E, n))
    else:
        a = 4**m
        E = 2 * a - s + 1
        if n < E:
            t = 2 * a - n + 1
            if s < t:
                pieces.append((s, t))
            pieces.append((t, n))
        else:
            pieces.append((s, E))
            if E < n:
                pieces.append((E, n))
    return pieces


def main():
    N = 4096
    w = characteristic(N)
    dp = exact_prefix_pal_lengths(w)
    d2 = independent_dp(w[:256])
    assert dp[:257] == d2
    count = 0
    for n in range(1, N + 1):
        k = 0 if n <= 1 else (n - 1).bit_length()
        lower = (k + 1) // 2
        assert lower <= dp[n] <= lower + 1, (n, dp[n], k)
        parts = construct_prefix(n)
        assert 0 == parts[0][0] and n == parts[-1][1]
        assert all(0 <= l < r <= n for l, r in parts)
        assert all(parts[i][1] == parts[i + 1][0] for i in range(len(parts) - 1))
        assert all(w[l:r] == w[l:r][::-1] for l, r in parts)
        assert len(parts) <= lower + 1
        count += 1
    for k in range(2, 12):
        n = (1 << k) - 1
        assert dp[n] == (k + 1) // 2 + 1, (k, n, dp[n])
        count += 1
    e = 0
    for j in range(1, 8):
        e0 = e
        e = 3 * 4**(j - 1) + 1 - e
        assert e == pairing_endpoints(j - 1)
        a = 4**(j - 1)
        b = 2 * a
        assert e0 <= a <= b < e
        assert [i for i in range(e0, e) if is_power_two(i)] == [a, b]
        # Exact symbolic palindrome test by symmetric power-indicator positions.
        assert e0 + (e - 1) == a + b
        if e <= N:
            assert w[e0:e] == w[e0:e][::-1]
        if e <= N:
            assert dp[e] == j
        count += 1
    print('VERIFY_OK', 'prefixes=', N, 'independent=', 256, 'dyadic_scales=', 10, 'claims_checked=',count)


if __name__ == '__main__':
    main()
