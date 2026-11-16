"""Exact finite classification of cubic-phase periodic Fourier magnitudes.

Only Python integer arithmetic is used; no external dependencies.
Run: python check.py
"""
from itertools import product
from collections import defaultdict


def autocorrelation_key(word):
    """Coefficients in the basis (1,omega), omega**2=-1-omega."""
    n = len(word)
    key = []
    for lag in range(n):
        count = [0, 0, 0]
        for j in range(n):
            count[(word[j]-word[(j+lag)%n]) % 3] += 1
        key.append((count[0]-count[2], count[1]-count[2]))
    return tuple(key)


def trivial_orbit_key(word):
    n = len(word)
    representatives = []
    for shift in range(n):
        forward = tuple(word[(shift+j) % n] for j in range(n))
        reverse_conj = tuple((-word[(shift-j) % n]) % 3 for j in range(n))
        for transformed in (forward, reverse_conj):
            representatives.append(tuple((v-transformed[0]) % 3 for v in transformed))
    return min(representatives)


def classify(n):
    spectral = defaultdict(lambda: defaultdict(list))
    for tail in product(range(3), repeat=n-1):
        word = (0,) + tail  # unique global-phase-normalized representative
        spectral[autocorrelation_key(word)][trivial_orbit_key(word)].append(word)
    return spectral


def main():
    expected = [
        (1,1,1,1,0),
        (2,3,2,2,0),
        (3,9,4,4,0),
        (4,27,7,7,0),
        (5,81,13,13,0),
        (6,243,30,32,1),
    ]
    print('n normalized_words intensity_spectra trivial_orbits ambiguous_spectra')
    for target in expected:
        n = target[0]
        spectral = classify(n)
        result = (n, sum(len(v) for classes in spectral.values() for v in classes.values()),
                  len(spectral), sum(len(classes) for classes in spectral.values()),
                  sum(len(classes)>1 for classes in spectral.values()))
        print(*result)
        assert result == target, (result, target)
        if n == 6:
            exceptions = [(s, cs) for s,cs in spectral.items() if len(cs)>1]
            assert len(exceptions) == 1
            s, cs = exceptions[0]
            assert s == ((6,0),(0,0),(0,0),(3,0),(0,0),(0,0))
            assert len(cs) == 3
            assert sorted(len(v) for v in cs.values()) == [6,6,6]
            reps = sorted(cs)
            assert reps == [(0,0,1,0,0,2),(0,0,1,0,1,1),(0,0,1,1,0,1)]
            assert sorted([tuple(sorted([rep.count(j) for j in range(3)])) for rep in reps]) == [(0,3,3),(0,3,3),(1,1,4)]
            assert sum(len(v) for v in cs.values()) == 18
            print('exceptional_representatives', reps)
            print('exceptional_normalized_words', sum(map(len,cs.values())))
            print('exceptional_Fourier_intensities', [9 if k % 2 == 0 else 3 for k in range(6)])
    print('PASS')

if __name__ == '__main__':
    main()
