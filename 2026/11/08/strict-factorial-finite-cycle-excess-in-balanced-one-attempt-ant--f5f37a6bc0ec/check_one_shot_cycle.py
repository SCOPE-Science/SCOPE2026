"""Standalone exact finite-graph checks for a balanced two-colour one-attempt adsorption theorem.

The analytic all-size inequalities and asymptotics are proved separately; these
checks compare two independent finite algorithms on the same finite examples.
"""
from fractions import Fraction
from functools import lru_cache
from math import factorial


def path_occupancy(n):
    a = [Fraction(0)] * (n + 1)
    for m in range(1, n + 1):
        a[m] = 1 + Fraction(2, m) * sum(a[:m-1])
    return a


def formula_density(n, a):
    total = sum((a[m] / 2 ** (m + 1) for m in range(1, n - 1)), Fraction())
    if n % 2:
        total += a[n] / 2 ** (n - 1)
    else:
        total += a[n-1] / 2 ** (n-1)
        total += (1+a[n-3]) / (n*2**(n-1))
    return total


def independent_graph_density(n):
    total = Fraction(0)
    for bits in range(1 << n):
        neighbors = [0] * n
        for i in range(n):
            j=(i+1) % n
            if ((bits >> i) ^ (bits >> j)) & 1:
                neighbors[i] |= 1 << j
                neighbors[j] |= 1 << i
        @lru_cache(None)
        def occupancy(mask):
            if mask == 0:
                return Fraction(0)
            k=mask.bit_count()
            s=Fraction(0)
            remaining=mask
            while remaining:
                bit=remaining & -remaining
                i=bit.bit_length()-1
                remaining-=bit
                s+=occupancy(mask & ~bit & ~neighbors[i])
            return 1+s/k
        total+=occupancy((1 << n)-1)
    return total/(n*2**n)


def beta_kernel_bounds(m):
    # The integral for B_m lies strictly below this rational bound and above
    # its first-order lower estimate, using 1-x <= exp(-x) <= 1.
    upper=Fraction(1, factorial(m)*(m+1)*(m+2))
    lower=upper-Fraction(4, factorial(m)*(m+1)*(m+2)*(m+3))
    return max(Fraction(0),lower),upper


def main():
    a=path_occupancy(32)
    count=0
    for n in range(3, 11):
        independent=independent_graph_density(n)
        formula=formula_density(n,a)
        assert formula==independent, (n,formula,independent)
        print(f'n={n}, exact density={formula}, finite algorithms agree')
        count+=1
    for n in range(3, 32):
        # The exact rational result is bounded by alternating Taylor sums for
        # 1-exp(-1).  Signed terms alternate decreasingly for k>=2.
        density=formula_density(n,a)
        order=max(40,2*n+4)
        sums=[]; s=Fraction(0)
        for j in range(order+1):
            s+=Fraction((-1)**j,factorial(j))
            sums.append(s)
        rho_upper=1-min(sums[-2:]);rho_lower=1-max(sums[-2:])
        assert rho_lower < rho_upper < density, (n, rho_lower, density, rho_upper)
        count+=1
    for m in range(1,25):
        lo,hi=beta_kernel_bounds(m)
        assert hi > lo >= 0
        count+=1
    print(f'PASS: {count} exact rational checks across independent graph recursion, finite-density inequalities and kernel enclosures.')

if __name__=='__main__':
    main()
