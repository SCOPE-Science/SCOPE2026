"""Exact finite verification of one-point-extension ranks for linear forests.

Python 3 standard library only. This is corroboration, not an all-order proof.
"""
from collections import Counter
from functools import lru_cache
from fractions import Fraction
from math import factorial


def partitions(n, minimum=1):
    if n == 0:
        yield ()
        return
    for x in range(minimum, n + 1):
        for rest in partitions(n - x, x):
            yield (x,) + rest


def forest(parts):
    adj = []
    for length in parts:
        offset = len(adj)
        adj.extend(set() for _ in range(length))
        for i in range(length - 1):
            a, b = offset + i, offset + i + 1
            adj[a].add(b)
            adj[b].add(a)
    return adj


def is_linear_forest(adj):
    n = len(adj)
    if any(len(row) > 2 for row in adj):
        return False
    seen = set()
    for i in range(n):
        if i not in seen:
            stack, nodes, degrees = [i], 0, 0
            seen.add(i)
            while stack:
                u = stack.pop()
                nodes += 1
                degrees += len(adj[u])
                for v in adj[u]:
                    if v not in seen:
                        seen.add(v)
                        stack.append(v)
            if degrees != 2 * (nodes - 1):
                return False
    return True


def allowed_masks(adj, selected):
    k = len(selected)
    induced = [{j for j, v in enumerate(selected) if v in adj[u]}
               for u in selected]
    answer = []
    for mask in range(1 << k):
        extended = [set(s) for s in induced] + [set()]
        for j in range(k):
            if (mask >> j) & 1:
                extended[j].add(k)
                extended[k].add(j)
        if is_linear_forest(extended):
            answer.append(mask)
    return answer


def prime_rank(adj, selected, depth):
    """Unroll rank for each abstract legal extension of an induced base."""
    n = len(adj)

    @lru_cache(None)
    def recurse(chosen, remaining):
        if remaining == 0:
            return True
        old = [i for i in range(n) if chosen & (1 << i)]
        for mask in allowed_masks(adj, old):
            exists = False
            for v in range(n):
                if chosen & (1 << v):
                    continue
                profile = sum(((u in adj[v]) << j) for j, u in enumerate(old))
                if profile == mask and recurse(chosen | (1 << v), remaining - 1):
                    exists = True
                    break
            if not exists:
                return False
        return True

    chosen = sum(1 << v for v in selected)
    return recurse(chosen, depth)


def rank_three_direct(adj):
    # Independent implementation that tests the relevant two-point prime types.
    n = len(adj)
    for u in range(n):
        possible_near = False
        possible_far = False
        for v in range(n):
            if u == v:
                continue
            required = set(allowed_masks(adj, [u, v]))
            observed = {int(u in adj[w]) + 2 * int(v in adj[w])
                        for w in range(n) if w not in (u, v)}
            if required <= observed:
                if v in adj[u]:
                    possible_near = True
                else:
                    possible_far = True
        if possible_near and possible_far:
            return True
    return False


def expected(parts):
    return sum(parts) >= 6 and max(parts, default=0) >= 5


def labelled_copies(parts):
    n = sum(parts)
    multiplicities = Counter(parts)
    result = factorial(n)
    for k, count in multiplicities.items():
        result //= factorial(count)
        if k >= 2:
            result //= 2 ** count
    return result


def exp_series(max_n, cutoff=None):
    # exp(z + sum_{k>=2} z^k/2), optionally truncating path sizes.
    c = [Fraction(1)]
    for n in range(1, max_n + 1):
        total = Fraction(0)
        for k in range(1, n + 1):
            if cutoff is not None and k > cutoff:
                continue
            wk = Fraction(1) if k == 1 else Fraction(1, 2)
            total += k * wk * c[n - k]
        c.append(total / n)
    return c


def main():
    checked = 0
    total = 13
    a = exp_series(total)
    b = exp_series(total, cutoff=4)
    print('n | unlabeled forests | rank>=3 types | labelled rank>=3')
    for n in range(total + 1):
        forests = list(partitions(n))
        qualifying = []
        for p in forests:
            g = forest(p)
            d = rank_three_direct(g)
            assert d == expected(p), ('pair profile', p)
            checked += 1
            if d:
                qualifying.append(p)
        count = sum(labelled_copies(p) for p in qualifying)
        coeff = factorial(n) * (a[n] - b[n])
        if n >= 6:
            assert coeff.denominator == 1 and coeff == count, (n, coeff, count)
        else:
            assert count == 0
        print(n, len(forests), len(qualifying), count)
    print('ALL_UNLABELLED_FAMILIES_DIRECTLY_CHECKED', checked)
    generic = 0
    for n in range(1, 11):
        for p in partitions(n):
            g = forest(p)
            assert prime_rank(g, (), 3) == expected(p), ('recursive rank3', p)
            assert not prime_rank(g, (), 4), ('recursive rank4', p)
            generic += 1
    print('GENERIC_RECURSIVE_CHECKS', generic, 'forest types, ranks 3 and 4')
    assert rank_three_direct(forest((5, 1)))
    assert rank_three_direct(forest((6,)))
    assert not rank_three_direct(forest((5,)))
    assert not rank_three_direct(forest((4, 4)))
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    main()
