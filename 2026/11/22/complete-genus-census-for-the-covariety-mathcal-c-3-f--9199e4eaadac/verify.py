"""Independent exact checks for the fixed-pseudo-Frobenius-3 census.

Python 3 standard library only. Exhaustive for every semigroup with F <=18;
then checks symbolic coefficient and total-count identities at larger parameters.
"""
from collections import Counter


def parameter_triples(F):
    """Explicit residue-tail models with their verified semigroup inequalities."""
    assert F >= 4
    k, r = divmod(F,3)
    if r == 0:
        for a in range(1,k+1):
            for b in range(1,k+1):
                if b <= 2*a and a <= 2*b+1 and a+b >= k:
                    yield a,b,k+1
    elif r == 1:
        for b in range((k+1)//2,k+1):
            for c in range(2,k+2):
                yield k+1,b,c
    else:
        for a in range((k+2)//2,k+2):
            for c in range(2,k+2):
                yield a,k+1,c


def formula_count(F):
    k, r = divmod(F, 3)
    if r == 0:
        return ((k+1)*(k+2)+2)//3
    if r == 1:
        return k*(k//2+1)
    return k*((k+1)//2+1)


def genus_coefficient(F, g):
    k, r = divmod(F, 3)
    if r == 0:
        t = g-k
        if not k <= t <= 2*k:
            return 0
        return min(k,(2*t+1)//3) - max(t-k,(t+2)//3)+1
    if r == 1:
        lo = (k+1)//2
        return max(0, min(k,g-k-2) - max(lo,g-2*k-1) + 1)
    lo = (k+2)//2
    return max(0, min(k+1,g-k-2) - max(lo,g-2*k-1) + 1)


def brute_semigroup_genera(F):
    """Independently enumerate ALL subsets below F; test closure & 3 in PF."""
    hist = Counter()
    for mask in range(1 << (F-1)):
        positive = [i for i in range(1,F) if mask & (1 << (i-1))]
        # Numeric 3 must be a gap. No use of the normal-form classification.
        if 3 in positive:
            continue
        members = set(positive)
        if any(x+y <= F and x+y not in members
               for x in positive for y in positive):
            continue
        if any(x+3 <= F and x+3 not in members for x in positive):
            continue
        hist[F-len(positive)] += 1
    return hist


def check():
    checks = 0
    for F in range(4,19):
        triples = list(parameter_triples(F))
        pred = Counter(a+b+c-1 for a,b,c in triples)
        real = brute_semigroup_genera(F)
        assert pred == real, (F, pred, real)
        assert sum(pred.values()) == formula_count(F), F
        checks += 1
    for F in range(19,751):
        triples = list(parameter_triples(F))
        count = len(triples)
        assert count == formula_count(F), (F,count,formula_count(F))
        actual_genus = Counter(a+b+c-1 for a,b,c in triples)
        assert all(genus_coefficient(F,g)==v for g,v in actual_genus.items()), F
        assert sum(genus_coefficient(F,g) for g in range(F+1)) == count, F
        checks += 1
    print('VERIFY_OK',checks,'parameter values; exhaustive F=4..18; formulas F=4..750')


if __name__ == '__main__':
    check()
