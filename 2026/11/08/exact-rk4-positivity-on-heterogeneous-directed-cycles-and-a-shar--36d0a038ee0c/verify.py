#!/usr/bin/env python3
"""Exact entry replay and numerical boundary stress checks for directed-cycle RK4.

Uses Python 3 standard library only. The analytic proof in RESULT.md establishes
all positive real rates and arbitrary cycle length >=5; these tests do not
replace its infinite-parameter argument.
"""
from fractions import Fraction as F
from math import factorial
from random import Random


def product(values):
    result = 1
    for value in values:
        result *= value
    return result


def h2(values):
    return sum((a*b for i, a in enumerate(values)
                for b in values[i:]), F(0))


def h3_pair(a, b):
    return a**3 + a*a*b + a*b*b + b**3


def direct_entry(rates, step, start, distance):
    n = len(rates)
    v = [rates[(start + j) % n] for j in range(distance + 1)]
    if distance == 0:
        z = step*v[0]
        return 1-z+z*z/2-z**3/6+z**4/24
    prefix = product(v[:-1])*step**distance
    if distance == 1:
        a,b = v
        return prefix*(1-step*(a+b)/2
                       +step**2*(a*a+a*b+b*b)/6
                       -step**3*h3_pair(a,b)/24)
    if distance == 2:
        return prefix*(F(1,2)-step*sum(v)/6
                       +step**2*h2(v)/24)
    if distance == 3:
        return prefix*(F(1,6)-step*sum(v)/24)
    if distance == 4:
        return prefix/F(24)
    return F(0)


def matmul(A, B):
    n = len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(n)), F(0))
             for j in range(n)] for i in range(n)]


def rk4_matrix(rates, step):
    n = len(rates)
    Q = [[F(0) for _ in range(n)] for _ in range(n)]
    for i,r in enumerate(rates):
        Q[i][i] -= r
        Q[i][(i+1) % n] += r
    power = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    answer = [row[:] for row in power]
    for k in range(1,5):
        power = matmul(power, Q)
        coefficient = step**k/F(factorial(k))
        for i in range(n):
            for j in range(n):
                answer[i][j] += coefficient*power[i][j]
    return answer


def one_jump(a,b,h):
    return (1-(a+b)*h/2+(a*a+a*b+b*b)*h*h/6
            -(a**3+a*a*b+a*b*b+b**3)*h**3/24)


def root_bisection(fn, high):
    lo=0.0
    hi=float(high)
    while fn(hi)>0:
        hi *= 2
    for _ in range(90):
        mid=(lo+hi)/2
        if fn(mid)>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def threshold(rates):
    n=len(rates)
    one=min(root_bisection(lambda h: one_jump(float(rates[i]),
                        float(rates[(i+1)%n]),h),
                        4/max(float(rates[i]),float(rates[(i+1)%n])))
            for i in range(n))
    three=min(4/sum(float(rates[(i+j)%n]) for j in range(4))
              for i in range(n))
    return min(one,three)


def main():
    rng=Random(20261102)
    exact=0
    row_checks=0
    for n in range(5,11):
        for _ in range(40):
            rates=[F(rng.randint(1,19),rng.randint(1,11)) for _ in range(n)]
            step=F(rng.randint(1,11),rng.randint(1,6))
            matrix=rk4_matrix(rates,step)
            for i in range(n):
                assert sum(matrix[i])==1
                row_checks+=1
                for j in range(n):
                    d=(j-i)%n
                    assert matrix[i][j]==direct_entry(rates,step,i,d)
                    exact+=1
    print('exact entry comparisons:', exact)
    print('exact row sum comparisons:',row_checks)

    # Inspect both sides of the nonnegative endpoint using the independent
    # polynomial-formula matrix; the analytic proof gives an exact boundary.
    boundary=0
    for n in range(5,11):
        for _ in range(100):
            rates=[F(rng.randint(1,50),rng.randint(1,11)) for _ in range(n)]
            t=threshold(rates)
            for mul,expected in [(0.999,True),(1.001,False)]:
                h=F.from_float(t*mul)
                entries=[float(direct_entry(rates,h,i,k))
                         for i in range(n) for k in range(n)]
                got=all(x>=-1e-11 for x in entries)
                assert got==expected,(n,rates,t,mul,min(entries))
                boundary+=1
    print('two-sided boundary comparisons:',boundary)

    for R in [F(1),F(2),F(4),F(5),F(10),F(100)]:
        t=F(4)/(R+3)
        f=one_jump(R,F(1),t)
        g=3*R**3-9*R*R-15*R-43
        assert f == -g/(3*(R+3)**3)
    print('exact single-defect phase identities:',6)

    alpha=root_bisection(lambda z:1-z/2+z*z/6-z**3/24,4)
    root=root_bisection(lambda R:-(3*R**3-9*R*R-15*R-43),5)
    assert abs(alpha-2.785293563405282)<1e-12
    assert abs(root-4.70845296658594)<1e-12
    print('sharp universal limiting factor:',f'{alpha:.15f}')
    print('single-defect phase boundary:',f'{root:.15f}')
    print('PASS')


if __name__=='__main__':
    main()
