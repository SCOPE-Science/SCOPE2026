import itertools
import math
import numpy as np

I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],dtype=complex)
Y=np.array([[0,-1j],[1j,0]],dtype=complex)
Z=np.array([[1,0],[0,-1]],dtype=complex)
P=[I,X,Y,Z]

def kron_pow(a,n):
    r=np.array([[1]],dtype=complex)
    for _ in range(n): r=np.kron(r,a)
    return r

def tetra_vertices(n):
    s=(-1)**(n//2)
    # Joint-eigenvalue triples (x,y,z) obey x*y=s*z.
    return [(x,y,s*x*y) for x in (-1,1) for y in (-1,1)]

def vertex_state(n,t):
    return (kron_pow(I,n)+t[0]*kron_pow(X,n)+t[1]*kron_pow(Y,n)+t[2]*kron_pow(Z,n))/(2**n)

def pt(rho,n,subset):
    a=rho.reshape([2]*2*n)
    axes=list(range(2*n))
    for q in subset:
        axes[q],axes[n+q]=axes[n+q],axes[q]
    return a.transpose(axes).reshape(rho.shape)

def spec_formula(p,N,odd):
    d=4**N
    vals=[(0.5-x)/d for x in p] if odd else [x/d for x in p]
    return sorted(sum(([v]*d for v in vals),[]))

tests=[(0.7,0.1,0.1,0.1),(0.4,0.3,0.2,0.1),(0.6,0.4,0,0),(1,0,0,0)]
checks=0
for N in (1,2,3):
    n=2*N+2
    tv=tetra_vertices(n)
    R=[vertex_state(n,t) for t in tv]
    # Vertex states are normalized orthogonal projectors of rank 4^N.
    for A in R:
        assert abs(np.trace(A)-1)<1e-10
        assert np.linalg.norm(A@A-A/(4**N))<1e-9
    for i in range(4):
        for j in range(4):
            if i!=j: assert abs(np.trace(R[i]@R[j]))<1e-9
    for p in tests:
        rho=sum(float(p[i])*R[i] for i in range(4))
        for m in range(1,n):
            subset=tuple(range(m))
            eig=sorted(np.linalg.eigvalsh(pt(rho,n,subset)).real.tolist())
            want=spec_formula(p,N,m%2==1)
            assert np.max(np.abs(np.array(eig)-np.array(want)))<2e-9
            w=max(p)
            neg=-sum(v for v in eig if v<0)
            want_neg=max(0.0,w-0.5) if m%2 else 0.0
            assert abs(neg-want_neg)<2e-9
            checks+=1
print(f"VERIFY_OK parity_spectra={checks} levels=3 test_weights={len(tests)}")
