"""Exact rational spot checks for a five-state absorbing pure-birth SDIRK update.
The universal assertions are proved in RESULT.md, not by finite tests.
Run: python verify.py (Python 3.10+ standard library only).
"""
from fractions import Fraction as F
from math import sqrt

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def add(A,B):
    return [[a+b for a,b in zip(aa,bb)] for aa,bb in zip(A,B)]

def scale(A,s):
    return [[s*a for a in row] for row in A]

def inv(A):
    n=len(A)
    rows=[list(row)+list(idrow) for row,idrow in zip(A,eye(n))]
    for i in range(n):
        p=next(k for k in range(i,n) if rows[k][i])
        rows[i],rows[p]=rows[p],rows[i]
        fac=rows[i][i]
        rows[i]=[x/fac for x in rows[i]]
        for k in range(n):
            if k!=i:
                fac=rows[k][i]
                rows[k]=[u-fac*v for u,v in zip(rows[k],rows[i])]
    return [row[n:] for row in rows]

def generator(n):
    Q=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n-1):
        Q[i][i]=-1;Q[i][i+1]=1
    return Q

def stage_matrix(n,h,x):
    I=eye(n);Q=generator(n)
    T=inv(add(I,scale(Q,-h*x)))
    K1=mul(Q,T)
    K2=mul(add(I,scale(K1,h*(1-2*x))),mul(Q,T))
    return add(I,scale(add(K1,K2),h/2))

def explicit_coeffs(h,x):
    t=1+h*x
    r=(2+h*(4*x-2)+h*h*(2*x*x-4*x+1))/(2*t*t)
    b1=h*(1+h*(3*x-1))/(t**3)
    b2=h*h*(1+h*(6*x*x-2*x))/(2*t**4)
    b3=h**3*x*(1-x+h*x*(3*x-1))/(t**5)
    tail=[1-r,
          h*h*(1+h*x*(4*x-1))/(2*t**3),
          h**3*x*(2*(1-x)+h*x*(4*x-1))/(2*t**4),
          h**4*x*x*(3-4*x+h*x*(4*x-1))/(2*t**5)]
    return r,[b1,b2,b3],tail

def exact_matrix(n,h,x):
    r,bs,ta=explicit_coeffs(h,x)
    M=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n-1):
        for j in range(i,n-1):
            M[i][j]=r if j==i else bs[j-i-1]
        M[i][n-1]=ta[n-i-2]
    M[n-1][n-1]=1
    return M

def pred_positive(h,x):
    r,bs,ta=explicit_coeffs(h,x)
    return r>=0 and ta[3]>=0

def p_formula(h):
    h=float(h)
    if h<=0: return 1.0
    if h<1/3:
        return (4-3*h-sqrt(h*h-40*h+16))/(4*h)
    if h<=2: return 1.0
    if h<1+sqrt(3):
        return 2/h-sqrt(2*(h-2)/h)
    return 0.0

def main():
    checks=0
    xs=[F(1,2),F(3,5),F(2,3),F(3,4),F(4,5),F(9,10),F(1)]
    hs=[F(1,500),F(1,20),F(1,10),F(1,4),F(1,3),F(1,2),F(1),F(2),F(11,5),F(5,2),F(3)]
    for n in (2,3,4,5):
        for h in hs:
            for x in xs:
                M=stage_matrix(n,h,x)
                E=exact_matrix(n,h,x)
                assert M==E,(n,h,x,M,E);checks+=n*n
                for row in M:
                    assert sum(row)==1;checks+=1
                if n<=4 and h<=2:
                    assert all(v>=0 for row in M for v in row);checks+=1
                if n==5:
                    assert all(v>=0 for row in M for v in row)==pred_positive(h,x);checks+=1
    # The small-step fourth-order coefficient integrates to -1/16 under density 2.
    assert (F(1)**3-F(1)**4)-(F(1,2)**3-F(1,2)**4)==-F(1,16);checks+=1
    for h in [F(1,100),F(1,20),F(1,10),F(1,4),F(1,3),F(1,2),F(2),F(11,5),F(5,2),F(8,3),F(3)]:
        N=4000
        observed=sum(pred_positive(h,F(1,2)+F(2*i+1,4*N)) for i in range(N))/N
        assert abs(observed-p_formula(h))<1/N + 2e-9,(h,observed,p_formula(h));checks+=1
    assert p_formula(F(1,3))==1.0 and p_formula(F(2))==1.0;checks+=2
    print('VERIFY_OK',checks)
if __name__=='__main__':main()
