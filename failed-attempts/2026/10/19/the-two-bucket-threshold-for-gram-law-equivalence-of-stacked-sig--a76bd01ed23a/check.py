#!/usr/bin/env python3
"""Exact-rational checks for the two-coordinate signed block-sketch formulas."""
from fractions import Fraction as Q
from itertools import product
from collections import Counter
from math import prod

checks = 0

def test(condition):
    global checks
    assert condition
    checks += 1

def block_distribution(b):
    # Independent bucket hashes and signs for two input coordinate columns.
    counts = {-1: 0, 0: 0, 1: 0}
    for h1, h2, s1, s2 in product(range(b), range(b), (-1, 1), (-1, 1)):
        counts[s1 * s2 if h1 == h2 else 0] += 1
    return {k: Q(v, 4*b*b) for k, v in counts.items()}

def convolution(ds):
    dist = {0: Q(1)}
    for bd in ds:
        out = {}
        for i, p in dist.items():
            for j, q in bd.items():
                out[i+j] = out.get(i+j,Q(0))+p*q
        dist = out
    return dist

def components(m,s):
    if s == 1:
        yield (m,)
    else:
        for b in range(1,m-s+2):
            for rest in components(m-b,s-1):
                yield (b,)+rest

def exact_rank_risk(bs):
    return Q(2, 2**len(bs)*prod(bs))

def exact_gram_variance(bs):
    s=len(bs)
    return sum((Q(1,b) for b in bs),Q(0))/s**2

def balanced(m,s):
    q,r=divmod(m,s)
    return (q,)*(s-r)+(q+1,)*r

for m in range(2,11):
    all_risks=[]
    all_vars=[]
    for s in range(1,m+1):
        family = list(components(m,s))
        br = exact_rank_risk(balanced(m,s))
        bv = exact_gram_variance(balanced(m,s))
        for bs in family:
            ds=[block_distribution(b) for b in bs]
            for b,d in zip(bs,ds):
                test(d[-1]==Q(1,2*b))
                test(d[1]==Q(1,2*b))
                test(d[0]==Q(b-1,b))
            dist=convolution(ds)
            test(sum(dist.values())==1)
            test(dist[len(bs)]+dist[-len(bs)]==exact_rank_risk(bs))
            test(sum((Q(z*z,len(bs)**2)*p for z,p in dist.items()),Q(0)) == exact_gram_variance(bs))
            test(br<=exact_rank_risk(bs))
            test(bv<=exact_gram_variance(bs))
            test(exact_rank_risk(bs)>=Q(1,2**(m-1)))
            test((exact_rank_risk(bs)==Q(1,2**(m-1))) == all(b<=2 for b in bs))
            test(exact_gram_variance(bs)>=Q(1,m))
            test((exact_gram_variance(bs)==Q(1,m)) == (len(set(bs))==1))
            all_risks.append((exact_rank_risk(bs),bs))
            all_vars.append((exact_gram_variance(bs),bs))
    test(min(v for v,_ in all_risks)==Q(1,2**(m-1)))
    test(min(v for v,_ in all_vars)==Q(1,m))
    pars=[bs for risk,bs in all_risks if risk==Q(1,2**(m-1))]
    test(min(len(bs) for bs in pars)==(m+1)//2)
    if m%2:
        bs=(1,)+(2,)*((m-1)//2)
        test(exact_rank_risk(bs)==Q(1,2**(m-1)))
        test(exact_gram_variance(bs)==Q(m+3,(m+1)**2))
        test(Q(m+3,(m+1)**2)-Q(1,m)==Q(m-1,m*(m+1)**2))
    else:
        bs=(2,)*(m//2)
        test(exact_rank_risk(bs)==Q(1,2**(m-1)))
        test(exact_gram_variance(bs)==Q(1,m))



# With per-block weight sqrt(b/m), orthogonal two-row Hadamard mixing
# makes a two-bucket signed one-hot column a pair of iid Rademacher signs.
def sparse_gram_counts(b, n=3):
    states = tuple(product(range(b), (-1, 1)))
    out = Counter()
    for columns in product(states, repeat=n):
        key = tuple(b*columns[i][1]*columns[j][1]*int(columns[i][0]==columns[j][0])
                    for i in range(n) for j in range(i+1,n))
        out[key] += 1
    return out

def dense_gram_counts(b,n=3):
    rows = tuple(product((-1,1),repeat=n))
    out = Counter()
    for sample in product(rows,repeat=b):
        key = tuple(sum(row[i]*row[j] for row in sample)
                    for i in range(n) for j in range(i+1,n))
        out[key] += 1
    return out

for b in (1,2,3,4):
    sparse=sparse_gram_counts(b)
    dense=dense_gram_counts(b)
    sparse_total=sum(sparse.values())
    dense_total=sum(dense.values())
    equal=( {k:Q(v,sparse_total) for k,v in sparse.items()}
           == {k:Q(v,dense_total) for k,v in dense.items()} )
    test(equal==(b<=2))

# Samplewise Hadamard identities on all four one-hot sign states.
for h, sign in product((0,1),(-1,1)):
    col=(sign if h==0 else 0, sign if h==1 else 0)
    out=(col[0]+col[1],col[0]-col[1])
    test(out[0] in (-1,1) and out[1] in (-1,1))
    test(out in product((-1,1),repeat=2))

# Classify all block compositions by whether their Gram law can be
# dense-Rademacher: rank-loss probabilities must agree for two columns.
for m in range(2,13):
    for s in range(1,m+1):
        for bs in components(m,s):
            risk = exact_rank_risk(bs)
            test((risk==Q(1,2**(m-1))) == all(b<=2 for b in bs))
            if all(b<=2 for b in bs):
                test(s >= (m+1)//2)

print(f"PASS: {checks} exact-rational assertions including Gram laws for three-coordinate input")
