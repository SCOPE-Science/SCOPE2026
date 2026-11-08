"""Independent finite checks and rational-moment identity checks.

Run: python3 verify.py
Requires Python 3 standard library only.
"""
from fractions import Fraction as Q
from itertools import combinations


def gap_count(a, b, c, d):
    z = a + b + c + d
    t = max(min(a, b+c+d), min(a+b, c+d), min(a+b+c, d))
    r = min(a, d)
    s = min(b, c)
    extra = min(b, d-a) * (c+1) if a <= d else min(c, a-d) * (b+1)
    return z + t + 1 + (r+1)*(b+c+1) + extra + (r+1)*(s+1)


def independently_count(word):
    seen = {''}
    for symbol in word:
        seen.update({prefix + symbol for prefix in tuple(seen)})
    return sum(bool(s) and s == s[::-1] for s in seen)


def main():
    tested = 0
    for n in range(3, 19):
        for i, j, k in combinations(range(n), 3):
            a, b, c, d = i, j-i-1, k-j-1, n-k-1
            word = '0'*a + '1' + '0'*b + '1' + '0'*c + '1' + '0'*d
            assert gap_count(a,b,c,d) == independently_count(word), (n,a,b,c,d)
            tested += 1
    assert tested == 3876
    print('GAP_FORMULA_OK', tested)

    # Recompute the exponential integrals from rate/moment formulas.
    # If X~Exp(rate), E[X^k exp(-tilt*X)] = rate*k!/(rate+tilt)^(k+1).
    from math import factorial
    def exp_moment(k, rate=1, tilt=0):
        return Q(rate*factorial(k), (rate+tilt)**(k+1))

    # M=min(U1,U4)~Exp(2); the independent gap Delta is Exp(1).
    E_M, E_M2 = exp_moment(1, 2), exp_moment(2, 2)
    # The inner minimum X=min(B,C)~Exp(2), and the remaining
    # independent difference Y~Exp(1). H=3X+Y.
    EX, EY = exp_moment(1, 2), exp_moment(1)
    E_H = 3*EX+EY
    E_H2 = 9*exp_moment(2,2)+6*EX*EY+exp_moment(2)
    # Condition on B: E[min(B,Delta)|B]=1-exp(-B),
    # E[min(B,Delta)^2|B]=2*(1-(1+B)*exp(-B)).
    E_J = (1-exp_moment(0,1,1))*exp_moment(1)
    E_J2 = (2*(1-exp_moment(0,1,1)-exp_moment(1,1,1)))*exp_moment(2)
    # E[H J] = E[B C (1-exp(-B))] + E[C^2(1-exp(-B))]
    #          + E[C min(B,C)] - E[exp(-B) C min(B,C)].
    term_B = (exp_moment(1)-exp_moment(1,1,1))*exp_moment(1)
    term_C = exp_moment(2)*(1-exp_moment(0,1,1))
    term_min = Q(1,2)*(exp_moment(2,2)+EX*EY) + Q(1,2)*exp_moment(2,2)
    # B<=C: B=X,C=X+Y, min=X; B>C: B=X+Y,C=X,min=X.
    disc_left = Q(1,2)*(exp_moment(2,2,1)+exp_moment(1,2,1)*EY)
    disc_right = Q(1,2)*exp_moment(2,2,1)*exp_moment(0,1,1)
    assert disc_left == Q(5,27) and disc_right == Q(1,27)
    E_HJ = term_B + term_C + term_min - disc_left-disc_right
    assert (E_H, E_H2, E_J, E_J2, E_HJ) == (Q(5,2),Q(19,2),Q(1,2),Q(1),Q(41,18))
    E_G = E_M*E_H + E_J
    E_G2 = E_M2*E_H2 + 2*E_M*E_HJ + E_J2
    assert E_G == Q(7,4) and E_G2 == Q(289,36)
    # The sum of four independent rate-one exponentials is Gamma(4,1).
    E_S2, E_S4 = 4*5, 4*5*6*7
    mean = E_G/E_S2
    second = E_G2/E_S4
    variance = second-mean*mean
    assert mean == Q(7,80)
    assert second == Q(289,30240)
    assert variance == Q(2299,1209600)
    print('RATIONAL_MOMENTS_OK', mean, variance)


if __name__ == '__main__':
    main()
