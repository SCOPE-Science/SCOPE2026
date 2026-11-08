"""Reproducible numerical checks of transverse spectra for reactive Stuart--Landau polygons.
Scientific test cases supplement the analytic dissipativity proof; numerical spectra are not proof.
Run: python verify_reactive_polygons.py (NumPy required).
"""
import numpy as np


def triangle(beta, epsilon=0.0, k=1.0):
    r = np.sqrt((np.asarray(beta,dtype=float)-3*epsilon)/k)
    assert np.all(r>0) and 2*np.max(r)<np.sum(r)
    theta = np.arccos((r[2]**2-r[0]**2-r[1]**2)/(2*r[0]*r[1]))
    w=np.array([r[0],r[1]*np.exp(1j*theta)],dtype=complex)
    return np.r_[w,-w.sum()]


def rectangular_quad(epsilon=0.0,k=1.0):
    # Fixed heterogeneous opposite pairs, beta=(1,4,1,4).
    a=np.sqrt((1-4*epsilon)/k)
    b=np.sqrt((4-4*epsilon)/k)
    return np.array([a,1j*b,-a,-1j*b],dtype=complex)


def jacobian(w,gamma,epsilon=0.0,k=1.0):
    m=len(w)
    j=np.zeros((2*m,2*m),dtype=float)
    coupling=np.array([[epsilon,-gamma],[gamma,epsilon]],dtype=float)
    for a in range(m):
        u=np.array([w[a].real,w[a].imag])
        j[2*a:2*a+2,2*a:2*a+2]-=2*k*np.outer(u,u)
        for b in range(m):
            j[2*a:2*a+2,2*b:2*b+2]+=coupling
    return j


def inspect(w,gamma,epsilon=0.0,k=1.0):
    m=len(w)
    assert abs(sum(w))<1e-12
    assert np.linalg.matrix_rank(np.stack([w.real,w.imag]))==2
    j=jacobian(w,gamma,epsilon,k)
    vals=np.linalg.eigvals(j)
    neutral=sorted(vals,key=lambda q:abs(q))[:m-2]
    other=sorted(vals,key=lambda q:abs(q))[m-2:]
    assert max(abs(q) for q in neutral)<2e-8, neutral
    assert max(q.real for q in other)<-1e-6, other
    if epsilon==0:
        e=(j+j.T)/2
        expected=np.zeros_like(j)
        for a in range(m):
            u=np.array([w[a].real,w[a].imag])
            expected[2*a:2*a+2,2*a:2*a+2]=-2*k*np.outer(u,u)
        assert np.linalg.norm(e-expected)<2e-12
    return min(-q.real for q in other)


def main():
    count=0
    for gam in (0.05,0.7,3.0,-2.0):
        for eps in (0,1e-3):
            w=triangle([1,1.5,2],eps)
            gap=inspect(w,gam,eps)
            assert gap>0
            count+=1
            w=rectangular_quad(eps)
            gap=inspect(w,gam,eps)
            assert gap>0
            count+=1
    print('VERIFY_OK noncollinear_heterogeneous_cases=%d nonzero_imaginary_couplings=4 dissipative_cases=8 positive_dissipative_cases=8 normal_eigenvalues_strict=1' % count)

if __name__=='__main__':
    main()
