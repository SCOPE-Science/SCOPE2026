"""Independent integer and floating-point checks for the skeletal threshold formulas.

The infinite-dimensional statements are established by the analytic argument in RESULT.md,
not by these finite checks. Standard-library Python only.
"""
import math


def sq_ratio_sign(n, j):
    """Sign of R(n,j)^2-1, computed with exact integers."""
    left = (n + 1)**2 * (n*(n+1))**j
    right = 4**n * (math.factorial(j)**2) * (j+1)
    return (left > right) - (left < right)


def log_ratio(n, j):
    return math.log(n+1) - n*math.log(2) + (j/2)*math.log(n*(n+1)) - math.lgamma(j+1) - math.log(j+1)/2


def root_alpha():
    lo, hi = .1, .9
    for _ in range(120):
        mid = (lo+hi)/2
        if mid*(1-math.log(mid)) > math.log(2):
            hi=mid
        else: lo=mid
    return (lo+hi)/2


def run():
    checks = 0
    alpha = root_alpha()
    C = -math.log(alpha) + alpha/2 - .5*math.log(2*math.pi)
    beta = -C/(-math.log(alpha))
    assert .32756 < alpha < .32757
    assert -.32339 < beta < -.32337
    for n in range(2, 251):
        signs=[sq_ratio_sign(n,j) for j in range(n+1)]
        checks += n+1
        assert signs[0] == -1 and signs[-1] == 1
        assert all(signs[j]<=signs[j+1] for j in range(n))
        assert signs[-1] == signs[-2]
        assert sum(signs[j]==0 for j in range(n)) <= 1
        # The recurrence for squared ratios is an exact integer equality.
        for j in range(n):
            top = (n*(n+1))**(j+1)*(n+1)**2
            den = 4**n*math.factorial(j+1)**2*(j+2)
            prev_top = (n*(n+1))**j*(n+1)**2
            prev_den = 4**n*math.factorial(j)**2*(j+1)
            assert top*prev_den*(j+1)*(j+2) == prev_top*den*n*(n+1)
            checks += 1
        if n in (4, 10, 100, 250):
            first=next(j for j,s in enumerate(signs) if s>=0)
            print('n=', n, 'first nonnegative face dimension=', first)
    # Check the local Stirling expansion at bounded displacements.
    for n in (10000, 40000, 100000):
        for t in (-2,-1,0,1,2):
            j=round(alpha*n)+t
            leading=(-math.log(alpha))*(j-alpha*n)+C
            err=abs(log_ratio(n,j)-leading)
            assert err < 20/n, (n,j,err)
            checks += 1
    print('alpha=', format(alpha,'.15f'), 'beta=',format(beta,'.15f'))
    print('PASS:',checks, 'finite arithmetic / asymptotic-spot checks')


if __name__ == '__main__':
    run()
