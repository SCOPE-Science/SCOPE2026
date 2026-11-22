"""Reproducible numerical checks of gradient-only harmonic sampling at regular simplex vertices."""
import numpy as np
from math import sqrt

def traceless_sym_basis(d):
    # Orthonormal basis for tracefree real symmetric d-by-d matrices.
    Z=[]
    for i in range(d):
        for j in range(i+1,d):
            B=np.zeros((d,d));B[i,j]=B[j,i]=1/sqrt(2);Z.append(B)
    for i in range(d-1):
        B=np.diag([1]* (i+1) + [-(i+1)] + [0]*(d-i-2))/sqrt((i+1)*(i+2))
        Z.append(B)
    return np.array(Z)

def simplex(d):
    n=d+1; H=np.eye(n)-np.ones((n,n))/n
    U,_,_=np.linalg.svd(H)
    # Columns span hyperplane of vector sum zero; numerical QR or svd
    basis=U[:,:d]
    v=(sqrt(n/d)*H@basis)
    assert np.allclose(v@v.T,(n/d)*H,atol=1e-12)
    return v

def grad_gram(d,retained):
    v=simplex(d);Bs=traceless_sym_basis(d)
    # Euclidean tangent gradient / sqrt(sphere integral energy)=sqrt(d+2)* tangent Au
    mat=[]
    for i in retained:
        u=v[i]; Au=np.einsum('ijk,k->ij',Bs,u)
        tang=Au-np.outer(Au@u,u)
        mat.append(tang.T)
    X=np.vstack(mat)*sqrt((d+2)/len(retained))
    return X.T@X

def expected_one_erasure(d):
    a=(d+1)*(d+2)/d**3
    b=(d+1)*(d+2)/d**2
    trace=(d+2)*(d*d+4*d+2)/(2*d**3)
    det=(d+1)*(d+2)**2/(2*d**4)
    roots=np.sort(np.roots([1,-trace,det]))
    return np.sort([a]+[roots[0]]*(d-1)+[roots[1]]*(d-1)+[b]*(d*(d-3)//2))

def expected_full(d):
    a=(d+2)/d**2; b=(d+2)/d
    return np.sort([a]*d + [b]*((d+1)*(d-2)//2))

def check():
    for d in range(3,10):
        for retained,expected in [(range(d+1),expected_full(d)),(range(d),expected_one_erasure(d))]:
            w=np.linalg.eigvalsh(grad_gram(d,list(retained)))
            assert len(w)==len(expected) and np.max(abs(w-expected))<4e-12, (d,w,expected)
        # Erasure nullity: k vertices retained -> (d-k)(d-k+1)/2, for 1<=k<d
        for k in range(1,d):
            w=np.linalg.eigvalsh(grad_gram(d,list(range(k))))
            null=int(np.sum(abs(w)<1e-10))
            assert null==(d-k)*(d-k+1)//2,(d,k,null)
        print('d=',d,'PASS')
if __name__=='__main__':check()
