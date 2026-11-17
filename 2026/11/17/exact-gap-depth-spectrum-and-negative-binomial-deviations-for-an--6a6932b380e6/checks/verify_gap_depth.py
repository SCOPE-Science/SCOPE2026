"""Independent finite checks for a countable affine interval model.

Checks enumerated stage multiplicities, the negative-binomial law,
and a local large-deviation approximation. Finite checks are not proofs.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb, exp, lgamma, log, pi, sqrt


def enumerated_count(n, cutoff):
    counts = {0: 1}
    for _ in range(n):
        nxt = defaultdict(int)
        for total, a in counts.items():
            for k in range(1, cutoff + 1):
                nxt[total + k] += a * (2 ** (k-1))
        counts = nxt
    return counts


def H(x):
    return x * log(x) - (x - 1) * log(x - 1) + (x - 1) * log(2)


def I(x):
    return x * log(3) - H(x)


def exact_logprob(n, s):
    return ((s-n)*log(2)+lgamma(s)-lgamma(n)-lgamma(s-n+1)-s*log(3))


def approx_logprob(n, s):
    x=s/n
    return -n*I(x)-0.5*log(2*pi*n*x*(x-1))


def main():
    word_tests=0
    for n in range(1,6):
        counts=enumerated_count(n,7)
        for s in range(n,n+7):
            assert counts[s] == 2**(s-n)*comb(s-1,n-1), (n,s)
            word_tests += 1
    prob_tests=0
    for n in range(1,12):
        # Exact geometric series identity via first n+20 terms and bound.
        terms=[Fraction(2**(s-n)*comb(s-1,n-1),3**s)
               for s in range(n,n+60)]
        assert 0 < sum(terms) < 1
        # Probability ratio from closed form, independent of enumeration.
        for s in range(n+1,n+9):
            ratio=Fraction(2*s,s-n)
            p_s=Fraction(2**(s-n)*comb(s-1,n-1),3**s)
            p_prev=Fraction(2**(s-1-n)*comb(s-2,n-1),3**(s-1))
            assert p_s/p_prev == Fraction(2*(s-1),3*(s-n))
            prob_tests+=1
    for m in (1.2,1.5,2.0,2.8,3.,4.,8.,30.):
        assert I(m)>-1e-10
    assert abs(I(3.)) < 1e-13
    assert abs(H(1.0000001)/1.0000001)<0.000003
    ld=[]
    for n in (40,80,160,320):
        s=3*n
        ratio=exp(exact_logprob(n,s)-approx_logprob(n,s))
        ld.append((n,ratio))
        assert 0.99<ratio<1.01
    # Verify spectrum peak and positive large-mean floor, not as proof.
    spectrum=[H(m)/(m*log(5)) for m in (1.01,1.4,2.,3.,4.,10.,1000.)]
    assert spectrum[0]<spectrum[1]<spectrum[2]<spectrum[3]
    assert spectrum[3]>spectrum[4]>spectrum[5]>spectrum[6]
    assert abs(spectrum[-1]-log(2)/log(5))<0.01
    print('VERIFY_OK exact_word_counts=%d probability_ratios=%d local_ld=%d spectrum_samples=%d' % (word_tests,prob_tests,len(ld),len(spectrum)))
    for n,ratio in ld:
        print('LD_N %d ratio %.10f' % (n,ratio))

if __name__ == '__main__':
    main()
