"""Check the complete minimizing-orbit classification using output from verify.cpp.
Run after compiling verify.cpp: python3 orbit_check.py
"""
import itertools
import subprocess

SUPPORT = [(i, j) for i in range(4) for j in range(4 - i)]
INDEX = {s: i for i, s in enumerate(SUPPORT)}
FREE = [i for i, s in enumerate(SUPPORT) if s not in {(0, 0), (1, 0), (0, 1)}]
EXPECTED_ORBIT_SIZES = {1: [1], 2: [3], 3: [2, 6], 4: [3, 6, 6, 6, 6, 6, 12], 6: [6]}


def unpack(code, q):
    a = [0] * 10
    for i in FREE:
        a[i] = code % q
        code //= q
    assert code == 0
    return tuple(a)


def pack(a, q):
    code = 0
    for i in reversed(FREE):
        code = code * q + a[i]
    return code


def normalize(a, q):
    c = a[INDEX[(0, 0)]]
    dx = a[INDEX[(1, 0)]] - c
    dy = a[INDEX[(0, 1)]] - c
    return tuple((a[k] - c - i * dx - j * dy) % q
                 for k, (i, j) in enumerate(SUPPORT))


def orbit(a, q):
    out = set()
    for p in itertools.permutations(range(3)):
        new = []
        for i, j in SUPPORT:
            bary = (i, j, 3 - i - j)
            x, y, _ = (bary[p[0]], bary[p[1]], bary[p[2]])
            new.append(a[INDEX[(x, y)]])
        b = normalize(new, q)
        out.add(pack(b, q))
        out.add(pack(tuple((-v) % q for v in b), q))
    return out


def main():
    output = subprocess.check_output(['./verify'], text=True)
    lines = output.splitlines()
    results = {}
    for i, line in enumerate(lines):
        if not line.startswith('q='):
            continue
        q = int(line.split()[0][2:])
        assert lines[i+1].startswith('min_codes=')
        ids = {int(s) for s in lines[i+1].split('=', 1)[1].strip(',').split(',')}
        all_ids = set(ids)
        orbits = []
        while ids:
            representative = min(ids)
            o = orbit(unpack(representative, q), q)
            assert o <= all_ids, (q, representative, o - all_ids)
            assert o <= ids, (q, representative, 'overlap')
            orbits.append((representative, len(o)))
            ids -= o
        sizes = sorted(x[1] for x in orbits)
        assert sizes == EXPECTED_ORBIT_SIZES[q], (q, sizes)
        results[q] = orbits
        print(f'q={q}: {len(all_ids)} normalized minimizers, '
              f'{len(orbits)} complete orbits, sizes={sizes}, '
              f'representatives={orbits} PASS')
    assert set(results) == set(EXPECTED_ORBIT_SIZES)
    print('All symmetry orbits verified PASS.')


if __name__ == '__main__':
    main()
