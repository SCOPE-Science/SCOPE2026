"""Reproducibility checks for the ordinary path-edge simplex angle law.

Usage: python verify_path_angles.py  (requires sympy and numpy).
Finite checks corroborate, but do not replace, the all-dimensional proof.
"""
import math
import numpy as np
import sympy as sp


def gram_from_vertices(m):
    B = sp.zeros(m+1, m)
    for j in range(m):
        B[j, j] = 1
        B[j+1, j] = 1
    return B


def formula_H(m):
    T=m+1
    inv=sp.Matrix(m,m,lambda r,c:(-1)**(r+c) * sp.Rational((min(r,c)+1)*(T-max(r,c)-1),T))
    if m%2:
        b=sp.Matrix([sp.Rational(1,2) if (j+1)%2 else 0 for j in range(m)])
        t=sp.Rational(m+1,4)
    else:
        b=sp.Matrix([sp.Rational(m-j,2*(m+1)) if (j+1)%2 else sp.Rational(j+1,2*(m+1)) for j in range(m)])
        t=sp.Rational(m*(m+2),4*(m+1))
    return inv-b*b.T/t


def exact():
    total=0
    for m in range(3,16):
        B=gram_from_vertices(m)
        G=B.T*B
        H0=formula_H(m)
        assert G*G.inv()==sp.eye(m)
        b=G.inv()*sp.ones(m,1)
        t=(sp.ones(1,m)*b)[0]
        H=G.inv()-b*b.T/t
        assert H==H0
        # Independent affine gradient construction using difference vectors:
        # A=(v_1-v_m,..,v_{m-1}-v_m); on coordinates 1..m-1
        # gradient Gram = inverse of A^T A, with g_m = -sum(g_1,..,g_{m-1}).
        A=B[:,0:m-1]-B[:,m-1]*sp.ones(1,m-1)
        K=(A.T*A).inv()
        R=sp.eye(m-1).row_join(-sp.ones(m-1,1))
        assert R.T*K*R==H
        pos=neg=zero=0
        for i in range(m):
            assert H[i,i]>0
            for j in range(i+1,m):
                s=sp.sign(H[i,j])
                if s>0:pos+=1
                elif s<0:neg+=1
                else:zero+=1
                if m%2==1 and i==0 and j==m-1:assert s==0
                else:assert s==(1 if (j-i)%2==0 else -1)
                total+=1
        if m%2==0:
            k=m//2; assert (pos,neg,zero)==(k*(k-1),k*k,0)
        else:
            k=(m-1)//2;assert (pos,neg,zero)==(k*k-1,k*(k+1),1)
    print('EXACT_AFFINE_GRAM_PASS', 'dimensions=3..15', 'ridge_pairs='+str(total))


def limit():
    m=650
    indices=np.arange(1,m+1,dtype=float)
    I,J=np.triu_indices(m,1)
    ii=indices[I]; jj=indices[J]
    green=np.sqrt(ii*(m+1-jj)/(jj*(m+1-ii)))
    # limiting unsigned Green kernel cosine distribution
    e=0
    for r in (.1,.25,.5,.75,.9):
        a=r*r; exact=2*a*(-math.log(a)-1+a)/(1-a)**2
        measured=float(np.mean(green<=r))
        assert abs(exact-measured)<.008,(r,exact,measured)
        e=max(e,abs(exact-measured))
    # Actual centered ambient facet-normal cosines, not merely Green values:
    K=m+1
    b=np.where((np.arange(1,m+1)%2)==1,(K-indices)/(2*K),indices/(2*K))
    t=m*(m+2)/(4*K)
    green_ij=(-1.)**(J-I)*ii*(K-jj)/K
    gdiag=indices*(K-indices)/K-b*b/t
    centered=(green_ij-b[I]*b[J]/t)/np.sqrt(gdiag[I]*gdiag[J])
    assert np.all(np.isfinite(centered))
    assert float(np.mean(centered>0))>.48
    assert float(np.mean(centered>0))<.52
    for threshold in (.2,.5,.8):
        a=threshold**2
        F=2*a*(-math.log(a)-1+a)/(1-a)**2
        assert abs(float(np.mean(abs(centered)<=threshold))-F)<.01
    print('LIMIT_DISTRIBUTION_CORROBORATION_PASS', 'm='+str(m), 'max_unsigned_CDF_gap='+format(e,'.5f'))


if __name__=='__main__':
    exact(); limit()
