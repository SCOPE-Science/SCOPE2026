"""Exact-rational checks for the two-step randomized projection crossover.

Run: python3 verify.py
Uses only the Python standard library. The analytic proof is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product

I = ((F(1), F(0)), (F(0), F(1)))

def add(A,B):
    return tuple(tuple(A[i][j]+B[i][j] for j in range(2)) for i in range(2))

def neg(A):
    return tuple(tuple(-A[i][j] for j in range(2)) for i in range(2))

def scale(a,A):
    return tuple(tuple(a*A[i][j] for j in range(2)) for i in range(2))

def mul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def trace(A): return A[0][0]+A[1][1]
def det(A): return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def outer(u): return tuple(tuple(u[i]*u[j] for j in range(2)) for i in range(2))

def second_moment(U,V):
    T=add(mul(U,U),mul(V,V))
    return scale(F(1,4), add(mul(mul(U,T),U),mul(mul(V,T),V)))

def calc(rho,sigma,tau):
    assert rho*rho+sigma*sigma==1 and 0<rho<1 and 0<tau<1
    P=outer((F(1),F(0)))
    Q=outer((rho,sigma))
    U=add(I,neg(P));V=add(I,neg(Q));W=add(I,neg(scale(1+tau,Q)))
    B0=second_moment(U,V);Bt=second_moment(U,W)
    D=add(Bt,neg(B0))
    s2=1-rho*rho
    tr_expected=tau*tau*(tau*tau+2*s2)/4
    det_expected=rho*rho*s2*tau*tau*(tau**4+tau*(tau+2)*s2-1)/16
    assert trace(D)==tr_expected,(rho,sigma,tau,'trace')
    assert det(D)==det_expected,(rho,sigma,tau,'det')
    for x,y in product(range(-2,3),repeat=2):
        e=(F(x),F(y))
        # independent enumeration of four length-two sampling words
        for B,M2 in ((B0,V),(Bt,W)):
            expr=F(0)
            for A1,A2 in product((U,M2),repeat=2):
                z=mul(A2,A1)
                out=(z[0][0]*e[0]+z[0][1]*e[1],z[1][0]*e[0]+z[1][1]*e[1])
                expr+=sum(v*v for v in out)/4
            rhs=e[0]*(B[0][0]*e[0]+B[0][1]*e[1])+e[1]*(B[1][0]*e[0]+B[1][1]*e[1])
            assert expr==rhs,(rho,sigma,tau,'enumeration')
    return D,B0,Bt

def main():
    assertions=0
    # primitive Pythagorean triples with rational direction cosines
    directions=[]
    from math import gcd
    for m in range(2,10):
        for n in range(1,m):
            if gcd(m,n)!=1 or (m-n)%2!=1: continue
            a=m*m-n*n;b=2*m*n;z=m*m+n*n
            directions.append((F(min(a,b),z),F(max(a,b),z)))
            directions.append((F(max(a,b),z),F(min(a,b),z)))
    for rho,sigma in directions:
        for tau in (F(1,10),F(1,4),F(2,5),F(1,2),F(3,5),F(4,5),F(9,10)):
            calc(rho,sigma,tau)
            assertions+=2+2*25*4
    D,B0,Bt=calc(F(4,5),F(3,5),F(3,5))
    assert B0[1][1]==F(1681,2500)
    assert Bt[1][1]==F(10297,15625)
    assert D[1][1]==-F(837,62500)
    assert det(D)<0 and trace(D)>0
    print(f'PASS: {len(directions)*7} rational parameter triples, {assertions} exact symbolic-formula/word-evaluation checks, and rational witness.')

if __name__=='__main__':main()
