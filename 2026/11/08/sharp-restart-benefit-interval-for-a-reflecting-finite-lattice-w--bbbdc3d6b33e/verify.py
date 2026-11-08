"""Independent exact checks for finite-path absorption under Poisson restart."""
from fractions import Fraction
from math import comb, sqrt


def coeff(k):
    return [comb(k+j,2*j) for j in range(k+1)]

def polyval(c,x):
    return sum(Fraction(a)*x**j for j,a in enumerate(c))

def tridiagonal_mean(L,r):
    # Solve -Qm = 1, transient sites 1,...,L, with reset-to-two rate r.
    A = [[Fraction(0) for _ in range(L+1)] for _ in range(L)]
    for i in range(1,L+1):
        row=A[i-1]
        neigh=([i-1] if i>0 else [])+([i+1] if i<L else [])
        for j in neigh:
            row[i-1]+=1
            if j>0:
                row[j-1]-=1
        if i!=2:
            row[i-1]+=r
            row[1]-=r
        row[-1]=1
    for k in range(L):
        p=next(i for i in range(k,L) if A[i][k]!=0)
        A[k],A[p]=A[p],A[k]
        v=A[k][k]
        for c in range(k,L+1): A[k][c]/=v
        for i in range(L):
            if i==k: continue
            v=A[i][k]
            for c in range(k,L+1): A[i][c]-=v*A[k][c]
    return A[1][-1]

def exact_mean(L,r):
    if not r: return Fraction(2*L-1)
    return (polyval(coeff(L),r)-polyval(coeff(L-2),r))/(r*polyval(coeff(L-2),r))

def check():
    tests=0
    for L in range(2,17):
        for r in [Fraction(0), Fraction(1,7), Fraction(1), Fraction(7,3)]:
            assert exact_mean(L,r)==tridiagonal_mean(L,r),(L,r)
            tests+=1
    for L in range(2,151):
        D=coeff(L);B=coeff(L-2)
        A=[D[j+1]-(B[j+1] if j+1<len(B) else 0) for j in range(L)]
        Q=[A[j]-(2*L-1)*(B[j] if j<len(B) else 0) for j in range(L)]
        assert Q[0]==0 and Q[L-1]==1
        assert Q[L-2]==0
        for j in range(1,L-2):
            c=Fraction(2*j*(2*L-1)*(L-j-2)*comb(L+j-2,2*j),(2*j+1)*(L-j-1))
            assert c>0 and Q[j]==-c,(L,j,Q[j],c)
    assert exact_mean(4,Fraction(1))<exact_mean(4,Fraction(0))
    assert exact_mean(4,Fraction(3))>exact_mean(4,Fraction(0))
    for L in range(2,15):
        for r in [Fraction(1,11),Fraction(5,2)]:
            assert exact_mean(L+1,r)>exact_mean(L,r)
    y=1+sqrt(2)
    r_opt=y+1/y-2
    assert abs(r_opt-2*(sqrt(2)-1))<1e-12
    for L in (15,30,70,130):
        assert abs(float(exact_mean(L,Fraction(82842712474619,10**14)))-(3+2*sqrt(2)))<(.3 if L==15 else 1e-7)
    print('PASS: %s independent rational generator solves; Q polynomial signs for L=2..150; monotonicity and asymptotics' % tests)

if __name__=='__main__': check()
