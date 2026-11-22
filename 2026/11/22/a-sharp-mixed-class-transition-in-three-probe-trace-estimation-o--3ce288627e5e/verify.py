#!/usr/bin/env python3
"""Reproducible exact finite checks for three-class stochastic probing on balanced bicliques.

Python 3 standard library only. The infinite parameter proof is in RESULT.md.
"""
from fractions import Fraction as Q
from math import comb

CHECKS = 0

def check(x, message):
    global CHECKS
    CHECKS += 1
    if not x:
        raise AssertionError(message)

def partitions_three(n):
    # Restricted growth sequences: one representative of each unlabeled partition.
    a = [0]
    def rec(k):
        if len(a) == 2*n:
            if k == 3:
                yield tuple(a)
            return
        for j in range(min(k+1, 3)):
            a.append(j)
            yield from rec(max(k, j+1))
            a.pop()
    yield from rec(1)

def signature(part, n):
    counts = [[0, 0] for _ in range(3)]
    for i, color in enumerate(part):
        counts[color][int(i>=n)] += 1
    return counts

def pair_cost(part, n, t):
    counts = signature(part, n)
    return sum(a*(a-1)//2+b*(b-1)//2+t*a*b for a,b in counts)

def predicted(n, t):
    baseline = n*(n-1)
    if t < 2:
        assert n >= 3
        score = [n*s-s*s+(2-t)*(s*s//4) for s in range(n+1)]
        best = max(score)
        ss = [s for s,x in enumerate(score) if x == best]
        count = 0
        for s in ss:
            for a in range(s+1):
                b=s-a
                if 0<a<n and 0<b<n and a*b == s*s//4:
                    count += comb(n,a)*comb(n,b)
        return baseline-best, count, ss
    k=n//2
    pure_count = comb(n,k) if n%2==0 else 2*comb(n,k)
    if t>2:
        return baseline-(n*n//4), pure_count, [k, (n+1)//2]
    ss=sorted(set([k,(n+1)//2]))
    mixed_count=sum(comb(n,a)*comb(n,s-a)
                    for s in ss for a in range(1,s))
    return baseline-(n*n//4), pure_count+mixed_count, ss

def inverse(M):
    n=len(M)
    a=[[Q(x) for x in row]+[Q(i==j) for j in range(n)]
       for i,row in enumerate(M)]
    for i in range(n):
        pivot = next(j for j in range(i,n) if a[j][i])
        a[i],a[pivot]=a[pivot],a[i]
        p=a[i][i]
        a[i]=[x/p for x in a[i]]
        for j in range(n):
            if j!=i:
                p=a[j][i]
                a[j]=[x-p*y for x,y in zip(a[j],a[i])]
    return [row[n:] for row in a]

def exact_green_test(n, mu):
    N=2*n
    H=[[Q(0) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        H[i][i]=mu+n
        for j in range(N):
            if (i<n)!=(j<n):H[i][j]=-1
    G=inverse(H)
    near=Q(n)/(mu*(mu+n)*(mu+2*n))
    far=Q(1)/(mu*(mu+2*n))
    for i in range(N):
        for j in range(N):
            expected=(far if ((i<n)!=(j<n)) else
                       (near+(1/(mu+n) if i==j else 0)))
            check(G[i][j]==expected, f'inverse n={n} mu={mu} {i,j}')
    for part in partitions_three(n):
        t=(far/near)**2
        from_matrix = sum(G[i][j]**2 for i in range(N)
                          for j in range(i+1,N) if part[i]==part[j])
        check(from_matrix==near**2*pair_cost(part,n,t), 'direct variance')


def main():
    for n in range(3,7):
        for t in [Q(101,100),Q(5,4),Q(3,2),Q(7,4),Q(199,100),
                  Q(2),Q(201,100),Q(3),Q(5)]:
            values=[pair_cost(part,n,t) for part in partitions_three(n)]
            found=min(values)
            expected,count,ss=predicted(n,t)
            check(found==expected, f'objective n={n}, t={t}, got {found} expected {expected}')
            check(values.count(found)==count,
                  f'optimizer count n={n}, t={t}, got {values.count(found)} expected {count}')
    for n in range(3,6):
        for mu in [Q(1,3),Q(1),Q(2)]:
            exact_green_test(n,mu)
    for n in range(3,30):
        for t in [Q(51,50),Q(5,4),Q(3,2),Q(7,4),Q(199,100)]:
            F=lambda s:n*s-s*s+(2-t)*(s*s//4)
            for s in range(1,n-1):
                diff=F(s+1)-F(s)
                check(diff==n-2*s-1+(2-t)*((s+1)//2),'difference')
                if s+2<=n:
                    check(F(s+2)-F(s+1)<diff,'strict concavity')
    print('PASS exact assertions:', CHECKS)
    print('Complete unlabeled partitions n=3..6, nine cross/within ratios, optimizer counts.')
    print('Direct rational inverses and pair variances n=3..5 at three screening shifts.')
    print('Discrete-gain and strict-concavity tests n=3..29; universal proof is analytic.')

if __name__=='__main__':
    main()
