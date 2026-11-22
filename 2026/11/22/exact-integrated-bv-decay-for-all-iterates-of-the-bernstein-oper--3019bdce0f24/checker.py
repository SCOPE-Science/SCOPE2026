from fractions import Fraction as F
from math import comb

def mul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(len(B[0]))] for i in range(len(A))]
def row_mul(v,A):
    return [sum((v[k]*A[k][j] for k in range(len(v))),F(0)) for j in range(len(A[0]))]
count=0
for n in range(2,10):
    N=n+1
    A=[[F(comb(n,j)*i**j*(n-i)**(n-j),n**n) for j in range(N)] for i in range(N)]
    assert all(sum(row)==1 and sum(F(j,n)*row[j] for j in range(N))==F(i,n) for i,row in enumerate(A))
    P=[[F(int(i==j)) for j in range(N)] for i in range(N)]
    mu=[F(1,N)]*N
    for r in range(1,9):
        # mu distribution for uniform x initial, after r iterations
        if r==1: pass
        else: mu=row_mul(mu,A)
        c=sum(mu[1:n])/2
        if r==1: assert c==F(n-1,2*(n+1))
        assert c>0
        for k in range(1,32):
            x=F(k,32)
            p=[F(comb(n,j))*x**j*(1-x)**(n-j) for j in range(N)]
            if r>1:p=row_mul(p,P)
            e1=sum((p[j]*(1-F(j,n)) for j in range(1,n)),F(0))
            en=sum((p[j]*F(j,n) for j in range(1,n)),F(0))
            for j in range(1,N):
                e=sum(p[a] for a in range(j,N))-x
                assert abs(e)<=max(e1,en)
                if j<=n//2+1:assert abs(e)<=e1
                else:assert abs(e)<=en
                count+=1
        P=mul(P,A)
print('PASS exact rational pointwise tests',count,'for n=2..9,r=1..8,31 rational x; mass/mean and first-iterate constants')
