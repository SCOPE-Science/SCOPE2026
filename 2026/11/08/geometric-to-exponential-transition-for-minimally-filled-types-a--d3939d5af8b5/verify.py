"""Exact finite-instance verification of the terminal-minimum count law."""
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial


def multiply(a, b):
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def exact_integral_law(n, m):
    """Exact gamma-integral expansion; coefficient arithmetic is rational."""
    pm = [Fraction(1, factorial(j)) for j in range(m + 1)]
    powers = [[Fraction(1)]]
    for _ in range(n - 1):
        powers.append(multiply(powers[-1], pm))
    ans = []
    for k in range(1, n + 1):
        total = Fraction(0)
        for j in range(n - k + 1):
            moment = sum((coef * Fraction(factorial(m*k - 1 + ell), (k+j)**(m*k+ell))
                          for ell, coef in enumerate(powers[j])), Fraction(0))
            total += (-1)**j * comb(n-k, j) * moment
        total *= Fraction(n * comb(n-1,k-1), factorial(m-1)*factorial(m)**(k-1))
        ans.append(total)
    return tuple(ans)


def exact_stopped_chain_law(n, m):
    """Independent recursive absorbing coupon-chain computation."""
    @lru_cache(None)
    def law(s):
        if min(s) >= m:
            k = sum(x == m for x in s)
            return tuple(Fraction(int(j == k)) for j in range(1,n+1))
        result = [Fraction(0) for _ in range(n)]
        active = 0
        for i, x in enumerate(s):
            if x == m+1:
                continue
            t = list(s)
            t[i] += 1
            got = law(tuple(t))
            for j, p in enumerate(got):
                result[j] += p
            active += 1
        return tuple(x / active for x in result)
    return law((0,)*n)


def main():
    checks=0
    for n in range(2, 6):
        for m in range(1,4):
            a=exact_integral_law(n,m)
            b=exact_stopped_chain_law(n,m)
            for j in range(n):
                assert a[j] == b[j], (n, m, j, a[j], b[j])
                checks += 1
                assert a[j] >= 0, (n, m, j)
                checks += 1
                assert a[j].denominator > 0, (n, m, j)
                checks += 1
            assert sum(a) == 1, (n, m, sum(a))
            checks += 1
            if m==1:
                mean=sum(Fraction(i+1)*p for i,p in enumerate(a))
                harmonic=sum((Fraction(1,i) for i in range(1,n+1)),Fraction(0))
                assert mean==harmonic,(n,mean,harmonic)
                checks+=1
    assert exact_integral_law(2,1)==(Fraction(1,2),Fraction(1,2))
    checks+=1
    print(f"PASS: {checks} exact-rational assertions across n=2..5, m=1..3")

if __name__ == '__main__':
    main()
