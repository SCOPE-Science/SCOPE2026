"""Cross-check gauge invariance and rate-independent dark capture on ring networks."""
import numpy as np
from numpy.random import default_rng
from scipy.linalg import expm
from check_modular import dim_formula, survival_formula

rng=default_rng(314159)
NCASES=0
for n in range(3,12):
    for rep in range(8):
        traps=tuple(sorted(rng.choice(n,size=int(rng.integers(1,n+1)),replace=False)))
        for half_flux,phi in ((False,0.0),(True,np.pi),(None,0.341)):
            angles=rng.normal(size=n)
            angles += (phi-angles.sum())/n
            H=np.zeros((n,n),complex)
            for j,a in enumerate(angles):
                H[(j+1)%n,j]+=np.exp(1j*a)
                H[j,(j+1)%n]+=np.exp(-1j*a)
            # Loss rates do not influence eigenvectors in the surviving subspace.
            rates=rng.uniform(0.2,2.,size=len(traps))
            Gamma=np.zeros((n,n),complex)
            for x,z in zip(traps,rates):Gamma[x,x]=z
            # Eigenvectors of the Hermitian Hamiltonian, found by direct diagonalization.
            eigen,vecs=np.linalg.eigh(H)
            P=np.zeros((n,n),complex)
            st=0
            while st<n:
                en=st+1
                while en<n and abs(eigen[en]-eigen[st])<1e-8:en+=1
                V=vecs[:,st:en]
                U,sv,Vh=np.linalg.svd(V[list(traps),:],full_matrices=True)
                rank=np.count_nonzero(sv>1e-8)
                D=V@Vh.conj().T[:,rank:]
                P+=D@D.conj().T
                st=en
            dim=0 if half_flux is None else dim_formula(n,traps,half_flux)
            assert abs(np.trace(P).real-dim)<1e-7
            assert np.linalg.norm(H@P-P@H)<1e-7
            assert np.linalg.norm(Gamma@P)<1e-7
            for j in range(n):
                pred=0 if half_flux is None else survival_formula(n,traps,half_flux,j)
                assert abs(P[j,j].real-pred)<1e-7,(n,traps,phi,j,P[j,j],pred)
            if rep==0 and n<=7:
                # Non-Hermitian norm loss: finite-time test, conservatively below
                # the exact asymptotic norm except for integration precision.
                U=expm((-1j*H-Gamma/2)*15.)
                for j in range(n):
                    val=np.linalg.norm(U[:,j])**2
                    assert val+1e-9>=P[j,j].real
            NCASES+=1
print(f'PASS: {NCASES} nonuniform-gauge/rate checks and finite-time consistency')
