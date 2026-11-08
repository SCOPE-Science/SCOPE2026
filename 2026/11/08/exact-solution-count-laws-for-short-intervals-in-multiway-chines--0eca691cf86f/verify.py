"""Exact finite checks for the interval CRT compatibility spectrum and moments."""
from itertools import product
from fractions import Fraction
from math import gcd, lcm, prod, comb
from functools import lru_cache


def arc(g, a, t):
    return frozenset((t+j) % g for j in range(a))


def predicted(g, lengths):
    return max(0, sum(lengths) - (len(lengths)-1)*g), min(lengths)


def moments(g, lengths):
    k = len(lengths)
    mean = Fraction(prod(lengths), g**(k-1))
    def c(a, d):
        return max(0,a-d)+max(0,a-(g-d))
    second = Fraction(sum(prod(c(a,d) for a in lengths) for d in range(g)),g**(k-1))
    return mean, second


@lru_cache(None)
def compositions(n, r):
    if r == 1:
        return ((n,),) if n >= 1 else ()
    return tuple((j,) + rest for j in range(1, n-r+2)
                 for rest in compositions(n-j, r-1))


def distribution(g, lengths):
    """Count starts on Z/gZ via cyclic gap compositions, not by enumerating starts."""
    b = [g**len(lengths)]
    for r in range(1,g+1):
        val = sum(prod(sum(max(0, d+a-g) for d in gaps) for a in lengths)
                  for gaps in compositions(g,r))
        assert (g*val) % r == 0
        b.append(g*val//r)
    return [sum((-1)**(r-h)*comb(r,h)*b[r] for r in range(h,g+1))
            for h in range(g+1)]


def all_spectra():
    cases = 0
    arrangements = 0
    for k, gs in ((3,range(2,9)),(4,range(2,6))):
        for g in gs:
            for a in product(range(g+1),repeat=k):
                low, high = predicted(g,a)
                actual = set()
                counts = [0]*(g+1)
                s = 0
                s2 = 0
                # first start fixed at zero by global translation
                for rest in product(range(g),repeat=k-1):
                    starts = (0,)+rest
                    h = len(set.intersection(*(set(arc(g,aa,t)) for aa,t in zip(a,starts))))
                    assert low<=h<=high
                    actual.add(h)
                    counts[h] += 1
                    s += h
                    s2 += h*h
                    arrangements += 1
                assert actual == set(range(low,high+1)), (g,k,a,actual,(low,high))
                assert [g*n for n in counts]==distribution(g,a), (g,k,a,"distribution",counts)
                m1,m2 = moments(g,a)
                assert Fraction(s,g**(k-1))==m1,(g,k,a,'mean',m1,s)
                assert Fraction(s2,g**(k-1))==m2,(g,k,a,'second',m2,s2)
                cases += 1
    return cases,arrangements


def crt_check():
    cases = 0
    for g in range(2,9):
        ms=[g,2*g,3*g] # quotient factors 1,2,3 are pairwise coprime
        assert all(gcd(ms[i],ms[j])==g for i in range(3) for j in range(i))
        L=lcm(*ms)
        for a in product(range(g+1),repeat=3):
            for t in product(range(g),repeat=2):
                ts=(0,)+t
                sets=[arc(m,aa,off) for m,aa,off in zip(ms,a,ts)]
                brute=sum(all(x%m in sets[i] for i,m in enumerate(ms)) for x in range(L))
                projection=len(set.intersection(*(set(arc(g,aa,off)) for aa,off in zip(a,ts))))
                assert brute==projection,(g,a,ts,brute,projection)
                cases += 1
    return cases

if __name__ == '__main__':
    sc, ar = all_spectra()
    direct = crt_check()
    print('VERIFY_OK spectra_parameter_cases=%d interval_start_configs=%d CRT_direct_cases=%d exact_first_second_moments=PASS full_probability_distribution=PASS complete_integer_spectra=PASS' % (sc,ar,direct))
