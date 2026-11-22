"""Reproducible exact checks for the Hamming ridge-angle law.

Requires Python 3 standard library.  Finite checks validate formulas; the
all-dimension conclusions are proved analytically in RESULT.md.
"""
from fractions import Fraction as Q
from math import comb


def Krawtchouk(d, h, k):
    return sum((-1)**j*comb(h,j)*comb(d-h,k-j)
               for j in range(max(0,k-d+h),min(h,k)+1))


def green(d,h):
    return sum((Q(Krawtchouk(d,h,k),4*k*k) for k in range(1,d+1)),Q())/2**d


def spectral(d):
    N=2**d
    a=sum((Q(comb(d,k),4*k*k) for k in range(1,d+1)),Q())/N
    b=sum((Q(comb(d,k),16*k**4) for k in range(1,d+1)),Q())/N
    return a,b


def check_symbolic():
    for d in range(2,19):
        a,b=spectral(d)
        gh=[green(d,h) for h in range(d+1)]
        assert gh[0]==a
        assert all(gh[h]>gh[h+1] for h in range(d))
        assert sum((comb(d,h)*gh[h] for h in range(d+1)),Q())==0
        assert sum((comb(d,h)*gh[h]**2 for h in range(d+1)),Q())==b
        assert sum((comb(d,h)*(gh[h]/a)**2 for h in range(1,d+1)),Q())==b/a**2-1
        assert gh[-1]==-(sum(Q(1,k) for k in range(1,d+1))**2+
                          sum(Q(1,k*k) for k in range(1,d+1)))/(8*2**d)
        if d>=3:
            assert gh[1]>0
        else:
            assert gh[1]<0
    print('Exact Fourier, shell-multiplicity and Parseval identities: d=2,...,18 PASS')


def check_direct():
    # Build the physical graph Laplacian and solve its inverse on 1-perp,
    # using exact Gauss-Jordan elimination, independently of Fourier series.
    def inverse(A):
        n=len(A)
        M=[[Q(x) for x in row]+[Q(i==j) for j in range(n)]
           for i,row in enumerate(A)]
        for k in range(n):
            pivot=next(i for i in range(k,n) if M[i][k])
            M[k],M[pivot]=M[pivot],M[k]
            r=M[k][k]; M[k]=[x/r for x in M[k]]
            for i in range(n):
                if i!=k and M[i][k]:
                    r=M[i][k]
                    M[i]=[x-r*y for x,y in zip(M[i],M[k])]
        return [row[n:] for row in M]
    for d in range(2,5):
        n=2**d
        L=[[Q(d if i==j else (-1 if (i^j).bit_count()==1 else 0))
            for j in range(n)] for i in range(n)]
        inv=inverse([[L[i][j]+Q(1,n) for j in range(n)] for i in range(n)])
        W=[[inv[i][j]-Q(1,n) for j in range(n)] for i in range(n)]
        # W L = I-J/n, and its columns are physical facet inward normals.
        for i in range(n):
            for j in range(n):
                assert sum((W[i][k]*L[k][j] for k in range(n)),Q()) == Q(i==j)-Q(1,n)
        for i in range(n):
            for j in range(n):
                gram=sum((W[k][i]*W[k][j] for k in range(n)),Q())
                assert gram==green(d,(i^j).bit_count())
    print('Independent rational Laplacian inverse/physical facet normals: d=2,3,4 PASS')


def check_large_dimension():
    # These are diagnostics, not proofs of the asymptotic theorem.
    for d in (50,100,200):
        a,b=spectral(d)
        c=green(d,1)
        total=b/a**2-1
        edge=Q(d)*c*c/(a*a)
        print(f'd={d}: d*energy={float(d*total):.9f}; d*adjacent_cos={float(d*c/a):.9f}; edge_energy_fraction={float(edge/total):.9f}')

if __name__=='__main__':
    check_symbolic();check_direct();check_large_dimension()
    print('HYPERCUBE_LAPLACIAN_ANGULAR_LOCALIZATION_PASS')
