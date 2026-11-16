#!/usr/bin/env python3
"""Finite exact and numerical verification of cyclic extrema covariance theorem."""
import itertools, math, cmath
from fractions import Fraction


def covariances(n):
    cnt=math.factorial(n)
    totals=[[0]*n for _ in range(2)]
    pairs=[[[[0]*n for _ in range(n)] for __ in range(2)] for ___ in range(2)]
    for p in itertools.permutations(range(n)):
        pp=[int(p[i-1]<p[i]>p[(i+1)%n]) for i in range(n)]
        vv=[int(p[i-1]>p[i]<p[(i+1)%n]) for i in range(n)]
        x=[pp,vv]
        for a in range(2):
            for i in range(n):
                totals[a][i]+=x[a][i]
                if not x[a][i]: continue
                for b in range(2):
                    for j in range(n):
                        pairs[a][b][i][j]+=x[b][j]
    return [[[[Fraction(pairs[a][b][i][j],cnt)-Fraction(totals[a][i]*totals[b][j],cnt*cnt)
        for j in range(n)] for i in range(n)] for b in range(2)] for a in range(2)]


def theorem(n, a,b, i,j):
    d=(j-i)%n
    if d not in (0,1,2,n-1,n-2): return Fraction(0)
    if a==b:
        table={0:Fraction(2,9),1:-Fraction(1,9),2:Fraction(1,45)}
    else:
        table={0:-Fraction(1,9),1:Fraction(7,72),2:-Fraction(7,360)}
    return table[min(d,n-d)]


def bands(n,j):
    c=math.cos(2*math.pi*j/n)
    return ((19-5*c+2*c*c)/180,(1-c)*(3-2*c)/12)


def test():
    count=0
    for n in range(5,9):
        c=covariances(n)
        for a in range(2):
            for b in range(2):
                for i in range(n):
                    for j in range(n):
                        assert c[a][b][i][j] == theorem(n,a,b,i,j), (n,a,b,i,j,c[a][b][i][j],theorem(n,a,b,i,j))
                        count += 1
        for j in range(n):
            # exact Fourier sums of covariance and their two eigenvalues
            q=cmath.exp(-2j*math.pi*j/n)
            A=sum(float(c[0][0][0][k])*(q**k) for k in range(n))
            B=sum(float(c[0][1][0][k])*(q**k) for k in range(n))
            plus,minus=bands(n,j)
            assert abs(A+B-plus)<1e-12
            assert abs(A-B-minus)<1e-12
            count+=2
        plus=[bands(n,j)[0] for j in range(n)]
        minus=[bands(n,j)[1] for j in range(n)]
        assert min(plus)>0
        assert abs(minus[0])<1e-13
        assert min(minus[1:])>0
        assert abs(max(plus+minus)-minus[n//2])<1e-12
        assert abs(min(plus+minus[1:])- (Fraction(4,45) if n==5 else minus[1]))<1e-12
        count+=5
    for n in range(5,601):
        eigen=[bands(n,j) for j in range(n)]
        minpos=min(p for p,m in eigen)
        minpos=min(minpos,min(m for _,m in eigen[1:]))
        maxe=max(max(p,m) for p,m in eigen)
        cmax=-1 if n%2==0 else -math.cos(math.pi/n)
        goalmax=(1-cmax)*(3-2*cmax)/12
        goalmin=(Fraction(4,45) if n==5 else (1-math.cos(2*math.pi/n))*(3-2*math.cos(2*math.pi/n))/12)
        assert abs(maxe-goalmax)<2e-13, (n,maxe,goalmax)
        assert abs(minpos-goalmin)<2e-13, (n,minpos,goalmin)
        count += 2
    for n in [101,1001,10001,100001]:
        c=math.cos(2*math.pi/n)
        cmin=-math.cos(math.pi/n)
        kap=((1-cmin)*(3-2*cmin))/((1-c)*(3-2*c))
        expected=5/math.pi**2
        assert abs(kap/n**2-expected)<3e-3
        count+=1
    print(f'PASS: {count} finite exact/numerical assertions; n=5..8 full covariance; n=5..600 extrema; asymptotic samples.')

if __name__=='__main__':test()
