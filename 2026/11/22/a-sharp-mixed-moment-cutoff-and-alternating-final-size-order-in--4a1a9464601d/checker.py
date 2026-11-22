"""Exact finite-support tests and supplementary epidemic root checks."""
from fractions import Fraction as Q
from math import exp, expm1


def barycentric(xs):
    return [Q(1, 1) / product(xs[i] - xs[j] for j in range(len(xs)) if i != j) for i in range(len(xs))]


def product(values):
    result = Q(1)
    for value in values:
        result *= value
    return result


def roots(xs, mass, kappa):
    xs = [float(x) for x in xs]
    mass = [float(v) for v in mass]
    def g(t):
        return kappa * sum(u * (-expm1(-x*t)) for x, u in zip(xs, mass)) - t
    assert kappa * sum(x*u for x, u in zip(xs, mass)) > 1
    lo, hi = 0., kappa * sum(mass) + 1.
    assert g(hi) < 0
    for _ in range(130):
        mid = (lo + hi)/2
        if g(mid)>0:
            lo=mid
        else:
            hi=mid
    t=(lo+hi)/2
    return t, 1-sum(exp(-x*t) for x in xs)/len(xs)


def moment(xs, us, j):
    return sum((u*x**j for x,u in zip(xs,us)),Q(0))


def main():
    xs = [Q(1, 2), Q(1), Q(3, 2)]
    p=[Q(1,3)]*3
    qa=[Q(5,8),Q(1,4),Q(5,8)]
    qb=[Q(3,8),Q(3,4),Q(3,8)]
    ua=[p[i]*(Q(1,2)+qa[i]) for i in range(3)]
    ub=[p[i]*(Q(1,2)+qb[i]) for i in range(3)]
    assert ua == [Q(3,8),Q(1,4),Q(3,8)]
    assert ub == [Q(7,24),Q(5,12),Q(7,24)]
    assert [moment(xs,ua,j) for j in range(3)] == [Q(1),Q(1),Q(19,16)]
    assert [moment(xs,ub,j) for j in range(3)] == [Q(1),Q(1),Q(55,48)]
    assert moment(xs,ua,2)-moment(xs,ub,2)==Q(1,24)
    a,aa=roots(xs,ua,2.)
    b,ab=roots(xs,ub,2.)
    assert 1.42228<a<1.42229 and 1.46012<b<1.46013 and a<b and aa<ab
    print('exact three-class witness and positive-root comparison PASS',a,b,aa,ab)

    for k in range(3,11):
        x=[Q(1,2)+Q(i,k-1) for i in range(k)]
        p=[Q(1,k)]*k
        b=barycentric(x)
        for j in range(k-1):
            assert sum(b[i]*x[i]**j for i in range(k))==0
        assert sum(b[i]*x[i]**(k-1) for i in range(k))==1
        eps=min(p[i]/(8*abs(b[i])) for i in range(k))
        qplus=[Q(1,2)+eps*b[i]/p[i] for i in range(k)]
        qminus=[Q(1,2)-eps*b[i]/p[i] for i in range(k)]
        assert all(0<q<1 for q in qplus+qminus)
        assert sum(p[i]*qplus[i] for i in range(k)) == Q(1,2)
        assert sum(p[i]*qminus[i] for i in range(k)) == Q(1,2)
        uplus=[p[i]*(Q(1,2)+qplus[i]) for i in range(k)]
        uminus=[p[i]*(Q(1,2)+qminus[i]) for i in range(k)]
        assert all(moment(x,uplus,j)==moment(x,uminus,j) for j in range(k-1))
        assert moment(x,uplus,k-1)-moment(x,uminus,k-1)==4*Q(1,2)*eps
        assert moment(x,uplus,1)==Q(1)
        if k<=5:
            zplus,_ = roots(x,uplus,2.)
            zminus,_ = roots(x,uminus,2.)
            assert (zplus-zminus)*((-1)**k) > 1e-12, (k,zplus,zminus)
        print('Vandermonde and common-marginal tests PASS k=',k)
    print('ALL CHECKS PASS')

if __name__=='__main__':
    main()
