"""Exact finite checks of low-degree Fourier sampling on Hamming shells.

Standalone standard-library script.  The infinite-parameter theorem is proved in RESULT.md;
finite matrix identities here are independent checks for the specified small cases.
"""
from fractions import Fraction as F
from itertools import combinations,product
from math import comb


def spectrum(q,n,k):
    p=F(q-1,q);v=p*(1-p)
    a=lambda j: F(__import__('math').prod(k-t for t in range(j)),__import__('math').prod(n-t for t in range(j)))
    a1,a2,a3,a4=[a(j) for j in range(1,5)]
    z=q-2
    out=[
        (1+n*(a1-p)**2/v+comb(n,2)*(a2-2*p*a1+p*p)**2/v**2,1),
        ((a1-a2)/v*(1+(n-2)*(F(k-1,n-2)-p)**2/v),n-1),
        ((a2-2*a3+a4)/v**2,n*(n-3)//2),
        ((a1/p)*(1+(n-1)*(F(k-1,n-1)-p)**2/v),n*z),
        ((a1/p)*F((k-1)*(n-k),(n-1)*(n-2))/v,n*(n-2)*z),
        (a2/p**2,comb(n,2)*z*z),
    ]
    assert all(val>0 for val,_ in out)
    assert sum(mult for _,mult in out)==comb(n,2)*(q-1)**2
    return out


def matrix(q,n,k):
    words=[]
    for support in combinations(range(n),k):
        for vals in product(range(1,q),repeat=k):
            x=[0]*n
            for i,v in zip(support,vals):x[i]=v
            words.append(tuple(x))
    N=len(words); assert N==comb(n,k)*(q-1)**k
    B=[]
    for x in words:
        row=[]
        for y in words:
            s=sum(q*(x[i]==y[i])-1 for i in range(n))
            squares=sum((q*(x[i]==y[i])-1)**2 for i in range(n))
            row.append(1+s+(s*s-squares)//2)
        B.append(row)
    return B


def times(A,B):
    n=len(A)
    Bt=list(zip(*B))
    return [[sum(a*b for a,b in zip(row,col)) for col in Bt] for row in A]


def check(q,n,k):
    B=matrix(q,n,k);N=len(B)
    vals={}
    for lam,mult in spectrum(q,n,k):
        mu=lam*N
        assert mu.denominator==1,(q,n,k,mu)
        vals[int(mu)]=vals.get(int(mu),0)+mult
    if N>sum(vals.values()):vals[0]=N-sum(vals.values())
    # B is q^n times the matrix of the restricted orthogonal Fourier projector.
    P=[[int(i==j) for j in range(N)] for i in range(N)]
    for power in range(len(vals)):
        actual=sum(P[i][i] for i in range(N))
        expected=sum(m*value**power for value,m in vals.items())
        assert actual==expected,('moment',q,n,k,power,actual,expected)
        P=times(P,B)
    # The predicted minimal polynomial annihilates the actual integer matrix.
    poly=[[int(i==j) for j in range(N)] for i in range(N)]
    for mu in vals:
        product_matrix=times(poly,B)
        poly=[[product_matrix[i][j]-mu*poly[i][j] for j in range(N)] for i in range(N)]
    assert all(all(z==0 for z in row) for row in poly),('annihilator',q,n,k)
    print('EXACT_OK',f'q={q}',f'n={n}',f'k={k}',f'shell={N}',f'spectrum_levels={len(vals)}',f'rank={sum(vals.values())-vals.get(0,0)}')


def main():
    for q,n,k in ((3,4,2),(3,5,2),(3,5,3),(4,4,2)):
        check(q,n,k)
    print('VERIFY_OK cases=4 exact_integer_spectral_moments_and_annihilators=PASS')

if __name__=='__main__':main()
