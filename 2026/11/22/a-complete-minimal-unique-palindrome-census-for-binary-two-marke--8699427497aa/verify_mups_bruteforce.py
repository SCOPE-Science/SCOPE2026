#!/usr/bin/env python3
"""Independent literal occurrence verification of minimal unique palindromes.
No published results or external files are required.
"""
from collections import Counter
from itertools import product


def literal_mups(text):
    occurrence_count = Counter(text[i:j] for i in range(len(text))
                               for j in range(i + 1, len(text) + 1))
    return sorted((text[i:j], i, j)
                  for i in range(len(text))
                  for j in range(i+1,len(text)+1)
                  if text[i:j] == text[i:j][::-1]
                  and occurrence_count[text[i:j]] == 1
                  and (j - i <= 2 or occurrence_count[text[i+1:j-1]] >= 2))


def theorem_mups(a, b, c):
    word = '0'*a + '1' + '0'*b + '1' + '0'*c
    result = []
    largest = max(a,b,c)
    if [a,b,c].count(largest) == 1:
        p = '0'*largest
        i = word.index(p)
        result.append((p,i,i+len(p)))
    left = min(a,b)
    right = min(b,c)
    if left != right:
        t = min(left,right)+1
        p = '0'*t + '1' + '0'*t
        i = word.index(p)
        result.append((p,i,i+len(p)))
    if max(a,c) >= b:
        p = '1'+'0'*b+'1'
        i = word.index(p)
        result.append((p,i,i+len(p)))
    return sorted(result)


def k_formula(a,b,c):
    if a == c: return 1
    if (a<b<c) or (c<b<a): return 3
    return 2

checks=0
for a,b,c in product(range(1,16),repeat=3):
    text='0'*a+'1'+'0'*b+'1'+'0'*c
    actual=literal_mups(text)
    predicted=theorem_mups(a,b,c)
    assert actual==predicted, (a,b,c,actual,predicted)
    assert len(actual)==k_formula(a,b,c), (a,b,c,actual)
    checks+=1
print('PASS literal palindrome-occurrence and identity check:',checks,'triples')
print('word-length range: 5..47')
