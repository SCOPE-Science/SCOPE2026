"""Exact-rational checks of the two-leakage-mode spectral formulas.

This finite checker verifies algebraic identities and sample orderings; the
all-parameter assertions are established analytically in RESULT.md.
"""
from fractions import Fraction as F


def spectral(a, u, delta):
    assert 0 < a < 1 and 0 < u < 1 and 0 < delta < 1-a
    b1 = 1 - (1-a)*u
    b2 = (1-delta)*(1-u)
    dc = a*(1-a)*u/b1
    nu1 = (1-(1-a*a)*u)/b1
    nu2 = 1-delta
    assert b1-b2 == a*u+delta*(1-u)
    assert b1 > b2 > 0
    assert nu1 == 1-dc
    assert nu2 - nu1 == dc-delta
    assert 0 < dc < (1-a)*u
    # Nystrom's second mode has exactly e3 as unit eigenvector.
    assert nu2 == (1-delta)**2*(1-u)/b2
    # On its first-mode branch the exact squared angle to e1 is:
    sn2 = a*a*u/(1-u+a*a*u)
    assert 0 < sn2 < u
    if delta < dc:
        assert nu2 > nu1 and delta < (1-a)*u
    elif delta > dc:
        assert nu1 > nu2
    else:
        assert nu1 == nu2


def check_original_matrix():
    # A fully rational 4-by-4 calculation, not merely scalar formulas.
    a, u, delta = F(1, 2), F(9, 25), F(9, 200)
    c, s = F(4, 5), F(3, 5)
    q1 = [c, s, F(0), F(0)]
    q2 = [F(0), F(0), c, s]
    diag = [F(1), a, 1-delta, F(0)]
    dot = lambda x, y: sum(xi*yi for xi,yi in zip(x,y))
    assert dot(q1,q1) == dot(q2,q2) == 1 and dot(q1,q2) == 0
    Aq1=[xi*di for xi,di in zip(q1,diag)]
    Aq2=[xi*di for xi,di in zip(q2,diag)]
    b1,b2=dot(q1,Aq1),dot(q2,Aq2)
    N=[[Aq1[i]*Aq1[j]/b1+Aq2[i]*Aq2[j]/b2
        for j in range(4)] for i in range(4)]
    matvec=lambda v: [dot(row,v) for row in N]
    nu1=dot(Aq1,Aq1)/b1
    nu2=dot(Aq2,Aq2)/b2
    assert matvec(Aq1)==[nu1*x for x in Aq1]
    assert matvec([F(0),F(0),F(1),F(0)])==[F(0),F(0),nu2,F(0)]
    assert nu2>nu1 and b1>b2
    assert dot(q1,[F(1),F(0),F(0),F(0)])==c
    assert (1-b1)/(1-nu2)==4


def run():
    check_original_matrix()
    tested = 0
    for ai in range(1, 10):
        a = F(ai, 10)
        for ui in range(1, 20):
            u = F(ui, 20)
            dc = a*(1-a)*u/(1-(1-a)*u)
            for ratio in [F(1, 4), F(1, 2), F(1), F(3, 2), F(2)]:
                delta = dc*ratio
                if delta >= 1-a:
                    continue
                spectral(a, u, delta)
                tested += 1
    for j in range(1, 101):
        u=F(j, 101)
        a=F(1, 2)
        delta=u/8
        spectral(a,u,delta)
        assert delta < u/(4-2*u)
        assert ((1-a)*u)/delta == 4
        tested += 1
    print('PASS: %d exact rational parameter instances and strict branch checks' % tested)


if __name__ == '__main__':
    run()
