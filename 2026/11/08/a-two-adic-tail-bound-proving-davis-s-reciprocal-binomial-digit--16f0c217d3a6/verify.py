"""Independent exact-arithmetic tests for the reciprocal-binomial 2-adic estimate."""
from fractions import Fraction
from math import comb


def nu2_integer(n):
    if n == 0:
        return 10**9
    n = abs(n)
    return (n & -n).bit_length() - 1


def nu2_rational(q):
    if q == 0:
        return 10**9
    return nu2_integer(q.numerator) - nu2_integer(q.denominator)


def hamming(n):
    return n.bit_count()


def main():
    max_n = 520
    terms = [Fraction(1)]
    for n in range(1, max_n + 1):
        terms.append(Fraction(1) + Fraction(n+1, 2*n) * terms[-1])
    for n in range(85):
        direct = sum((Fraction(1, comb(n, j)) for j in range(n+1)), Fraction(0))
        assert terms[n] == direct, n
    for n in range(85):
        alternative = Fraction(n+1, 2**(n+1))*sum((Fraction(2**j,j) for j in range(1,n+2)), Fraction(0))
        assert terms[n] == alternative, n
    full = 0
    min_gap = 999999
    for n in range(100):
        for h in range(1,101):
            bound = nu2_integer(h)-hamming(n)-hamming(n+h)-1
            difference = nu2_rational(terms[n+h]-terms[n])
            assert difference>=bound, (n,h,difference,bound)
            min_gap=min(min_gap,difference-bound)
            full+=1
    dyadic=0
    sharp=0
    for e in range(1,9):
        for k in range(2**e):
            bound = e-2*hamming(k)-2
            val = nu2_rational(terms[2**e+k]-terms[k])
            assert val>=bound, (e,k,val,bound)
            dyadic+=1
            sharp+=(val==bound)
    lemma=0
    for u in range(200):
        for v in range(1,200):
            assert nu2_integer(u+v)<=hamming(u)+hamming(v-1)
            lemma+=1
    for i in range(1,20001):
        assert 2*hamming(i)<=i+1
    # A finite-precision check of the convergent two-adic series identity:
    # f(n)=-(n+1) * sum_{i=1}^infinity 2**i/(n+1+i).
    tail=0
    for n in range(25):
        trunc=sum((Fraction(2**i,n+1+i) for i in range(1,151)),Fraction(0))
        assert nu2_rational(terms[n]+(n+1)*trunc)>=100, n
        tail+=1
    print('VERIFY_OK direct_binomial_rows=85 finite_identity_rows=85 global_pairs=%d min_margin=%d dyadic_pairs=%d attained_bound=%d digit_lemma_pairs=%d binary_weight_samples=20000 tail_precision_cases=%d' % (full,min_gap,dyadic,sharp,lemma,tail))


if __name__ == '__main__':
    main()
