#!/usr/bin/env python3
"""Two independent enumerators: maximal-singleton-run composition DP and rational polynomial recurrence."""
from collections import defaultdict
from fractions import Fraction
from math import comb


def macro_dynamic(N):
    dp = {(0, 0, 0): 1}  # length, last-is-singleton-run, number of components
    for n in range(N+1):
        current = [(k,v) for k,v in dp.items() if k[0] == n]
        for (length, lastA, d), count in current:
            for l in range(2, N-n+1):
                key = (n+l, 0, d+1)
                dp[key] = dp.get(key, 0) + count
            if not lastA:
                for l in range(1, N-n+1):
                    key = (n+l, 1, d+1)
                    dp[key] = dp.get(key, 0) + count
    result = [defaultdict(int) for _ in range(N+1)]
    for (n, state, d), count in dp.items():
        if n:
            result[n][d] += count
    return result


def add(p, q, sign=1, shift=0):
    out = p.copy()
    for k,v in q.items():
        out[k+shift] = out.get(k+shift, 0) + sign*v
        if not out[k+shift]:
            del out[k+shift]
    return out


def rational_recurrence(N):
    F = [{} for _ in range(N+1)]
    for n in range(1, N+1):
        p = {1:1} if n == 1 else {2:1,1:-1} if n == 3 else {}
        if n>=1:
            p=add(p,F[n-1],2)
        if n>=2:
            p=add(p,F[n-2],-1)
            p=add(p,F[n-2],1,1)
        if n>=3:
            p=add(p,F[n-3],-1,1)
            p=add(p,F[n-3],1,2)
        F[n]=p
    return F


def extremal(n):
    k,r=divmod(n,3)
    return k+1 if r==0 else 1 if r==1 else 2*k+1+comb(k+2,2)


def main():
    N=30
    a=macro_dynamic(N)
    b=rational_recurrence(N)
    for n in range(1,N+1):
        assert dict(a[n]) == b[n], (n,a[n],b[n])
        assert sum(b[n].values())==2**(n-1)
        assert min(b[n])==1 and max(b[n])==(2*n+1)//3
        assert b[n][max(b[n])]==extremal(n)
        E=Fraction(sum(k*v for k,v in b[n].items()),2**(n-1))
        V=Fraction(sum(k*k*v for k,v in b[n].items()),2**(n-1))-E*E
        assert E == (Fraction(3*(n+1),8) if n>=3 else Fraction(1))
        expected_variance = Fraction(7*(n-1),64) if n>=5 else {1:Fraction(0),2:Fraction(0),3:Fraction(1,4),4:Fraction(23,64)}[n]
        assert V == expected_variance, (n, V, expected_variance)
    print('PASS: two independent algebraic recurrence/structural DP methods for n=1..30')
    print('n=12:',dict(sorted(b[12].items())))
    print('n=30: mean=', E,'variance=',V, 'max=',max(b[30]), 'maximizers=',b[30][max(b[30])])


if __name__=='__main__':
    main()
