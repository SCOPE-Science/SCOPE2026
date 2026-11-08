"""Finite cross-checks of period-doubling palindrome-pair length spectrum."""
from functools import lru_cache
from itertools import product


def morph(w):
    return ''.join('10' if a == '1' else '11' for a in w)


def symmetric(w):
    return w[::-1] in w+w


def two_palindromes(w):
    return any(w[:i] == w[:i][::-1] and w[i:] == w[i:][::-1]
               for i in range(len(w)+1))


@lru_cache(None)
def complexity(n):
    if n == 1: return 2
    if n == 2: return 3
    if n % 2 == 0: return 2*complexity(n//2)
    return complexity((n-1)//2)+complexity((n+1)//2)


def pal_periodicities(n):
    if n == 1: return 2
    k = n.bit_length()-1
    q = 1 << k
    r = n-q
    if 4*r < q: return 3*q//2
    if 2*r < q: return 2*q
    if 4*r < 3*q: return 3*q-r
    return 7*q//2-r


def allowed(n):
    while n % 2 == 0: n //= 2
    return n in (1,3,5)


def main():
    for n in range(1,14):
        for chars in product('01', repeat=n):
            w=''.join(chars)
            assert symmetric(w) == two_palindromes(w), (n,w)
    for length in (1,3,5):
        for chars in product('01', repeat=length):
            base=''.join(chars)
            assert two_palindromes(base)
            for k in range(7):
                w=base
                for j in range(k): w=morph(w)
                assert symmetric(w), (base,k,w)
    bad='0111010'
    assert not two_palindromes(bad)
    for k in range(9):
        assert not symmetric(bad), k
        bad=morph(bad)
    pd='1'
    while len(pd)<8192: pd=morph(pd)
    pd2=morph(pd)
    assert '0111010' in pd
    for n in range(1,193):
        words={pd[i:i+n] for i in range(len(pd)-n+1)}
        words2={pd2[i:i+n] for i in range(len(pd2)-n+1)}
        assert words==words2,(n,'incomplete-prefix factor set')
        assert len(words)==complexity(n),(n,len(words),complexity(n))
        allsym=all(symmetric(w) for w in words)
        assert allsym == allowed(n),(n,allsym,allowed(n))
        assert pal_periodicities(n)<=len(words),(n, 'count incompatible')
        assert (pal_periodicities(n)==len(words)) == (n<=1 or
                n//(n & -n) in (1,3,5,7)),(n,'f=C filter mismatch')
    print('PASS: inversion equivalence, morphism lifting, 7-obstructions,')
    print('      factor completeness and complexity, all lengths 1..192.')

if __name__ == '__main__': main()
