"""Independent direct-neighbor enumeration for binary majority on crown graphs."""
from collections import Counter
from math import comb


def update(n, state):
    nxt = 0
    for side in (0, 1):
        for i in range(n):
            v = side*n+i
            neighbors = [state >> ((1-side)*n+j) & 1 for j in range(n) if j != i]
            ones = sum(neighbors)
            d = n-1
            bit = int(2*ones > d) if 2*ones != d else (state >> v)&1
            nxt |= bit << v
    return nxt


def theorem(n):
    if n % 2 == 0:
        c = comb(n, n//2)
        return c+2, (c+2)*(c+1)//2, 1
    c = comb(n, (n-1)//2)
    return (n+3)*c+2, 1, 2 if n == 3 else 3


if __name__ == '__main__':
    for n in range(3, 9):
        fixed, cycles2, depth = theorem(n)
        fixed_meas, periodic_meas, max_depth = 0, 0, 0
        for x in range(1 << (2*n)):
            y=update(n, x)
            z=update(n, y)
            if y==x:
                fixed_meas+=1
            if z==x:
                periodic_meas+=1
            seq=[x]
            for _ in range(5):
                seq.append(update(n, seq[-1]))
            assert seq[5]==seq[3] if n%2 else seq[3]==seq[1]
            tau = next(t for t in range(4) if seq[t+2]==seq[t])
            max_depth=max(max_depth,tau)
        assert fixed_meas==fixed, (n,fixed_meas,fixed)
        assert (periodic_meas-fixed_meas)//2==cycles2
        assert max_depth==depth, (n,max_depth,depth)
        print(f'n={n}: fixed={fixed_meas}, primitive_2_cycles={cycles2}, maximal_entry={max_depth}')
    print('PASS')
