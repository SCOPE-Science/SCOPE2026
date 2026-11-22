"""Finite checks for the hub–clique Sinkhorn theorem. Requires Python 3 standard library.

This script tests algebraic identities, balancing, the local derivative, and
finite-termination resonances. Finite tests do not prove all-size statements.
"""
from fractions import Fraction as F
from math import sqrt, log, exp

count = 0

def ck(test, msg):
    global count
    if not test:
        raise AssertionError(msg)
    count += 1


def matrix(m, t):
    n=m+1
    return [[(1. if i==j==0 else t if (i==0) != (j==0)
              else (2. if i==j else 1.)) for j in range(n)] for i in range(n)]

def balanced_c(m, t):
    lo,hi=0.,1./m
    for _ in range(100):
        mid=(lo+hi)/2
        # monotone LHS t(m,c) relative to t
        lhs=(m+1)*mid**2
        rhs=t*t*(1-m*mid)*(1-mid)
        if lhs<rhs:lo=mid
        else:hi=mid
    return (lo+hi)/2

def two_normalizations(A):
    n=len(A)
    row_sums=[sum(x) for x in A]
    R=[[A[i][j]/row_sums[i] for j in range(n)] for i in range(n)]
    col_sums=[sum(R[i][j] for i in range(n)) for j in range(n)]
    C=[[R[i][j]/col_sums[j] for j in range(n)] for i in range(n)]
    return R,C

def full_sweep(A, v):
    n=len(A)
    row=[sum(A[i][j]*v[j] for j in range(n)) for i in range(n)]
    u=[1/z for z in row]
    col=[sum(A[i][j]*u[i] for i in range(n)) for j in range(n)]
    return [1/z for z in col]

def matvec(A,v):return [sum(x*y for x,y in zip(row,v)) for row in A]

for m in range(2,81):
    M=m*m+2*m+2
    c1=F(1,m+2)
    c2=F(m+2,M)
    t1sq=F(m+1)*c1**2/((1-m*c1)*(1-c1))
    t2sq=F(m+1)*c2**2/((1-m*c2)*(1-c2))
    ck(t1sq==F(1,2),f'first boundary {m}')
    ck(t2sq==F((m+2)**2,2*m),f'second boundary {m}')
    ck(F(1)-(m+1)*c1 == F(1-c1,m+1),f'positive crossing {m}')
    ck(F(1)-(m+1)*c2 == -F(1-c2,m+1),f'negative crossing {m}')
    ck(c1<c2<F(1,m),f'c order {m}')
    ck((F(1)-c2)/F(m+1)==F(m,M),f'optimal contrast {m}')
    ck(sqrt((m+1)/m) < m/(m-1),f'termination order {m}')
    ck((m+2)/sqrt(2*m) >= m/(m-1)-1e-14,f'optimal order {m}')
    for t in [0.02,0.2,1/sqrt(2),sqrt((m+1)/m),m/(m-1),
              (m+2)/sqrt(2*m),3*(m+2)/sqrt(2*m),25]:
        c=balanced_c(m,t)
        a=(1-c)/(m+1)
        b=1-(m+1)*c
        ck(abs((m+1)*c*c-t*t*(1-m*c)*(1-c))<2e-10, f'c root {m},{t}')
        ck(0<c<1/m+1e-15, f'c range {m},{t}')
        ck(abs((1-m*c)+m*c-1)<5e-13, f'hub rows {m},{t}')
        ck(abs(c+(m+1)*a-1)<5e-13, f'leaf rows {m},{t}')
        # The hub-contrast eigenvector is (m,-1,...,-1).
        ck(abs((1-m*c)*m-m*c-m*b)<5e-12,f'hub eigenvalue {m},{t}')
        ck(abs(c+(m+1)*a-1)<5e-12,f'leaf-mode normalization {m},{t}')
        rate=max(a*a,b*b)
        opt=F(m,M)**2
        ck(rate+1e-10>=float(opt), f'global optimality sample {m},{t}')
    # Verify exactly the initial first row and subsequent column normalizations.
    for special in ['two', 'one']:
        t=sqrt((m+1)/m) if special=='two' else m/(m-1)
        R,C=two_normalizations(matrix(m,t))
        errR=max(abs(sum(R[i][j] for i in range(m+1))-1) for j in range(m+1))
        errC=max(abs(sum(row)-1) for row in C)
        ck(errC<1e-12,f'two-scale completion {m},{special}')
        ck((errR>1e-10) if special=='two' else (errR<1e-12), f'number of steps {m},{special}')
        ck(max(abs(sum(C[i][j] for i in range(m+1))-1) for j in range(m+1))<1e-12,
           f'column sums {m},{special}')

# Check non-resonant obstruction and actual projective Jacobian finite differences.
for m in [2,3,4,6,10]:
    for t in [0.31,0.93,1.44,2.4,7.6]:
        A=matrix(m,t)
        R,C=two_normalizations(A)
        if abs(t-m/(m-1))>1e-8 and abs(t-sqrt((m+1)/m))>1e-8:
            ck(max(abs(sum(row)-1) for row in C)>1e-7,f'not finite {m},{t}')
        c=balanced_c(m,t)
        d=[sqrt(1-m*c)]+[sqrt((1-c)/(m+1))]*m
        Fd=full_sweep(A,d)
        ck(max(abs(Fd[i]-d[i]) for i in range(m+1))<1e-10, f'fixed point {m},{t}')
        B=[[d[i]*A[i][j]*d[j] for j in range(m+1)] for i in range(m+1)]
        w=[1.,-1.]+[0.]*(m-1)
        z=matvec(B,matvec(B,w))
        eps=1e-5
        plus=full_sweep(A,[d[i]*exp(eps*w[i]) for i in range(m+1)])
        minus=full_sweep(A,[d[i]*exp(-eps*w[i]) for i in range(m+1)])
        deriv=[(log(plus[i]/d[i])-log(minus[i]/d[i]))/(2*eps) for i in range(m+1)]
        ck(max(abs(deriv[i]-z[i]) for i in range(m+1))<5e-9, f'Jacobian B squared {m},{t}')

print(f'PASS: {count} finite exact-rational and numerical assertions')
