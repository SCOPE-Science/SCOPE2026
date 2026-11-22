"""Exact arithmetic tests for cyclic sinc-power Fourier symbols.

Every rational represents an angle divided by pi. No floating point is used
for the spectral identities or nullity comparisons.
"""
from fractions import Fraction as F
from math import factorial, comb, ceil


def positive_part(x):
    return x if x > 0 else F(0)


def b_spline_symbol(p, r, t):
    """2pi times the wrapped p-fold uniform density at theta=pi*t,
    with each uniform law supported on [-pi*r/p,pi*r/p].
    """
    a = r / p
    result = F(0)
    # The support of the unfolded convolution is [-r,r].
    for ell in range(-3, 4):
        x = t + 2*ell
        if abs(x) >= r:
            continue
        z = x + r
        total = sum((-1)**j*comb(p,j)*positive_part(z-2*a*j)**(p-1)
                    for j in range(p+1))
        result += total
    return 2*result/(factorial(p-1)*(2*a)**p)


def samples(p,N,r):
    return [b_spline_symbol(p,r,F(2*k,N)) for k in range(N)]


def nullity(p,N,r):
    return sum(z==0 for z in samples(p,N,r))


def predicted_nullity(N,r):
    assert 0<r<=1
    q=F(N)*r/2
    return N+1-2*((q.numerator+q.denominator-1)//q.denominator)


def predicted_min(p,N,r):
    a=r/F(p)
    eps=r-1
    delta=F(0) if N%2==0 else F(1,N)
    constant = F(2,1)/(factorial(p-1)*(2*a)**p)
    return constant*(positive_part(eps+delta)**(p-1)+positive_part(eps-delta)**(p-1))


def run():
    total=0
    cutoff_cases=0
    crossover_cases=0
    for p in range(2,11):
        for N in range(2,33):
            for r in [F(1,4),F(2,5),F(3,5),F(3,4),F(4,5),F(9,10),F(19,20), F(1),F(21,20),F(11,10),F(6,5),F(5,4),F(7,5)]:
                spectrum=samples(p,N,r)
                assert all(v>=0 for v in spectrum), (p,N,r,'nonpositive')
                # A symmetric-unimodal symbol is minimized at a Nyquist-nearest mode.
                k=N//2
                assert spectrum[k]==min(spectrum), (p,N,r,k,spectrum[k],min(spectrum))
                if r<=1:
                    assert sum(x==0 for x in spectrum)==predicted_nullity(N,r),(p,N,r,'nullity')
                    cutoff_cases+=1
                eps=r-1
                delta=F(0) if N%2==0 else F(1,N)
                if abs(eps)+delta <= 2*r/p and abs(eps)<=F(1,4):
                    assert spectrum[k]==predicted_min(p,N,r),(p,N,r,'crossover')
                    crossover_cases+=1
                total+=1
    print(f'PASS: {total} exact rational spectra, {cutoff_cases} rank comparisons, {crossover_cases} exact edge/crossover comparisons.')
    for p in range(2,9):
        for N in [p+1 if (p+1)%2 else p+2, 2*p+1, 4*p+1]:
            got=min(samples(p,N,F(1)))
            target=F(p**p, 2**(p-1)*factorial(p-1)*N**(p-1))
            assert got==target,(p,N,got,target)
    print('PASS: 21 critical-width odd-cycle exact gap comparisons.')

if __name__=='__main__':run()
