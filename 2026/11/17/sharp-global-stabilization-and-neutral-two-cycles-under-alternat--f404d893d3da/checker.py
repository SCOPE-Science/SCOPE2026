"""Exact rational checks for periodically allocated coordinate feedback in the Lozi map.

The script checks the specified concrete example and finite trajectories.
The all-parameter theorem follows from the symbolic argument in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product


def mul(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def mv(A, v):
    return tuple(sum(A[i][j]*v[j] for j in range(2)) for i in range(2))


def step(X, a, b, R, s_x, s_y):
    x, y = X
    x_star, y_star = R
    return (x_star+s_x*(y+1-a*abs(x)-x_star),
            y_star+s_y*(b*x-y_star))


def main():
    a,b,t = F(7,5),F(3,10),F(1,2)
    R=(1/(1+a-b),b/(1+a-b))
    rstar=(1-b)/(a*a+b*(1-b)*t)
    assert rstar==F(140,413)
    A=lambda r: ((-a*r,r),(b,F(0)))
    B=((-a,F(1)),(b*t,F(0)))
    for r in (F(1,4),rstar,F(1,2)):
        M=mul(B,A(r))
        P=mul(((a,F(1)),(b*t,F(0))),((a*r,r),(b,F(0))))
        assert (M[0][0],-M[0][1],-M[1][0],M[1][1]) == (P[0][0],P[0][1],P[1][0],P[1][1])
        tr = M[0][0]+M[1][1]; det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
        assert tr==a*a*r+b+b*r*t and det==b*b*r*t
        assert (1-tr+det>0)==(r<rstar)
        assert (1-tr+det==0)==(r==rstar)
        for x,y in product((F(-100),F(-1),F(0),F(1,5),F(2),F(100)),repeat=2):
            X=(x,y)
            for n in range(8):
                d=tuple(abs(X[i]-R[i]) for i in range(2))
                X1=step(X,a,b,R,r,F(1))
                X2=step(X1,a,b,R,F(1),t)
                d2=tuple(abs(X2[i]-R[i]) for i in range(2))
                maj=mv(P,d)
                assert d2[0]<=maj[0] and d2[1]<=maj[1]
                X=X2
    v=(a,-b*(1-b)*t)
    J_A=A(rstar)
    v1=mv(J_A,v)
    assert v1==(-(1-b),a*b)
    assert mv(mul(B,J_A),v)==v
    for eps in (F(1,100),-F(1,100),F(1,1000)):
        X=(R[0]+eps*v[0],R[1]+eps*v[1])
        X1=step(X,a,b,R,rstar,F(1))
        assert X1==(R[0]+eps*v1[0],R[1]+eps*v1[1]); assert X1 != X
        assert step(X1,a,b,R,F(1),t)==X
        assert X[0]>0 and X1[0]>0
    print('PERIODIC_LOZI_COORDINATE_SHARP_OK exact_matrix_cases=3 comparison_trajectories=108 critical_two_cycles=3')

if __name__=='__main__': main()
