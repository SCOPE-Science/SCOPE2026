"""Exact tests for centered hypersimplex quadratic-evaluation frames.
Run: python checker.py
Standard-library only. The general proof is independent of these finite checks.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def C(n, r):
    return comb(n, r) if 0 <= r <= n else 0


def frame_spectrum(n, k):
    assert n >= 5 and 2 <= k <= n // 2
    l1 = F(n*(n-2*k)**2, (n-2)*k*k*(n-k)**2)*C(n-2,k-1)
    l2 = F(2*n*n, k*k*(n-k)**2)*C(n-4,k-2)
    return l1, l2


def gram(n, k):
    subsets = [frozenset(s) for s in combinations(range(n),k)]
    M = len(subsets)
    G = [[F((n*len(a&b)-k*k)**2,k*k*(n-k)**2)-F(1,n-1)
          for b in subsets] for a in subsets]
    return G


def matmul(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]


def exact_spectrum_check(n, k):
    G = gram(n, k)
    a,b = frame_spectrum(n,k)
    M=len(G)
    # Generalized Johnson projective Gram has only 0,a,b as eigenvalues.
    H=matmul(G,G)
    assert all(sum(G[i][j] for j in range(M))==0 for i in range(M))
    # Multiplicities from the trace and second trace; check matrix annihilator.
    assert sum(G[i][i] for i in range(M)) == (n-1)*a + F(n*(n-3),2)*b
    assert sum(H[i][i] for i in range(M)) == (n-1)*a*a + F(n*(n-3),2)*b*b
    for i in range(M):
        for j in range(M):
            lhs=sum(H[i][h]*G[h][j] for h in range(M))
            assert lhs == (a+b)*H[i][j]-a*b*G[i][j], (n,k,i,j)
    return M*M+2*M+2


def pell_solutions(num):
    x,m=2,1
    for r in range(1,num+1):
        n=x+1
        assert x*x-3*m*m==1
        assert (n-m)%2==0
        k=(n-m)//2
        if r>=2:
            assert 2 <= k < n/2
            assert k*(n-k)==n*(n+1)//6
            l1,l2=frame_spectrum(n,k)
            assert l1==l2
        yield r,n,k
        x,m=2*x+3*m,x+2*m


def main():
    checks=0
    for n,k in [(5,2),(6,2),(7,2),(8,2),(8,3)]:
        checks+=exact_spectrum_check(n,k)
    pairs=list(pell_solutions(8))
    assert pairs[:5]==[(1,3,1),(2,8,2),(3,27,6),(4,98,21),(5,363,77)]
    checks+=8
    # All frame-tight pairs with n<=200 belong to the Pell list.
    known={(n,k) for r,n,k in pairs if n<=200 and r>=2}
    for n in range(5,201):
        for k in range(2,n//2+1):
            a,b=frame_spectrum(n,k)
            assert (a==b)==((n,k) in known)
            checks+=1
    print('EXACT_FRAME_CHECKS_PASS',checks)
    print('FIRST_FIVE_PELL_PAIRS',pairs[:5])

if __name__=='__main__':
    main()
