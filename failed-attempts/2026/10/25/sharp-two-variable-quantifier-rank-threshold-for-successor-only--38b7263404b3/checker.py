#!/usr/bin/env python3
"""Exact FO-two-variable unary type refinement on finite successor paths.

Computational verification for bounded sizes, not an infinite proof.
"""
MAX_N=22
colors={(n,i):0 for n in range(1,MAX_N+1) for i in range(n)}
for q in range(1,7):
    groups={}
    for n in range(1,MAX_N+1):
        signature=frozenset(colors[(n,i)] for i in range(n))
        groups.setdefault(signature,[]).append(n)
    partition=sorted(groups.values(),key=lambda a:a[0])
    expected=([[n] for n in range(1,2*q)]+[list(range(2*q,MAX_N+1))] if q>=2 else [list(range(1,MAX_N+1))])
    assert partition==expected,(q,partition,expected)
    features={}
    for n in range(1,MAX_N+1):
        for i in range(n):
            occurrences=frozenset((0 if i==j else 1 if j==i+1 else 2 if j==i-1 else 3,colors[(n,j)]) for j in range(n))
            features[(n,i)]=(colors[(n,i)],occurrences)
    unique={v:k for k,v in enumerate(set(features.values()))}
    colors={key:unique[f] for key,f in features.items()}
print("PASS: all directed paths of sizes 1..22 and ranks 1..6")
