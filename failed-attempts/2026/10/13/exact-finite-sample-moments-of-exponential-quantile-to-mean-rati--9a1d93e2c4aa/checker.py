from fractions import Fraction

def check(max_n=300, max_m=1000):
    exact_checks = 0
    pairs = 0
    for n in range(1, max_n + 1):
        A = Fraction(0)
        B = Fraction(0)
        sw = Fraction(0)
        sq = Fraction(0)
        for k in range(1, n + 1):
            r = n-k+1
            a = Fraction(1, r)
            w = n*a
            A += a
            B += a*a
            sw += w
            sq += w*w
            pairs += 1
            direct_mean = sw / n
            direct_second = (sw*sw + sq) / (n*(n+1))
            direct_var = direct_second - direct_mean*direct_mean
            compact_mean = A
            compact_second = Fraction(n, n+1) * (A*A + B)
            compact_var = Fraction(n*B - A*A, n+1)
            assert direct_mean == compact_mean; exact_checks += 1
            assert direct_second == compact_second; exact_checks += 1
            assert direct_var == compact_var; exact_checks += 1
            assert compact_var >= 0; exact_checks += 1
            if n > 1:
                assert compact_var > 0; exact_checks += 1
    old = Fraction(1) + Fraction(1,2)  # m=1: H_3-H_1 = 1/2+1/3, reset below
    for m in range(1, max_m + 1):
        # Direct closed decrement between successive odd-sample median expectations.
        dec = Fraction(1,2*m+2) + Fraction(1,2*m+3) - Fraction(1,m+1)
        target = -Fraction(1, (2*m+2)*(2*m+3))
        assert dec == target; exact_checks += 1
        assert dec < 0; exact_checks += 1
    print('VERIFY_OK')
    print(f'pairs_checked={pairs}')
    print(f'max_n={max_n}')
    print(f'median_steps_checked={max_m}')
    print(f'exact_assertions={exact_checks}')

if __name__ == '__main__':
    check()
