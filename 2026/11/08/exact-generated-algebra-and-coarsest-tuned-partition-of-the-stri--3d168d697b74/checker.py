"""Independent finite-quotient checks of strict-future modal algebra atom counts.

For a finite prefix and a cofinal set of recurrent colors, the quotient has
one state for each displayed prefix point and one tail state per color.
Tail states access every tail state, including themselves: the infinite
underlying strict chain has future occurrences of every recurrent color.
"""
from itertools import product


def diamond(mask, successor_masks):
    return sum(1 << i for i, row in enumerate(successor_masks) if row & mask)


def closure(color, palette, k):
    n = len(color)
    s = len(palette)
    colors = color + tuple(palette)
    N = len(colors)
    successors = []
    tail = ((1 << s) - 1) << n
    for i in range(n):
        successors.append(sum(1 << j for j in range(i + 1, n)) | tail)
    for i in range(s):
        successors.append(tail)
    full = (1 << N) - 1
    atoms = [(sum((1 << j) for j, c in enumerate(colors) if (c >> i) & 1)) for i in range(k)]
    algebra = {0, full}
    for a in atoms:
        algebra |= {a, full ^ a}
    for _ in range(100):
        old = len(algebra)
        newly = set(algebra)
        for x in tuple(algebra):
            newly |= {full ^ x, diamond(x, successors)}
        if len(newly) > 1 << 15:
            raise AssertionError('test quotient unexpectedly large')
        algebra = newly
        for x in tuple(algebra):
            algebra |= {x & y for y in tuple(algebra)}
        if len(algebra) == old:
            break
    else:
        raise AssertionError('closure did not stabilize')
    return algebra


def expected_partition(prefix, palette):
    n = len(prefix)
    N0 = 1 + max((i for i, a in enumerate(prefix) if a not in palette), default=-1)
    s = len(palette)
    cells = [(1 << i) for i in range(N0)]
    for j, a in enumerate(palette):
        cells.append(sum(1 << i for i in range(N0,n) if prefix[i] == a) | (1 << (n+j)))
    return cells,N0+s


def test():
    tests = 0
    for k in (0, 1, 2):
        alphabet = tuple(range(1 << k))
        for palette_mask in range(1,1 << len(alphabet)):
            palette = tuple(a for a in alphabet if (palette_mask >> a) & 1)
            for n in range(0, 5 if k == 2 else 7):
                for prefix in product(alphabet,repeat=n):
                    cells, count = expected_partition(prefix,palette)
                    universe = (1 << (n+len(palette))) - 1
                    # all predicted atoms partition the quotient states
                    assert sum(cells) == universe, (prefix,palette,cells)
                    assert not any(cells[i]&cells[j] for i in range(len(cells)) for j in range(i+1,len(cells)))
                    algebra = closure(prefix,palette,k)
                    assert len(algebra) == 2 ** count,(prefix,palette,count,len(algebra))
                    assert all(cell in algebra for cell in cells),(prefix,palette,'missing cell')
                    tests += 1
    print('STRICT_OMEGA_GENERATED_ALGEBRA_OK', tests, 'complete finite quotient tests')


if __name__ == '__main__':
    test()
