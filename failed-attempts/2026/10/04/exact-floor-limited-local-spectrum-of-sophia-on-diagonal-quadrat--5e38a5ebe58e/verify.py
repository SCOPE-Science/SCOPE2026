import cmath
import math

def h_refresh(lam, beta2, j):
    return lam*(1.0-beta2**j)

def chi(lam, eta, gamma, eps):
    return eta*lam/max(gamma*lam, eps)

def roots(beta1, x):
    T = 1.0 + beta1 - (1.0-beta1)*x
    disc = cmath.sqrt(T*T - 4.0*beta1)
    return (0.5*(T+disc), 0.5*(T-disc))

def rho(beta1, x):
    return max(abs(r) for r in roots(beta1, x))

# Hessian EMA exact closed form.
for lam in (0.2, 1.0, 7.0):
    for beta2 in (0.0, 0.5, 0.99):
        h = 0.0
        for j in range(1, 20):
            h = beta2*h + (1.0-beta2)*lam
            assert abs(h-h_refresh(lam,beta2,j)) < 1e-13

# Exact stability ceiling.
for beta1 in (0.0, 0.2, 0.5, 0.96):
    cap = 2.0*(1.0+beta1)/(1.0-beta1)
    assert rho(beta1, 0.999*cap) < 1.0
    boundary = roots(beta1, cap)
    assert min(abs(r+1.0) for r in boundary) < 1e-10
    assert min(abs(r+beta1) for r in boundary) < 1e-10
    assert rho(beta1, 1.001*cap) > 1.0

# Complex plateau and exact modulus.
for beta1 in (0.1, 0.5, 0.96):
    q = math.sqrt(beta1)
    lo = (1.0-q)/(1.0+q)
    hi = (1.0+q)/(1.0-q)
    for x in (0.2*lo+0.8*hi, 0.5*(lo+hi), 0.8*lo+0.2*hi):
        rs = roots(beta1,x)
        assert abs(rs[0].imag) > 1e-10
        assert abs(abs(rs[0])-q) < 1e-11
        assert abs(abs(rs[1])-q) < 1e-11

# Denominator-floor identity and plateau threshold.
beta1 = 0.96
eta = 6e-4
eps = 1e-12
sq = math.sqrt(beta1)
lo = (1.0-sq)/(1.0+sq)
hi = (1.0+sq)/(1.0-sq)
threshold = eps*lo/eta
assert abs(lo-0.010205144336438057) < 1e-15
assert abs(hi-97.98979485566335) < 1e-12
assert abs(threshold-1.700857389406343e-11) < 1e-24

for gamma in (0.01,0.05):
    q = eta/gamma
    assert lo < q < hi
    for lam in (threshold, 10.0*threshold, 1.0, 100.0):
        x = chi(lam,eta,gamma,eps)
        if lam >= threshold*(1.0+1e-12):
            assert abs(rho(beta1,x)-math.sqrt(beta1)) < 5e-10

# Flat-curvature first-order asymptotic rho = 1 - chi + O(chi^2).
for x in (1e-4, 3e-5, 1e-5):
    err = abs(rho(beta1,x) - (1.0-x))
    assert err < 2.0*x*x/(1.0-beta1)

# Limiting mode matrix trace and determinant by direct arithmetic.
for beta1 in (0.2,0.7,0.96):
    for x in (0.01,0.5,2.0):
        a11 = 1.0-(1.0-beta1)*x
        a12 = -beta1*x
        a21 = 1.0-beta1
        a22 = beta1
        det = a11*a22-a12*a21
        tr = a11+a22
        assert abs(det-beta1) < 1e-13
        assert abs(tr-(1.0+beta1-(1.0-beta1)*x)) < 1e-13

print("verification passed")
