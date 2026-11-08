"""Standard-library reproducibility checks for the balanced max-plus recurrence.

The finite tests corroborate the analytic universal proof in RESULT.md;
they are not a substitute for proof over all integer initial states.
"""
from pathlib import Path
import json


def F(xy, c):
    x, y = xy
    return (1 + x - max(0, x, y), y + max(0, c + x) - c)


def load_cert():
    return json.loads(Path(__file__).with_name('cycle_certificate.json').read_text(encoding='utf-8'))


def sequence(cert, key):
    prefix = [tuple(z) for z in cert['prefixes'][key]]
    bottom = prefix[-1][1]
    assert prefix[-1] == (0, bottom)
    return prefix + [(1, j) for j in range(bottom, 2)]


def first_hit(initial, c, target=(1, 2), bound=100000):
    xy = initial
    for t in range(bound + 1):
        if xy == target:
            return t
        if xy == (0, 1):
            return None
        xy = F(xy, c)
    raise RuntimeError('unresolved finite check')


def main():
    cert = load_cert()
    checks = 0
    for c in list(range(1, 13)) + [20, 50, 1000]:
        key = str(c) if c <= 3 else '4+'
        seq = sequence(cert, key)
        assert len(seq) == cert['periods'][key] and len(set(seq)) == len(seq)
        for i, xy in enumerate(seq):
            assert F(xy, c) == seq[(i + 1) % len(seq)]
            checks += 1
        assert seq[0] == (1, 2)
        # This integer rectangle deliberately includes points outside the cycles.
        for x in (range(-25, 26) if c <= 50 else range(-5, 6)):
            for y in (range(-25, 26) if c <= 50 else range(-5, 6)):
                got = first_hit((x, y), c, bound=1000000)
                if (x, y) == (0, 1):
                    assert got is None
                else:
                    assert got is not None
                checks += 1
    for n in range(2, 81):
        assert first_hit((0, n), 1, bound=100000) == n * n + 2 * n + 2
        checks += 1
    for c in range(1, 18):
        for x in range(-50, 51):
            for y in range(-50, 51):
                if F((x, y), c) == (0, 1):
                    assert (x, y) == (0, 1)
                checks += 1
    print('VERIFY_OK checks=' + str(checks))


if __name__ == '__main__':
    main()
