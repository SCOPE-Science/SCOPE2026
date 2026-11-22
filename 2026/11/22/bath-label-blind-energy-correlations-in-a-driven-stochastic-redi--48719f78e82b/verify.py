"""Independent stationary moment-identity checks for star energy redistribution.

This code evaluates the polynomial Markov generator on all monomials of degree at most two,
then checks the stated stationary moments by exact rational arithmetic.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import factorial, comb


def stationary_moments(N, rate, hot, cold):
    assert N % 2 == 0 and N >= 2 and rate > 0 and hot > 0 and cold > 0
    T = (hot + cold) / 2
    delta = (hot - cold) / 2
    alpha = 2 * rate / (1 + 2 * rate)
    D = (1 + 2 * rate) ** 2 * (N + 2 * rate + 1)
    means = [T] + [T + alpha * delta] * (N // 2) + [T - alpha * delta] * (N // 2)
    hub_var = T*T + (2*rate/(1+2*rate) + 2*(rate+1)/D) * delta*delta
    moments = {(): F(1)}
    for i, v in enumerate(means):
        moments[(i,)] = v
    moments[(0,0)] = T*T + hub_var
    for i in range(1,N+1):
        s=1 if i<=N//2 else -1
        leaf_var = T*T + 2*T*s*alpha*delta + (4*rate/(1+2*rate)-alpha*alpha + 2/D)*delta*delta
        moments[(i,i)] = means[i]*means[i]+leaf_var
        moments[(0,i)] = means[0]*means[i] + delta*delta/((1+2*rate)*(N+2*rate+1))
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            moments[(i,j)] = means[i]*means[j] + delta*delta/D
    return moments


def edge_update(poly, i, j):
    out = {}
    for mono,c in poly.items():
        power_i = mono.count(i)
        power_j = mono.count(j)
        n = power_i+power_j
        others = tuple(x for x in mono if x!=i and x!=j)
        # E[U^p(1-U)^q] * (x_i+x_j)^(p+q)
        beta = F(factorial(power_i)*factorial(power_j),factorial(n+1))
        for k in range(n+1):
            new = tuple(sorted(others + (i,)*k + (j,)*(n-k)))
            out[new] = out.get(new,F(0)) + c*beta*comb(n,k)
    return out


def bath_update(poly,i,temp):
    out={}
    for mono,c in poly.items():
        power=mono.count(i)
        new=tuple(x for x in mono if x!=i)
        out[new]=out.get(new,F(0))+c*factorial(power)*temp**power
    return out


def check(N,rate,hot,cold):
    moments=stationary_moments(N,rate,hot,cold)
    for mono in moments:
        test={(mono):F(1)}
        target=moments[mono]
        residual=F(0)
        for i in range(1,N+1):
            new=edge_update(test,0,i)
            residual += sum(c*moments[m] for m,c in new.items())-target
            new=bath_update(test,i, hot if i<=N//2 else cold)
            residual += rate*(sum(c*moments[m] for m,c in new.items())-target)
        assert residual == 0,(N,rate,hot,cold,mono,residual)
    return len(moments)


def main():
    count=0
    for N in (2,4,6,8,10):
        for rate in (F(1,7),F(1),F(5,3),F(17)):
            for hot,cold in ((F(2),F(1)),(F(9,4),F(1,3)),(F(5),F(5))):
                count+=check(N,rate,hot,cold)
    print('STAR_KMP_ALL_DEGREE_TWO_GENERATOR_IDENTITIES_PASSED',count)

if __name__ == '__main__': main()
