"""Exact arithmetic checks for moment bounds of first real Grassmannian harmonics.

Run with Python 3: python verify_grassmannian.py
These finite checks supplement, but do not replace, the proof in RESULT.md.
"""
from fractions import Fraction as F
from math import factorial
from itertools import product

def poch(a, n):
    r = F(1)
    for j in range(n): r *= a + j
    return r

def grass_even_moment(diagonal, m):
    assert len(diagonal) == 4 and sum(diagonal) == 0
    d = [diagonal[0] + diagonal[i] for i in (1, 2, 3)]
    q = [x*x for x in d]
    s = F(0)
    for a in range(m+1):
        for b in range(m-a+1):
            c = m-a-b
            s += F(factorial(m),factorial(a)*factorial(b)*factorial(c)) * q[0]**a * q[1]**b * q[2]**c * poch(F(1,2),a)*poch(F(1,2),b)*poch(F(1,2),c)/poch(F(3,2),m)
    return s/F(2*m+1)

def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]

def givens(i,j,c,s):
    a=[[F(int(i==j)) for j in range(4)] for i in range(4)]
    a[i][i]=a[j][j]=F(c); a[i][j]=-F(s); a[j][i]=F(s)
    return a

def plucker_check():
    rotations=[(0,1,F(3,5),F(4,5)),(1,3,F(5,13),F(12,13)),(0,2,F(8,17),F(15,17)),(2,3,F(15,17),F(-8,17)),(0,3,F(12,13),F(5,13))]
    count=0
    for offset in range(5):
        R=[[F(int(i==j)) for j in range(4)] for i in range(4)]
        for k in range(5):
            i,j,c,s=rotations[(offset+k)%5]
            R=matmul(givens(i,j,c,s),R)
        assert matmul([[R[j][i] for j in range(4)] for i in range(4)],R)==[[F(int(i==j)) for j in range(4)] for i in range(4)]
        x=[R[i][0] for i in range(4)]; y=[R[i][1] for i in range(4)]
        p={(i,j):x[i]*y[j]-x[j]*y[i] for i in range(4) for j in range(i+1,4)}
        u=[p[0,1]+p[2,3],p[0,2]-p[1,3],p[0,3]+p[1,2]]
        v=[p[0,1]-p[2,3],p[0,2]+p[1,3],p[0,3]-p[1,2]]
        assert sum(z*z for z in u)==sum(z*z for z in v)==1
        for diag in [(3,-1,-1,-1),(1,1,-1,-1),(4,2,-1,-5),(1,3,-2,-2)]:
            actual=sum(diag[i]*(x[i]*x[i]+y[i]*y[i]) for i in range(4))
            expected=sum((diag[0]+diag[j])*u[j-1]*v[j-1] for j in (1,2,3))
            assert actual==expected, (diag,actual,expected)
            count+=1
    return count

def main():
    print('EXACT_PLUCKER_AND_BILINEAR_IDENTITY_OK',plucker_check())
    count=0
    for a,b,c in product(range(-3,4),repeat=3):
        d=-a-b-c
        diag=(a,b,c,d)
        T=sum(x*x for x in diag)
        if T==0:continue
        assert sum((diag[0]+diag[j])**2 for j in (1,2,3))==T
        for m in range(1,6):
            mu=grass_even_moment(diag,m)
            variance=F(T,9)
            ratio=mu/variance**m
            low=F(3**m,2*m+1)
            high=F(9**m,(2*m+1)**2)
            assert low<=ratio<=high,(diag,m,ratio,low,high)
            if m==2:
                assert mu==F(4,75)*(T*T-sum(x**4 for x in diag))
            count+=1
    print('EXACT_MOMENTS_AND_SHARP_ENVELOPES_OK',count)
    for m in range(1,9):
        for diag,expected in [((1,1,-1,-1),F(9**m,(2*m+1)**2)),((3,-1,-1,-1),F(3**m,2*m+1))]:
            T=sum(x*x for x in diag)
            assert grass_even_moment(diag,m)/F(T,9)**m==expected
    print('SHARP_EIGENVALUE_MULTIPLICITIES_OK',16)
    print('ALL_GRASSMANNIAN_LP_CHECKS_OK')
if __name__=='__main__':main()
