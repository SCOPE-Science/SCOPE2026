"""Independent finite-horizon checks for binary step reinforcement.

No finite check is used as a proof of asymptotic or analytic-continuation claims.
"""
from fractions import Fraction
from math import gamma, sqrt, pi


def markov_character(alpha, max_n):
    """Direct distribution recursion on the number of one-steps."""
    masses = [Fraction(1, 2), Fraction(1, 2)]
    ans = {}
    for n in range(1, max_n + 1):
        ans[n] = sum(((-1) ** k) * v for k, v in enumerate(masses))
        if n == max_n:
            break
        new = [Fraction(0)] * (n + 2)
        for k, v in enumerate(masses):
            pr_one = (1 - alpha) / 2 + alpha * Fraction(k, n)
            new[k] += v * (1 - pr_one)
            new[k+1] += v * pr_one
        masses = new
    return ans


def ode_coefficients(alpha, max_n):
    """Formal coefficients from A'=A^2+alpha B^2, B'=(1+alpha)AB."""
    a = [Fraction(0)] * max_n
    b = [Fraction(0)] * max_n
    b[0] = Fraction(1)
    for j in range(max_n - 1):
        a[j+1] = sum(a[k] * a[j-k] + alpha * b[k] * b[j-k] for k in range(j+1)) / (j+1)
        b[j+1] = (1+alpha) * sum(a[k] * b[j-k] for k in range(j+1)) / (j+1)
    return {n:a[n-1] for n in range(1,max_n+1)}, a, b


def check():
    checks = 0
    for alpha in [Fraction(1,7), Fraction(1,4), Fraction(1,2), Fraction(3,4), Fraction(6,7)]:
        nmax = 34
        direct = markov_character(alpha,nmax)
        from_ode, a, b = ode_coefficients(alpha,nmax)
        for n in range(1,nmax+1):
            assert direct[n] == from_ode[n]
            checks += 1
            assert direct[n] == 0 if n % 2 else direct[n] > 0
            checks += 1
        assert from_ode[2] == alpha
        checks += 1
        assert from_ode[4] == alpha*alpha*(alpha+2)/3
        checks += 1
        for n in range(1,nmax):
            assert a[n] == 0 if n%2==0 else a[n] > 0
            checks += 1
            assert b[n] == 0 if n%2 else b[n] > 0
            checks += 1
    # Floating-point asymptotic diagnostics independent from exact assertions.
    diagnostics = []
    for alpha in [0.25,0.5,0.75]:
        nmax=201
        a=[0.0]*nmax;b=[0.0]*nmax;b[0]=1.0
        for j in range(nmax-1):
            a[j+1]=sum(a[k]*a[j-k]+alpha*b[k]*b[j-k] for k in range(j+1))/(j+1)
            b[j+1]=(1+alpha)*sum(a[k]*b[j-k] for k in range(j+1))/(j+1)
        h=(1+alpha)/(2*alpha)
        radius=sqrt(pi)*gamma(h)/(2*alpha*gamma(h+0.5))
        data=[]
        for n in [20,40,80,160,200]:
            observed=a[n-1]
            predicted=2/(1+alpha)*radius**(-n)
            data.append((n,observed/predicted))
        assert data[-1][1] > data[0][1] and data[-1][1] < 1.005
        checks += 1
        diagnostics.append({'alpha':alpha,'radius':radius,'ratios':data})
    print('exact_assertions=',checks)
    print('asymptotic_diagnostics=',diagnostics)

if __name__=='__main__':
    check()
