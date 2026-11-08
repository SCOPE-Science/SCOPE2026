"""Separate algorithmic finite checks for the dyadic complete-square Fourier norm.

Standard Python only.  The FFT, set construction, and recurrence are separate
implementations of the stated mathematical identities.  Finite tests do not
replace the proof for arbitrary depth.
"""
import cmath
import math


def squares(k):
    n = 1 << k
    return set((x*x) % n for x in range(n))


def s(k):
    if k < 1:
        raise ValueError('k must be positive')
    return ((1 << (k-1)) + (4 if k % 2 == 0 else 5)) // 3


def fft(vals):
    """Independent iterative radix-two FFT with negative exponential sign."""
    a = [complex(z) for z in vals]
    n = len(a)
    j = 0
    for i in range(1, n):
        b = n >> 1
        while j & b:
            j ^= b
            b >>= 1
        j ^= b
        if i < j:
            a[i], a[j] = a[j], a[i]
    m = 2
    while m <= n:
        root = cmath.exp(-2j*math.pi/m)
        for start in range(0, n, m):
            w = 1+0j
            for r in range(m//2):
                u = a[start+r]
                v = w*a[start+r+m//2]
                a[start+r] = u+v
                a[start+r+m//2] = u-v
                w *= root
        m *= 2
    return a


def delta(k):
    if k < 4:
        raise ValueError('delta used only for k >= 4')
    h = float(1 << (k-3))
    c = float(s(k-2))
    d = 0.0 if k == 4 else float(s(k-4) - (1 << (k-5)))
    even = 2*h+2*math.hypot(c,h)-4*c
    odd = 2*math.sqrt(d*d+h*h+math.sqrt(2)*d*h)
    odd += 2*math.sqrt(d*d+h*h-math.sqrt(2)*d*h)-4*abs(d)
    return (even+odd)/(1 << k)


def exact_norm(k):
    # Formula in RESULT.md is a two-step radical recurrence.
    if k == 1:
        return 1.0
    if k == 2:
        return (1+math.sqrt(2))/2
    if k == 3:
        return 1+math.sqrt(5)/4
    return exact_norm(k-2)+delta(k)


def slope_two_steps():
    return (2*math.sqrt(10)+math.sqrt(37-6*math.sqrt(2))
            +math.sqrt(37+6*math.sqrt(2)))/24


def check():
    previous = {}
    for k in range(1, 13):
        n = 1 << k
        q = squares(k)
        assert len(q) == s(k), (k, len(q), s(k))
        mask = [int(x in q) for x in range(n)]
        spectrum = fft(mask)
        actual = sum(abs(z) for z in spectrum)/n
        expected = exact_norm(k)
        assert abs(actual-expected) < 1e-8, (k,actual,expected)
        assert abs(sum(abs(z)**2 for z in spectrum)-n*len(q)) < 1e-6, k
        if k >= 3:
            old = previous[k-2]
            h = 1 << (k-3)
            for a, z in enumerate(spectrum):
                extra = h*cmath.exp(-2j*math.pi*a/n) if a % h == 0 else 0
                predicted = old[a%(n//4)]+extra
                assert abs(z-predicted) < 2e-7, (k,a,z,predicted)
        previous[k] = spectrum
        print('depth',k,'squares',len(q),'operator_norm',f'{actual:.12f}','PASS')
    C = slope_two_steps()
    assert abs(C-0.76703126959424948)<2e-14
    assert abs(exact_norm(30)-C*15-0.2915432524273311)<2e-8
    assert abs(exact_norm(31)-C*15.5-0.21970849728034743)<2e-8
    for k in range(5, 48):
        assert abs(delta(k)-C) <= (80/3)*2**(-k) + 5e-15
    print('dyadic slope',format(C/2,'.15f'),'PASS')
    print('DYADIC_SQUARE_WIENER_NORM_PASS')


if __name__ == '__main__':
    check()
