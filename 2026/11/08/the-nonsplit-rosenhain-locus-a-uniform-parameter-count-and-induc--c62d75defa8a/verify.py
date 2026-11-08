"""Exact finite-field checks of a Rosenhain nonsplit locus and its zeta factor.

This checks examples only; the all-prime-power theorem uses the supplied proof.
No external Python packages are needed.
"""


def count_marked(p):
    squares = {t*t % p for t in range(1, p)}
    nonsplit, split, smooth = 0, 0, 0
    for lam in range(p):
        if lam in (0, 1):
            continue
        for mu in range(p):
            nu = lam*(1-mu)*pow(1-lam, -1, p) % p
            if len({0, 1, lam, mu, nu}) != 5:
                continue
            smooth += 1
            delta = lam*(lam-mu) % p
            if delta not in squares:
                nonsplit += 1
            else:
                split += 1
    assert smooth == (p-3)**2, (p, smooth)
    assert nonsplit == (p-1)*(p-3)//2, (p, nonsplit)
    assert split == (p-3)*(p-5)//2, (p, split)
    return nonsplit


def point_counts(p, lam, mu, theta):
    delta = lam*(lam-mu) % p
    sq = {z*z % p for z in range(1, p)}
    assert delta not in sq and delta
    nu = lam*(1-mu)*pow(1-lam, -1, p) % p
    assert len({0, 1, lam, mu, nu}) == 5
    def f0(x):
        out = theta
        for r in (0, 1, lam, mu, nu):
            out = out*(x-r) % p
        return out
    n_p = 1+sum(1 if f0(x)==0 else (2 if f0(x) in sq else 0) for x in range(p))
    assert n_p == p+1
    # F_{p^2} = F_p[s]/(s^2-delta).
    elems = [(a, b) for a in range(p) for b in range(p)]
    zero = (0, 0)
    def c(x): return (x % p, 0)
    def plus(x, y): return ((x[0]+y[0])%p, (x[1]+y[1])%p)
    def minus(x, y): return ((x[0]-y[0])%p, (x[1]-y[1])%p)
    def times(x, y):
        return ((x[0]*y[0]+delta*x[1]*y[1])%p,
                (x[0]*y[1]+x[1]*y[0])%p)
    def inverse(x):
        norm = (x[0]*x[0]-delta*x[1]*x[1])%p
        assert norm != 0
        z = pow(norm, -1, p)
        return (x[0]*z%p, -x[1]*z%p)
    def divide(x, y): return times(x, inverse(y))
    squares = {times(v, v) for v in elems}
    def number_of_points(rhs):
        return 1+sum(1 if (v:=rhs(x))==zero else
                     (2 if v in squares else 0) for x in elems)
    def f2(x):
        value = c(theta)
        for root in (0, 1, lam, mu, nu):
            value = times(value, minus(x, c(root)))
        return value
    c2 = number_of_points(f2)
    root_delta = (0, 1)
    alpha = divide(times(c(1-lam),plus(c(mu-2*lam),times(c(2),root_delta))),c(mu-1))
    factor = c(theta*(1-mu)*pow(1-lam,-1,p))
    def elliptic_rhs(t):
        return times(factor, times(t, times(minus(t,c(1)),minus(t,alpha))))
    e2 = number_of_points(elliptic_rhs)
    a = p*p+1-e2
    assert c2 == p*p+1-2*a, (p, lam, mu, theta, c2, e2, a)
    return c2, e2, a




def check_q9():
    # F9=F3[z]/(z^2+1), a characteristic-three boundary check.
    p, d = 3, 2
    els = [(a,b) for a in range(p) for b in range(p)]
    z, one = (0,0), (1,0)
    def add(x,y): return ((x[0]+y[0])%p,(x[1]+y[1])%p)
    def neg(x): return ((-x[0])%p,(-x[1])%p)
    def sub(x,y): return add(x,neg(y))
    def mul(x,y): return ((x[0]*y[0]+d*x[1]*y[1])%p,
                          (x[0]*y[1]+x[1]*y[0])%p)
    def inverse(x):
        assert x != z
        return next(y for y in els if mul(x,y)==one)
    def div(x,y): return mul(x,inverse(y))
    sq = {mul(x,x) for x in els if x!=z}
    nonsplit, smooth = 0, 0
    for lam in els:
        if lam in (z,one):
            continue
        for mu in els:
            nu=div(mul(lam,sub(one,mu)),sub(one,lam))
            if len({z,one,lam,mu,nu})!=5:
                continue
            smooth += 1
            if mul(lam,sub(lam,mu)) in sq:
                continue
            nonsplit += 1
            def f(x):
                t=one
                for r in (z,one,lam,mu,nu):
                    t=mul(t,sub(x,r))
                return t
            pts=1+sum(1 if f(x)==z else (2 if f(x) in sq else 0)
                      for x in els)
            assert pts==10, (lam,mu,nu,pts)
    assert (smooth,nonsplit)==(36,24)


def main():
    ps = (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41)
    for p in ps:
        count_marked(p)
    examples = [(5,2,3),(7,2,3),(11,2,4),(13,2,3),
                (17,2,5),(19,2,4),(23,2,3)]
    for p, lam, mu in examples:
        for theta in (1, 2):
            point_counts(p, lam, mu, theta)
    check_q9()
    print('VERIFY_ROSENHAIN_NONSPLIT_OK 11_prime_parameter_censuses 14_quadratic_field_curve_checks 24_F9_odd_trace_checks')


if __name__ == '__main__':
    main()
