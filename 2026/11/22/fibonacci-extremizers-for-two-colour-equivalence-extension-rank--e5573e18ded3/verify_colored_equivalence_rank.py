"""Finite checks of the two-colour equivalence one-point-extension rank.

Execute with Python 3.9 or later, without additional packages.
A finite check corroborates, but does not replace, the all-size proofs.
"""
from functools import lru_cache
from itertools import combinations, permutations, product


def normal(caps, used):
    return tuple(sorted((int(flag), a, b) for (a, b), flag in zip(caps, used)))


@lru_cache(None)
def game_ge(state, depth):
    """The defining game: universal request, existential realization."""
    if depth == 0:
        return True
    for i, (flag, a, b) in enumerate(state):
        if flag:
            for color in (0, 1):
                qty = a if color == 0 else b
                if qty == 0:
                    return False
                next_state = list(state)
                next_state[i] = (1, a - (color == 0), b - (color == 1))
                if not game_ge(tuple(sorted(next_state)), depth - 1):
                    return False
    for color in (0, 1):
        possible = False
        for i, (flag, a, b) in enumerate(state):
            if flag == 0 and (a if color == 0 else b) > 0:
                next_state = list(state)
                next_state[i] = (1, a - (color == 0), b - (color == 1))
                if game_ge(tuple(sorted(next_state)), depth - 1):
                    possible = True
                    break
        if not possible:
            return False
    return True


def separate_ge(state, depth):
    if any(flag and (a < depth or b < depth) for flag, a, b in state):
        return False
    free = tuple(sorted((0, a, b) for flag, a, b in state if flag == 0))
    return game_ge(free, depth)


def host_multisets(max_total):
    """All class-size-vector multisets up to max_total, no empty E-classes."""
    types = [(a, b) for a in range(max_total + 1)
             for b in range(max_total + 1 - a) if a + b > 0]
    types.sort()
    def rec(start, remaining, acc):
        yield tuple(acc)
        for j in range(start, len(types)):
            a, b = types[j]
            if a + b <= remaining:
                acc.append((a, b))
                yield from rec(j, remaining - a - b, acc)
                acc.pop()
    yield from rec(0, max_total, [])


def check_relative(max_total=7):
    hosts = states = comparisons = 0
    for caps in host_multisets(max_total):
        hosts += 1
        profiles = [list(product(range(a+1), range(b+1))) for a, b in caps]
        for selected in product(*profiles):
            state = tuple(sorted((int(r+b > 0), a-r, b-s)
                                 for (a, b), (r, s) in zip(caps, selected)))
            states += 1
            for depth in range(0, max_total+1):
                if game_ge(state, depth) != separate_ge(state, depth):
                    raise AssertionError((caps, selected, depth, state))
                comparisons += 1
    print('RELATIVE_SEPARATION_OK', hosts, states, comparisons)


def pairs_and_unmatched(rank):
    """Enumerate all joint couplings of the two forced staircase profiles."""
    colors = tuple(range(1, rank + 1))
    for count in range(rank + 1):
        for red in combinations(colors, count):
            for blue in combinations(colors, count):
                for arranged in permutations(blue):
                    matched = tuple(zip(red, arranged))
                    red_unused = tuple((r, 0) for r in colors if r not in red)
                    blue_unused = tuple((0, b) for b in colors if b not in blue)
                    yield tuple(sorted(matched + red_unused + blue_unused))


def fibonacci(x):
    a, b = 0, 1
    for _ in range(x):
        a, b = b, a + b
    return a


def predicted(rank):
    """Canonical extremizers: top joint, top crossed, or split bottom."""
    if rank == 0:
        return {()}
    if rank == 1:
        return {((1, 1),), ((0, 1), (1, 0))}
    out = set()
    for tail in predicted(rank - 1):
        out.add(tuple(sorted(((rank, rank),) + tail)))
    for tail in predicted(rank - 2):
        out.add(tuple(sorted(((rank, rank-1), (rank-1, rank)) + tail)))
    return out


def check_extremal(max_rank=5):
    for depth in range(max_rank + 1):
        candidates = list(pairs_and_unmatched(depth))
        passing = {caps for caps in candidates if game_ge(
            tuple(sorted((0, a, b) for a, b in caps)), depth)}
        wanted = predicted(depth)
        assert passing == wanted, (depth, passing.symmetric_difference(wanted))
        assert len(passing) == fibonacci(depth + 2), (depth, len(passing))
        assert all(sum(a+b for a, b in caps) == depth*(depth+1) for caps in passing)
        print('EXTREMAL_OK', depth, len(candidates), len(passing))


if __name__ == '__main__':
    check_relative(7)
    check_extremal(5)
    print('ALL_CHECKS_OK', game_ge.cache_info())
