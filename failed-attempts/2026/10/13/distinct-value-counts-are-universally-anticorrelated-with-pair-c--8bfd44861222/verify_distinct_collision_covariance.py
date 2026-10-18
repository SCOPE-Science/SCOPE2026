#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import comb
import mpmath as mp

def cov_formula(p, n):
    q2 = sum(x*x for x in p)
    r = n - 2
    return comb(n, 2) * sum(
        x * (1-x)**r * (x - (2-x)*q2)
        for x in p
    )

def exhaustive(p, n):
    m = len(p)
    EK = EC = EKC = Fraction(0)
    word_count = 0
    for word in product(range(m), repeat=n):
        pr = Fraction(1)
        for a in word:
            pr *= p[a]
        K = len(set(word))
        C = sum(
            1
            for i in range(n)
            for j in range(i+1, n)
            if word[i] == word[j]
        )
        EK += pr*K
        EC += pr*C
        EKC += pr*K*C
        word_count += 1
    return word_count, EKC - EK*EC

def uniform_var_k(n, m, dps=80):
    mp.mp.dps = dps
    m = mp.mpf(m)
    a = 1 - 1/m
    b = 1 - 2/m
    return m*a**n + m*(m-1)*b**n - m*m*a**(2*n)

def uniform_cov(n, m):
    mp.mp.dps = 80
    m = mp.mpf(m)
    return -mp.mpf(comb(n,2))/m * (1-1/m)**(n-1)

def uniform_var_c(n, m):
    mp.mp.dps = 80
    m = mp.mpf(m)
    return mp.mpf(comb(n,2))*(m-1)/(m*m)

def run():
    profiles = [
        [Fraction(1,2), Fraction(1,2)],
        [Fraction(1,3), Fraction(2,3)],
        [Fraction(1,2), Fraction(1,3), Fraction(1,6)],
        [Fraction(3,5), Fraction(1,5), Fraction(1,5)],
        [Fraction(1,2), Fraction(1,4), Fraction(1,8), Fraction(1,8)],
    ]

    exhaustive_checks = 0
    weighted_sign_checks = 0
    total_words = 0

    for p in profiles:
        q2 = sum(x*x for x in p)
        assert 0 < q2 < 1
        for n in range(2, 7):
            words, cov_enum = exhaustive(p, n)
            cov_closed = cov_formula(p, n)
            assert cov_enum == cov_closed
            assert cov_closed < 0
            total_words += words
            exhaustive_checks += 1

            r = n - 2
            w = [x*(2-x) for x in p]
            W = sum(w)
            f = [x/(2-x) for x in p]
            g = [(1-x)**r for x in p]
            Ew_f = sum(wi*fi for wi,fi in zip(w,f))/W
            Ew_g = sum(wi*gi for wi,gi in zip(w,g))/W
            Ew_fg = sum(wi*fi*gi for wi,fi,gi in zip(w,f,g))/W
            assert Ew_f == q2/(2-q2)
            assert Ew_fg <= Ew_f*Ew_g
            assert Ew_f < q2
            weighted_sign_checks += 1

    uniform_checks = 0
    for m in range(2, 9):
        p = [Fraction(1,m)]*m
        for n in range(2, 10):
            closed = cov_formula(p, n)
            target = -Fraction(comb(n,2), m) * Fraction(m-1,m)**(n-1)
            assert closed == target
            # Pair-match variance by pairwise independence.
            varc = Fraction(comb(n,2)*(m-1), m*m)
            assert varc > 0
            uniform_checks += 2

    mp.mp.dps = 80
    asymptotic_checks = 0
    for c in [mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2")]:
        prev_err = None
        for M in [10_000, 100_000, 1_000_000]:
            n = int(mp.nint(c*mp.sqrt(M)))
            vk = uniform_var_k(n, M)
            vc = uniform_var_c(n, M)
            cv = uniform_cov(n, M)
            rho = cv / mp.sqrt(vk*vc)
            assert -1 < rho < 0
            err = abs(rho + 1)
            if prev_err is not None:
                assert err < prev_err
            prev_err = err
            asymptotic_checks += 1
        assert prev_err < mp.mpf("0.02")

    print(
        "VERIFY_OK "
        f"exhaustive_checks={exhaustive_checks} "
        f"weighted_sign_checks={weighted_sign_checks} "
        f"uniform_checks={uniform_checks} "
        f"asymptotic_checks={asymptotic_checks} "
        f"enumerated_words={total_words}"
    )

if __name__ == "__main__":
    run()
