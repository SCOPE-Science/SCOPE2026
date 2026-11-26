#!/usr/bin/env python3
from itertools import product

F={'0':'0','1':'01','2':'011'}
G={'0':'011','1':'0121','2':'012121'}
H={'0':'01','1':'02','2':'022'}
D={'0':-1,'1':0,'2':1}

def morph(word,M):
    return ''.join(M[c] for c in word)

def dtern(word):
    return sum(D[c] for c in word)

def dbin(word):
    return word.count('1')-word.count('0')

# Letterwise identities that drive the analytic proof.
for a in '012':
    assert dbin(F[a])==D[a]
    assert dtern(H[a])==D[a]
    assert dtern(G[a])==D[a]

# Replay iterates directly to guard composition order and block-growth claims.
for n in range(13):
    vals=[]
    vals_g=[]
    for a in '012':
        x=a
        for _ in range(n):
            x=morph(x,H)
        y=morph(x,F)
        yg=morph(morph(x,G),F)
        assert dbin(y)==D[a]
        assert dbin(yg)==D[a]
        vals.append(len(y))
        vals_g.append(len(yg))
    assert min(vals) >= 2**n
    assert min(vals_g) >= 3*(2**n)

# Additive extension: the identities hold for arbitrary short ternary words.
for L in range(7):
    for tup in product('012', repeat=L):
        v=''.join(tup)
        assert dbin(morph(v,F))==dtern(v)
        assert dtern(morph(v,H))==dtern(v)
        assert dtern(morph(v,G))==dtern(v)

print('VERIFY_OK morphism_imbalance_invariant=1 iterates_n=0..12 block_growth_ge_2^n=1 arbitrary_words_len<=6=1 analytic_factor_bound=recorded')
