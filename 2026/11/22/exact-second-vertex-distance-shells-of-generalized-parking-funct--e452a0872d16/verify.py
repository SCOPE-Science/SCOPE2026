"""Exact integer verification for the second vertex-distance shell.

Exhaustively constructs vertices from the vertex-layer theorem, independently
ranks all unordered squared distances and compares their multiplicities with
the closed second-shell formula. Finite verification supplements the proof.
"""
from collections import Counter
from itertools import accumulate, permutations
from math import factorial


def predicted(b):
    n = len(b)
    t = [x - 1 for x in accumulate(b)]
    def F(k):
        return sum(x*x for x in t[n-k:])
    m = n//2
    D = F(m)+F(n-m)
    missing = t[m]**2
    imbalance = (t[m]**2-t[m-1]**2) if n%2==0 else (t[m+1]**2-t[m-1]**2)
    overlaps = {k: D - F(k) - F(n+1-k)+2*t[n-k]*t[k-1]
                for k in range(1, (n+1)//2+1)}
    gamma = min([missing, imbalance, *overlaps.values()])
    count = 0
    if missing == gamma:
        count += factorial(n)//(2 if n%2 else 1)
    if imbalance == gamma:
        count += factorial(n)
    for k, deficit in overlaps.items():
        if deficit == gamma:
            count += factorial(n)//(2 if 2*k==n+1 else 1)
    return D, D-gamma, count


def exhaustive(b):
    n = len(b)
    vals = [x-1 for x in accumulate(b)]
    vertices = set()
    for z in range(n+1):
        vertices.update(permutations((0,)*z+tuple(vals[z:])))
    vertices = sorted(vertices)
    freq = Counter()
    for i, u in enumerate(vertices):
        for v in vertices[i+1:]:
            freq[sum((a-b)**2 for a,b in zip(u,v))]+=1
    top = sorted(freq, reverse=True)
    return top[0], top[1], freq[top[1]]


def main():
    tests = [
       (2,1,1,1), (5,2,7,9), (8,8,52,27,56),
       (23,17,28,2,16), (31,11,10,50,10),
       (38,38,25,25,64), (2,1,3,5,7),
       (2,1,2,3,4,5), (7,2,3,5,11,13),
    ]
    for b in tests:
        p = predicted(b)
        q = exhaustive(b)
        assert p == q, (b,p,q)
    print('GENERALIZED_PARKING_SECOND_SHELL_EXACT_PASS cases='+str(len(tests)))

if __name__ == '__main__':
    main()
