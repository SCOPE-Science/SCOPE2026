"""Reproduce algebraic and numerical checks for a binary-pupil Type-II preconditioner."""
import numpy as np
import sympy as sp


def symbolic_mode_check():
    a, rho, p = sp.symbols('a rho p', real=True)
    w = p / (a*a + rho*rho)
    K = sp.Matrix([[1,a],[a,-rho*rho]])
    M = sp.Matrix([[1-a*a*w,a*w],[a*w,-w]])
    B = (K*M).applyfunc(sp.factor)
    assert (B-sp.Matrix([[1,0],[a*(1-p),p]])).applyfunc(sp.simplify) == sp.zeros(2)
    assert (B*B-B-sp.Matrix([
        [0,0],[a*p*(1-p),p*(p-1)]])).applyfunc(sp.simplify) == sp.zeros(2)
    for mask in (0,1):
        assert (B*B-B).subs(p,mask) == sp.zeros(2)


def exact_witness():
    # Fourier components a=(1,2), pupil=(1,0), transformed data=(1,1).
    a=sp.Matrix([1,2]); p=sp.Matrix([1,0]); beta=sp.Matrix([1,1]); rho=sp.S(1)
    blocks=[]
    for j in range(2):
        w=p[j]/(a[j]*a[j]+rho*rho)
        k=sp.Matrix([[1,a[j]],[a[j],-rho*rho]])
        m=sp.Matrix([[1-a[j]*a[j]*w,a[j]*w],[a[j]*w,-w]])
        blocks.append(k*m)
    assert blocks[0]==sp.eye(2)
    assert blocks[1]==sp.Matrix([[1,0],[2,0]])
    B0=beta.dot(beta)
    R2=sum((a[j]*(1-p[j])*beta[j])**2 for j in range(2))
    t=sp.cancel(B0/(B0+R2))
    G2=sp.cancel(B0*R2/(B0+R2))
    D2=sum((a[j]*beta[j])**2/(1+a[j]**2) for j in range(2) if p[j]==0)
    assert (B0,R2,t,G2,D2)==(2,4,sp.Rational(1,3),sp.Rational(4,3),sp.Rational(4,5))
    x_true=sp.Matrix([a[j]*beta[j]/(a[j]**2+rho**2) for j in range(2)])
    x_ret=sp.Matrix([t*p[j]*x_true[j] for j in range(2)])
    assert x_true==sp.Matrix([sp.Rational(1,2),sp.Rational(2,5)])
    assert x_ret==sp.Matrix([sp.Rational(1,6),0])
    assert sp.factor(sum((x_true[j]-x_ret[j])**2 for j in range(2)))==sp.Rational(61,225)


def numerical_checks():
    rng=np.random.default_rng(24067)
    checks=0
    for n in (2,4,6,8):
        F=np.fft.fft(np.eye(n), axis=0, norm='ortho')
        for case in range(120):
            eig=rng.uniform(0.1,4,size=n)
            pupil=rng.integers(0,2,size=n)
            for j in range(1,n):
                eig[(-j)%n]=eig[j]
                pupil[(-j)%n]=pupil[j]
            a=F.conj().T@np.diag(eig)@F
            Pi=F.conj().T@np.diag(pupil)@F
            assert np.max(np.abs(a.imag))<1.e-12
            a=a.real; Pi=Pi.real
            rho=float(rng.uniform(.1,3))
            W=F.conj().T@np.diag(pupil/(eig*eig+rho*rho))@F
            W=W.real
            I=np.eye(n); Z=np.zeros((n,n))
            K=np.block([[I,a],[a,-rho*rho*I]])
            Minv=np.block([[I-a@W@a,a@W],[W@a,-W]])
            B=K@Minv
            B_expected=np.block([[I,Z],[a@(I-Pi),Pi]])
            np.testing.assert_allclose(B,B_expected,atol=2.e-12,rtol=2.e-12)
            np.testing.assert_allclose(B@B,B,atol=2.e-12,rtol=2.e-12)
            b=rng.normal(size=n)
            c=np.r_[b,np.zeros(n)]
            q=B@c
            E=float(b@b)
            R2=float(np.linalg.norm(a@(I-Pi)@b)**2)
            t=E/(E+R2)
            r=c-t*q
            np.testing.assert_allclose(float(r@r),E*R2/(E+R2),rtol=5.e-12,atol=1.e-11)
            np.testing.assert_allclose(r@q,0,atol=2.e-11)
            np.testing.assert_allclose(B@q,q,atol=2.e-11)
            xtrue=np.linalg.solve(a@a+rho*rho*I,a@b)
            xnum=(t*Minv@c)[n:]
            np.testing.assert_allclose(xnum,t*Pi@xtrue,atol=3.e-12,rtol=3.e-12)
            # Compare with the full range least-squares floor.
            bhat=F@b
            D2=float(sum((eig[j]**2/(1+eig[j]**2))*abs(bhat[j])**2
                         for j in range(n) if pupil[j]==0))
            assert E*R2/(E+R2)+1.e-9>=D2
            checks+=1
    return checks

if __name__=='__main__':
    symbolic_mode_check()
    exact_witness()
    cases=numerical_checks()
    print('PASS: symbolic 2x2 identity, exact-rational two-mode witness,',cases,'seeded Fourier cases')
