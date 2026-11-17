"""Exact finite verifier for single-chord completion of consecutive cycle sums.

Usage: python verify.py --start 8 --stop 301
Set bounds on --stop for bounded execution; verification ranges concatenate.
Only Python standard library required.
"""
import argparse
import csv
from pathlib import Path


def cycle_sums(n):
    """A bit is set when a nonempty cyclic interval has the given sum."""
    bits = 0
    for first in range(n):
        s = 0
        for length in range(n):
            s += (first + length) % n + 1
            bits |= 1 << s
    return bits


def extensions(path):
    """Sums of disjoint initial and terminal segments of path's interior."""
    inner = path[1:-1]
    k = len(inner)
    prefix = [0]
    suffix = [0]
    for value in inner:
        prefix.append(prefix[-1] + value)
    for value in reversed(inner):
        suffix.append(suffix[-1] + value)
    return {prefix[i] + suffix[j] for i in range(k + 1)
            for j in range(k - i + 1)}


def supported_sums(n, b):
    """Construct only sums of vertex sets known to induce a connected graph."""
    assert 3 <= b < n
    # The chord is (1,b). The two internally disjoint cycle paths are
    # 1,2,...,b and b,b+1,...,n,1.  Endpoints belong to the union.
    side1 = extensions(list(range(1, b + 1)))
    side2 = extensions([b] + list(range(b + 1, n + 1)) + [1])
    small, large = sorted((side1, side2), key=len)
    large_bits = 0
    for value in large:
        large_bits |= 1 << value
    extra = 0
    for value in small:
        extra |= large_bits << (1 + b + value)
    return cycle_sums(n) | extra


def brute_sums(n, b):
    """Independent exhaustive connectivity check for small n."""
    neighbor = [0] * n
    for i in range(n):
        j = (i + 1) % n
        neighbor[i] |= 1 << j
        neighbor[j] |= 1 << i
    neighbor[0] |= 1 << (b - 1)
    neighbor[b - 1] |= 1
    result = 0
    for subset in range(1, 1 << n):
        # Count actual selected labels and determine connectedness by BFS.
        rest = subset
        total = 0
        while rest:
            x = rest & -rest
            total += x.bit_length()
            rest -= x
        found = subset & -subset
        frontier = found
        while frontier:
            vbit = frontier & -frontier
            frontier -= vbit
            v = vbit.bit_length() - 1
            new = neighbor[v] & subset & ~found
            found |= new
            frontier |= new
        if found == subset:
            result |= 1 << total
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', type=int, default=8)
    parser.add_argument('--stop', type=int, default=600)
    args = parser.parse_args()
    assert 8 <= args.start < args.stop <= 600
    path = Path(__file__).resolve().with_name('chords.csv')
    with path.open(newline='', encoding='utf-8') as file:
        pairs = [(int(x['n']), int(x['b'])) for x in csv.DictReader(file)]
    assert pairs and [n for n, b in pairs] == list(range(8, 600))
    checked = 0
    for n, b in pairs:
        if not args.start <= n < args.stop:
            continue
        T = n * (n + 1) // 2
        target = (1 << (T + 1)) - 2
        assert cycle_sums(n) & target != target, ("cycle unexpectedly complete", n)
        mask = supported_sums(n, b)
        assert mask & target == target, ('missing target', n, b,
                                        (target & ~mask).bit_count())
        assert mask >> (T + 1) == 0, ('invalid sum', n)
        if n <= 14:
            # All connected subgraphs are checked independently for small n.
            assert brute_sums(n, b) == mask, ('independent check', n, b)
        checked += 1
    assert checked == args.stop - args.start
    print('VERIFY_OK', 'range', args.start, args.stop - 1,
          'instances', checked, 'exact_integer=yes')


if __name__ == '__main__':
    main()
