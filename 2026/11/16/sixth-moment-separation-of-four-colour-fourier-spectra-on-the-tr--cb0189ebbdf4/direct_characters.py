"""Exact character-sum census for four-colour triangular-prism proper colourings.
Uses no floating-point arithmetic or third-party packages.
Run with: python3 direct_characters.py
"""
from collections import Counter
from itertools import product

Q = 4
N = 6
EDGES = ((0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5))
EXPECTED = {
    'cyclic': {0:3072,8:348,24:399,40:198,56:30,72:9,88:39,264:1},
    'klein': {0:3072,8:408,24:291,40:258,56:18,72:9,88:39,264:1},
}
EXPECTED_MOMENTS = {
    'cyclic':(264,2044416,87824400384),
    'klein':(264,2044416,87789010944),
}

def valid_colours():
    return [col for col in product(range(Q), repeat=N)
            if all(col[i] != col[j] for i,j in EDGES)]


def characters(colours, group):
    # Exponents represent fourth roots of unity in cyclic case.
    # In the Klein case values are signed real characters.
    histogram = Counter()
    for freq in product(range(Q), repeat=N):
        if group == 'cyclic':
            if sum(freq) % 4:
                histogram[0] += 1
                continue
            r, im = 0, 0
            for col in colours:
                exponent = sum(u*x for u,x in zip(freq,col)) % 4
                if exponent == 0:r += 1
                elif exponent == 1:im += 1
                elif exponent == 2:r -= 1
                else:im -= 1
            assert im == 0, (freq,r,im)
            z = abs(r)
        else:
            xorsum = 0
            for u in freq:xorsum ^= u
            if xorsum:
                histogram[0] += 1
                continue
            r = 0
            for col in colours:
                parity = sum(((u & x).bit_count() & 1) for u,x in zip(freq,col)) & 1
                r += (-1)**parity
            z = abs(r)
        histogram[z] += 1
    return dict(sorted(histogram.items()))


def main():
    colours=valid_colours()
    assert len(colours)==264
    for group in ('cyclic','klein'):
        spectrum=characters(colours,group)
        assert spectrum==EXPECTED[group], (group,spectrum)
        m=tuple(sum(mult*amp**r for amp,mult in spectrum.items())//(4**N)
                for r in (2,4,6))
        assert all(sum(mult*amp**r for amp,mult in spectrum.items())%(4**N)==0
                   for r in (2,4,6))
        assert m==EXPECTED_MOMENTS[group],(group,m)
        print(group, 'spectrum',spectrum,'moments',m)
    print('PASS: independent complete character enumeration over 4096 frequencies')

if __name__=='__main__':main()
