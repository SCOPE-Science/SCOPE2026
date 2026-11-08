"""Exact finite sanity checks for the local prime-plus-Zumkeller sieve.

The uniform analytic estimate is proved separately, not by this enumeration.
"""
from math import gcd, isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def partition(q, a):
    assert q > 2 and q % 2 == 1 and prime(q)
    assert a >= 1 and q <= (1 << (a+1)) - 1
    M = (1 << (a+1)) - 1
    H = (q+1) * M // 2
    v, u = divmod(H, q)
    assert 0 <= u < q <= M and 0 <= v <= M
    left = {(1 << i) for i in range(a+1) if (u >> i) & 1}
    left.update({q << i for i in range(a+1) if (v >> i) & 1})
    full = {1 << i for i in range(a+1)} | {q << i for i in range(a+1)}
    assert sum(left) == sum(full - left) == H
    return left, full-left


def divisors(n):
    small = [d for d in range(1, isqrt(n)+1) if n % d == 0]
    return set(small) | {n//d for d in small}


def check():
    prime_cases = product_cases = 0
    for q in range(3, 200, 2):
        if not prime(q):
            continue
        a = 1
        while q > (1 << (a+1))-1:
            a += 1
        prime_cases += 1
        for b in range(a, a+3):
            left, right = partition(q,b)
            base = (1 << b)*q
            for cofactor in (1,3,5,7,9,11):
                if gcd(base,cofactor) != 1:
                    continue
                ds = divisors(cofactor)
                L = {x*d for x in left for d in ds}
                R = {x*d for x in right for d in ds}
                assert L.isdisjoint(R)
                assert L | R == divisors(base*cofactor)
                assert sum(L) == sum(R)
                product_cases += 1

    targets = [100001,123457,150001,200003,300001,500001,750001,1000001]
    congruence_checks = represented_checks = selected_primes = 0
    for N in targets:
        if N % 2 == 0:
            continue
        q=3
        while not prime(q) or N%q == 0:
            q+=2
        a=1
        while q>(1 << (a+1))-1:
            a+=1
        B=(1<<a)*q
        assert gcd(B*q,N) == 1
        count_first = sum(prime(p) for p in range(N % B, N//2+1, B) if p >= 2)
        count_second = sum(prime(p) for p in range(N % (B*q), N//2+1, B*q) if p>=2)
        count_direct = 0
        for p in range(N % B, N//2+1,B):
            if p < 2 or not prime(p) or (N-p)%(B*q)==0:
                continue
            count_direct += 1
            C=N-p
            assert C % B == 0 and C % (B*q) != 0
            m=C//B
            assert m%q != 0
            t=0
            while m%2==0:
                m//=2; t+=1
            b=a+t
            L,R=partition(q,b)
            assert gcd((1<<b)*q,m)==1
            if represented_checks < 150:
                ds=divisors(m)
                assert sum(x*d for x in L for d in ds)==sum(x*d for x in R for d in ds)
                represented_checks+=1
        assert count_first-count_second==count_direct
        assert count_direct>0
        selected_primes+=count_direct
        congruence_checks+=1
    print('CHECK_OK', 'prime_bases='+str(prime_cases),
          'coprime_partitions='+str(product_cases),
          'odd_targets='+str(congruence_checks),
          'local_class_prime_witnesses='+str(selected_primes),
          'sampled_complement_partitions='+str(represented_checks))


if __name__=='__main__':
    check()
