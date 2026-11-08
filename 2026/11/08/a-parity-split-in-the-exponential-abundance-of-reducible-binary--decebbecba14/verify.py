"""Independent finite enumeration of binary uniform endomorphism factorizations.

Run with Python 3: python verify.py
The symbolic asymptotic proof is in RESULT.md; this program only tests finite cases.
"""
from functools import lru_cache
from itertools import product

@lru_cache(None)
def weighted_words(total, wa, wb):
    if total == 0:
        return ('',)
    if total < 0:
        return ()
    ans = []
    if total >= wa:
        ans.extend('a' + w for w in weighted_words(total-wa, wa, wb))
    if total >= wb:
        ans.extend('b' + w for w in weighted_words(total-wb, wa, wb))
    return tuple(ans)

def images_of_length(length):
    return map(''.join, product('ab', repeat=length))

def substitute(word, a, b):
    return ''.join(a if c == 'a' else b for c in word)

def reducible_uniform_maps(n):
    outcomes = set()
    for sa in range(1, n+1):
        for sb in range(1, n+1):
            if sa == sb == 1:  # Rank-two outer map would be a unit.
                continue
            inner_images = weighted_words(n, sa, sb)
            if len(inner_images) < 2:
                continue
            for outer_a in images_of_length(sa):
                for outer_b in images_of_length(sb):
                    if outer_a + outer_b == outer_b + outer_a:
                        continue
                    for inner_a in inner_images:
                        for inner_b in inner_images:
                            if inner_a == inner_b:
                                continue
                            if len(inner_a) == len(inner_b) == 1:
                                continue  # Inner map is a generator permutation.
                            fa = substitute(inner_a, outer_a, outer_b)
                            fb = substitute(inner_b, outer_a, outer_b)
                            assert len(fa) == len(fb) == n and fa != fb
                            outcomes.add((fa, fb))
    return outcomes

def fibonacci(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a+b
    return a

def main():
    expected = {2:10, 3:38, 4:144, 5:374, 6:1648, 7:2970, 8:13316}
    for n in range(2,9):
        assert len(weighted_words(n,1,2)) == fibonacci(n+1)
        outcomes = reducible_uniform_maps(n)
        R = len(outcomes)
        rank2 = 4**n - 2**n
        assert R == expected[n] and R < rank2
        assert R >= fibonacci(n+1)*(fibonacci(n+1)-1)
        if n % 2 == 0:
            assert R >= 2**(n//2)*(2**n - 1)
        print(f'n={n} reducible={R} rank_two={rank2} irreducible={rank2-R}')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
