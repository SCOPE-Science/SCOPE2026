#!/usr/bin/env python3
"""Independent vertex-level exhaustive check for small labelled triangular tubes."""
REFERENCE = {3:102, 4:188, 5:510, 6:2918, 7:9240}

def count(n):
    adj=[]
    for i in range(n):
        for j in range(3):
            adj.append((3*((i-1)%n)+j, 3*((i+1)%n)+j,
                        3*i+(j+1)%3, 3*i+(j+2)%3))
    masks=[sum(1<<z for z in nbrs) for nbrs in adj]
    fixed = 0
    for state in range(1<<(3*n)):
        ok = True
        for v,mask in enumerate(masks):
            ones = (state & mask).bit_count()
            bit = (state>>v) & 1
            # Direct application of the opposite-neighborhood minority vote.
            nextbit = (1 if ones < 2 else 0 if ones > 2 else bit)
            if nextbit != bit:
                ok = False
                break
        if ok:
            fixed += 1
    return fixed

for n, expected in REFERENCE.items():
    got = count(n)
    assert got == expected, (n, got, expected)
    print(f'length={n} configurations={1<<(3*n)} fixed={got} PASS')
print('Exhaustive direct synchronous update check: PASS')
