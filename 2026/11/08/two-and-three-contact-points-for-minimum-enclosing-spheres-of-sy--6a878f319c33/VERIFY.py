"""Exact-rational tests for the smallest enclosing ball of symmetric moment-curve arcs.

The symbolic inequalities and contact-barycenter argument in RESULT.md prove the
unrestricted theorem. These finite checks exercise the formula independently.
"""
from fractions import Fraction as F


def gamma(d, t):
    return tuple(t**j for j in range(1, d+1))


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def normsq(a):
    return dot(a, a)


def data(d, a):
    M = a*a
    p = gamma(d, a)
    minus = gamma(d, -a)
    E = tuple((x+y)/2 for x, y in zip(p, minus))
    S = normsq(tuple((x-y)/2 for x, y in zip(p, minus)))
    lam = (M+1)/(2*M) if d % 2 == 0 and M > 1 else F(1)
    c = tuple(lam*x for x in E)
    R2 = S if lam == 1 else normsq(c)
    return c, R2, S, lam


def main():
    assertions = 0
    cases = 0
    for d in range(2, 19):
        for a in [F(1,4), F(1,2), F(3,4), F(1), F(5,4), F(3,2), F(2), F(3)]:
            c, R2, S, lam = data(d, a)
            M=a*a
            E = tuple((x+y)/2 for x,y in zip(gamma(d,a),gamma(d,-a)))
            assert c == tuple(lam*x for x in E); assertions +=1
            assert all(x==0 for x in c[::2]); assertions +=1
            assert dot(tuple(c[i]-E[i] for i in range(d)), tuple(gamma(d,a)[i]-gamma(d,-a)[i] for i in range(d))) == 0; assertions +=1
            if d%2 or M<=1:
                assert R2==S; assertions+=1
                assert c==E; assertions+=1
            else:
                assert R2 == ((M+1)**2/(4*M*M))*normsq(E); assertions+=1
                assert (F(0)<lam<F(1)); assertions+=1
                # The three contact points have center c as their strictly positive barycenter.
                bary = tuple((lam/2)*(gamma(d,a)[i]+gamma(d,-a)[i]) for i in range(d))
                assert bary == c; assertions+=1
            for i in range(-30,31):
                t=a*F(i,30)
                ds=normsq(tuple(v-cj for v,cj in zip(gamma(d,t),c)))
                assert ds <= R2; assertions+=1
                should_touch = abs(i)==30 or (i==0 and d%2==0 and M>=1)
                assert (ds==R2)==should_touch, (d,a,t,ds,R2); assertions+=1
            cases +=1
    print(f"PASS: {cases} parameter cases, {assertions} exact-rational assertions")

if __name__=='__main__':
    main()
