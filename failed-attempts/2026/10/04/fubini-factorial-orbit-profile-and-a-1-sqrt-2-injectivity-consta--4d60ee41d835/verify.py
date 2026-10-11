#!/usr/bin/env python3
from itertools import permutations
from math import factorial, sqrt


def partitions_rgs(n):
    if n == 0:
        yield ()
        return
    a = [0] * n
    def rec(i, mx):
        if i == n:
            yield tuple(a)
            return
        for v in range(mx + 2):
            a[i] = v
            yield from rec(i + 1, max(mx, v))
    a[0] = 0
    yield from rec(1, 0)


def stirling_table(N):
    S = [[0]*(N+1) for _ in range(N+1)]
    S[0][0] = 1
    for n in range(1, N+1):
        for k in range(1, n+1):
            S[n][k] = S[n-1][k-1] + k*S[n-1][k]
    return S


def fubini(n, S):
    return sum(factorial(k)*S[n][k] for k in range(n+1))


def bit(mask, n, i, j):
    return (mask >> (i*n+j)) & 1


def injective_signatures(n):
    out = set()
    if n == 0:
        return {(0,0,0)}
    for part in partitions_rgs(n):
        k = max(part)+1
        # Equivalence matrix.
        em = 0
        for i in range(n):
            for j in range(n):
                if part[i] == part[j]:
                    em |= 1 << (i*n+j)
        for lin in permutations(range(n)):
            rank = [0]*n
            for r,x in enumerate(lin): rank[x] = r
            l1 = 0
            for i in range(n):
                for j in range(n):
                    if rank[i] < rank[j]:
                        l1 |= 1 << (i*n+j)
            for qord in permutations(range(k)):
                qrank = [0]*k
                for r,b in enumerate(qord): qrank[b] = r
                l2 = 0
                for i in range(n):
                    for j in range(n):
                        if i == j: continue
                        if part[i] == part[j]:
                            less = rank[i] < rank[j]
                        else:
                            less = qrank[part[i]] < qrank[part[j]]
                        if less:
                            l2 |= 1 << (i*n+j)
                out.add((em,l1,l2))
    return out


def pullback(sig, k, eqpart, n):
    em,l1,l2 = sig
    eqm = E = L1 = L2 = 0
    for i in range(n):
        for j in range(n):
            pos = i*n+j
            vi,vj = eqpart[i],eqpart[j]
            if vi == vj: eqm |= 1 << pos
            if bit(em,k,vi,vj): E |= 1 << pos
            if bit(l1,k,vi,vj): L1 |= 1 << pos
            if bit(l2,k,vi,vj): L2 |= 1 << pos
    return (eqm,E,L1,L2)


def main():
    S = stirling_table(80)
    expected_a = [1,1,6,78,1800,64920]
    expected_b = [1,1,7,97,2311,84961]
    injective = {}
    for n in range(0,6):
        sigs = injective_signatures(n)
        injective[n] = sigs
        a = factorial(n)*fubini(n,S)
        assert len(sigs) == a == expected_a[n], (n,len(sigs),a)

    for n in range(0,6):
        all_sigs = set()
        if n == 0:
            all_sigs.add((0,0,0,0))
        else:
            for eqpart in partitions_rgs(n):
                k = max(eqpart)+1
                for sig in injective[k]:
                    all_sigs.add(pullback(sig,k,eqpart,n))
        b = sum(S[n][k] * factorial(k)*fubini(k,S) for k in range(n+1))
        assert len(all_sigs) == b == expected_b[n], (n,len(all_sigs),b)

    # Exact recurrence values and asymptotic approach.
    A=[]; B=[]
    for n in range(81):
        an=factorial(n)*fubini(n,S)
        bn=sum(S[n][k]*factorial(k)*fubini(k,S) for k in range(n+1))
        A.append(an); B.append(bn)
    target=1/sqrt(2)
    errs=[]
    for n in (20,40,80):
        r=A[n]/B[n]
        errs.append(abs(r-target))
    assert errs[2] < errs[1] < errs[0] < 0.02, errs
    assert errs[2] < 0.004, errs
    print("VERIFY_OK")

if __name__ == '__main__':
    main()
