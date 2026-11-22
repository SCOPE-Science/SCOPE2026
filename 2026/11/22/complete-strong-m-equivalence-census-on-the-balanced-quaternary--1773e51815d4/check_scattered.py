#!/usr/bin/env python3
"""Exact census for injective scattered-subword profiles on the (2,2,2,2) layer.

Run with Python 3, standard library only. No external data.
"""
from collections import Counter, defaultdict
from itertools import permutations
from math import factorial

ALPHABET = '0123'

def words(counts, prefix=''):
    if sum(counts)==0:
        yield prefix
        return
    for a in range(4):
        if counts[a]:
            counts[a]-=1
            yield from words(counts, prefix+ALPHABET[a])
            counts[a]+=1

patterns = tuple(''.join(p) for size in (2,3,4)
                 for p in permutations(ALPHABET, size))
assert len(patterns)==12+24+24 == 60

def scattered_occurrences(word, pattern):
    # Dynamic programming counts subsets of increasing positions, not factors.
    dp=[1]+[0]*len(pattern)
    for letter in word:
        for j in range(len(pattern)-1,-1,-1):
            if pattern[j]==letter:
                dp[j+1]+=dp[j]
    return dp[-1]

def profile(word):
    return tuple(scattered_occurrences(word,p) for p in patterns)

W=list(words([2,2,2,2]))
assert len(W)==factorial(8)//2**4==2520
classes=defaultdict(list)
for w in W:
    classes[profile(w)].append(w)
dist=Counter(map(len,classes.values()))
assert dist=={1:2184,2:156,4:6}, dist
assert len(classes)==2346
assert sum(k*v for k,v in dist.items())==2520
print('total_words=2520')
print('profiles=2346')
print('class_size_histogram='+str(sorted(dist.items())))
print('four_word_class_representatives='+str(sorted(min(c) for c in classes.values() if len(c)==4)))
