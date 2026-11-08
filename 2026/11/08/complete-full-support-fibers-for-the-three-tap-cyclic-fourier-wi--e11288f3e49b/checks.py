"""Independent reproducibility checks for a three-tap cyclic Fourier fiber theorem.

The mathematical proof, not these finite experiments, establishes its all-order claim.
Run: python3 checks.py
"""
from cmath import exp, pi
from random import Random


def correlations(v):
    n = len(v)
    return [
        (
            abs(v[t]) ** 2 + abs(v[(t+1)%n]) ** 2 + abs(v[(t+2)%n]) ** 2,
            v[t]*v[(t+1)%n].conjugate()+v[(t+1)%n]*v[(t+2)%n].conjugate(),
            v[t]*v[(t+2)%n].conjugate(),
        )
        for t in range(n)
    ]


def samples(v):
    n=len(v)
    return [
        abs(v[t]+v[(t+1)%n]*exp(2j*pi*k/n)+v[(t+2)%n]*exp(4j*pi*k/n))**2
        for t in range(n) for k in range(n)
    ]


def close(x, y, tolerance=4e-9):
    assert abs(x-y) < tolerance, (x,y)


def test():
    # Exact Gaussian-rational calculation of all Fourier autocorrelation rows
    # for the period-two exceptional family (rho=1).
    A=complex(2,1)
    B=complex(3,-2)
    delta=(B*A.conjugate())/(A*B.conjugate())
    close(abs(delta),1)
    for m in (3,5,7,9):
        f=[A if t%2==0 else B for t in range(2*m)]
        h=[delta*value if t%2==0 else value for t,value in enumerate(f)]
        for row1,row2 in zip(correlations(f),correlations(h)):
            for v1,v2 in zip(row1,row2):close(v1,v2)
        for p1,p2 in zip(samples(f),samples(h)):close(p1,p2)

    # Exact rational arithmetic: δ=-1 yields literal integer complex
    # correlations; no floating-point simplifications are used.
    for m in (3,5,7,9):
        f=[2 if t%2==0 else 3j for t in range(2*m)]
        h=[-2 if t%2==0 else 3j for t in range(2*m)]
        assert correlations(f)==correlations(h)
        assert any(x!=y for x,y in zip(f,h))
        for p1,p2 in zip(samples(f),samples(h)): close(p1,p2)

    # Nontrivial mth roots of unity; tests are numerical only.
    for m in (3,5,7,9):
        rho=exp(2j*pi/m)
        A,B=2+1j,3-2j
        f=[]
        for j in range(m): f.extend((A*rho**j,B*rho**j))
        delta=(B*A.conjugate()*rho.conjugate())/(A*B.conjugate())
        h=[delta*z if t%2==0 else z for t,z in enumerate(f)]
        close(abs(delta),1)
        for p1,p2 in zip(samples(f),samples(h)):close(p1,p2)

    # A generic full-support signal does not share its measurements with
    # a nontrivial parity rephasing.
    rng=Random(270311)
    for n in (6,10,14,18):
        f=[complex(0.7+rng.random(),0.6+rng.random()) for _ in range(n)]
        h=[(1j if t%2==0 else 1)*z for t,z in enumerate(f)]
        assert max(abs(x-y) for x,y in zip(samples(f),samples(h)))>0.01

    # DFT of sample intensities indeed recovers the claimed 3 correlations.
    for n in (6,10,14):
        f=[complex(0.7+rng.random(),0.6+rng.random()) for _ in range(n)]
        rows=correlations(f)
        for t in range(n):
            w=[f[t],f[(t+1)%n],f[(t+2)%n]]
            powers=[abs(sum(w[j]*exp(2j*pi*k*j/n) for j in range(3)))**2 for k in range(n)]
            zero=sum(powers)/n
            # coefficient of positive powers = conjugate of C_1 and C_2
            lag1=sum(powers[k]*exp(2j*pi*k/n) for k in range(n))/n
            lag2=sum(powers[k]*exp(4j*pi*k/n) for k in range(n))/n
            close(zero,rows[t][0]);close(lag1,rows[t][1]);close(lag2,rows[t][2])
    print('THREE_TAP_FIBER_PASS exact_rows=48 root_periods=4 generic_controls=4 dft_checks=30')


if __name__=='__main__':test()
