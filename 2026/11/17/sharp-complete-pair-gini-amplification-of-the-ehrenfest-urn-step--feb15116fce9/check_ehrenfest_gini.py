"""Exact arithmetic checks of the Ehrenfest Gini seminorm formula.

The unrestricted theorem is proved algebraically in RESULT.md. This checker
exhausts only the explicitly reported finite state sizes.
"""
from fractions import Fraction
from random import Random


def binary_output_numerators(n, mask):
    return [
        (n-i) * (bool(mask & (1 << (i+1))) if i < n else False)
        + i * (bool(mask & (1 << (i-1))) if i > 0 else False)
        for i in range(n+1)
    ]


def pair_differences(z):
    return sum(abs(v-w) for i,v in enumerate(z) for w in z[i+1:])


def exhaustive_cuts():
    total = 0
    for n in range(1, 15):
        N = n+1
        best_num, best_den, best_mask = 0, 1, None
        for mask in range(1, 1 << (N-1)):
            s = mask.bit_count()
            if s == 0 or s == N:
                continue
            d = pair_differences(binary_output_numerators(n,mask))
            num,den = d,n*s*(N-s)
            if num * best_den > best_num * den:
                best_num,best_den,best_mask = num,den,mask
            total += 1
        expected = Fraction(1 if n <=2 else n*n+2*n-4,1 if n <=2 else n*n)
        found = Fraction(best_num,best_den)
        assert found == expected, (n,found,expected,best_mask)
        if n>=3:
            assert best_mask == 2 or found == expected
    print('EXHAUSTIVE_BINARY_CUTS_N1_TO_N14_PASSED',total)


def algebraic_envelope():
    for n in range(3,101):
        N=n+1
        rate=Fraction(n*n+2*n-4,n*n)
        for s in range(2,N//2+1):
            for b in range(3):
                if b>s or s-b>n-1:
                    continue
                mass=Fraction((n+2)*(s-b)+b,n)
                assert mass*(N-mass)<=rate*s*(N-s), (n,s,b)
    print('JENSEN_MASS_ENVELOPE_INTEGER_SIZES_N3_TO_N100_PASSED')


def impulse_checks():
    for n in range(1,101):
        N=n+1
        m=1 if n<=2 else n*n+2*n-4
        d=1 if n<=2 else n*n
        for j in range(N):
            vals=binary_output_numerators(n,1<<j)
            ratio=Fraction(pair_differences(vals),n*n)
            if n >=2 and j in (0,n):
                assert ratio==Fraction(1,n)
            if n>=2 and 1<=j<=n-1:
                assert ratio==Fraction((n-1)*(n+2)+abs(n-2*j),n*n)
            assert ratio<=Fraction(m,d)
        if n>=3:
            assert Fraction(pair_differences(binary_output_numerators(n,2)),n*n)==Fraction(m,d)
    print('EXACT_COLUMN_AND_SHARPNESS_IDENTITIES_N1_TO_N100_PASSED')


def random_real_tests():
    rng=Random(492381)
    total=0
    for n in range(1,31):
        for _ in range(10):
            nums=[rng.randint(-30,30) for i in range(n+1)]
            if len(set(nums))==1:
                continue
            v=[Fraction(nums[i-1]*i+(n-i)*nums[i+1],n) if 0<i<n else Fraction(nums[1] if i==0 else nums[n-1]) for i in range(n+1)]
            ratio=Fraction(pair_differences(v),pair_differences(nums))
            expected=Fraction(1 if n<=2 else n*n+2*n-4,1 if n<=2 else n*n)
            assert ratio<=expected,(n,ratio,expected)
            total+=1
    print('EXACT_RATIONAL_NONBINARY_SIGNALS_PASSED',total)


def weighted_jensen_stationary():
    from math import comb
    for n in range(1,20):
        pi=[Fraction(comb(n,i),2**n) for i in range(n+1)]
        P=[[Fraction((n-i),n) if j==i+1 else Fraction(i,n) if j==i-1 else Fraction(0) for j in range(n+1)] for i in range(n+1)]
        for j in range(n+1):
            assert sum(pi[i]*P[i][j] for i in range(n+1))==pi[j]
    print('EXACT_BINOMIAL_STATIONARY_MEASURE_N1_TO_N19_PASSED')


if __name__=='__main__':
    exhaustive_cuts()
    algebraic_envelope()
    impulse_checks()
    random_real_tests()
    weighted_jensen_stationary()
    print('ALL_EHRENFEST_GINI_CHECKS_PASSED')
