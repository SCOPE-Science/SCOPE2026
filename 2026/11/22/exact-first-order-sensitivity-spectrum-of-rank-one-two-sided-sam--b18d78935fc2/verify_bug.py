"""Numerical verification for the exact local sensitivity spectrum of rank-one two-sided BUG.

The proof in RESULT.md is analytic; these checks diagnose matrix identities and
small-perturbation behavior on independent random instances.
"""
import numpy as np

def unit(x):
    return x / np.linalg.norm(x)

def update(B, u, v):
    k = B @ v
    ell = B.T @ u
    k = unit(k)
    ell = unit(ell)
    return np.outer(k, ell) * (k @ B @ ell)

def derivative(E, a, b, u, v):
    pa, pb = np.eye(len(a)) - np.outer(a, a), np.eye(len(b)) - np.outer(b, b)
    s, t = b @ v, a @ u
    return (np.outer(a, a) @ E @ np.outer(b, b)
            + np.outer(pa @ E @ v, b)/s
            + np.outer(a, u @ E @ pb)/t)

def theoretical_singulars(m, n, u, v):
    p2 = 1/(u[0]**2) - 1
    q2 = 1/(v[0]**2) - 1
    ans = ([np.sqrt(1+p2+q2)] + [np.sqrt(1+p2)]*(n-2)
           + [np.sqrt(1+q2)]*(m-2) + [1.,1.]
           + [0.]*((m-1)*(n-1)))
    return np.sort(np.array(ans))[::-1]

def full_matrix(m, n, a, b, u, v):
    cols = []
    for i in range(m):
        for j in range(n):
            E = np.zeros((m,n)); E[i,j] = 1
            cols.append(derivative(E,a,b,u,v).ravel())
    return np.array(cols).T

def run():
    rng = np.random.default_rng(20261115)
    counter = 0
    for m, n in [(2,2),(2,3),(3,2),(3,4),(4,3),(5,6)]:
        a = np.eye(m)[0];b = np.eye(n)[0]
        for trial in range(65):
            u = unit(np.concatenate(([rng.uniform(.11,1.)],rng.normal(size=m-1))))
            v = unit(np.concatenate(([rng.uniform(.11,1.)],rng.normal(size=n-1))))
            T = full_matrix(m,n,a,b,u,v)
            actual=np.linalg.svd(T,compute_uv=False)
            expected=theoretical_singulars(m,n,u,v)
            assert np.allclose(actual,expected,atol=3e-11,rtol=2e-11), (m,n,actual,expected)
            counter += 1
            A=np.outer(a,b)
            E=rng.normal(size=(m,n));E /= np.linalg.norm(E)
            exact=derivative(E,a,b,u,v)
            for eps in (1e-4,1e-5,1e-6):
                approx=(update(A+eps*E,u,v)-A)/eps
                assert np.linalg.norm(approx-exact)<(2e4*eps)*max(1,np.linalg.norm(exact)), (m,n,eps)
                counter += 1
    # Special equal-alignment case: tangent singular values all one, normal singulars zero.
    for m,n in [(2,2),(3,5),(6,4)]:
        a=np.eye(m)[0];b=np.eye(n)[0]
        actual=np.linalg.svd(full_matrix(m,n,a,b,a,b),compute_uv=False)
        expected=theoretical_singulars(m,n,a,b)
        assert np.allclose(actual,expected,atol=1e-13)
        counter += 1
    print('VERIFY_OK',counter,'matrix spectral and Frechet derivative checks')

if __name__=='__main__': run()
