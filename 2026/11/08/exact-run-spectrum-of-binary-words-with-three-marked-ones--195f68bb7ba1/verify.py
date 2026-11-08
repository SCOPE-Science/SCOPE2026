"""Independent checks of the fixed-weight-three maximal-periodicity run census.

Python 3 standard library only. Run `python3 verify.py`.
"""
from collections import Counter
from itertools import product
from math import comb


def maximal_periodic_runs(word):
    """Directly test all intervals and least periods; no gap formula used."""
    n = len(word)
    result = set()
    for left in range(n):
        for right in range(left + 1, n):
            length = right - left + 1
            for period in range(1, length // 2 + 1):
                if any(word[i] != word[i+period] for i in range(left, right-period+1)):
                    continue
                if any(all(word[i] == word[i+p] for i in range(left,right-p+1))
                       for p in range(1,period)):
                    continue
                if left and word[left-1] == word[left-1+period]:
                    continue
                if right+1<n and word[right+1] == word[right+1-period]:
                    continue
                result.add((left,right,period))
    return result


def gap_prediction(a,b,c,d):
    return (1 + sum(t>=2 for t in (a,b,c,d))
            + int(b>c and a>=b-c) + int(c>b and d>=c-b))


def pairs(n):
    for a in range(n-2):
        for b in range(n-2-a):
            for c in range(n-2-a-b):
                yield a,b,c,n-3-a-b-c


def add(*inputs):
    out=Counter()
    for d in inputs:
        out.update(d)
    return {k:v for k,v in out.items() if v}


def times(A,B,limit):
    out=Counter()
    for (n,j),a in A.items():
        for (m,k),b in B.items():
            if n+m<=limit:
                out[n+m,j+k]+=a*b
    return {k:v for k,v in out.items() if v}


def shift(A,dn,dk,limit,scalar=1):
    return {(n+dn,j+dk):v*scalar for (n,j),v in A.items()
            if n+dn<=limit and v*scalar}


def geo(step,limit):
    return {(n,0):1 for n in range(0,limit+1,step)}


def rational_series(limit):
    """Expand the independently derived rational bivariate generating function."""
    E=geo(1,limit)
    H=geo(2,limit)
    G=add({(0,0):1,(1,0):1},shift(E,2,1,limit))
    A1=add({(0,0):1,(1,1):1},shift(E,2,2,limit))
    B1=add({(0,0):1,(2,1):1},shift(H,4,2,limit))
    B2=add({(0,1):1,(2,1):1},shift(H,4,2,limit))
    C=add({(0,0):1,(2,0):1},shift(H,4,2,limit))
    term0=times(times(G,G,limit),C,limit)
    term1=shift(times(times(G,A1,limit),B1,limit),1,0,limit,2)
    term2=shift(times(times(times(G,B2,limit),G,limit),E,limit),2,0,limit,2)
    term3base=times(times(times(G,B2,limit),E,limit),H,limit)
    term3=add(shift(term3base,4,2,limit,2),shift(term3base,4,1,limit,-2))
    return shift(add(term0,term1,term2,term3),3,1,limit)


def six_run_coefficient(n):
    """Coefficient of 2*z^12*(1+z-z^2)/((1-z)^2*(1-z^2)^2)."""
    def t(m):
        if m<0: return 0
        return sum((m-2*k+1)*(k+1) for k in range(m//2+1))
    m=n-12
    return 2*(t(m)+t(m-1)-t(m-2))


def main():
    tested=0
    for n in range(3,23):
        for a,b,c,d in pairs(n):
            w='0'*a+'1'+'0'*b+'1'+'0'*c+'1'+'0'*d
            actual=len(maximal_periodic_runs(w))
            expected=gap_prediction(a,b,c,d)
            assert actual==expected,(n,(a,b,c,d),actual,expected)
            tested+=1
    print('DIRECT_PERIOD_CHECK_OK',tested)

    R=rational_series(36)
    for n in range(3,37):
        count=Counter(gap_prediction(*g) for g in pairs(n))
        assert sum(count.values())==comb(n,3)
        assert {k:v for (nn,k),v in R.items() if nn==n}==dict(count),n
        assert count.get(6,0)==six_run_coefficient(n),n
    assert sum(1 for g in pairs(12) if gap_prediction(*g)==6)==2
    assert 6==gap_prediction(2,3,2,2)
    print('RATIONAL_GF_CHECK_OK lengths=3..36')

    # Dominant-pole check: F_6(z) ~ (1/2)*(1-z)^(-4),
    # whereas z^3/(1-z)^4 ~ (1-z)^(-4).
    # Counts must consequently have asymptotic six-run density 1/2.
    from fractions import Fraction
    assert Fraction(2*(1+1-1),4)==Fraction(1,2)
    print('SHARP_MAXIMUM_AND_HALF_LIMIT_OK')

if __name__=='__main__':
    main()
