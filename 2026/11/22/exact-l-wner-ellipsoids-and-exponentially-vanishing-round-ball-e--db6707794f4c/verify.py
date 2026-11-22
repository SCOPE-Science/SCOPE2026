"""Finite checks of the intrinsic Euclidean enclosing ellipsoid of even-cycle edge polytopes.

Requires Python 3 and NumPy. Run: python3 verify.py.
"""
from math import cos, pi, sqrt
import numpy as np


def cycle_check(m):
    n = 2*m
    d = n-2
    V = np.zeros((n,n))
    for i in range(n):
        V[i,i] = 1.
        V[i,(i+1)%n] = 1.
    mean = V.mean(axis=0)
    assert np.allclose(mean, np.full(n,2/n))
    W = V-mean
    # Build the affine tangent space independently from the centered vertices.
    U,s,VT = np.linalg.svd(W,full_matrices=False)
    assert s[d-1]>1e-9 and s[d]<1e-9
    B=VT[:d].T
    Y=W@B
    C=Y.T@Y/n
    vals=np.linalg.eigvalsh(C)
    assert vals.min()>1e-12
    formula=np.array(sorted(4/n*cos(pi*k/n)**2 for k in range(1,n) if k!=m))
    assert np.allclose(vals,formula,rtol=1e-8,atol=1e-11)
    D=np.sum((Y@np.linalg.inv(C))*Y,axis=1)
    assert np.allclose(D,np.full(n,d),rtol=1e-8,atol=1e-8)
    R2=float((W*W).sum(axis=1)[0]); assert np.allclose((W*W).sum(axis=1),R2)
    assert np.isclose(R2,2-2/m)
    axes=np.sqrt(d*vals)
    expected=np.array(sorted(2*np.sqrt(d/n)*abs(cos(pi*k/n)) for k in range(1,n) if k!=m))
    assert np.allclose(axes,expected)
    volume_ratio=np.prod(axes)/R2**(d/2)
    assert np.isclose(volume_ratio,m/2**(m-1),rtol=1e-8,atol=1e-11)
    assert np.isclose(axes[-1]/axes[0],1/np.tan(pi/n),rtol=1e-7,atol=1e-9)
    return volume_ratio


def main():
    for m in range(2,21):
        ratio=cycle_check(m)
        print(f'm={m} d={2*m-2} volume_ratio={ratio:.12g}')
    print('EVEN_CYCLE_LOEWNER_PASS orders=2..20')


if __name__=='__main__':
    main()
