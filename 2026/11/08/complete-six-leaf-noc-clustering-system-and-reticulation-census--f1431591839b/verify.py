#!/usr/bin/env python3
"""Independent finite census replay from the two provided C++ sources."""
import collections
import csv
import pathlib
import re
import subprocess
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
EXPECTED = {
    2: {0: 1},
    3: {0: 4, 1: 3},
    4: {0: 26, 1: 94, 2: 90},
    5: {0: 236, 1: 2630, 2: 10940, 3: 9940},
    6: {0: 2752, 1: 79076, 2: 1037235, 3: 4511390, 4: 4023915},
}

def table():
    out = collections.defaultdict(dict)
    with (HERE / 'counts.tsv').open(newline='', encoding='utf8') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            n, k, count = (int(row[x]) for x in ('n', 'k', 'count'))
            assert k not in out[n]
            out[n][k] = count
    assert dict(out) == EXPECTED, (out, EXPECTED)

def direct_python(n):
    """A small-n naive bitmask family census, without C++ candidate recursion."""
    full = (1 << n) - 1
    mids = [x for x in range(1, full) if x.bit_count() >= 2]
    freq = collections.Counter()
    for mask in range(1 << len(mids)):
        chosen = [x for i, x in enumerate(mids) if (mask >> i) & 1]
        family = chosen + [1 << i for i in range(n)] + [full]
        if any(not any((x & ~union_for(x, family)) & (1 << b)
                       for b in range(n)) for x in chosen):
            continue
        k = 0
        for x in family:
            supers = [y for y in family if x != y and (x & y) == x]
            covers = [y for y in supers if not any(
                z != x and z != y and (x & z) == x and (z & y) == z
                for z in family)]
            k += len(covers) >= 2
        freq[k] += 1
    return dict(freq)

def union_for(x, family):
    ans = 0
    for y in family:
        m = x & y
        if m and m != x and m != y:
            ans |= y
    return ans

def cpp_hist(binary, n):
    out = subprocess.check_output([str(binary), str(n)], text=True, timeout=120)
    return {int(k): int(v) for k, v in re.findall(r'^k=(\d+) count=(\d+)$', out, re.M)}

def main():
    table()
    for n in (2,3,4):
        assert direct_python(n) == EXPECTED[n]
        print('PYTHON_NAIVE_OK', n, EXPECTED[n])
    with tempfile.TemporaryDirectory() as temp:
        for src in ('noc_incremental.cpp', 'noc_direct.cpp'):
            binary = pathlib.Path(temp) / src.removesuffix('.cpp')
            subprocess.run(['g++', '-std=c++17', '-O3', '-Wall', '-Wextra',
                            str(HERE / src), '-o', str(binary)], check=True,
                           capture_output=True, text=True, timeout=60)
            for n in range(2, 7):
                result = cpp_hist(binary, n)
                assert result == EXPECTED[n], (src, n, result, EXPECTED[n])
                print('CPP_CENSUS_OK', src, n, sum(result.values()))
    print('VERIFY_OK 2 independent full six-leaf enumerators; naive small-n control')

if __name__ == '__main__':
    main()
