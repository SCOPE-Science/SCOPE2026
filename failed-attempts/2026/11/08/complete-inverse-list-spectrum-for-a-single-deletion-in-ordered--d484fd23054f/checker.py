"""Exact finite cross-checks for one-deletion overlapping-ell-mer read lists.
Run: python3 checker.py
No external dependencies; all arithmetic is over integers.
"""
from collections import Counter, defaultdict
from itertools import product


def read_vector(x, ell):
    return tuple(x[i:i+ell] for i in range(len(x)-ell+1))


def run_lengths(z):
    lengths = []
    for a in z:
        if not lengths or a != previous:
            lengths.append(1)
        else:
            lengths[-1] += 1
        previous = a
    return lengths


def predicted_degree(y, q, ell):
    defects = [i for i in range(len(y)-1)
               if y[i][1:] != y[i+1][:-1]]
    if len(defects) >= 2:
        return 0
    if len(defects) == 1:
        i = defects[0]
        return int(y[i][2:] == y[i+1][:-2])
    z = y[0] + tuple(w[-1] for w in y[1:])
    runs = run_lengths(z)
    if len(runs) == 1:
        return 2*q-1
    return 2*q + sum(length >= ell-1 for length in runs[1:-1])


def composition_count_distribution(q, n, ell):
    """Independent run-composition expansion of the coefficient formula."""
    m = n-1
    result = Counter()
    for cuts in product((False, True), repeat=m-1):
        lengths = []
        current = 1
        for cut in cuts:
            if cut:
                lengths.append(current)
                current = 1
            else:
                current += 1
        lengths.append(current)
        r = len(lengths)
        word_count = q*(q-1)**(r-1)
        degree = 2*q-1 if r == 1 else 2*q+sum(
            u >= ell-1 for u in lengths[1:-1])
        result[degree] += word_count
    defects = n-ell-1
    result[1] += defects*(q**n-q**(n-ell+1))
    if result[1] == 0:
        del result[1]
    return result


def exhaustive_check(q, n, ell):
    inverse = defaultdict(set)
    for x in product(range(q), repeat=n):
        reads = read_vector(x, ell)
        for i in range(len(reads)):
            inverse[reads[:i] + reads[i+1:]].add(x)
    actual = Counter(map(len, inverse.values()))
    expected = composition_count_distribution(q, n, ell)
    assert actual == expected, (q, n, ell, actual, expected)
    assert len(inverse) == q**(n-1) + (n-ell-1)*(
        q**n-q**(n-ell+1))
    assert max(actual) == 2*q + (n-3)//(ell-1)
    for y, parents in inverse.items():
        assert len(parents) == predicted_degree(y, q, ell), (
            q,n,ell,y,len(parents),predicted_degree(y,q,ell))
    return len(inverse), sum(d*c for d,c in actual.items())


def run_checks():
    cases = 0
    observations = 0
    incidences = 0
    for q in (2,3,4,5):
        for ell in range(2,5):
            for n in range(ell+1, min(9,ell+6)):
                if q**n > 22000:
                    continue
                o, v = exhaustive_check(q,n,ell)
                cases += 1
                observations += o
                incidences += v
    assert cases >= 40
    print(f"PASS: {cases} (alphabet, length, read-width) cases; "
          f"{observations} feasible outputs; {incidences} source/output pairs")

if __name__ == '__main__':
    run_checks()
