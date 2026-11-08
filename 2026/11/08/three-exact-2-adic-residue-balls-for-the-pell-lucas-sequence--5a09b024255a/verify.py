#!/usr/bin/env python3
"""Independent exact modular checks for the Pell--Lucas support theorem."""

def expected(modulus):
    return {x for x in range(modulus) if x % 16 in (2, 14) or x % 64 == 6} if modulus >= 64 else {
        x % modulus for x in range(64) if x % 16 in (2, 14) or x % 64 == 6
    }

def actual_image(k):
    mod = 1 << k
    q0 = q1 = 2 % mod
    pairs = set()
    image = set()
    while (q0, q1) not in pairs:
        pairs.add((q0, q1))
        image.add(q0)
        q0, q1 = q1, (2 * q1 + q0) % mod
    assert (q0, q1) == (2 % mod, 2 % mod)
    return image, len(pairs)

def x_at(n,mod):
    x0 = x1 = 1
    for _ in range(n):
        x0, x1 = x1, (2*x1+x0) % mod
    return x0 % mod

def main():
    tested_indices = 0
    for k in range(1,15):
        m=1<<k
        got, period=actual_image(k)
        want=expected(m)
        assert got==want,(k,got^want)
        assert len(want)==([1,1,2,3,5][k-1] if k<=5 else 9*(1<<(k-6)))
        assert (1<<k)==m
        if k <= 10:
            u=1 << max(0,k-3)
            x=[x_at(i,m) for i in range(4*u+5)]
            if k>=3:
                for offset,base in ((1,1),(3,7)):
                    values={x[4*t+offset] for t in range(u)}
                    assert values=={v for v in range(m) if v%8==base}
                    for t in range(1,u):
                        assert ((x[4*t+offset]-x[offset]) % m) % (8*(t&-t))==0
                tested_indices+=4*u+5
    for j in range(1,12):
        m=1<<j
        vals={(z+4*z*z)%m for z in range(m)}
        assert len(vals)==m
    print('VERIFY_OK levels=1..14 all_cycle_images=PASS three_balls=PASS counts=PASS odd_subsequences=PASS quadratic_bijections=PASS sample_indices=',tested_indices)
if __name__=='__main__': main()
