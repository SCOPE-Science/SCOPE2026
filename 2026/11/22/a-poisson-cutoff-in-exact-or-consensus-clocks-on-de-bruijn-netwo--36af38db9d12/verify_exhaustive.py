"""Independent direct-state verification of OR dynamics on de Bruijn digraphs."""
from itertools import product
from random import Random


def step(mask, q, d):
    n = q ** d
    cutoff = q ** (d - 1)
    target = 0
    for v in range(n):
        tail = v // q
        sources = (a * cutoff + tail for a in range(q))
        if any((mask >> u) & 1 for u in sources):
            target |= 1 << v
    return target


def theoretical_cumulative(q, d, t):
    return (2 ** (q ** t) - 1) ** (q ** (d - t))


def exhaustive(q, d):
    n = q ** d
    allmask = (1 << n) - 1
    hits = [0] * (d + 1)
    no_hit = 0
    for x in range(1 << n):
        y = x
        if x == allmask:
            hits[0] += 1
            continue
        if x == 0:
            assert step(x, q, d) == 0
            no_hit += 1
            continue
        for t in range(1, d + 1):
            y = step(y, q, d)
            if y == allmask:
                hits[t] += 1
                break
        else:
            raise AssertionError((q, d, x, y))
    expected = [theoretical_cumulative(q, d, 0)]
    expected += [theoretical_cumulative(q, d, t) - theoretical_cumulative(q, d, t-1) for t in range(1,d+1)]
    assert hits == expected, (q,d,hits,expected)
    assert no_hit == 1
    return (q,d,hits)


def random_checks(q, d, samples=2500):
    rng = Random(948110)
    n = q ** d
    allmask = (1 << n) - 1
    for _ in range(samples):
        x = rng.getrandbits(n)
        y = x
        for t in range(d + 1):
            group_size = q ** t
            groups = q ** (d - t)
            # Source words with equal final d-t symbols are separated by q^(d-t).
            block_coverage = all(any((x >> (a*groups+r)) & 1 for a in range(group_size)) for r in range(groups))
            assert (y == allmask) == block_coverage, (q,d,t,x)
            if t != d:
                y = step(y, q, d)


if __name__ == "__main__":
    for q, d in ((2,1),(2,2),(2,3),(2,4),(3,1),(3,2)):
        print("CENSUS", *exhaustive(q,d))
    random_checks(2,5,1000)
    random_checks(3,3,1000)
    print("DIRECT_DYNAMICS_ALL_CHECKS_PASSED")
