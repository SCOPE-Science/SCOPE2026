"""Bounded exact verification of the two-colour extension game."""

from functools import lru_cache
from itertools import combinations, permutations, product


def spend(pair, colour):
    return (pair[0] - (colour == 0), pair[1] - (colour == 1))


@lru_cache(None)
def survives(depth, marked, free):
    if depth == 0:
        return True
    for i, pair in enumerate(marked):
        for colour in range(2):
            if pair[colour] == 0:
                return False
            updated = tuple(sorted(marked[:i] + marked[i+1:] + (spend(pair, colour),)))
            if not survives(depth - 1, updated, free):
                return False
    return all(any(pair[colour] and survives(
        depth - 1, tuple(sorted(marked + (spend(pair, colour),))), free[:i] + free[i+1:]
    ) for i, pair in enumerate(free)) for colour in range(2))


def all_hosts(budget):
    pairs = [(r, b) for r in range(budget+1) for b in range(budget-r+1) if r+b]

    def multisets(lo, remaining, prefix):
        yield prefix
        for i in range(lo, len(pairs)):
            cost = sum(pairs[i])
            if cost <= remaining:
                yield from multisets(i, remaining-cost, prefix + (pairs[i],))

    yield from multisets(0, budget, ())


def marked_positions(host):
    selections = [list(product(range(r+1), range(b+1))) for r, b in host]
    for selection in product(*selections):
        marked, free = [], []
        for (r, b), (red_used, blue_used) in zip(host, selection):
            if red_used or blue_used:
                marked.append((r-red_used, b-blue_used))
            else:
                free.append((r, b))
        yield tuple(sorted(marked)), tuple(free)


def staircase_hosts(t):
    sizes = set(range(1, t+1))
    for k in range(t+1):
        for r in combinations(sorted(sizes), k):
            for b in combinations(sorted(sizes), k):
                for q in permutations(b):
                    yield tuple(sorted(list(zip(r, q)) + [(v, 0) for v in sizes.difference(r)]
                                       + [(0, v) for v in sizes.difference(b)]))


def main():
    nhost = npos = checks = 0
    for host in all_hosts(7):
        nhost += 1
        for marked, free in marked_positions(host):
            npos += 1
            for d in range(8):
                bound = all(min(p) >= d for p in marked) and survives(d, (), free)
                assert survives(d, marked, free) == bound, (host, marked, free, d)
                checks += 1
    assert (nhost, npos, checks) == (573, 24963, 199704)
    print('RELATIVE_SEPARATION_OK', nhost, npos, checks)

    predicted = [{()}, {((1, 1),), ((0, 1), (1, 0))}]
    for t in range(2, 6):
        predicted.append({tuple(sorted(h + ((t, t),))) for h in predicted[t-1]} |
                         {tuple(sorted(h + ((t, t-1), (t-1, t)))) for h in predicted[t-2]})
    for t, want in enumerate(predicted):
        candidates = set(staircase_hosts(t))
        got = {h for h in candidates if survives(t, (), h)}
        assert got == want and all(not survives(t+1, (), h) for h in got)
        assert len(got) == (1, 2, 3, 5, 8, 13)[t]
        print('EXTREMAL_OK', t, len(candidates), len(got))
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    main()
