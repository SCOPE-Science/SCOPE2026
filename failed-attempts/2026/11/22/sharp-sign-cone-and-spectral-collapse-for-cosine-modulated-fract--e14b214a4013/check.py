"""Independent exact and floating-point checks for cosine-modulated stable circle kernels.

Run: python check.py
Numerical tests support, but do not replace, the all-integer proof.
"""
from fractions import Fraction
from math import exp, isclose, log
import random

count = 0
rng = random.Random(20261117)

def verify(condition, text):
    global count
    count += 1
    if not condition:
        raise AssertionError(f'{count}: {text}')


def log_denominator(alpha, t, k, n):
    # D_n = u_{|n-k|}/u_n + u_{n+k}/u_n
    u = t*(n**alpha - abs(n-k)**alpha)
    v = t*(n**alpha - (n+k)**alpha)
    m = max(u,v)
    from math import log
    return m + log(exp(u-m)+exp(v-m))


def boundary(alpha, t, k):
    if alpha > 1:
        return 0.
    return -2*exp(-log_denominator(alpha,t,k,k))

# Verify one strict maximum at n=k for fractional stable exponents.
for alpha in [0.1,0.25,0.4,0.5,0.75,0.9,0.99]:
    for k in range(1,15):
        for t in [0.02,0.15,0.7,2.,4.]:
            d=[log_denominator(alpha,t,k,n) for n in range(0,5*k+100)]
            for n in range(k):
                verify(d[n] < d[n+1] + 1.e-12, f'pre-peak a={alpha},k={k},t={t},n={n}')
            for n in range(k,len(d)-1):
                verify(d[n] > d[n+1] - 1.e-12, f'post-peak a={alpha},k={k},t={t},n={n}')
            verify(all(d[n] < d[k]+1.e-11 for n in range(len(d)) if n!=k), 'unique maximizer')

# For alpha=1, the logarithmic ratio is strictly increasing below k, flat above it.
for k in range(1,20):
    for t in [0.02,.3,1.,3.]:
        d=[log_denominator(1.,t,k,n) for n in range(0,5*k+10)]
        for n in range(k):
            verify(d[n] < d[n+1] + 1e-11, 'Poisson pre-plateau')
        for n in range(k,len(d)-1):
            verify(isclose(d[n],d[n+1],abs_tol=5e-12,rel_tol=1e-12), 'Poisson plateau')

# Exact rational arithmetic certificate for the finite-rank Poisson boundary.
for q in [Fraction(1,2),Fraction(2,3),Fraction(3,4),Fraction(4,5)]:
    for k in range(1,20):
        b= -2*q**k/(1+q**(2*k))
        for n in range(0,4*k+5):
            c = q**n + b*(q**abs(n-k)+q**(n+k))/2
            if n < k:
                exact=(q**n-q**(2*k-n))/(1+q**(2*k))
                verify(c == exact, f'nonzero coefficient n={n},k={k},q={q}')
                verify(c > 0, 'positive low coefficient')
            else:
                verify(c==0, f'vanishing tail n={n},k={k},q={q}')

# Test the proposed coefficient boundary against independent direct Fourier convolution.
for _ in range(6000):
    k=rng.randrange(1,11)
    alpha=rng.choice([.15,.4,.7,.9,1.,1.3,1.7])
    t=rng.uniform(.04,1.1)
    n=rng.randrange(0,90)
    b=boundary(alpha,t,k)
    # Convolution formula verified against Fourier mass at n and the spectral inequality.
    # Work with normalized coefficient to avoid underflow.
    u=t*(n**alpha-abs(n-k)**alpha)
    v=t*(n**alpha-(n+k)**alpha)
    rel=1+b*(exp(u)+exp(v))/2
    if alpha<1 and n!=k:
        verify(rel>-2e-11, f'alpha<1 wrong sign: {alpha},{t},{k},{n},{rel}')
    elif alpha<1 and n==k:
        verify(abs(rel)<1e-11, 'missing frequency')
    elif alpha==1:
        if n>=k: verify(abs(rel)<1e-11,'Poisson tail')
        else: verify(rel>0, 'Poisson low frequency')
    elif alpha>1:
        verify(rel == 1, 'classical high-exponent b=0')

# For alpha>1, a negative modulation eventually forces a negative coefficient.
for alpha in [1.3,1.5,2.]:
    for t in [.3,.6,1.]:
        for k in [1,2,3,8]:
            for negative_b in [-.2,-2.]:
                N=2
                while N<10_000 and log_denominator(alpha,t,k,N) < log(2.0/(abs(negative_b))):
                    N*=2
                verify(N<10_000, f'find negative Fourier mode a={alpha},k={k},t={t}')
                verify(log_denominator(alpha,t,k,N)>-1.e-12,f'positive log D a={alpha},t={t},k={k},b={negative_b},n={N},D={log_denominator(alpha,t,k,N)}')

print('PASS', count, 'assertions (exact rational and finite numerical)')
