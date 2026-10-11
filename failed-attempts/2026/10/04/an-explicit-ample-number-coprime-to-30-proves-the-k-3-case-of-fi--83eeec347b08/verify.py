#!/usr/bin/env python3
from math import comb, isqrt
from functools import lru_cache
import itertools

PRIMES = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137]
EXPS = [53, 32, 27, 20, 18, 14, 11, 11, 9, 8, 7, 7, 6, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2]
EXPECTED_N = 620292621350581595028788086460529920524835904967474139327792360930732793395120244743880376383226268545987559098771892559442316407609738081067885836143275657304648271565207000271510801969286511134165572223709287438361671058622276645794887113763333824201182721793334478788976256555206276595970169364248794528714439830251723041454975723539907118879778865193261927620897356292999057
EXPECTED_A = 4049133544250342561183325521264172563005480191320800479542494459697603112797635044312286342288876256821977562257067011133903745199643554947861982777035319862599949177417621412966898015644050302785597441965242309323324272569620209275645157830398009101069585728309165802195604952107308511903423174568579984014507189732152001080722827137532141825789248283717033830043635021423667314688
EXPECTED_DIFF = 4048513251628991979588296733177712033084955355415833005403166667336672380004239924067542461912493030553431574697968239241344302883235945209780914891199176586942644529146056205966626504842081016274463276393018600035885910898561586998999362943284245767245384545587372467716815975850753305626827204399215735219978475292321749357681372161808601918670368504851840568116014124067374315631

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d <= isqrt(n):
        if n % d == 0:
            return False
        d += 2
    return True

def recursive_a_small(exps):
    @lru_cache(None)
    def rec(v):
        if all(x == 0 for x in v):
            return 1
        total = 1
        ranges = [range(x + 1) for x in v]
        for w in itertools.product(*ranges):
            if w != v:
                total += rec(w)
        return total
    return rec(tuple(exps))

def ordered_factorization_a(exps):
    omega_big = sum(exps)
    total_K = 0
    for m in range(1, omega_big + 1):
        km = 0
        for t in range(1, m + 1):
            term = comb(m, t)
            for alpha in exps:
                term *= comb(alpha + t - 1, t - 1)
            km = km - term if (m - t) & 1 else km + term
        assert km >= 0
        total_K += km
    return 2 * total_K

def main():
    assert len(PRIMES) == len(EXPS) == 30
    assert len(set(PRIMES)) == 30
    assert all(is_prime(p) and p > 5 for p in PRIMES)
    assert sum(EXPS) == 280

    n = 1
    for p, e in zip(PRIMES, EXPS):
        n *= p ** e
    assert n == EXPECTED_N
    assert n % 2 and n % 3 and n % 5

    for v in ([1], [2], [3], [1,1], [2,1], [1,1,1], [3,2]):
        assert ordered_factorization_a(list(v)) == recursive_a_small(list(v))

    a = ordered_factorization_a(EXPS)
    assert a == EXPECTED_A
    assert a - n == EXPECTED_DIFF
    assert a > n

    print("VERIFY_OK")
    print("omega=30")
    print("Omega=280")
    print("N=" + str(n))
    print("a(N)=" + str(a))
    print("a(N)-N=" + str(a-n))

if __name__ == "__main__":
    main()
