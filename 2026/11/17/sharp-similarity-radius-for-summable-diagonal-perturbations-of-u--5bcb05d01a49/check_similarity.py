"""Exact finite-support checks for an ordered-tail-shear intertwiner.

These checks cover finite rational instances only. The theorem's infinite operator
norm convergence and spectral necessity follow from the separate written proof.
"""
from fractions import Fraction as Q


def shift(x, w):
    return [w[k] * x[k+1] for k in range(len(x)-1)] + [Q(0)]


def shear(x, d, w, j):
    """Apply I-d_j R_j to a truncated column; j is zero based."""
    y=x[:]
    for k in range(j, len(x)-1):
        y[k+1] -= d[j]*x[k]/w[k]
    return y


def product(x, d, w):
    y=x[:]
    for j in range(len(d)):
        y=shear(y,d,w,j)
    return y


def perturbed(x, d, w):
    y=shift(x,w)
    for j in range(len(d)):
        y[j]+=d[j]*x[j]
    return y


def test_intertwining():
    count=0
    for profile in range(7):
        w=[Q(2+(k+profile)%5) for k in range(36)]
        d=[Q(((-1)**(k+profile))*(k+1),18*(k+2)) for k in range(8)]
        for m in range(21):
            x=[Q(0)]*len(w)
            x[m]=Q(1)
            lhs=perturbed(product(x,d,w),d,w)
            rhs=product(shift(x,w),d,w)
            assert lhs==rhs, (profile,m)
            count+=1
    return count


def test_boundary_eigenvectors():
    count=0
    for i in range(1,11):
        n=20
        w=[Q(3)]*n
        d=[Q(((-1)**k),k+2) for k in range(n)]
        d[i]=Q(3) if i%2==0 else Q(-4)
        lam=d[i]
        v=[Q(0)]*n
        v[0]=Q(1)
        for k in range(n-1):
            v[k+1]=(lam-d[k])*v[k]/w[k]
        assert all(t==0 for t in v[i+1:])
        assert perturbed(v,d,w)==[lam*t for t in v]
        count+=1
    return count

if __name__=='__main__':
    m=test_intertwining()
    n=test_boundary_eigenvectors()
    print(f'PASS: {m} exact weighted intertwiner columns; {n} sharp boundary eigenvectors')
