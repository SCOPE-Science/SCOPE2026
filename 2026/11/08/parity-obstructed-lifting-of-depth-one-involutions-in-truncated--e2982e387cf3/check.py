"""Exhaustive truncated-composition checks over binary fields.
Usage: python nottingham_depth1_check.py
"""
from itertools import product

def gf_mult(a, b, r, poly):
    out = 0
    for _ in range(r):
        if b & 1: out ^= a
        b >>= 1
        a <<= 1
        if a & (1 << r): a ^= poly
    return out

def square_series(a, n, mult):
    # a is [0,1,a2,...,an], compute f(f(t)) modulo t^(n+2).
    d = n + 1
    power = [0] * (d + 1)
    power[0] = 1
    total = [0] * (d + 1)
    for i in range(1, n + 1):
        nxt = [0] * (d + 1)
        for j, x in enumerate(power):
            if x:
                for k in range(1, min(n, d-j) + 1):
                    if a[k]: nxt[j+k] ^= mult[x][a[k]]
        power = nxt
        if a[i]:
            for j in range(1, d + 1):
                if power[j]: total[j] ^= mult[a[i]][power[j]]
    return total

def verify(r, polynomial, max_n):
    q = 1 << r
    mult = [[gf_mult(i,j,r,polynomial) for j in range(q)] for i in range(q)]
    for n in range(2,max_n+1):
        total = lifted = 0
        for coeff in product(range(q),repeat=n-2):
            for a2 in range(1,q):
                a = [0,1,a2,*coeff]
                comp = square_series(a,n,mult)
                if any(comp[j] != (1 if j == 1 else 0) for j in range(1,n+1)):
                    continue
                total += 1
                if comp[n+1] == 0:lifted += 1
        want = (q-1) * q**((n-1)//2)
        # For even n, the next odd obstruction is automatic; for odd n, exactly 1/q lift.
        want_lifted = want if n%2==0 else want//q
        assert (total,lifted)==(want,want_lifted), (q,n,total,lifted,want,want_lifted)
        print(f'q={q:2} N={n:2} depth1={total:7} lifts={lifted:7} PASS')

if __name__=='__main__':
    verify(1,0b11,10)
    verify(2,0b111,7)
    verify(3,0b1011,5)
    print('ALL_NOTTINGHAM_DEPTH_ONE_TESTS_PASS')
