"""Reproduce finite matrix identities and local beta-law checks for rank-r projectors."""
import numpy as np
from scipy.special import beta as beta_function
from scipy.stats import beta as beta_law

rng = np.random.default_rng(314159)
checks = 0

for r, m in [(2, 2), (2, 3), (4, 2), (3, 5), (6, 3)]:
    d = r + m
    P = np.diag([1.0] * r + [0.0] * m)
    Q = np.eye(d) - P
    for e in [1e-5, 0.03, 0.35, 0.88]:
        v = np.zeros(d)
        v[0] = np.sqrt(1 - e)
        v[r] = np.sqrt(e)
        w = Q @ v / np.sqrt(e)
        for _ in range(30):
            g = rng.normal(size=d)
            x = g - np.dot(g, v) * v
            x /= np.linalg.norm(x)
            D = float(x @ Q @ x)
            c = float(x @ w)
            M = np.array([[e, np.sqrt(e) * c], [np.sqrt(e) * c, D]])
            lam = float(np.linalg.eigvalsh(M)[0])
            R = 2 * (D - c*c) / (e + D + np.sqrt((D-e)**2 + 4*e*c*c))
            assert abs(R*e-lam) < 2e-12, (r,m,e,R,lam)
            assert 0 <= R <= 1+1e-12
            # Independently form the positive-definite original Rayleigh quotient.
            H = 2.5 * np.eye(d) + 1.7 * P
            B = np.column_stack([v, x])
            max_rayleigh = np.linalg.eigvalsh(B.T @ H @ B)[1]
            assert abs(max_rayleigh - (4.2 - 1.7*lam)) < 3e-12
            checks += 3

    # Vectorized local weak-limit test using a single Gaussian coupling.
    n = 25000
    g = rng.normal(size=(n,d))
    for e in [1e-7]:
        v = np.zeros(d)
        v[0] = np.sqrt(1-e)
        v[r] = np.sqrt(e)
        g_proj = g - (g @ v)[:,None] * v[None,:]
        x = g_proj / np.linalg.norm(g_proj,axis=1)[:,None]
        D = np.sum(x[:,r:]**2,axis=1)
        c = x[:,r]
        R = 2*(D-c*c)/(e+D+np.sqrt((D-e)**2+4*e*c*c))
        W = np.sum(g[:,r+1:]**2,axis=1)/np.sum(g[:,r:]**2,axis=1)
        a, b = (m-1)/2, 0.5
        assert abs(float(R.mean()) - a/(a+b)) < .014, (r,m,R.mean())
        assert np.mean(abs(R-W)) < .006, (r,m, np.mean(abs(R-W)))
        for q in (1,2,3):
            true_mom = beta_function(a+q,b)/beta_function(a,b)
            assert abs(float(np.mean(R**q))-true_mom) < .014, (r,m,q)
            checks += 1
        grid=np.array([.10,.25,.50,.75,.90])
        observed=np.mean(R[:,None]<=grid[None,:],axis=0)
        theoretical=beta_law.cdf(grid,a,b)
        assert np.max(abs(observed-theoretical)) < .017, (r,m,observed,theoretical)
        checks += 4

# Exact normalized-distribution moments, independent of r.
for m in range(2,12):
    a,b=(m-1)/2,.5
    assert abs(beta_function(a+1,b)/beta_function(a,b)-(m-1)/m) < 1e-13
    checks += 1

# Directly iterate fresh random tangent planes. The fixed-horizon calculation
# verifies both the three-step expectation and approximate independence of ratios.
for r, m in [(2,2), (3,3)]:
    d = r+m
    N = 2500
    e0 = 1e-5
    ratios = np.empty((N,3))
    for z in range(N):
        v = np.zeros(d)
        v[0] = np.sqrt(1-e0)
        v[r] = np.sqrt(e0)
        ee = e0
        for j in range(3):
            g = rng.normal(size=d)
            x = g - np.dot(g,v)*v
            x /= np.linalg.norm(x)
            B = np.column_stack([v,x])
            sub_Q = B[r:,:].T @ B[r:,:]
            eigvals,eigvecs = np.linalg.eigh(sub_Q)
            v = B @ eigvecs[:,0]
            e_next = float(np.sum(v[r:]**2))
            ratios[z,j] = e_next/ee
            ee = e_next
    target = (m-1)/m
    assert abs(float(np.mean(np.prod(ratios,axis=1)))-target**3) < .025, (r,m)
    assert abs(float(np.corrcoef(ratios[:,0],ratios[:,1])[0,1])) < .065, (r,m)
    assert np.all((ratios>=-1e-12)&(ratios<=1+1e-9))
    checks+=3

print(f'PASS {checks} matrix/beta-moment/limit/joint checks; 5 codimensions, exact RR matrix formula')
