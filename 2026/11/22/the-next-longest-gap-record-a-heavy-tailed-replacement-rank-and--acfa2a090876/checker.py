"""Reproducible checks for a marked longest-gap record law.

The program tests finite algebra and simulates actual point insertions. It does not
substitute numerical observations for the infinite-dimensional convergence proof.
"""
import bisect
import math
import random


def verify():
    checks = 0
    def check(ok, message):
        nonlocal checks
        if not ok:
            raise AssertionError(message)
        checks += 1

    # Exact telescoping identities for the limiting replacement rank.
    for k in range(2, 301):
        pmf_sum = math.fsum(1.0 / (j * (j - 1)) for j in range(2, k + 1))
        check(abs(pmf_sum - (1 - 1 / k)) < 2e-14, 'rank telescoping')
        check(abs((1 / ((k - 1) * k)) - (1 / (k - 1) - 1 / k)) < 2e-15,
              'rank mass difference')

    # Conditional maximum CDF and the unconditional analytic mixture.
    for yi in range(1, 251):
        y = yi / 40
        q = -math.expm1(-y)
        cutoff = 10000
        partial = math.fsum(q ** j / (j * (j + 1)) for j in range(1, cutoff))
        exact = 1 - y / math.expm1(y)
        # Omitted tail <= 1/cutoff, uniformly in q.
        check(-2e-13 <= exact - partial < 1.1 / cutoff + 5e-13,
              'analytic mixture with rigorous tail control')
        check(abs((1 - exact) - y / math.expm1(y)) < 3e-15,
              'survival formula')

    # Independent exponential descending gaps: a finite structural identity.
    for k in range(2, 70):
        # The CDF of a maximum of k-1 exponentials is q^(k-1).
        for yi in (4, 12, 40, 80):
            y = yi / 20
            product = math.prod([1 - math.exp(-y)] * (k - 1))
            check(abs(product - (1 - math.exp(-y)) ** (k - 1)) < 1e-12,
                  'independent exponential maximum CDF')

    # Direct discrete-time uniform insertion: retain original gap parent ranks.
    rng = random.Random(91547)
    table = []
    for n, trials in ((40, 140), (300, 140), (2400, 180)):
        clock_total = 0.0
        k2 = 0
        drop_below_one = 0
        cut_wins = 0
        for _ in range(trials):
            raw = [rng.expovariate(1.0) for _ in range(n)]
            total = math.fsum(raw)
            gaps = sorted((x / total for x in raw), reverse=True)
            ends = []
            cumulative = 0.0
            for g in gaps:
                cumulative += g
                ends.append(cumulative)
            ends[-1] = 1.0
            fragments = {}
            steps = 0
            while True:
                u = rng.random()
                i = bisect.bisect_left(ends, u)
                low = ends[i - 1] if i else 0.0
                relative = min(1.0, max(0.0, (u - low) / gaps[i]))
                fragments.setdefault(i, []).append(relative)
                steps += 1
                # A strict new maximum occurs exactly on the first hit to rank 1.
                if i == 0:
                    break
                check(gaps[0] > gaps[1], 'largest original intact until first hit')
            new_gaps = gaps[:]
            for i, locs in fragments.items():
                cuts = [0.0] + sorted(locs) + [1.0]
                new_gaps[i] = gaps[i] * max(b - a for a, b in zip(cuts[:-1], cuts[1:]))
                check(new_gaps[i] < gaps[i] + 1e-14, 'fragments never longer')
            new_rank = max(range(n), key=lambda i: new_gaps[i])
            drop = n * (gaps[0] - new_gaps[new_rank])
            check(drop > 0, 'strict record when previous maximum hit')
            check(new_gaps[new_rank] == max(new_gaps), 'new maximum parent rank')
            clock_total += math.log(n) * steps / n
            k2 += new_rank == 1
            drop_below_one += drop <= 1
            cut_wins += new_rank in fragments
        table.append((n, clock_total / trials, k2 / trials,
                      drop_below_one / trials, cut_wins / trials))
    print('PASS:', checks, 'assertions')
    print('Finite illustration: n, mean scaled W, Pr(K_n=2), Pr(D_n<=1), cut-parent winner')
    for row in table:
        print('%5d %.4f %.4f %.4f %.4f' % row)
    print('Limit benchmarks: 1, 0.5, %.4f, 0' % (1 - 1 / math.expm1(1)))
    print('Caveat: cut-parent winner decays very slowly, often of order 1/log n.')


if __name__ == '__main__':
    verify()
