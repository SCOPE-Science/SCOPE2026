"""Independent small-degree verification of square-root fibers over idempotent maps.

Standard-library only. All composition is evaluated from explicit finite maps.
"""
from itertools import product
from collections import defaultdict
from functools import lru_cache
from math import comb, factorial
from fractions import Fraction

def fixed_block(a):
    assert a >= 1
    return sum(comb(a - 1, u) * u ** (a - 1 - u)
               for u in range(a))

def paired_block(a, b):
    assert a >= 1 and b >= 1
    return sum(comb(a - 1, u) * comb(b - 1, v)
               * v ** (a - 1 - u) * u ** (b - 1 - v)
               for u in range(a) for v in range(b))

def root_count(sizes):
    sizes = tuple(sorted(sizes))
    @lru_cache(None)
    def matching(rest):
        if not rest:
            return 1
        i, *tail = rest
        total = fixed_block(sizes[i]) * matching(tuple(tail))
        for j in tail:
            total += paired_block(sizes[i], sizes[j]) * matching(
                tuple(x for x in tail if x != j))
        return total
    return matching(tuple(range(len(sizes))))

def check_exhaustive(n):
    counts = defaultdict(int)
    for g in product(range(n), repeat=n):
        f = tuple(g[g[x]] for x in range(n))
        if all(f[f[x]] == f[x] for x in range(n)):
            counts[f] += 1
    expected_idempotents = sum(comb(n, k) * k ** (n-k) for k in range(1,n+1))
    assert len(counts) == expected_idempotents
    rank_counts = defaultdict(int)
    for f, actual in counts.items():
        roots = set(f)
        sizes = tuple(sum(f[x] == r for x in range(n)) for r in roots)
        rank_counts[len(roots)] += actual
        predicted = root_count(sizes)
        assert actual == predicted, (n, f, sizes, actual, predicted)
    return len(counts), sum(counts.values()), max(counts.values()), dict(rank_counts)

def egf_numbers(max_n, weight=1):
    # Exact formal power-series arithmetic, independent from sympy.
    N=max_n
    def mul(a,b):
        return [sum(a[i]*b[j-i] for i in range(j+1)) for j in range(N+1)]
    def expser(a):
        out=[Fraction(0)]*(N+1);out[0]=1
        for k in range(1,N+1):
            out[k]=sum(Fraction(j)*a[j]*out[k-j] for j in range(1,k+1))/k
        return out
    z=[Fraction(0)]*(N+1);z[1]=1
    ez=expser(z)
    zez=[Fraction(0)]+ez[:-1]
    ezez=expser(zez)
    R=[Fraction(0)]+ezez[:-1]
    R2=mul(R,R)
    total=expser([weight*R[j]+weight*weight*R2[j]/2 for j in range(N+1)])
    return [int(c*factorial(j)) for j,c in enumerate(total)]

def main():
    egf=egf_numbers(9)
    assert egf[:9]==[1,1,4,25,194,1791,19312,237637,3280524],egf
    print('EGF coefficients n=0..8:',egf[:9])
    for n in range(1,8):
        idems,total,maxroot,ranks=check_exhaustive(n)
        assert total==egf[n]
        for weight in (2,3):
            assert sum(count*weight**rank for rank,count in ranks.items())==egf_numbers(9,weight)[n]
        print('n=%d idempotents=%d square-roots-over-idempotents=%d largest-fiber=%d rank_counts=%s' %
              (n,idems,total,maxroot, sorted(ranks.items())))
    for prof, val in [((3,),3),((2,1),2),((2,2),4),((3,2),9),((1,1,1,1),10)]:
        assert root_count(prof)==val,(prof,root_count(prof))
    print('FIXED_IDEMPOTENT_SQUARE_ROOT_PROFILE_VERIFIED')

if __name__=='__main__':main()
