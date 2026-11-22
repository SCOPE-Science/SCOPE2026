#!/usr/bin/env python3
"""Exact integer checks for Walsh convolution of path total-dominating sets.

No external packages. The infinite-size statements are established by the
mathematical proof; these computations independently test its finite cases.
"""

def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for base in range(0, len(a), 2*h):
            for j in range(base, base+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def fib(k):
    a,b=0,1
    for _ in range(k):
        a,b=b,a+b
    return a


def path_independent(m, x):
    return (x & (x << 1)) == 0


def independence_walsh(m):
    return fwht([int(path_independent(m, x)) for x in range(1 << m)])


def h_recurrence(m, w):
    """Signed sum over independent subsets, coordinate signs in w."""
    z_prev2 = 1  # Z_0
    if m == 0:
        return 1
    z_prev1 = 1 + (-1 if (w & 1) else 1)  # Z_1
    for j in range(1, m):
        t = -1 if ((w >> j) & 1) else 1
        z_prev2, z_prev1 = z_prev1, z_prev1 + t * z_prev2
    return z_prev1


def is_total_dominating(n, x):
    for i in range(n):
        if not ((i and ((x >> (i-1)) & 1)) or
                (i+1 < n and ((x >> (i+1)) & 1))):
            return False
    return True


def tds_walsh(n):
    return fwht([int(is_total_dominating(n,x)) for x in range(1<<n)])


def factored(n, w):
    """Walsh product evaluated from the two disjoint parity chains.
    Every coordinate appears once, even when an endpoint is forced.
    """
    odd = [(w>>i)&1 for i in range(0,n,2)]
    even = [(w>>i)&1 for i in range(1,n,2)]
    # For sign of full choice, followed by signs of excluded (zero) positions
    forced = []
    if n & 1:
        # Odd positions: no forced bits; even positions: both ends forced.
        free_odd = odd
        free_even = even[1:-1] if len(even)>=2 else []
        forced = [even[0]] + ([even[-1]] if len(even)>1 else [])
    else:
        # Odd positions: terminal forced; even positions: initial forced.
        free_odd = odd[:-1]
        free_even = even[1:]
        forced = [odd[-1], even[0]]
    def val(chain):
        mask = sum(bit<<i for i,bit in enumerate(chain))
        sign = -1 if sum(chain)%2 else 1
        return sign * h_recurrence(len(chain),mask)
    return (-1 if sum(forced)%2 else 1) * val(free_odd)*val(free_even)


def main():
    tests=0
    def check(value):
        nonlocal tests
        assert value, 'exact verification failed at check {}'.format(tests+1)
        tests += 1

    # Independent-set Fourier data from an exact FWHT and separate recurrence.
    for m in range(0,16):
        coeffs=independence_walsh(m)
        check(coeffs[0] == fib(m+2))
        for w,v in enumerate(coeffs):
            check(v == h_recurrence(m,w))
        resonance = (m%3==1)
        check((0 in coeffs) == resonance)
        gap = min(abs(v) for v in coeffs if v)
        check(gap == (2 if resonance else 1))
        check((h_recurrence(m,(1<<m)-1) == 0) if resonance else (abs(h_recurrence(m,(1<<m)-1)) == 1))
        if resonance:
            check(abs(h_recurrence(m, ((1<<m)-1) ^ 1)) == 2)

    # Independent distributional identity, all sign characters, through n=16.
    observed={}
    for n in range(2,17):
        v=tds_walsh(n)
        observed[n]=(len(v)-sum(x==0 for x in v),sum(x==0 for x in v))
        m=n//2
        expected_total=(fib(m+1)**2 if n%2==0 else fib(m+3)*fib(m))
        check(v[0] == expected_total)
        check((0 in v) == (n%3==1))
        check(min(abs(x) for x in v if x) == (4 if n%3==1 else 1))
        for w,x in enumerate(v):
            check(x==factored(n,w))
        if n%3==1:
            check(v[0]%4==0)
    check(observed[4] == (4,12))
    check(observed[7] == (44,84))
    check(observed[10] == (484,540))
    check(observed[13] == (4444,3748))

    # Third route: direct signed enumeration of total-dominating sets at small sizes.
    for n in range(2,9):
        masks=[x for x in range(1<<n) if is_total_dominating(n,x)]
        spectrum=tds_walsh(n)
        for w in range(1<<n):
            signed=sum(-1 if ((w&x).bit_count()%2) else 1 for x in masks)
            check(signed==spectrum[w])
    print('TOTAL_DOMINATION_WALSH_EXACT_PASS assertions={}'.format(tests))
    print('ranks/nullities n=4,7,10,13:',*[ (n,observed[n]) for n in (4,7,10,13)])

if __name__ == '__main__':
    main()
