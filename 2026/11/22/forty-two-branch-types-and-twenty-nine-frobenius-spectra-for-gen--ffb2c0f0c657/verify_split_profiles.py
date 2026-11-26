"""Check the ordered component counts and the realizable aggregate collision."""
import csv
import sys
from collections import Counter
from itertools import product
from math import factorial, gcd, lcm, prod
from pathlib import Path


def fixed_matchings(partition, h):
    sizes = Counter()
    for d in partition:
        j = gcd(d, h)
        sizes[d//j] += j
    return prod(sum(factorial(m)//(factorial(m-2*k)*2**k*factorial(k))*d**k
                    for k in range(m//2+1) if d%2 == 0 or m == 2*k)
                for d, m in sizes.items())


def parse(text):
    return dict(tuple(map(int, entry.split(':'))) for entry in text.split())


def main(path):
    with path.open(newline='') as data:
        rows = {tuple(map(int, row['branch_partition'].split())): row for row in csv.DictReader(data)}
    assert len(rows) == 42
    totals, ordered = set(), set()
    for partition, row in rows.items():
        assert sum(partition) == 10
        order = lcm(*partition)
        a, b, total = (parse(row[k]) for k in ('orbit_945', 'orbit_1350', 'all_kernels'))
        assert Counter(a) + Counter(b) == total
        assert sum(d*m for d,m in a.items()) == 945
        assert sum(d*m for d,m in b.items()) == 1350
        assert all(order%d == 0 for d in total)
        for h in range(1, order+1):
            if order%h == 0:
                assert sum(d*m for d,m in a.items() if h%d == 0) == fixed_matchings(partition,h)
        totals.add(tuple(sorted(total.items())))
        ordered.add((tuple(sorted(a.items())), tuple(sorted(b.items()))))
    assert (len(totals),len(ordered)) == (29,38)
    r, s = rows[(4,2,2,2)], rows[(4,2,2,1,1)]
    assert r['rational_J2_points'] == s['rational_J2_points'] == '8'
    assert r['all_kernels'] == s['all_kernels'] == '1:7 2:64 4:540'
    assert (r['orbit_945'],r['orbit_1350']) == ('1:7 2:19 4:225','2:45 4:315')
    assert (s['orbit_945'],s['orbit_1350']) == ('1:3 2:21 4:225','1:4 2:43 4:315')
    assert all((x*x+a*x+b)%5 for (a,b),x in product([(0,2),(0,3),(1,1)],range(5)))
    assert all((x**4+2)%5 for x in range(5))
    assert not any((b*c)%5 == 2 and (b+c-a*a)%5 == 0 and a*(c-b)%5 == 0
                   for a,b,c in product(range(5),repeat=3))
    print('42 branch types; 29 aggregate and 38 ordered component profiles; collision checked')


if __name__ == '__main__':
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name('kernel_spectra.csv'))
