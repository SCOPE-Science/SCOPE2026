"""Reproducibility checks for cyclic length-three hard-rod diffraction.

Uses Python's standard library only. All reported comparisons are finite
checks; the infinite-limit argument is mathematical, not numerical.
"""
from math import comb, cos, sin, pi, factorial
from cmath import exp
from fractions import Fraction


def count_exact(n, k):
    if k == 0: return 1
    if k > n // 3: return 0
    return n * comb(n - 2*k - 1, k - 1) // k


def admissible(mask, n):
    return all(not ((mask >> i) & 1 and ((mask >> ((i+1) % n)) & 1 or
                                        (mask >> ((i+2) % n)) & 1)) for i in range(n))


def partition_and_pairs(n, z):
    # Exact weighted sums of cyclic configurations.
    weights = [count_exact(n, k) * z**k for k in range(n//3+1)]
    Z = sum(weights)
    rho = Fraction(sum(k * weights[k] for k in range(len(weights))), n * Z)
    U = [0] * (n+1)
    U[3] = 1
    for d in range(4, n+1): U[d] = U[d-1] + z*U[d-3]
    pair = [rho] + [Fraction(z*z*U[d]*U[n-d], Z) for d in range(1, n)]
    return Z, rho, pair


def intensity_from_pairs(n, z, j):
    Z, rho, pair = partition_and_pairs(n, z)
    # The mean Fourier amplitude vanishes at all nonconstant frequencies.
    assert j % n
    return sum(float(pair[d])*cos(2*pi*j*d/n) for d in range(n)) / n


def spectral_bruteforce(n, z, j):
    Z, total = 0, 0.0
    for mask in range(1<<n):
        if not admissible(mask, n): continue
        k = mask.bit_count(); w = z**k
        T = sum(exp(2j*pi*j*l/n) for l in range(n) if (mask >> l)&1)
        Z += w
        total += w*(T.real*T.real + T.imag*T.imag)
    return Z, total/(Z*n*n)


def profile(c, j, num=15, subdivisions=3200):
    # Taylor series H_0(v)=sum_{r>=0}v^(3r)/(3r)!, composed with a
    # finite interval integral. Midpoint quadrature approximates its value.
    u = (27*c)**(-1/3)
    H0 = lambda v: sum(v**(3*r)/factorial(3*r) for r in range(num))
    if j == 0:
        H1 = sum(u**(3*r)/factorial(3*r+1) for r in range(num))
        return H1/(9*H0(u))
    omega=exp(2j*pi/3)
    w=0j
    for i in range(subdivisions):
        t=(i+0.5)/subdivisions
        w+=(1-t)*exp(2j*pi*j*t)*H0(u*(1-t+t*omega))
    return (2*w.real)/(9*H0(u)*subdivisions)


def finite_profile(m,c,j):
    # Exact weighted pair probabilities; evaluates a finite-volume harmonic.
    n=3*m; z=round(c*n**3)
    return intensity_from_pairs(n,z,m+j)


def main():
    tests=0
    for n in range(6,16):
        for z in (1,2):
            brute_counts = [0]*(n//3+1)
            for mask in range(1<<n):
                if admissible(mask,n): brute_counts[mask.bit_count()]+=1
            assert brute_counts == [count_exact(n,k) for k in range(n//3+1)]
            tests+=1
            Z, rho, pair = partition_and_pairs(n,z)
            assert Z == sum(brute_counts[k]*z**k for k in range(len(brute_counts)))
            for j in range(1,min(n,5)):
                Z2, value = spectral_bruteforce(n,z,j)
                assert Z==Z2
                assert abs(value-intensity_from_pairs(n,z,j))<2e-12, (n,z,j,value,intensity_from_pairs(n,z,j))
                tests+=1
    for c in (0.1,1.0,10.0):
        for j in (0,1,2):
            pred=profile(c,j)
            v1=finite_profile(12,c,j)
            v2=finite_profile(24,c,j)
            v3=finite_profile(48,c,j)
            assert abs(v3-pred)<abs(v1-pred)*0.44+3e-6, (c,j,pred,v1,v3)
            assert abs(v3-pred)<abs(v2-pred)*0.72+3e-6, (c,j,pred,v2,v3)
            assert pred>=-1e-10
            tests+=1
            print('c=%.2g offset=%d asymptotic=%.12g finite(n=36,72,144)=(%.12g, %.12g, %.12g)' % (c,j,pred,v1,v2,v3))
    assert abs(profile(1e8,0)-1/9)<1e-8
    assert abs(profile(1e-6,0)/((1/3)*1e-2)-1)<0.07
    tests+=2
    print('PASS',tests,'finite assertions')

if __name__=='__main__': main()
