"""Exact-arithmetic finite checks for a theorem on consecutive squared cobalancing numbers.

The infinite proof is in RESULT.md. Python 3 standard library only.
"""
from math import gcd


def pell_arrays(n):
    p = [0, 1]
    q = [1, 1]
    for _ in range(n - 1):
        p.append(2*p[-1] + p[-2])
        q.append(2*q[-1] + q[-2])
    return p, q


def g_all(values):
    g = 0
    for z in values:
        g = gcd(g, z)
    return g


def formula(k, p, q):
    if k % 2:
        d = q[k] * gcd((3*p[k]-1)//2, 7)
        t = 5*k
    else:
        d = (p[k]//2) * gcd((q[k]-1)//2, 14)
        t = 5*k//2
    return 4*gcd(d, t), d


def run():
    limit = 500
    p, q = pell_arrays(4*limit + 300)
    u = [0, 0]
    b = [0, 0]
    for _ in range(limit+100):
        u.append(6*u[-1] - u[-2] + 1)
        b.append(6*b[-1] - b[-2] + 2)
    a = [z*z for z in u]
    assert all(b[n] == 2*u[n] for n in range(len(u)))
    assert all(4*u[n]+1 == p[2*n-1] for n in range(1, len(u)))

    prefix = [0]
    for x in a:
        prefix.append(prefix[-1] + x)

    for k in range(1, limit+1):
        target, d_target = formula(k, p, q)
        diff_g = g_all(a[n+k] - a[n] for n in range(0, 12))
        assert diff_g == d_target, ("period-difference", k, diff_g, d_target)
        s_g = g_all(prefix[n+k+1]-prefix[n+1] for n in range(0, 12))
        assert 4*s_g == target, ("window-gcd", k, 4*s_g, target)
        # Exact Pell summation identity, for multiple starting indices.
        for n in (0, 1, 2, 4, 7):
            v = p[4*(n+k)]-p[4*n]-16*(p[2*(n+k)]-p[2*n])+20*k
            assert v % 256 == 0
            assert v//256 == prefix[n+k+1]-prefix[n+1]

    for r in range(2, 9):
        h = 2**r
        for n in range(0, 80):
            assert (u[n+h]-u[n]-2**(r-1)) % 2**r == 0
        s_h = prefix[h+1]-prefix[1]
        assert s_h % 2**r == 2**(r-1)
        for odd_m in (1, 3, 5, 7):
            k = h*odd_m
            if k + 1 < len(prefix):
                s = prefix[k+1]-prefix[1]
                assert s % 2**r == 2**(r-1)

    print("VERIFY_OK k=1..500 gcd_windows=6000 gcd_differences=6000")
    print("PELL_SUM_IDENTITY_OK samples=2500")
    print("DYADIC_SHIFT_OK r=2..8 n=0..79")
    print("EXAMPLES", {k: formula(k,p,q)[0] for k in (1,3,4,6,8,12,21,24,30,42,60)})

if __name__ == '__main__':
    run()
