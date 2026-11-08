#!/usr/bin/env python3
"""Exact all-codebook enumeration for balanced four-letter DNA codes.

Only uses the Python standard library. The count is of labeled word sets, not
sets modulo symbol or coordinate permutations.
"""
import itertools
import json
from collections import Counter
from pathlib import Path

ALPHABET = 'ACGT'
COMP = dict(zip(ALPHABET, 'TGCA'))

def rc(w):
    return ''.join(COMP[x] for x in reversed(w))

def ham(a,b):
    return sum(x != y for x,y in zip(a,b))

def gc_mask(w):
    return ''.join('1' if x in 'CG' else '0' for x in w)

WORDS = tuple(''.join(p) for p in itertools.product(ALPHABET,repeat=4)
              if sum(x in 'CG' for x in p)==2)
MASKS = {m:tuple(w for w in WORDS if gc_mask(w)==m)
         for m in sorted(set(map(gc_mask,WORDS)))}
PAIRS = {m:tuple((a,b) for i,a in enumerate(ww) for b in ww[i+1:]
                 if ham(a,b)>=3) for m,ww in MASKS.items()}
assert len(WORDS)==96 and len(MASKS)==6
assert all(len(p)==40 for p in PAIRS.values())
# Exactly two masks are invariant under position reversal.
fixed = ('0110','1001')
paired = ('0011','0101')
FIXED = {m:tuple(p for p in PAIRS[m] if set(rc(x) for x in p)==set(p)) for m in fixed}
assert len(FIXED[fixed[0]])==len(FIXED[fixed[1]])==4

def good(code):
    return all(ham(a,b)>=3 for i,a in enumerate(code) for b in code[i+1:])

# This loops over every saturation choice: one two-word pair in each of
# six GC masks, with the reverse-complement partner forced by closure.
solutions = set()
for a in PAIRS[paired[0]]:
    ra = tuple(rc(x) for x in a)
    for b in PAIRS[paired[1]]:
        rb = tuple(rc(x) for x in b)
        for c in FIXED[fixed[0]]:
            for d in FIXED[fixed[1]]:
                code=tuple(sorted(a+b+c+d+ra+rb))
                if good(code):
                    assert len(code)==12
                    assert {rc(x) for x in code}==set(code)
                    solutions.add(code)
assert len(solutions)==16
assert all(sum(ham(a,b)==4 for i,a in enumerate(code) for b in code[i+1:])==18
           for code in solutions)

pal = Counter(sum(w==rc(w) for w in code) for code in solutions)
assert pal=={0:8,4:8}

# Natural group: base permutations commuting with complementation and
# coordinate permutations commuting with reversal. It preserves GC=2.
base_maps = [dict(zip(ALPHABET,p)) for p in itertools.permutations(ALPHABET)
             if all(dict(zip(ALPHABET,p))[COMP[x]]==COMP[dict(zip(ALPHABET,p))[x]]
                    for x in ALPHABET)]
pos_maps = [p for p in itertools.permutations(range(4))
            if all(p[3-i]==3-p[i] for i in range(4))]
assert len(base_maps)==8 and len(pos_maps)==8

def transform(code,b,p):
    return tuple(sorted(''.join(b[w[p[j]]] for j in range(4)) for w in code))

remaining=set(solutions)
groups=[]
while remaining:
    code=min(remaining)
    orbit={transform(code,b,p) for b in base_maps for p in pos_maps}
    assert orbit<=solutions
    groups.append(orbit)
    remaining-=orbit
assert sorted(map(len,groups))==[2,2,4,4,4]
assert sorted((len(group),sum(w==rc(w) for w in min(group))) for group in groups)==[(2,4),(2,4),(4,0),(4,0),(4,4)]

# For each nonpalindromic 12-word code the 6 RC pairs admit 2^6 ways
# to pick one orientation. Each is a conventional King-style 6-word
# code, and every such optimum has exactly one such closure.
oriented=set()
for code in solutions:
    if any(rc(w)==w for w in code):
        continue
    orbitpairs=sorted({tuple(sorted((w,rc(w)))) for w in code})
    assert len(orbitpairs)==6
    for choice in itertools.product((0,1),repeat=6):
        oriented.add(tuple(sorted(o[z] for o,z in zip(orbitpairs,choice))))
assert len(oriented)==512
assert all(len(o)==6 and good(o) and all(ham(x,rc(y))>=3 for x in o for y in o)
           for o in oriented)

artifact = {'description':'All labeled optimal 12-word, RC-closed, GC-balanced length-four DNA Hamming-3 codes',
            'codes':[list(c) for c in sorted(solutions)],
            'num_optimal_codes':16,
            'palindrome_counts':{str(k):v for k,v in sorted(pal.items())},
            'natural_symmetry_orbit_sizes':sorted(map(len,groups)),
            'oriented_six_word_codes':512,
            'pair_distance_distribution':{'3':48,'4':18}}
path=Path(__file__).with_name('optimal_codes.json')
if path.exists():
    assert json.loads(path.read_text('utf-8'))==artifact
else:
    path.write_text(json.dumps(artifact,indent=2,ensure_ascii=True)+'\n',encoding='utf-8')
print('MASK_ENUM_OK: 96 words, 40 pair choices per mask, 4 invariant pair choices per fixed mask, 16 optimum closures, 512 oriented codes')
print('SYMMETRY_OK: 5 natural symmetry orbits of sizes 2,2,4,4,4')
