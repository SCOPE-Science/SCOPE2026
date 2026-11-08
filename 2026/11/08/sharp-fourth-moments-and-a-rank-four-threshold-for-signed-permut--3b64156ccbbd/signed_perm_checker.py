"""Exact moment and extremizer checks for signed-permutation matrix coefficients."""
from fractions import Fraction as Q
from itertools import permutations,product

def moments_direct(A):
    n=len(A)
    E2=Q(0); E4=Q(0)
    for pi in permutations(range(n)):
        for signs in product((-1,1),repeat=n):
            x=sum(signs[i]*A[i][pi[i]] for i in range(n))
            E2+=x*x
            E4+=x**4
    scale=Q(1, __import__('math').factorial(n)*2**n)
    return E2*scale,E4*scale

def moment_formula(A):
    n=len(A)
    S=sum(x*x for row in A for x in row)
    U=sum(x**4 for row in A for x in row)
    D=sum(A[i][j]**2*A[k][l]**2 for i in range(n) for j in range(n)
          for k in range(i+1,n) for l in range(n) if l!=j)
    return Q(S,n), Q(U,n)+Q(6*D,n*(n-1))

def ratio(A):
    s,m=moment_formula(A)
    return m/(s*s)

def check():
    samples=0
    for n in (2,3,4):
        arrays=[]
        for shift in range(3):
            arrays.append([[((7*i+11*j+3*shift+5*i*j) % 9)-4 for j in range(n)] for i in range(n)])
        arrays.append([[1 if i==j else 0 for j in range(n)] for i in range(n)])
        arrays.append([[1 if i==0 else 0 for j in range(n)] for i in range(n)])
        arrays.append([[1 if i==0 and j==0 else 0 for j in range(n)] for i in range(n)])
        for a in arrays:
            d= moments_direct(a)
            f= moment_formula(a)
            assert d==f,(n,a,d,f)
            r=ratio(a)
            assert 1<=r<=max(4,n),(n,a,r)
            samples+=1
    print('EXACT_FULL_GROUP_SECOND_AND_FOURTH_MOMENTS_OK', samples)
    for n in range(2,18):
        e=[[int(i==0 and j==0) for j in range(n)] for i in range(n)]
        star=[[int(i==0) for j in range(n)] for i in range(n)]
        match=[[int(i==j) for j in range(n)] for i in range(n)]
        assert ratio(star)==1
        assert ratio(e)==n
        assert ratio(match)==4
        if n==4:
            w=[[int(i==j)*(i+1) for j in range(n)] for i in range(n)]
            assert ratio(w)==4
        for a in (e,star,match):
            S=sum(a[i][j]**2 for i in range(n) for j in range(n))
            b=[[Q(a[i][j]**2,S) for j in range(n)] for i in range(n)]
            P=sum(b[i][j]*b[k][l] for i in range(n) for j in range(n)
                  for k in range(i,n) for l in range(n) if (k>i or l>j) and (i==k or j==l))
            D=sum(b[i][j]*b[k][l] for i in range(n) for j in range(n)
                  for k in range(i+1,n) for l in range(n) if j!=l)
            T=sum(z*z for row in b for z in row)
            assert T+2*P+2*D==1
            assert ratio(a)==n*T+Q(6*n,n-1)*D
            if n>=4:
                assert n-ratio(a)==2*n*P+2*Q(n*(n-4),n-1)*D
    print('EXACT_END_POINT_AND_UPPER_DEFICIT_WITNESSES_OK', 'n=2..17')
    for n in (2,3,4,5,6):
        A=[[((i+2)*(j+3)+7*i*j)%7-3 for j in range(n)] for i in range(n)]
        E2,E4=moment_formula(A)
        S=sum(a*a for row in A for a in row)
        Y=[sum(A[i][pi[i]]**2 for i in range(n)) for pi in permutations(range(n))]
        EY2=Q(sum(y*y for y in Y),len(Y))
        Var=EY2-E2*E2
        D=sum(A[i][j]**2*A[k][l]**2 for i in range(n) for j in range(n) for k in range(i+1,n) for l in range(n) if j!=l)
        assert E4-E2*E2 == Var + Q(4*D,n*(n-1))
    print('EXACT_TWO_NONNEGATIVE_LOWER_DEFICIT_TERMS_OK')
    print('ALL_SIGNED_PERMUTATION_MATRIX_COEFFICIENT_CHECKS_OK')
if __name__=='__main__':
    check()
