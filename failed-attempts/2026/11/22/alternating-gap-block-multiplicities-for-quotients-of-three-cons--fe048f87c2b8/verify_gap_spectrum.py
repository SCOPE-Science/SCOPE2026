#!/usr/bin/env python3
"""Independent finite verification of a triple-coin quotient gap-spectrum theorem."""
from collections import Counter


def expected_histogram(p: int, k: int) -> Counter:
    assert p >= 2 and k >= 1
    c = (2 * p + 2) // 3 - (p + 2) // 3
    out = Counter({k * ((p + 2) // 3): 1})
    for ell in range(1, k):
        out[ell] += c if (k - ell) % 2 else (p - c)
    return out


def expected_genus(p: int, k: int) -> int:
    c = (2 * p + 2) // 3 - (p + 2) // 3
    return k * ((p + 2) // 3) + p * ((k - 1) ** 2 // 4) + c * (k // 2)


def direct_histogram(p: int, k: int):
    """Unrestricted coin membership via recurrence, without using interval identities."""
    a = p * k + 1
    stop = p * k * k + 4 * p * k + 40
    bound = p * (stop + 1)
    reach = bytearray(bound + 1)
    reach[0] = 1
    for x in range(1, bound + 1):
        for coin in (a, a + 1, a + 2):
            if x >= coin and reach[x - coin]:
                reach[x] = 1
                break
    gaps = Counter()
    gaps_count = 0
    last_gap_end = -1
    run = 0
    for n in range(stop + 1):
        if reach[p * n]:
            if run:
                gaps[run] += 1
                gaps_count += run
                last_gap_end = n - 1
                run = 0
        else:
            run += 1
    assert run == 0, (p, k, stop)
    assert all(reach[p * n] for n in range(stop - (a + 2), stop + 1)), (p, k)
    return gaps, gaps_count, last_gap_end


def main():
    tests = [(p, k) for p in range(2, 16) for k in range(1, 16)]
    tests += [(19, 4), (19, 9), (19, 15), (23, 5), (23, 8),
              (31, 4), (31, 7), (37, 6), (41, 5)]
    total_blocks = 0
    total_gaps = 0
    total_points = 0
    for p, k in tests:
        hist, genus, last_gap = direct_histogram(p, k)
        pred = expected_histogram(p, k)
        assert hist == pred, (p, k, hist, pred)
        assert genus == expected_genus(p, k), (p, k, genus)
        assert genus == sum(ell * c for ell, c in pred.items())
        assert last_gap > 0
        total_blocks += sum(hist.values())
        total_gaps += genus
        total_points += p * (p * k * k + 4 * p * k + 41)
    print('PASS', len(tests), 'parameter pairs', 'gap blocks', total_blocks,
          'missing integers', total_gaps, 'coin membership positions', total_points)
    for p, k in [(2, 5), (3, 5), (5, 4), (7, 8)]:
        print('example', (p, k), 'histogram', sorted(expected_histogram(p, k).items()))


if __name__ == '__main__':
    main()
