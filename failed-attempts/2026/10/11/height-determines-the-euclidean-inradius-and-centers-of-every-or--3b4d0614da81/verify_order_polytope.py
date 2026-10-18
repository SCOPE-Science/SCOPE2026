#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 60
SQ2 = Decimal(2).sqrt()


def closure_from_mask(n, mask):
    reach = [0] * n
    bit = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (mask >> bit) & 1:
                reach[i] |= 1 << j
            bit += 1
    for k in range(n):
        km = 1 << k
        for i in range(k):
            if reach[i] & km:
                reach[i] |= reach[k]
    code = 0
    bit = 0
    for i in range(n):
        for j in range(i + 1, n):
            if reach[i] >> j & 1:
                code |= 1 << bit
            bit += 1
    return code, reach


def covers(n, reach):
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            if not (reach[i] >> j & 1):
                continue
            between = False
            for k in range(i + 1, j):
                if (reach[i] >> k & 1) and (reach[k] >> j & 1):
                    between = True
                    break
            if not between:
                out.append((i, j))
    return out


def check_poset(n, reach):
    cv = covers(n, reach)
    preds = [[] for _ in range(n)]
    succs = [[] for _ in range(n)]
    for i, j in cv:
        preds[j].append(i)
        succs[i].append(j)

    dm = [0] * n
    for j in range(n):
        if preds[j]:
            dm[j] = 1 + max(dm[i] for i in preds[j])
    dp = [0] * n
    for i in range(n - 1, -1, -1):
        if succs[i]:
            dp[i] = 1 + max(dp[j] for j in succs[i])
    h = 1 + max(dm)
    assert 1 + max(dp) == h

    den = Decimal(2) + Decimal(h - 1) * SQ2
    r = Decimal(1) / den
    L = [r * (Decimal(1) + SQ2 * Decimal(dm[i])) for i in range(n)]
    U = [Decimal(1) - r * (Decimal(1) + SQ2 * Decimal(dp[i])) for i in range(n)]
    eps = Decimal('1e-50')
    for i in range(n):
        assert L[i] + eps >= r
        assert L[i] <= Decimal(1) - r + eps
        assert U[i] + eps >= r
        assert U[i] <= Decimal(1) - r + eps
        assert L[i] <= U[i] + eps
    for i, j in cv:
        assert L[j] - L[i] + eps >= SQ2 * r
        assert U[j] - U[i] + eps >= SQ2 * r
        assert dm[j] >= dm[i] + 1
        assert dp[i] >= dp[j] + 1

    uniq_depth = all(dm[i] + dp[i] == h - 1 for i in range(n))
    on_longest = all(dm[i] + dp[i] + 1 == h for i in range(n))
    assert uniq_depth == on_longest
    if uniq_depth:
        for i in range(n):
            assert abs(L[i] - U[i]) <= eps
    else:
        assert any(U[i] - L[i] > eps for i in range(n))


def main():
    expected = {1: 1, 2: 2, 3: 7, 4: 40, 5: 357, 6: 4824}
    total = 0
    for n in range(1, 7):
        m = n * (n - 1) // 2
        seen = {}
        for mask in range(1 << m):
            code, reach = closure_from_mask(n, mask)
            if code not in seen:
                seen[code] = reach
        assert len(seen) == expected[n], (n, len(seen), expected[n])
        for reach in seen.values():
            check_poset(n, reach)
        total += len(seen)
    assert total == 5231
    print('VERIFY_OK order-polytope inradius posets=5231 n=1..6')


if __name__ == '__main__':
    main()
