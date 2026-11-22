#!/usr/bin/env python3
"""Exact rational certificate for a covariance-operator top eigenvalue.

No numerical integration, floating point, external dependencies, or finite-rank
spectral approximation is used to justify the eigenvalue bounds.
"""
from fractions import Fraction as Q


def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:
        p.pop()
    return tuple(p)


def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b)))])


def scale(a,c):
    return trim([c*z for z in a])


def sub(a,b):
    return add(a,scale(b,-1))


def mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):
            c[i+j]+=u*v
    return trim(c)


def primitive(a):
    return trim([Q(0)]+[v/Q(i+1) for i,v in enumerate(a)])


def at1(a):
    return sum(a,Q(0))


def integral(a):
    return at1(primitive(a))


def dot(a,b):
    return integral(mul(a,b))

ONE=(Q(1),)
X=(Q(0),Q(1))
W=(Q(1),Q(-4),Q(4))
A=(Q(0),Q(1),Q(-1))


def transform(f):
    # C f(s) = int_s^1 (2u-1)^2 (int_0^u f(t)dt)du
    #          - s(1-s) int_0^1 t(1-t) f(t)dt.
    h=primitive(mul(W,primitive(f)))
    return sub(sub((at1(h),),h),scale(A,dot(A,f)))


def check():
    assert W==mul((-Q(1),Q(2)),(-Q(1),Q(2)))
    assert integral(A)==Q(1,6) and dot(A,A)==Q(1,30)
    # Independent algebraic verification of the Hilbert-Schmidt trace:
    # Tr(C0^2) = 2 int_0^1 w(v) int_0^v w(u)u^2 du dv,
    # <a,C0 a> = int_0^1 w(u) [int_0^u a]^2 du.
    bare=2*integral(mul(W,primitive(mul(W,(Q(0),Q(0),Q(1))))))
    cross=integral(mul(W,mul(primitive(A),primitive(A))))
    tr2=bare-2*cross+dot(A,A)**2
    assert bare==Q(13,630)
    assert cross==Q(47,11340)
    assert tr2==Q(109,8100)

    f=ONE
    for j in range(5):
        f=transform(f)
        assert len(f)>0
    kf=transform(f)
    norm=dot(f,f)
    quotient=dot(f,kf)/norm
    residual2=dot(kf,kf)/norm-quotient**2
    assert norm>0 and residual2>0

    # The spectrum is nonnegative because C is a covariance operator.
    # lambda_1 >= quotient. Because sum_j lambda_j^2 = tr2,
    # lambda_2^2 <= tr2 - quotient^2 < (1/100)^2.
    assert tr2-quotient**2>0
    assert tr2-quotient**2<Q(1,10000)
    b=Q(1,100)
    assert quotient>b

    # Temple's inequality then yields lambda_1 <= quotient + r^2/(q-b).
    L=Q(11573423652792,10**14)
    U=Q(11573423652794,10**14)
    upper=quotient+residual2/(quotient-b)
    assert L<quotient<=upper<U
    print('EXACT CERTIFICATE PASSED')
    print('polynomial degree',len(f)-1)
    print('trace_C_squared =',tr2)
    print('Rayleigh_lower =',format(float(quotient),'.17g'))
    print('variance_residual =',format(float(residual2),'.12g'))
    print('Temple_upper =',format(float(upper),'.17g'))
    print('certified enclosure =',str(L),'< lambda_1 <',str(U))
    print('certificate exact rational comparisons: PASS')
    print('No claim is made about a closed-form expression for lambda_1.')

if __name__=='__main__':
    check()
