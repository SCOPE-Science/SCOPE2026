"""Standalone finite checks for two-successive-adjacent-swap sphere formulas."""
from itertools import product
from math import comb
from collections import Counter


def brute(word):
    n = len(word)
    outputs = set()
    for i in range(n - 1):
        a = list(word)
        a[i], a[i + 1] = a[i + 1], a[i]
        for j in range(n - 1):
            b = a[:]
            b[j], b[j + 1] = b[j + 1], b[j]
            outputs.add(tuple(b))
    return len(outputs)


def predicted(word):
    n = len(word)
    e = [word[i] != word[i + 1] for i in range(n - 1)]
    r = sum(e)
    adjacent_active = sum(e[i] and e[i + 1] for i in range(n - 2))
    pal = sum(word[i] == word[i + 2] != word[i + 1] for i in range(n - 2))
    one_active = sum(e[i] != e[i + 1] for i in range(n - 2))
    if r < n - 1:
        singles = r
    else:
        touched = set()
        for i in range(n - 2):
            if word[i] == word[i + 2]:
                touched.add(i)
                touched.add(i + 1)
        singles = len(touched)
    return 1 + comb(r, 2) + adjacent_active - 2 * pal + one_active + singles


def families(q, n):
    a = b = 0
    for word in product(range(q), repeat=n):
        transitions = [word[i] != word[i + 1] for i in range(n-1)]
        palindrome_triples = [i for i in range(n-2)
                              if word[i] == word[i+2] != word[i+1]]
        no_zero_case = all(transitions) and all(
            palindrome_triples[i+1] - palindrome_triples[i] > 1
            for i in range(len(palindrome_triples)-1))
        one_zero_case = transitions.count(False) == 1 and not palindrome_triples
        a += no_zero_case
        b += one_zero_case
    return a, b


def predicted_families(q, n):
    if n == 2:
        return q*(q-1), q
    a_prev = q*(q-1)
    a = q*(q-1)**2
    for _ in range(4, n+1):
        a_prev, a = a, (q-2)*(a + a_prev) if _ >= 5 else q*q*(q-1)*(q-2)
    # f(k): first letter fixed, adjacent different, no palindromic triples
    def f(k):
        return 1 if k == 1 else (q-1)*(q-2)**(k-2)
    b = q*sum(f(j)*f(n-j) for j in range(1, n))
    return a, b


total = 0
for q, maxn in [(2, 12), (3, 9), (4, 7), (5, 6)]:
    for n in range(2, maxn+1):
        counter = Counter()
        family_a = family_b = 0
        for word in product(range(q), repeat=n):
            observed = brute(word)
            formula = predicted(word)
            assert observed == formula, (q, n, word, observed, formula)
            counter[observed] += 1
            total += 1
            if q >= 3:
                e = [word[i] != word[i+1] for i in range(n-1)]
                pal = [i for i in range(n-2) if word[i] == word[i+2] != word[i+1]]
                is_a = all(e) and all(pal[i+1]-pal[i]>1 for i in range(len(pal)-1))
                is_b = e.count(False)==1 and not pal
                assert (observed == comb(n,2)) == (is_a or is_b), (q,n,word,observed)
                family_a += is_a
                family_b += is_b
        if q >= 3:
            assert max(counter) == comb(n, 2)
            assert (family_a,family_b) == predicted_families(q,n), (q,n,(family_a,family_b),predicted_families(q,n))
            assert counter[max(counter)] == family_a+family_b
        print('q=%d n=%d checked=%d maximum=%d optimizers=%d' % (
            q,n,q**n,max(counter),counter[max(counter)]))

print('PASS: all %d words checked against direct two-swap generation and nonbinary extremizer formulas.' % total)
