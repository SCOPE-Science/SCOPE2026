"""Reproducible rational checks for alternating-step BDF3 Floquet identities.

The universal assertions in the accompanying theorem have separate analytic proofs.
This program performs exact coefficient checks and numerical root isolation.
Requires only Python's standard library.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext


def derivative_weights(nodes):
    """Solve the Vandermonde conditions for first-derivative interpolation."""
    a = [[x**k for x in nodes] + [F(int(k == 1))] for k in range(4)]
    for j in range(4):
        pivot = next(i for i in range(j, 4) if a[i][j])
        a[j], a[pivot] = a[pivot], a[j]
        v = a[j][j]
        a[j] = [z / v for z in a[j]]
        for i in range(4):
            if i != j:
                u = a[i][j]
                a[i] = [x - u*y for x, y in zip(a[i], a[j])]
    return [a[i][-1] for i in range(4)]


def coefficients(r):
    denom = 5*r*r + 5*r + 1
    return r*r*(4*r+3)/denom, -r*(r+1)/denom


def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def transfer(r):
    a,b = coefficients(r)
    return [[a,b],[F(1),F(0)]]


def spectral_invariants(r):
    q = r + 1/r
    d = 5*q*q+30*q+41
    return (-q*q+q+7)/d, (q+2)/d


def quartic(q):
    return q**4 - 22*q**3 - 173*q*q - 390*q - 279


def check():
    count = 0
    ratios = [F(1), F(2), F(1,2), F(3), F(1,3), F(30), F(1,30),
              F(10**5), F(1,10**5), F(7,11), F(19,17)]
    for r in ratios:
        nodes = [F(0),-F(1),-1-1/r,-2-1/r]
        w0,w1,w2,w3 = derivative_weights(nodes)
        assert sum((w0,w1,w2,w3)) == 0
        assert w0 == (5*r*r+5*r+1)/((r+1)*(2*r+1))
        assert w1 == -2*r-1
        assert w2 == r*(2*r+1)/(r+1)
        assert w3 == -r/(2*r+1)
        a,b = coefficients(r)
        assert a == (w2+w3)/w0
        assert b == w3/w0
        matrix = matmul(transfer(1/r),transfer(r))
        tr = matrix[0][0]+matrix[1][1]
        det = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        tt,dd = spectral_invariants(r)
        assert tr == tt
        assert det == dd
        assert spectral_invariants(r) == spectral_invariants(1/r)
        q = r+1/r
        D = 5*q*q+30*q+41
        assert 1-25*det == (5*q*q+5*q-9)/D > 0
        assert 1-5*tr+25*det == (10*q*q+50*q+56)/D > 0
        assert 1+5*tr+25*det == (60*q+126)/D > 0
        count += 13
    for q in [F(2),F(3),F(5),F(29),F(10000)]:
        assert (5*q*q+30*q+41) > 0
        assert -(5*q*q+20*q+19) < 0
        assert -(35*q*q+152*q+169) < 0
        count += 3
    assert quartic(F(2)) < 0
    assert quartic(F(2855,100)) < 0
    assert quartic(F(28551,1000)) > 0
    count += 3
    with localcontext() as ctx:
        ctx.prec = 70
        a,b = Decimal('28.55'), Decimal('28.551')
        for _ in range(240):
            m = (a+b)/2
            if quartic(m) > 0:
                b = m
            else:
                a = m
        q=(a+b)/2
        r=(q+(q*q-4).sqrt())/2
        rho=((q+2)/(5*q*q+30*q+41)).sqrt()
        assert Decimal('28.5149315928') < r < Decimal('28.5149315930')
        assert Decimal('0.0783782974') < rho < Decimal('0.0783782976')
        print('q_critical:',q)
        print('r_optimal:',r)
        print('Floquet_minimum:',rho)
        count += 2
    print('EXACT_AND_INTERVAL_CHECKS_PASSED:',count)


if __name__ == '__main__':
    check()
