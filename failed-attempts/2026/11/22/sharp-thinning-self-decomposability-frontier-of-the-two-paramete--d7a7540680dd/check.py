"""Exact-rational checks for a generalized Lindley count law and thinning innovations.
Scientific reproduction only; no external dependencies other than Python stdlib.
"""
from fractions import Fraction as Q


def critical(theta):
    return (1+theta)**3/(theta*(theta+2)**2)


def ratio(theta):
    return Q(1)/(1+theta),Q(1)/(2+theta)


def scaled_a(c,t):
    return c*t/(1-c+c*t)


def coefficient(theta,alpha,t,k):
    q,r=ratio(theta)
    qt,rt=scaled_a(q,t),scaled_a(r,t)
    return (alpha*(q**k-qt**k)-(r**k-rt**k))/k


def canonical(theta,alpha,k):
    q,r=ratio(theta)
    return alpha*q**(k+1)-r**(k+1)


def assert_canonical(theta,alpha,upto=25):
    q,r=ratio(theta)
    for k in range(upto):
        assert canonical(theta,alpha,k)>0
        direct=(alpha*q**(k+1)*(1-q)-r**(k+1)*(1-r))
        assert canonical(theta,alpha,k)-canonical(theta,alpha,k+1)==direct
    return None


if __name__=='__main__':
    theta=Q(1,4)
    ac=critical(theta)
    assert ac==Q(125,81)
    assert critical(Q(1))==Q(8,9)
    # At the sharp boundary, the first two canonical terms tie, others decrease.
    assert canonical(theta,ac,0)==canonical(theta,ac,1)
    assert_canonical(theta,ac)
    for k in range(1,26):
        assert coefficient(theta,ac,Q(99,100),k)>=0
    # Subcritical parameters violate the innovation PGF at a valid thinning rate.
    alpha_bad=Q(6,5)
    assert Q(1)<alpha_bad<ac
    assert coefficient(theta,alpha_bad,Q(99,100),1)<0
    # Sufficient side has positive innovations in several exact tests.
    for theta in [Q(1,10),Q(1,4),Q(1,2),Q(1),Q(7,2)]:
        for alpha in [max(Q(11,10),critical(theta)), max(Q(11,10),critical(theta))+1]:
            assert_canonical(theta,alpha)
            for t in [Q(1,10),Q(1,2),Q(9,10),Q(99,100)]:
                for k in range(1,31):
                    assert coefficient(theta,alpha,t,k)>0
    # Rational WNBL overlap: beta=7/10, p=49/51 and (alpha, theta)=(17/10,2/49).
    theta_overlap=Q(2,49)
    alpha_overlap=Q(17,10)
    beta_overlap=Q(7,10)
    p_overlap=Q(49,51)
    q_overlap,r_overlap=ratio(theta_overlap)
    assert q_overlap==p_overlap
    assert r_overlap==p_overlap*(1-beta_overlap**2)==Q(49,100)
    assert alpha_overlap==1+beta_overlap
    assert critical(theta_overlap)==Q(132651,20000)>alpha_overlap
    overlap_first=coefficient(theta_overlap,alpha_overlap,Q(1,2),1)
    assert overlap_first==Q(-249361,2400900)
    # For any alpha>1 the law is always compound-Poisson, irrespective of thinning property.
    for theta in [Q(1,10),Q(1,4),Q(1),Q(3)]:
        q,r=ratio(theta)
        for alpha in [Q(11,10),Q(2),Q(4)]:
            for k in range(1,32):
                assert (alpha*q**k-r**k)>0
    print('PASS: all exact checks; threshold(1/4)=125/81; subcritical innovation first log coefficient negative')
