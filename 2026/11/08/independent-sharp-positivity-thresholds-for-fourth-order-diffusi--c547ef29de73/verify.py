"""Reproducible exact-rational checks of the block-network Padé theorem.

This is a finite regression test, not a proof of the universal quantifiers.
"""
from fractions import Fraction as Q
from itertools import product


def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def mul(A, B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Q(0))
             for j in range(len(B[0]))] for i in range(len(A))]


def inv(A):
    n=len(A); M=[list(A[i])+eye(n)[i] for i in range(n)]
    for k in range(n):
        j=next(j for j in range(k,n) if M[j][k])
        M[k],M[j]=M[j],M[k]
        v=M[k][k]; M[k]=[x/v for x in M[k]]
        for i in range(n):
            if i!=k:
                v=M[i][k]
                M[i]=[u-v*w for u,w in zip(M[i],M[k])]
    return [row[n:] for row in M]


def D(z):
    return z*z+6*z+12


def direct(sizes,rates,b,h):
    blocks=[j for j,n in enumerate(sizes) for _ in range(n)]
    N=len(blocks)
    L=[[Q(0) for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(i+1,N):
            w=rates[blocks[i]] if blocks[i]==blocks[j] else b
            L[i][j]=L[j][i]=-w
            L[i][i]+=w;L[j][j]+=w
    L2=mul(L,L)
    num=[[h*h*L2[i][j]-6*h*L[i][j]+12*(i==j) for j in range(N)] for i in range(N)]
    den=[[h*h*L2[i][j]+6*h*L[i][j]+12*(i==j) for j in range(N)] for i in range(N)]
    return mul(num,inv(den)),blocks


def threshold(N,n,b):
    return b*(2+Q(n,N-n))


def test(sizes,rates,b,h):
    T,blocks=direct(sizes,rates,b,h)
    N=sum(sizes);gamma=N*b
    assert all(sum(row)==1 for row in T)
    allowed=all(a<=threshold(N,n,b) for a,n in zip(rates,sizes) if n>=2)
    for i in range(N):
        assert T[i][i]>0
        for j in range(N):
            if i==j:continue
            if blocks[i]!=blocks[j]:
                expected=12*h*b/D(gamma*h)
                assert expected>0
            else:
                k=blocks[i];n=sizes[k]; lam=n*rates[k]+(N-n)*b
                expected=12*h/Q(n)*(lam/D(lam*h)-(N-n)*b/D(gamma*h))
                A=lam*((N-n)*b*lam-gamma*gamma)
                B=6*lam*n*b
                C=12*n*rates[k]
                P=-A*h*h+B*h+C
                assert (expected>0)==(P>0)
                if rates[k]<=threshold(N,n,b):assert expected>0
            assert T[i][j]==expected, (sizes,rates,b,h,i,j,T[i][j],expected)
    if allowed: assert all(x>0 for row in T for x in row)
    return 1


def main():
    count=0
    for sizes in [(2,2,2),(3,2,2),(3,4,2),(2,3,1),(4,3,1),(2,2,2,1),
                  (1,1,2),(2,1),(3,3),(3,1,1),(2,2,3,2)]:
        N=sum(sizes)
        for b in [Q(1,2),Q(1),Q(3,2)]:
            bounds=[threshold(N,n,b) for n in sizes]
            for factors in product([Q(0),Q(1),Q(6,5)],repeat=len(sizes)):
                # Limit the largest combinatorial sweep while spanning all signs.
                if len(sizes)>3 and sum(f>1 for f in factors)>1:continue
                rates=[f*u for f,u in zip(factors,bounds)]
                for h in [Q(1,7),Q(1),Q(4),Q(25)]:
                    count+=test(sizes,rates,b,h)
    print('VERIFY_OK exact matrix instances:',count)

if __name__=='__main__':main()
