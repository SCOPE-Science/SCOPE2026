#!/usr/bin/env python3
"""Finite consistency checks for added-chord hypercube parity dynamics.

Uses bit-packed independent matrix arithmetic; not a proof of the all-dimension theorem.
"""
from collections import Counter


def rank(rows):
    pivots = {}
    for row in rows:
        while row:
            bit = row.bit_length() - 1
            if bit in pivots:
                row ^= pivots[bit]
            else:
                pivots[bit] = row
                break
    return len(pivots)


def multiply(A, B):
    result = []
    for row in A:
        total = 0
        while row:
            low = row & -row
            total ^= B[low.bit_length()-1]
            row ^= low
        result.append(total)
    return result


def matrix(d, r):
    size = 1 << d
    v = (1 << r) - 1
    rows = []
    for x in range(size):
        row = 0
        for i in range(d):
            row ^= 1 << (x ^ (1 << i))
        if x == 0:
            row ^= 1 << v
        if x == v:
            row ^= 1
        rows.append(row)
    return rows


def fixed_dimension(B, t):
    I = [1 << i for i in range(len(B))]
    P = I
    for _ in range(t):
        P = multiply(P, B)
    return len(B) - rank([a ^ b for a,b in zip(P,I)])


def first_periodic_entry(B, depth):
    size = len(B)
    P = [1 << i for i in range(size)]
    ans = []
    for _ in range(depth+1):
        if depth == 0:
            # Every state is recurrent under the invertible map.
            ans.append(1 << size)
        else:
            # Number with B^(t+2)x=B^t x. This counts entry by time t.
            B2 = multiply(B, B)
            diff = multiply(P, [a ^ b for a,b in zip(B2,[1<<i for i in range(size)])])
            ans.append(1 << (size-rank(diff)))
        P = multiply(P,B)
    return ans


def main():
    for d in range(3,8):
        N = 1 << d
        identity = [1 << i for i in range(N)]
        for r in range(2,d+1):
            B = matrix(d,r)
            powers=[identity]
            for k in range(1,7):
                powers.append(multiply(powers[-1],B))
            if d % 2:
                assert powers[6] == identity
                assert [fixed_dimension(B,t) for t in (1,2,3,6)] == [N//2-2,N-4,N//2,N]
                assert rank(B) == N
                assert powers[3] != identity
                assert rank([a^b for a,b in zip(powers[2],identity)])==4
            else:
                assert rank(B) == N//2+2
                assert [rank(powers[t]) for t in range(1,5)] == [N//2+2,4,2,2]
                assert powers[5] == powers[3]
                assert powers[4] != powers[3]
                assert first_periodic_entry(B,3) == [4, 1 << (N//2), 1 << (N-2), 1 << N]
            print(f"matrix d={d} chord_distance={r} PASS")
    # Independent exhaustive state evolution on Q3 and Q4.
    for d in (3,4):
        N = 1 << d
        total = 1 << N
        for r in range(2,d+1):
            B = matrix(d,r)
            def step(x):
                y = 0
                for i,row in enumerate(B):
                    y |= ((row & x).bit_count() & 1) << i
                return y
            by_entry = Counter()
            by_primitive = Counter()
            for x in range(total):
                encountered = {}
                orbit=[]
                s=x
                while s not in encountered:
                    encountered[s] = len(orbit)
                    orbit.append(s)
                    s=step(s)
                entry=encountered[s]
                period=len(orbit)-entry
                by_entry[entry]+=1
                if entry == 0:
                    by_primitive[period]+=1
            if d%2:
                assert by_entry == Counter({0: total})
                assert by_primitive == Counter({1:2**(N//2-2),2:2**(N-4)-2**(N//2-2),3:2**(N//2)-2**(N//2-2),6:total-2**(N-4)-2**(N//2)+2**(N//2-2)})
            else:
                assert by_entry == Counter({0:4,1:2**(N//2)-4,2:2**(N-2)-2**(N//2),3:3*2**(N-2)})
                assert by_primitive == Counter({1:2,2:2})
            print(f"exhaustive d={d} chord_distance={r}: {total} states PASS, entry={dict(by_entry)}, periodic_points={dict(by_primitive)}")
    print('ALL CHECKS PASSED')

if __name__ == '__main__':
    main()
