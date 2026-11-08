"""Exact arithmetic checks for a mixed Wythoff representation distribution.

The script is a finite consistency check, not a proof of the asymptotic law.
It requires only the Python standard library.
"""
from math import isqrt, sqrt, log

PHI = (1 + sqrt(5)) / 2
ALPHA = 1 / PHI
BETA = 1 - ALPHA


def lower(k):
    assert k >= 1
    return (k + isqrt(5 * k * k)) // 2


def upper(k):
    return lower(k) + k


def phase_profile(t):
    if t < BETA:
        return BETA - t
    if t < 2 * BETA:
        return t - BETA
    return BETA


def direct_pairs(limit):
    count = [0] * (limit + 1)
    for h in range(1, limit + 1):
        u = lower(h)
        if u + 2 > limit:
            break
        for k in range(1, limit + 1):
            s = u + upper(k)
            if s > limit:
                break
            count[s] += 1
    return count


def independent_convolution(limit):
    lower_set = {lower(h) for h in range(1, limit + 1) if lower(h) <= limit}
    upper_set = {upper(k) for k in range(1, limit + 1) if upper(k) <= limit}
    count = [0] * (limit + 1)
    for n in range(1, limit + 1):
        count[n] = sum((m in lower_set and n - m in upper_set) for m in range(1, n))
    return count


def main():
    limit = 6000
    counts = direct_pairs(limit)
    assert counts[1:11] == [0, 0, 1, 0, 1, 2, 0, 3, 1, 2]
    conv = independent_convolution(450)
    assert counts[:451] == conv
    for m in range(1, limit + 1):
        a = lower(m)
        b = upper(m)
        assert b == a + m
    max_dev = max(abs(counts[n] - (n - 1) * phase_profile((n * ALPHA) % 1)) for n in range(1, limit + 1))
    assert max_dev <= 10.0 * log(limit + 1)
    for j in (1, 2):
        target = BETA ** j * (1 - 2 * BETA + 2 * BETA / (j + 1))
        observed = sum((counts[n] / n) ** j for n in range(1, limit + 1)) / limit
        assert abs(observed - target) < 0.025
        print(f"MOMENT power={j} observed={observed:.12f} target={target:.12f}")
    print(f"VERIFY_OK direct_range=1..{limit} independent_convolution=1..450 exact_integer_floors=yes max_phase_error={max_dev:.6f}")


if __name__ == '__main__':
    main()
