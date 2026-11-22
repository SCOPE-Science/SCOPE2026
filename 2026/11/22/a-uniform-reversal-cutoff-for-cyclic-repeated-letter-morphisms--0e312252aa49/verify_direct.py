#!/usr/bin/env python3
"""Independent concrete-factor verification using a base-three digit count.
This is a sanity check, not the all-alphabet proof.
"""

def digit_twos(i):
    result = 0
    while i:
        result += (i % 3 == 2)
        i //= 3
    return result

def counts(word, n):
    factors = {tuple(word[i:i+n]) for i in range(len(word)-n+1)}
    reversed_factors = [v for v in factors if v[::-1] in factors]
    palindromes = [v for v in factors if v[::-1] == v]
    return len(reversed_factors), len(palindromes)

def main():
    print('Independent digit-formula factor checks')
    for q in (3, 4, 5):
        N = 3**(q+3)
        sequence = [digit_twos(i) % q for i in range(N)]
        pairs = {(sequence[i], sequence[i+1]) for i in range(N-1)}
        assert len(pairs) == q*q, (q, len(pairs))
        for n in range(1, 10):
            expected_r = q if n==1 else q*q if n==2 else 4*q if n==3 else 3*q if 4<=n<=7 else q if n==8 else 0
            expected_p = q if n in (1,2) else 2*q if n==3 else q if 4<=n<=8 else 0
            actual = counts(sequence, n)
            assert actual == (expected_r, expected_p), (q,n,actual)
        print(f'q={q}: verified all pairs and all n=1..9, prefix length {N}')
    print('PASS: 27 exact independent finite-prefix comparisons')

if __name__ == '__main__':
    main()
