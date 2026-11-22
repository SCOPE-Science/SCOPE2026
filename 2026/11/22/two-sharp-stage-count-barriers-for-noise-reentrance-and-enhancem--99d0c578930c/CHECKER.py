"""Independent exact finite-chain Poisson-corrector checks for one-site speed defects.

Requires Python 3 and SymPy. All selected rates and finite-chain computations are rational.
Analytic global claims are proved separately; these tests only guard algebra and indexing.
"""
import sympy as S


def independent_dispersion(n, p, q, s):
    p, q, s = map(S.Rational, (p, q, s))
    d = [s] + [S.Integer(1)] * (n-1)
    a = 1/s-1
    v = n*(p-q)/(n+a)
    generator = S.zeros(n)
    rhs = S.zeros(n, 1)
    for i in range(n):
        generator[i, (i+1) % n] += d[i]*p
        generator[i, (i-1) % n] += d[i]*q
        generator[i,i] -= d[i]*(p+q)
        rhs[i] = v-d[i]*(p-q)
    generator[n-1,:] = S.ones(1,n)
    rhs[n-1] = 0
    phi = generator.inv()*rhs
    pi = [(1/z)/(n+a) for z in d]
    return S.factor(sum(pi[i]*d[i]*(
        p*(1+phi[(i+1)%n]-phi[i])**2 +
        q*(-1+phi[(i-1)%n]-phi[i])**2)
        for i in range(n))/2)


def explicit_dispersion(n, p, q, s):
    p, q, s = map(S.Rational, (p, q, s))
    a=1/s-1
    b=(p-q)*(p**n+q**n)/((p+q)*(p**n-q**n))
    return S.factor((p+q)*n*n*(n+2*a+b*a*a)/(2*(n+a)**3))


def main():
    count = 0
    for n in range(3,9):
        for p,q,s in [
            (S.Rational(3,2), 1, S.Rational(1,2)),
            (3, 1, S.Rational(1,5)),
            (10, 1, S.Rational(3,2)),
            (20, 1, S.Rational(1,7)),
            (11, 10, S.Rational(2,3)),
        ]:
            assert S.factor(independent_dispersion(n,p,q,s)-explicit_dispersion(n,p,q,s))==0
            count+=1
    a,n,B=S.symbols('a n B', positive=True)
    fn=n*n*(n+2*a+B*a*a)/(n+a)**3
    derivative=-n*n*(B*a*a+(4-2*B*n)*a+n)/(n+a)**4
    assert S.factor(S.diff(fn,a)-derivative)==0
    count+=1
    y=n*B
    assert S.factor((fn-1)*(n+a)**3+a*(a*a+n*(3-y)*a+n*n))==0
    count+=1
    for N,p,q in [(5,20,1),(6,20,1),(6,50,1),(7,8,1)]:
        bb=S.Rational(p-q,p+q)*S.Rational(p**N+q**N,p**N-q**N)
        yy=N*bb
        assert yy>4
        count+=1
        if N>=6:
            assert yy>5
            test_a=S.Integer(N)
            assert explicit_dispersion(N,p,q,S.Rational(1,1+test_a)) > S.Rational(p+q,2)
            count+=1
        else:
            assert yy<5
            count+=1
    print('PASS:',count,'independent exact rational and symbolic checks')


if __name__ == '__main__':
    main()
