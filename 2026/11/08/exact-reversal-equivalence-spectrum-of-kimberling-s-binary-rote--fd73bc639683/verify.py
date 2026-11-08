#!/usr/bin/env python3
"""Exact finite-factor certificate for a Tribonacci morphic image.

No third-party packages are needed. All finite sets are obtained from
substitution identities rather than a sampled prefix of the infinite word.
"""
from collections import Counter

phi = {'0':'01','1':'02','2':'0'}
pi = {'0':'100','1':'101','2':'10'}
expected_pairs = {'00','01','02','10','20'}
expected_six = {
    '001020','010010','010102','010201','020100','020101',
    '020102','100102','101020','102010','201001','201010','201020'
}
expected_P = [0,2,2,2,2,2,1,2,1,1,0,0]
expected_Q = [0,0,1,2,2,2,3,2,1,0,0,0]
expected_ten = {
    '0010010110','0010100101','0010110010','0100101100','0101001011',
    '0101100100','0101100101','0110010010','0110010100','0110010110',
    '1001001011','1001010010','1001011001','1010010110','1011001001',
    '1011001010','1011001011','1100100101','1100101001','1100101100'
}
expected_palindromes = {
    1:['0','1'], 2:['00','11'], 3:['010','101'],
    4:['0110','1001'],5:['00100','01010'],6:['010010'],
    7:['0010100','1001001'],8:['10100101'],9:['100101001']
}

def morph(word, mapping):
    return ''.join(mapping[c] for c in word)

def iterate(word, mapping, order):
    for _ in range(order):
        word = morph(word, mapping)
    return word

def factors(word, n):
    return {word[i:i+n] for i in range(len(word)-n+1)}

# To prove the exact Tribonacci two-factor language, compute the closure
# of factors of phi(uv) starting with the factor 01 of phi(0).
pair_closure = {'01'}
while True:
    expanded = pair_closure | set().union(*(
        factors(morph(uv, phi),2) for uv in pair_closure
    ))
    if expanded == pair_closure:
        break
    pair_closure = expanded
assert pair_closure == expected_pairs, pair_closure
assert all(factors(morph(uv,phi),2) <= expected_pairs for uv in expected_pairs)

# Every fourth substituted block contains at least six characters.
assert min(len(iterate(c,phi,4)) for c in phi) >= 6
six = set().union(*(
    factors(iterate(uv,phi,4),6) for uv in expected_pairs
))
assert six == expected_six, sorted(six)

# Every binary factor of length <=11 away from the initial position
# meets at most six successive pi-blocks, each of length >=2.
assert min(map(len,pi.values())) == 2
bprefix = '0' + morph(iterate('0',phi,8),pi)
assert len(bprefix) >= 11
language = {}
for n in range(1,12):
    L = {bprefix[:n]}
    for u in six:
        L.update(factors(morph(u,pi),n))
    language[n] = L
    assert len(L) == 2*n, (n,len(L))
    P = sorted(w for w in L if w == w[::-1])
    Q = {frozenset((w,w[::-1])) for w in L
         if w != w[::-1] and w[::-1] in L}
    assert len(P) == expected_P[n], (n,P)
    assert len(Q) == expected_Q[n], (n,Q)
    if n in expected_palindromes:
        assert P == expected_palindromes[n], (n,P)
assert language[10] == expected_ten
assert all(w[::-1] not in language[10] for w in language[10])

# Independent prefix cross-check is supporting evidence only, NOT a proof
# of infinite completeness. Exactness comes from the block argument above.
long_prefix = '0' + morph(iterate('0',phi,13),pi)
for n,L in language.items():
    assert factors(long_prefix,n) == L
print('PASS: exact Tribonacci pair/six-factor closure; Kimberling P,Q')
print('PASS: 20 length-10 factors, no reverse partners; 15 palindromes')
print('PASS: 11 independent long-prefix cross-checks')
