#!/usr/bin/env python3
"""Direct finite checks for cyclic palindromes of three-marker binary words.

No packages are required beyond the Python standard library.
The universal mathematical argument is given in RESULT.md.
"""
from itertools import combinations

def cyclic_palindromes(word):
    """Literal palindromic windows of lengths 1,...,n from all n starting sites."""
    n = len(word)
    circular = word + word
    answer = set()
    for start in range(n):
        for length in range(1, n + 1):
            factor = circular[start:start + length]
            if factor == factor[::-1]:
                answer.add(factor)
    return answer

def predicted_total(gaps):
    a, b, c = sorted(gaps)
    n = a + b + c + 3
    if a == b == c:
        return n + a // 2
    if a == b or b == c:
        return n + (n - 1) // 2
    return 2 * n - c - 2

def predicted_max(n):
    return 2 * n - (n + 2) // 3 - 2

def maximizing_gap_multisets(n):
    optimum = predicted_max(n)
    triples = []
    for a in range(n - 2):
        for b in range(a, n - 2 - a):
            c = n - 3 - a - b
            if c < b:
                continue
            if predicted_total((a,b,c)) == optimum:
                triples.append((a,b,c))
    return triples

def asserted_maximizers(n):
    k, r = divmod(n, 3)
    if r == 0:
        return [(k-2, k-1, k)]
    if r == 1:
        return [(k-3, k, k+1), (k-2, k-1, k+1)]
    return [(k-2,k,k+1)]

def main():
    tested = 0
    for n in range(3, 37):
        for a in range(n - 2):
            for b in range(n - 2 - a):
                c = n - 3 - a - b
                word = '1'+'0'*a+'1'+'0'*b+'1'+'0'*c
                expected = predicted_total((a,b,c))
                observed = len(cyclic_palindromes(word))
                assert observed == expected, (n, a, b, c, observed, expected)
                tested += 1
        if n >= 14:
            expected_triples = sorted(asserted_maximizers(n))
            observed_triples = maximizing_gap_multisets(n)
            assert observed_triples == expected_triples, (n, observed_triples, expected_triples)
    brute_extrema = 0
    for n in range(14, 25):
        values = {}
        for a in range(n - 2):
            for b in range(a, n - 2 - a):
                c = n - 3 - a - b
                if c < b:
                    continue
                word = '1'+'0'*a+'1'+'0'*b+'1'+'0'*c
                values[(a,b,c)] = len(cyclic_palindromes(word))
        brute_max = max(values.values())
        winners = sorted(g for g,v in values.items() if v == brute_max)
        assert brute_max == predicted_max(n)
        assert winners == sorted(asserted_maximizers(n)), (n,winners)
        brute_extrema += 1
    print('VERIFY_OK', 'words='+str(tested), 'lengths=3..36',
          'maximizers=14..36', 'independent_extrema='+str(brute_extrema))

if __name__ == "__main__":
    main()
