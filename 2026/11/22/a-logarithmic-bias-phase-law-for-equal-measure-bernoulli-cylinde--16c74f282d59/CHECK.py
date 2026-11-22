#!/usr/bin/env python3
"""Independent finite-state and generating-series diagnostics for biased single-word avoidance.

Run with Python 3: python CHECK.py. Arithmetic for exact comparisons uses fractions.
The finite tests below do not substitute for the all-parameter analytic proof.
"""
from fractions import Fraction
from math import log


def words(k):
    return ('0' * k + '11' + '0' * k, '1' + '0' * (2 * k) + '1')


def border_series(w, p):
    q = 1 - p
    c = [Fraction(0)] * len(w)
    c[0] = Fraction(1)
    for d in range(1, len(w)):
        if w[:len(w)-d] == w[d:]:
            tail = w[len(w)-d:]
            c[d] = p ** tail.count('1') * q ** tail.count('0')
    return c


def denominator(w, p):
    c = border_series(w, p)
    m = p ** w.count('1') * (1 - p) ** w.count('0')
    d = [Fraction(0)] * (len(w) + 1)
    for i, v in enumerate(c):
        d[i] += v
        d[i+1] -= v
    d[len(w)] += m
    return c, d


def gf_survival_coeffs(w, p, max_n):
    c, d = denominator(w, p)
    out = []
    for n in range(max_n+1):
        top = c[n] if n < len(c) else Fraction(0)
        out.append((top-sum(d[j] * out[n-j] for j in range(1, min(n, len(d)-1)+1))) / d[0])
    return out


def suffix_state(w, current, bit):
    s = w[:current] + bit
    if s.endswith(w):
        return None
    return max(j for j in range(len(w)) if s.endswith(w[:j]) or j == 0)


def dp_survival_coeffs(w, p, max_n):
    t = {(j, b): suffix_state(w, j, b) for j in range(len(w)) for b in '01'}
    state = [Fraction(0) for _ in w]
    state[0] = Fraction(1)
    ans = [sum(state)]
    for _ in range(max_n):
        nxt = [Fraction(0) for _ in w]
        for j, mass in enumerate(state):
            for bit, prob in [('0', 1-p), ('1', p)]:
                idx = t[j, bit]
                if idx is not None:
                    nxt[idx] += mass * prob
        state = nxt
        ans.append(sum(state))
    return ans


def bisect(f, a, b, iterations=90):
    fa, fb = f(a), f(b)
    assert fa * fb < 0, (fa, fb, a, b)
    for _ in range(iterations):
        m = (a+b)/2
        if f(m)*fa <= 0:
            b = m
        else:
            a, fa = m, f(m)
    return (a+b)/2


def t_threshold(k):
    return bisect(lambda t: 2*t**k-1-t**(3*k)*(1-t), 2**(-1/k), 1.0)


def p_threshold(k):
    t=t_threshold(k)
    return 1/(1+sum(t**(-j) for j in range(k)))


def direct_pole(w,p):
    n=len(w)
    # Independently compute autocorrelation weights using the actual word.
    coeff=[float(v) for v in border_series(w,Fraction(str(p)))]
    m=p**w.count('1')*(1-p)**w.count('0')
    def f(z):
        return (1-z)*sum(v*z**i for i,v in enumerate(coeff))+m*z**n
    a=1.;b=1.0
    while f(b)>=0 and b < 1/min(p,1-p)+1:
        b=b*1.015+1e-7
    assert f(b)<0,(w,p,b,f(b))
    return bisect(f,a,b,70)


def main():
    exact_comparisons=0
    structural_comparisons=0
    for k in range(2,9):
        u,v=words(k)
        for p in [Fraction(1,4),Fraction(2,5),Fraction(1,2),Fraction(3,4)]:
            for w in [u,v]:
                n_max=2*len(w)+8
                assert gf_survival_coeffs(w,p,n_max)==dp_survival_coeffs(w,p,n_max)
                exact_comparisons+=n_max+1
            cu=border_series(u,p)
            cv=border_series(v,p)
            n=2*k+2
            for d in range(1,n):
                expected_u=(p*p*(1-p)**(2*k-(n-d))) if n-k<=d<n else Fraction(0)
                expected_v=(p*(1-p)**(2*k)) if d==n-1 else Fraction(0)
                assert cu[d]==expected_u, (k,p,d,cu[d],expected_u)
                assert cv[d]==expected_v, (k,p,d,cv[d],expected_v)
                structural_comparisons+=2
        pk=p_threshold(k)
        assert 1-2**(-1/k)<pk<1/(k+1)
        for factor, desired in [(0.85,1),(1.15,-1)]:
            p=pk*factor
            # Equal-length and equal-measure word pairs with opposite escape ranking.
            ru,rv=direct_pole(u,p),direct_pole(v,p)
            assert (ru-rv)*desired > 1e-9, (k,factor,p,ru,rv)
            structural_comparisons+=1
    print('PASS exact survival coefficients:',exact_comparisons)
    print('PASS explicit overlap and crossover checks:',structural_comparisons)
    for k in (2,3,4,5,8,16,40):
        pk=p_threshold(k)
        c=log(2)
        two_term=c/k-c*(1+2*c)/(8*k*k)
        print('k',k,'p_k',format(pk,'.14g'),'two_term',format(two_term,'.14g'))


if __name__=='__main__':
    main()
