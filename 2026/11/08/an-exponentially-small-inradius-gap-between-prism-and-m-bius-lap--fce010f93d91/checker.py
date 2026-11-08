"""Reproducible finite checks for a comparison of two canonical Laplacian simplices.
Python 3 standard library only; exact rational pseudoinverse matrices and independent spectral formulas.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
from math import cos, pi, sqrt, isclose


def graph_laplacian(m, kind):
    n=2*m
    edges=set()
    if kind=='prism':
        for t in range(2):
            for j in range(m):
                a=t*m+j; b=t*m+(j+1)%m
                edges.add(tuple(sorted((a,b))))
        for j in range(m):edges.add((j,m+j))
    elif kind=='mobius':
        for j in range(n):edges.add(tuple(sorted((j,(j+1)%n))))
        for j in range(m):edges.add((j,m+j))
    else:raise ValueError(kind)
    L=[[F(0) for _ in range(n)] for _ in range(n)]
    for a,b in edges:
        L[a][a]+=1;L[b][b]+=1;L[a][b]-=1;L[b][a]-=1
    assert all(sum(row)==0 for row in L)
    assert all(L[j][j]==3 for j in range(n))
    return L


def inverse(M):
    n=len(M)
    A=[M[i][:]+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        piv=next(i for i in range(k,n) if A[i][k])
        if piv!=k:A[k],A[piv]=A[piv],A[k]
        den=A[k][k];A[k]=[x/den for x in A[k]]
        for i in range(n):
            if i!=k and A[i][k]:
                fac=A[i][k]
                A[i]=[x-fac*y for x,y in zip(A[i],A[k])]
    return [row[n:] for row in A]


def exact_trace(m, kind):
    L=graph_laplacian(m,kind);n=len(L)
    K=[[v+F(1,n) for v in row] for row in L]
    Q=inverse(K)
    Z=[[v-F(1,n) for v in row] for row in Q]
    # Full pseudoinverse certificate, not just numerical evaluation.
    assert all(sum(row)==0 for row in Z)
    assert all(sum(L[i][k]*Z[k][j] for k in range(n))==F(int(i==j))-F(1,n) for i in range(n) for j in range(n))
    return sum(v*v for row in Z for v in row)


def closed(m,kind):
    with localcontext() as ctx:
        ctx.prec=70
        r3=Decimal(3).sqrt();q=Decimal(2)-r3;h=q**m
        cm=Decimal((m*m-1)*(m*m+11))/Decimal(720)
        if kind=='prism':
            return cm+Decimal(m)/(6*r3)*(1+h)/(1-h)+Decimal(m*m)*h/(6*(1-h)**2)
        return cm+Decimal(m)/(6*r3)*(1-h)/(1+h)-Decimal(m*m)*h/(6*(1+h)**2)


def difference(m):
    with localcontext() as ctx:
        ctx.prec=70
        q=Decimal(2)-Decimal(3).sqrt();h=q**m
        return Decimal(m)*h/3*(2/(Decimal(3).sqrt()*(1-h*h))+Decimal(m)*(1+h*h)/(1-h*h)**2)


def main():
    count=0
    for m in range(3,11):
        a=exact_trace(m,'prism'); b=exact_trace(m,'mobius')
        with localcontext() as ctx:
            ctx.prec=65
            A=Decimal(a.numerator)/Decimal(a.denominator)
            B=Decimal(b.numerator)/Decimal(b.denominator)
            assert abs(A-closed(m,'prism'))<Decimal('1e-50')
            assert abs(B-closed(m,'mobius'))<Decimal('1e-50')
            assert abs((A-B)-difference(m))<Decimal('1e-50')
            assert a>b
            assert isclose((2*m*float(a))**-.5,(2*m*float(closed(m,'prism')))**-.5,rel_tol=1e-12)
        print('m=',m, 'exact gap=',a-b)
        count+=1
    with localcontext() as ctx:
        ctx.prec=70
        for m in range(3,50):
            a=closed(m,'prism');b=closed(m,'mobius')
            assert a>b
            assert abs((a-b)-difference(m))<Decimal('1e-40')
    print('PRISM_MOBIUS_LAPLACIAN_SIMPLEX_CHECKS_PASSED exact_m=',count,'spectral_m=47')

if __name__=='__main__':main()
