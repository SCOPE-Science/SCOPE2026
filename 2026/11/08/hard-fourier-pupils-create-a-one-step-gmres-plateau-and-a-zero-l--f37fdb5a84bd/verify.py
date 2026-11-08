"""Numerical and exact-algebra checks for ideal hard-pupil Schur preconditioning.

Run: python research34_optical_pupil_check.py
Assumes numpy and sympy. These checks supplement, not replace, the proof.
"""
import numpy as np
import sympy as sp


def checks():
    # Exact rational two-mode proof of idempotence and soft-pupil polynomial identity.
    a, alpha, eps = sp.symbols('a alpha eps', real=True)
    A = sp.diag(a,2*a)
    p2 = sp.diag(a*a+alpha*alpha,4*a*a+alpha*alpha)
    K = sp.BlockMatrix([[sp.eye(2),A],[A,-alpha*alpha*sp.eye(2)]]).as_explicit()
    for leakage in [sp.Integer(0),eps]:
        Lamb = sp.diag(1,leakage)
        B = p2.inv()*Lamb
        R = sp.BlockMatrix([[sp.eye(2)-A*B*A,A*B],[B*A,-B]]).as_explicit()
        T = sp.simplify(K*R)
        expected = sp.BlockMatrix([[sp.eye(2),sp.zeros(2)],[(sp.eye(2)-Lamb)*A,Lamb]]).as_explicit()
        assert sp.simplify(T-expected)==sp.zeros(4)
        if leakage==0:
            assert sp.simplify(T*T-T)==sp.zeros(4)
        else:
            assert sp.simplify((T-sp.eye(4))*(T-eps*sp.eye(4)))==sp.zeros(4)

    rng = np.random.default_rng(8119)
    maxerr = 0.
    for n in [3,4,5,7,9]:
        j = np.arange(n)
        F = np.exp(-2j*np.pi*j[:,None]*j[None,:]/n)/np.sqrt(n)
        for trial in range(32):
            a = rng.normal(size=n)+1j*rng.normal(size=n)
            mask = (rng.integers(0,2,size=n)).astype(float)
            if mask.sum() == 0 or mask.sum() == n:
                mask[:]=0;mask[0]=1
            al = .2+rng.random()
            A = F.conj().T@np.diag(a)@F
            Pi = F.conj().T@np.diag(mask)@F
            P = A.conj().T@A+al*al*np.eye(n)
            K = np.block([[np.eye(n),A],[A.conj().T,-al*al*np.eye(n)]])
            b = rng.normal(size=n)+1j*rng.normal(size=n)
            c = np.r_[b,np.zeros(n,dtype=complex)]
            def matrices(eps):
                L = Pi+eps*(np.eye(n)-Pi)
                B = np.linalg.solve(P,L)
                R = np.block([[np.eye(n)-A@B@A.conj().T,A@B],[B@A.conj().T,-B]])
                T = K@R
                return T,R
            T,R = matrices(0.)
            assert np.allclose(T@T,T,atol=2e-12)
            # GMRES minimizes over span{Krylov1,Krylov2}: T*span contains only Tc.
            z = T@c
            coef = np.vdot(z,c)/np.vdot(z,z)
            gmres1 = np.linalg.norm(c-coef*z)**2
            E=np.linalg.norm((np.eye(n)-Pi)@A.conj().T@b)**2
            Bnorm=np.linalg.norm(b)**2
            expected=Bnorm*E/(Bnorm+E)
            maxerr=max(maxerr,abs(gmres1-expected))
            assert np.allclose(gmres1,expected,atol=3e-9)
            # Full physical solution constrained to x in mask Fourier subspace.
            bh=F@b
            lower=np.sum((1-mask)*np.abs(a)**2*np.abs(bh)**2/(1+np.abs(a)**2))
            Z=np.block([[np.eye(n),np.zeros((n,int(mask.sum())))],[np.zeros((n,n)),F.conj().T[:,mask.astype(bool)]]])
            z0=np.linalg.lstsq(K@Z,c,rcond=None)[0]
            actual=np.linalg.norm(K@(Z@z0)-c)**2
            assert np.allclose(actual,lower,atol=3e-9)
            assert lower<=gmres1+2e-9
            for eps0 in [.1,.3,1.]:
                Te,Re=matrices(eps0)
                assert np.allclose((Te-np.eye(2*n))@(Te-eps0*np.eye(2*n)),0,atol=2e-11)
                # Second-degree GMRES polynomial p(Te)=0 with p(0)=1.
                poly=(Te-np.eye(2*n))@(Te-eps0*np.eye(2*n))/eps0
                assert np.linalg.norm(poly@c) < 1e-8
                yy=np.linalg.solve(Te,c)
                assert np.linalg.norm(K@Re@yy-c)<1e-8
                if eps0<1:
                    ii=np.where(mask<.5)[0][0]
                    v=np.array([[1,0],[(1-eps0)*np.conjugate(a[ii]),eps0]],dtype=complex)
                    t=1+eps0**2+(1-eps0)**2*abs(a[ii])**2
                    kapp=(t+np.sqrt(t*t-4*eps0**2))/(2*eps0)
                    assert np.allclose(np.linalg.cond(v),kapp,rtol=3e-12)
    print('VERIFY_OK; 160 random Fourier instances, 480 soft-pupil instances; max GMRES residual-square error:',maxerr)
if __name__=='__main__': checks()
