import numpy as np

# A small block-structured constrained eigenvalue problem.
C = np.diag([2.0, 0.7])
B = np.array([[1.2, 0.3], [0.3, -0.4]])
E = np.array([[0.8, -0.2, 0.5], [0.4, 0.6, -0.3]])
D = np.diag([0.5, 1.7, 3.0])
H = np.block([[B, E], [E.T, D]])
A = np.hstack([np.diag(np.sqrt(np.diag(C))), np.zeros((2, 3))])

lambda_star = D[0, 0]
w = np.array([1.0, 0.0, 0.0])
Cinv = np.linalg.inv(C)
G = E.T @ Cinv @ E
J = E.T @ Cinv @ (B - lambda_star * np.eye(B.shape[0])) @ Cinv @ E

c = float(w @ G @ w)
d = float(w @ J @ w)
for j in range(1, D.shape[0]):
    wj = np.eye(D.shape[0])[:, j]
    d -= float((wj @ G @ w) ** 2 / (D[j, j] - lambda_star))


def penalty_data(rho):
    M = H + rho * (A.T @ A)
    vals, vecs = np.linalg.eigh(M)
    x = vecs[:, 0]
    f = float(vals[0])
    fp = float(np.linalg.norm(A @ x) ** 2)
    return f, fp


def hermite_estimate(base_rho, q):
    # Interpolate F(t)=f(1/t) in the scaled variable x=base_rho*t
    # at x_j=2^{-j}, using both F and F'.  The constant coefficient
    # of the degree-(2q-1) Hermite interpolant is the estimate of F(0).
    scales = 2.0 ** np.arange(q)
    nodes = 1.0 / scales
    n = 2 * q
    V = np.zeros((n, n))
    rhs = np.zeros(n)
    powers = np.arange(n)
    for j, (scale, node) in enumerate(zip(scales, nodes)):
        rho = base_rho * scale
        f, fp = penalty_data(rho)
        V[2 * j, :] = node ** powers
        V[2 * j + 1, 1:] = powers[1:] * node ** (powers[1:] - 1)
        rhs[2 * j] = f
        # If G(x)=F(x/base_rho), then G'(x_j)=-scale^2*base_rho*f'(rho).
        rhs[2 * j + 1] = -(scale**2) * base_rho * fp
    coeff = np.linalg.solve(V, rhs)
    return float(coeff[0])


print(f"numpy={np.__version__}")
print(f"lambda_star={lambda_star:.16e}")
print(f"c={c:.16e}")
print(f"d={d:.16e}")
print("rho raw_error hf1_error richardson2_error hermite2_error hermite2_error_times_rho4")
for rho in [10.0, 20.0, 40.0, 80.0, 160.0, 320.0]:
    f1, fp1 = penalty_data(rho)
    f2, fp2 = penalty_data(2.0 * rho)
    hf1 = f1 + rho * fp1
    richardson2 = 2.0 * f2 - f1
    hermite2 = 5.0 * f1 - 4.0 * f2 + rho * fp1 + 8.0 * rho * fp2
    hermite2_generic = hermite_estimate(rho, 2)
    assert abs(hermite2 - hermite2_generic) < 5e-13
    print(
        f"{rho:7.1f} "
        f"{f1-lambda_star:+.12e} "
        f"{hf1-lambda_star:+.12e} "
        f"{richardson2-lambda_star:+.12e} "
        f"{hermite2-lambda_star:+.12e} "
        f"{(hermite2-lambda_star)*rho**4:+.12e}"
    )

print("rho first_coeff_est second_coeff_est")
for rho in [20.0, 40.0, 80.0, 160.0, 320.0]:
    f1, _ = penalty_data(rho)
    c_est = rho * (lambda_star - f1)
    d_est = rho**2 * (f1 - lambda_star + c / rho)
    print(f"{rho:7.1f} {c_est:+.12e} {d_est:+.12e}")

print("q rho hermite_error scaled_error")
for q in [1, 2, 3]:
    for rho in [5.0, 10.0, 20.0, 40.0]:
        err = hermite_estimate(rho, q) - lambda_star
        print(f"{q:d} {rho:7.1f} {err:+.12e} {err*rho**(2*q):+.12e}")
