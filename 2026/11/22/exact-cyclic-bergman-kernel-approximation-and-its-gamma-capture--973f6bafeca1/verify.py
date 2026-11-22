"""Reproduce checks for circular kernel approximation of monomials.

Python 3, standard library only. These are finite diagnostics; the analytic
proof and asymptotic argument are stated separately in RESULT.md.
"""
import cmath
import math


def solve(A, b):
    n = len(b)
    a = [list(map(complex, row)) + [complex(y)] for row, y in zip(A, b)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda i: abs(a[i][col]))
        a[col], a[pivot] = a[pivot], a[col]
        d = a[col][col]
        assert abs(d) > 1e-12
        for j in range(col, n + 1):
            a[col][j] /= d
        for i in range(n):
            if i == col:
                continue
            w = a[i][col]
            for j in range(col, n + 1):
                a[i][j] -= w * a[col][j]
    return [a[i][n] for i in range(n)]


def beta2_formula(m, N, u):
    q, j = divmod(N, m)
    A, B = j + 1, m - j - 1
    return (N + 1) * u**q * (1 - u)**2 / (A + B * u)


def beta2_root(m, N):
    q, j = divmod(N, m)
    assert q >= 1
    A, B = j + 1, m - j - 1
    lo, hi = 0.0, 1.0
    for _ in range(90):
        u = (lo + hi) / 2
        val = q*A + ((q-1)*B-(q+2)*A)*u - (q+1)*B*u*u
        if val > 0:
            lo = u
        else:
            hi = u
    return (lo + hi) / 2


def direct_projection(m, N, u):
    radius = u**(0.5 / m)
    a = [radius * cmath.exp(2j*math.pi*k/m) for k in range(m)]
    gram = [[(1-a[k]*a[h].conjugate())**-2
             for h in range(m)] for k in range(m)]
    v = [math.sqrt(N+1)*z**N for z in a]
    coeff = solve(gram, v)
    return sum(v[k].conjugate()*coeff[k] for k in range(m)).real


def beta_gamma_test(beta, m, j, q):
    # Log-sum-exp applied to an absolutely convergent positive series.
    N = m*q+j
    u = math.exp(-beta/q)
    L = 6000
    vals = [math.lgamma(j+m*l+beta)-math.lgamma(beta)
            -math.lgamma(j+m*l+1)+l*math.log(u) for l in range(L)]
    x = max(vals)
    denom = x + math.log(sum(math.exp(v-x) for v in vals))
    captured = math.exp(vals[q]-denom)
    c = beta**beta*math.exp(-beta)/math.gamma(beta)
    return q*captured/c


def main():
    tests = 0
    for m in range(2, 9):
        for N in range(m, 3*m+1):
            u = beta2_root(m, N)
            assert abs(direct_projection(m, N, u)
                       - beta2_formula(m, N, u)) < 2e-8
            assert beta2_formula(m,N,u) >= beta2_formula(m,N,u*0.97)
            assert beta2_formula(m,N,u) >= beta2_formula(m,N,(u+1)/2)
            tests += 3
    for m in [2,4,7]:
        for j in range(m):
            for q in [40,100,400,1500]:
                u = beta2_root(m, q*m+j)
                A=j+1
                expected=1-2/q+(2+2*A/m)/q**2
                assert abs(u-expected) < 30/q**3
                approx=4*math.exp(-2)/q*(1-A/(m*q))
                assert abs(beta2_formula(m,q*m+j,u)/approx-1)<.007
                tests += 2
    for beta in [1.0,1.5,2.0,4.0]:
        for m,j in [(2,0),(3,2),(5,1)]:
            # Evaluate at asymptotic optimal radius. It suffices for
            # diagnosing the Gamma law, not for proving optimization.
            ratio = beta_gamma_test(beta,m,j,300)
            assert abs(ratio-1) < .035, (beta,m,j,ratio)
            tests += 1
    print('PASS:',tests,'finite checks (direct Gram, root, expansions, Gamma scaling)')

if __name__=='__main__':
    main()
