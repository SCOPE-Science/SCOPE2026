"""Exact independent finite-state verification of clique-petal voter absorption."""
from fractions import Fraction as F
from math import factorial, comb


def determinant(a):
    a = [list(row) for row in a]
    n = len(a)
    if n == 0:
        return F(1)
    sign = 1
    det = F(1)
    for k in range(n):
        j = next((j for j in range(k, n) if a[j][k]), None)
        if j is None:
            return F(0)
        if j != k:
            a[j], a[k] = a[k], a[j]
            sign = -sign
        p = a[k][k]
        det *= p
        for i in range(k+1, n):
            b = a[i][k] / p
            if b:
                for l in range(k+1, n):
                    a[i][l] -= b * a[k][l]
                a[i][k] = F(0)
    return det*sign


def solve(a,b):
    n=len(a)
    z=[list(a[i])+[b[i]] for i in range(n)]
    for k in range(n):
        p=next(i for i in range(k,n) if z[i][k])
        z[p],z[k]=z[k],z[p]
        pivot=z[k][k]
        for j in range(k,n+1): z[k][j]/=pivot
        for i in range(n):
            if i==k: continue
            val=z[i][k]
            for j in range(k,n+1): z[i][j]-=val*z[k][j]
    return [z[i][-1] for i in range(n)]


def birth_death_generator(r):
    # k=1,...,r counts initial negative voters; hub is permanently positive.
    Q=[[F(0) for _ in range(r)] for _ in range(r)]
    for k in range(1,r+1):
        death=F(k*(r-k+1),r)
        birth=F(k*(r-k),r)
        Q[k-1][k-1]=-(death+birth)
        if k>1: Q[k-1][k-2]=death
        if k<r: Q[k-1][k]=birth
    return Q


def laplace_via_generator(r,s):
    Q=birth_death_generator(r)
    mat=[[F(s if i==j else 0)-Q[i][j] for j in range(r)] for i in range(r)]
    rhs=[F(0)]*r
    rhs[0]=F(1) # rate of transition 1 -> 0
    return solve(mat,rhs)[-1]


def survival_coeff(r,j):
    return F((-1)**(j-1)*2*factorial(r)**2, factorial(r-j)*factorial(r+j))


def main():
    nchecks=0
    for r in range(1,11):
        Q=birth_death_generator(r)
        for s in [F(1,3),F(1),F(5,2),F(11)]:
            expected=F(1)
            for k in range(1,r+1):
                rate=F(k*k,r)
                expected *=rate/(rate+s)
            got=laplace_via_generator(r,s)
            assert got==expected,(r,s,got,expected)
            nchecks+=1
            mat=[[F(s if i==j else 0)-Q[i][j] for j in range(r)] for i in range(r)]
            char=determinant(mat)
            prod=F(1)
            for k in range(1,r+1): prod*=s+F(k*k,r)
            assert char==prod,(r,s,char,prod)
            nchecks+=1
        # The unforced original birth-death mean and the coalescent mean coincide.
        mean=solve([[-v for v in row] for row in Q],[F(1)]*r)[-1]
        mean_expected=sum([F(r,k*k) for k in range(1,r+1)],F(0))
        assert mean==mean_expected,(r,mean,mean_expected)
        nchecks+=1
        coeffs=[survival_coeff(r,j) for j in range(1,r+1)]
        assert sum(coeffs,F(0))==1
        nchecks+=1
        for k in range(1,r):
            assert sum([coeffs[j-1]*j**(2*k) for j in range(1,r+1)],F(0))==0
            nchecks+=1
        assert coeffs[0]==F(2*r,r+1)
        nchecks+=1
    print('VOTER_CLIQUE_EXACT_GEN_CHECK_PASSED', nchecks)


if __name__=='__main__': main()
