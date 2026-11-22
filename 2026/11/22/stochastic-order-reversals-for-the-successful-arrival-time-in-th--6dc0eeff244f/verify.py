"""Reproducible finite exact checks for a two-choice secretary timing theorem.

Usage: python3 verify.py
Uses Python's standard library only. Finite checks supplement, not replace,
the analytic natural-density proof.
"""
from fractions import Fraction as F
from itertools import permutations
from math import exp, floor


def harmonics(n):
    return [F(0)] + [sum((F(1, k) for k in range(1, j + 1)), F(0)) for j in range(1, n+1)]


def formula(n, b, a):
    """Exact unconditional success-at-index probabilities for one/two choices.

    b is the one-choice rejected count; a<b is the early two-choice count.
    """
    q = [F(0)] * n
    for i in range(b+1, n+1):
        q[i-1] = F(b, n*(i-1))
    if a is None:
        return q
    p = [F(0)] * n
    for i in range(a+1, b+1):
        p[i-1] = F(a, n*(i-1))
    h = F(0)
    for i in range(b+1, n+1):
        p[i-1] = F(b, n*(i-1))*(1+F(a, b)*h)
        h += F(1, i-1)
    return p


def brute(n, b, a):
    count = [0]*n
    for perm in permutations(range(1, n+1)):
        record_max, used = 0, 0
        for i, x in enumerate(perm, 1):
            eligible = int(i > a) + int(i > b)
            if x > record_max:
                if used < eligible:
                    used += 1
                    if x == n:
                        count[i-1] += 1
                record_max = x
    from math import factorial
    return [F(c, factorial(n)) for c in count]


def criterion(n, b, a):
    s = sum((F(1,j) for j in range(b,n)), F(0))
    t = sum((F(1,j*j) for j in range(b,n)), F(0))
    v = sum((F(1,j) for j in range(a,b)), F(0))
    return (s*s+t)/2-s/F(n-1)-v


def cdf_order(n,b,a):
    p1 = formula(n,b,None)
    p2 = formula(n,b,a)
    total1,total2 = sum(p1),sum(p2)
    cum1=cum2=F(0)
    dif=[]
    for i in range(n):
        cum1+=p1[i]/total1
        cum2+=p2[i]/total2
        dif.append(cum2-cum1)
    return min(dif) < 0, dif


def main():
    tests = 0
    for n in range(3,9):
        for b in range(2,n):
            for a in range(1,b):
                assert formula(n,b,a)==brute(n,b,a), (n,b,a)
                tests+=n
    for n in range(4,61):
        for b in range(2,n):
            a_values = sorted({1, max(1,b//3),max(1,b//2),b-1})
            for a in a_values:
                if a>=b: continue
                different,dif=cdf_order(n,b,a)
                assert different==(criterion(n,b,a)>0), (n,b,a)
                assert dif[-1]==0
                tests+=len(dif)+2
    alpha=exp(-1);beta=exp(-1.5)
    c1=(1-alpha)/2;c2=(1-exp(-.5))/2
    expected=exp(-.5)*(1-alpha/2)**2
    assert 0.4039 < expected < 0.4040
    H=[0.0]*250001;H2=[0.0]*250001
    for i in range(1,len(H)):
        H[i]=H[i-1]+1/i;H2[i]=H2[i-1]+1/(i*i)
    count=0
    for n in range(500,250001):
        b=floor(alpha*n+c1);a=floor(beta*n+c2)
        s=H[n-1]-H[b-1];t=H2[n-1]-H2[b-1]
        v=H[b-1]-H[a-1]
        count+=(s*s+t)/2-s/(n-1)-v>0
    observed=count/(250001-500)
    assert abs(observed-expected)<.0001, (observed,expected)
    print('Finite exact assertions:',tests)
    print('Numerical rounded-cutoff frequency for N=500..250000:',observed)
    print('Theoretical asymptotic density:',expected)
    print('PASS: all checks')


if __name__=='__main__':
    main()
