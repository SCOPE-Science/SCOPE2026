"""Finite independent checks for the rank-two classification of idempotent unary maps."""
from collections import defaultdict
from itertools import combinations
from math import comb, factorial
from fractions import Fraction


def compositions(parts):
    n = len(parts)
    f = []
    for size in parts:
        root = len(f)
        f.extend([root] * size)
    return tuple(f)


def partitions(n, minimum=1):
    if n == 0:
        yield ()
    for first in range(minimum, n + 1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def indicator(f):
    roots = [i for i, v in enumerate(f) if i == v]
    counts = {r: 0 for r in roots}
    for x, v in enumerate(f):
        if x != v:
            counts[v] += 1
    sizes = list(counts.values())
    return (any(s == 0 for s in sizes), any(s == 1 for s in sizes),
            any(s >= 2 for s in sizes), sum(s >= 1 for s in sizes) >= 2,
            len(f) >= 2)


def atom2(f, x, y):
    terms = (x, y, f[x], f[y])
    return tuple(terms[i] == terms[j] for i in range(4) for j in range(i+1, 4))


def rank2_signature(f):
    """Exact two-move EF signature using the language {f, =} and f^2=f."""
    return frozenset((f[x] == x, frozenset(atom2(f, x, y) for y in range(len(f))))
                     for x in range(len(f)))


def check_unlabelled(limit=30):
    seen = defaultdict(list)
    patterns = {}
    for n in range(1, limit+1):
        for p in partitions(n):
            f = compositions(p)
            I = indicator(f)
            S = rank2_signature(f)
            if I in patterns:
                assert patterns[I] == S, ('same indicator, different EF', p)
            else:
                patterns[I] = S
            seen[S].append(p)
    assert len(seen) == len(patterns) == 12
    assert len(set(patterns.values())) == 12
    min_reps = {signature: min(ps, key=lambda p:(sum(p), p)) for signature, ps in seen.items()}
    expected = [(1,), (1,1), (2,), (1,2), (3,), (1,3), (2,2),
                (1,2,2), (2,3), (1,2,3), (3,3), (1,3,3)]
    assert set(min_reps.values()) == set(expected)
    assert max(sum(p) for p in min_reps.values()) == 7
    return patterns, min_reps


def check_species(limit=12):
    """Independently evaluate the labelled-component exponential formula."""
    from collections import Counter
    for n in range(1,limit+1):
        count = 0
        for p in partitions(n):
            a = Counter(p)
            numerator = factorial(n)
            denominator = 1
            for m, c in a.items():
                numerator *= m ** c
                denominator *= (factorial(m) ** c) * factorial(c)
            assert numerator % denominator == 0
            count += numerator // denominator
        assert count == sum(comb(n,k)*k**(n-k) for k in range(1,n+1))
    return limit




def check_class_egfs(limit=12):
    """Verify every classwise EGF coefficient against rooted-star partition counts."""
    def add(a,b):return [a[i]+b[i] for i in range(limit+1)]
    def sub(a,b):return [a[i]-b[i] for i in range(limit+1)]
    def mul(a,b):return [sum(a[k]*b[i-k] for k in range(i+1)) for i in range(limit+1)]
    def expseries(a):
        z=[Fraction(0) for _ in range(limit+1)];z[0]=1
        for n in range(1,limit+1):
            z[n]=sum(k*a[k]*z[n-k] for k in range(1,n+1))/Fraction(n)
        return z
    zero=[Fraction(0) for _ in range(limit+1)]
    one=zero.copy();one[0]=1
    A=zero.copy();A[1]=1
    B=zero.copy();B[2]=1
    C=zero.copy()
    for j in range(3,limit+1):C[j]=Fraction(1,factorial(j-1))
    ea,eb,ec=expseries(A),expseries(B),expseries(C)
    nonzeroS=sub(ea,one)
    classes={
        ('only-singletons',False):A,
        ('only-singletons',True):sub(nonzeroS,A),
    }
    base={
        'one-double':B,'one-large':C,
        'many-double':sub(sub(eb,one),B),
        'many-large':sub(sub(ec,one),C),
        'mixed':mul(sub(eb,one),sub(ec,one))
    }
    for typ,arr in base.items():
        classes[(typ,False)]=arr
        classes[(typ,True)]=mul(arr,nonzeroS)
    assert len(classes)==12
    for n in range(1,limit+1):
        observed=defaultdict(int)
        for p in partitions(n):
            c=__import__('collections').Counter(p)
            numerator=factorial(n)
            denominator=1
            for m,k in c.items():
                numerator *= m**k
                denominator *= factorial(m)**k*factorial(k)
            assert numerator%denominator==0
            ss,dd,ll=c[1],c[2],sum(k for m,k in c.items() if m>=3)
            if dd+ll==0: key=('only-singletons',ss>=2)
            else:
                typ=('one-double' if dd==1 else 'one-large') if dd+ll==1 else ('mixed' if dd and ll else 'many-double' if dd else 'many-large')
                key=(typ,ss>=1)
            observed[key]+=numerator//denominator
        for key,series in classes.items():
            assert observed[key]==factorial(n)*series[n],(n,key,observed[key],factorial(n)*series[n])
    return len(classes)

def check_labelled(limit=8):
    total = 0
    for n in range(1, limit+1):
        count = 0
        seen = {}
        for fixed_mask in range(1,1<<n):
            roots = [x for x in range(n) if fixed_mask & (1<<x)]
            rest = [x for x in range(n) if not (fixed_mask & (1<<x))]
            k = len(roots)
            for code in range(k**len(rest)):
                f = list(range(n))
                q = code
                for x in rest:
                    f[x] = roots[q%k]
                    q //= k
                assert all(f[f[x]] == f[x] for x in range(n))
                I = indicator(f)
                S = rank2_signature(f)
                if I in seen:
                    assert seen[I] == S
                else:
                    seen[I] = S
                count += 1
        assert count == sum(comb(n,k)*k**(n-k) for k in range(1,n+1))
        total += count
    return total


if __name__ == '__main__':
    patterns, rep = check_unlabelled()
    labelled = check_labelled()
    species_n = check_species()
    egf_classes = check_class_egfs()
    print('RANK_TWO_IDEMPOTENT_CLASSIFICATION_OK',
          'distinct_theories=', len(patterns),
          'sharp_representative_bound=', max(sum(p) for p in rep.values()),
          'labelled_maps_checked=',labelled, 'species_identity_n_through=', species_n, 'class_egfs_verified=', egf_classes)
