#!/usr/bin/env python3
"""Independent exact exterior-basis multiplication check of a finite square-map law."""
from collections import Counter
from itertools import product
from math import comb
from random import Random


def sign_of_product(a,b):
    if a & b:
        return 0
    inversions = sum(((a >> (j+1)).bit_count()) for j in range(4) if b >> j & 1)
    return -1 if inversions % 2 else 1


def square_coefficients(q, vector):
    masks = [1,2,4,8,3,5,9,6,10,12]
    output = [0]*16
    for i,a in enumerate(masks):
        for j,b in enumerate(masks):
            s = sign_of_product(a,b)
            if s:
                output[a|b] = (output[a|b] + s*vector[i]*vector[j])%q
    assert all(output[k]==0 for k in range(16) if k not in (7,11,13,14,15))
    return tuple(output[k] for k in (7,11,13,14,15))


def check(q):
    counter=Counter(square_coefficients(q, x) for x in product(range(q), repeat=10))
    predicted_nonzero=q*q*(q**3-1)
    predicted_zero=q**7+q**5-q**2
    expected={t:(predicted_zero if t==(0,)*5 else predicted_nonzero)
              for t in product(range(q), repeat=5)}
    assert counter == expected, f'mismatch q={q}, max difference={max(abs(counter[k]-v) for k,v in expected.items())}'
    print(f'q={q}: pairs={q**10}, targets={q**5}, zero_fiber={predicted_zero}, every_nonzero_fiber={predicted_nonzero}; PASS')

for q in (2,3):
    if q==2:
        sq={square_coefficients(q,x) for x in product(range(q),repeat=10)}
        assert sq == {(0,)*5}, f'characteristic two boundary failed: {sq}'
        print('q=2: all 1024 inputs have zero square; PASS')
    else:
        check(q)
print('All checks passed; test is finite corroboration, not an infinite-field proof.')


def multiply(q, a, b):
    out = [0]*16
    for i, x in enumerate(a):
        if not x: continue
        for j, y in enumerate(b):
            if not y: continue
            if i & j: continue
            out[i|j] = (out[i|j] + x*y*sign_of_product(i,j)) % q
    return out


def test_full_nonzero_scalar(q, attempts=64):
    rng=Random(12)
    for _ in range(attempts):
        root_scalar = rng.randrange(1,q)
        target=[root_scalar*root_scalar % q]+[rng.randrange(q) for _ in range(15)]
        u=[0]+target[1:]
        u2=multiply(q,u,u)
        inverse2=pow(2,-1,q)
        inverse8=pow(8,-1,q)
        roots=[]
        for scalar in set((root_scalar, (-root_scalar)%q)):
            r=[0]*16
            r[0]=scalar
            for j in range(1,16):
                r[j]=(u[j]*inverse2*pow(scalar,-1,q)-u2[j]*inverse8*pow(scalar,-3,q))%q
            assert multiply(q,r,r)==target
            roots.append(r)
        assert len(roots)==2
    print(f'q={q}: {attempts} prescribed targets with nonzero square scalar; two explicitly constructed roots per target; PASS')

for q in (3,5):
    test_full_nonzero_scalar(q)
