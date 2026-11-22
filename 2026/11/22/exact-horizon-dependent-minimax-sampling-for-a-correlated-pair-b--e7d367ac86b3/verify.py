"""Independent finite-dimensional checks for the exact-horizon block sampler theorem.
This checker supports, but does not replace, the all-horizons mathematical proof.
"""
import itertools
import math
import numpy as np


def vectors(n, rho):
    out = np.eye(n)
    out[0, 0] = -math.sqrt(1-rho*rho)
    out[0, 1] = rho
    return out


def risk_matrix_explicit(p, rho, k):
    n = len(p)
    v = vectors(n, rho)
    ans = np.zeros((n,n))
    for seq in itertools.product(range(n),repeat=k):
        coeff = math.prod(p[j] for j in seq)
        for a,b in zip(seq,seq[1:]):
            coeff *= float(v[a] @ v[b])**2
        ans += coeff*np.outer(v[seq[0]],v[seq[0]])
    return ans


def risk_matrix_transfer(p, rho, k):
    n=len(p)
    v=vectors(n,rho)
    c=rho*rho
    T = np.array([[p[0],c*p[1]],[c*p[0],p[1]]],dtype=float)
    h=np.array(p[:2])*(np.linalg.matrix_power(T,k-1)@np.ones(2))
    ans=sum(h[i]*np.outer(v[i],v[i]) for i in range(2))
    for j in range(2,n):
        ans += p[j]**k * np.outer(v[j],v[j])
    return ans


def optimum(n,rho,k):
    c_k=((1+rho)*(1+rho*rho)**(k-1))**(1/k)
    den=2+(n-2)*c_k
    p=np.array([1/den]*2+[c_k/den]*(n-2))
    rate=(c_k/den)**k
    return p,rate


def main():
    rng=np.random.default_rng(20261117)
    tests=0
    for n in (3,4,5):
        for rho in (0.15,0.5,0.82):
            for k in range(1,5):
                p_opt,risk=optimum(n,rho,k)
                mat=risk_matrix_explicit(p_opt,rho,k)
                assert abs(np.linalg.eigvalsh(mat)[-1]-risk)<2e-12
                assert np.allclose(mat,risk_matrix_transfer(p_opt,rho,k),atol=2e-12)
                tests+=2
                for _ in range(8):
                    p=rng.dirichlet(np.ones(n))
                    actual=risk_matrix_explicit(p,rho,k)
                    implied=risk_matrix_transfer(p,rho,k)
                    assert np.allclose(actual,implied,rtol=1e-12,atol=1e-12)
                    assert np.linalg.eigvalsh(actual)[-1]+2e-12>=risk
                    tests+=2
    for n in (3,5):
        for rho in (0.2,0.5,0.9):
            A=np.eye(n)
            A[0,1]=rho
            A[1,1]=math.sqrt(1-rho*rho)
            v=vectors(n,rho)
            for j in range(n):
                updated=[i for i in range(n) if i!=j]
                for _ in range(8):
                    x=rng.standard_normal(n)
                    y=A@x
                    B=A[:,updated]
                    dx=np.linalg.lstsq(B,-y,rcond=None)[0]
                    out=y+B@dx
                    pred=np.outer(v[j],v[j])@y
                    assert np.allclose(out,pred,atol=1e-12)
                    tests+=1
    for rho in (0.1,0.5,0.95):
        p1,r1=optimum(3,rho,1)
        for k in (2,3,5,8):
            pk,rk=optimum(3,rho,k)
            assert np.linalg.eigvalsh(risk_matrix_transfer(p1,rho,k))[-1]>rk*(1+1e-9)
            assert pk[0]>p1[0] and pk[2]<p1[2]
            tests+=2
    print(f"VERIFY_OK {tests} finite checks")

if __name__=='__main__':
    main()
