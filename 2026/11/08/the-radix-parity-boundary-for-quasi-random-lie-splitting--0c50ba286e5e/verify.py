"""Exact reproducibility tests for a radical-inverse operator-ordering parity theorem.
The mathematical proof is in RESULT.md; this file supplies finite diagnostics only.
"""
from fractions import Fraction


def radical_inverse(n, base):
    value = Fraction(0)
    power = base
    while n:
        n, digit = divmod(n, base)
        value += Fraction(digit, power)
        power *= base
    return value


def xi(n, base):
    return 1 if radical_inverse(n, base) >= Fraction(1, 2) else -1


def source_sign_sum(n, base):
    return sum(xi(j, base) for j in range(1, n+1))


def witness_error(n, base, tau):
    # Exact 3x3 upper triangular products, represented by upper entries:
    # I + a*E12 + b*E23 + c*E13.
    a = b = c = Fraction(0)
    for j in range(1,n+1):
        # If xi=+1, Lie product exp(tau A)exp(tau B), else reversed.
        stepc = tau*tau if xi(j,base) == 1 else Fraction(0)
        # multiplication on left: (I+tA+tB+stepc*E13) (I+aA+bB+cE13)
        c = c + stepc + tau*b
        a += tau
        b += tau
    # exact exp(n tau (A+B)) E13 coefficient = (n tau)^2 /2.
    return abs(c - (n*tau)**2/Fraction(2))


def run():
    tests = 0
    for base in range(2,14):
        for n in range(0,151):
            s = source_sign_sum(n,base)
            if base % 2 == 0:
                m = base // 2
                assert xi(n+1,base) == (1 if (n+1)%base >= m else -1)
                assert abs(s) <= base
                tests += 2
            else:
                m = (base-1)//2
                if n < 90:
                    eta = lambda x: -1 if xi(x,base) == 1 else 1
                    assert eta(base*n + m) == eta(n)
                    assert sum(eta(base*n+j) for j in range(base)) == eta(n)
                    tests+=2
            if n <= 100:
                tau = Fraction(2, n+3)
                assert witness_error(n,base,tau) == tau*tau*abs(s)/2
                tests+=1
        if base%2:
            m=(base-1)//2
            for k in range(2,6):
                nk=m*(base**k-1)//(base-1)-1
                assert source_sign_sum(nk,base) == 1-m*k
                tests+=1
    print('VERIFY_OK exact rational tests:',tests)

if __name__=='__main__':
    run()
