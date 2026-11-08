"""Independent finite-matrix checks for the stated quantum-reset Bell limit.
Run: python check.py (requires NumPy >=1.24). No external files required.
"""
import math
import numpy as np

ID = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = [X, Y, Z]
P = np.zeros((4, 4), complex)
P[3, 3] = 1
HXX = np.kron(X, ID) + np.kron(ID, X)
HZZ = np.kron(Z, Z)


def exact_density(j, q):
    """Compute the full Poisson age mixture by the independent spectral formula."""
    h = -j * HZZ + HXX / 2
    e, v = np.linalg.eigh(h)
    init = np.zeros(4, complex)
    init[3] = 1
    a = v.conj().T @ init
    energy_denominator = q + 1j * (e[:, None] - e[None, :])
    out = v @ ((a[:, None] * a.conj()[None, :]) * q / energy_denominator) @ v.conj().T
    return (out + out.conj().T) / 2


def independent_liouvillian_density(j, q):
    """Solve the 16-by-16 stationary linear system, without diagonalizing H."""
    h = -j * HZZ + HXX / 2
    op = q * np.eye(16) + 1j * (np.kron(h, np.eye(4)) - np.kron(np.eye(4), h.T))
    out = np.linalg.solve(op, (q * P).reshape(-1)).reshape(4, 4)
    return (out + out.conj().T) / 2


def ideal_density(k):
    """Closed-form effective 00/11 stationary mixture."""
    out = np.zeros((4, 4), complex)
    d = 1 + k * k
    out[0, 0] = 1 / (2 * d)
    out[3, 3] = (1 + 2 * k * k) / (2 * d)
    out[0, 3] = 1j * k / (2 * d)
    out[3, 0] = out[0, 3].conjugate()
    return out


def trace_norm(a):
    return sum(np.linalg.svd(a, compute_uv=False))


def bell_value(rho):
    t = np.array([[np.trace(rho @ np.kron(a, b)).real for b in PAULI] for a in PAULI])
    s = np.linalg.svd(t, compute_uv=False)
    return 2 * math.sqrt(s[0] ** 2 + s[1] ** 2)


def ideal_bell(k):
    return 2 * math.sqrt(1 + (k / (1 + k * k)) ** 2)


def run():
    n = 0
    for j, q in [(0.2, 0.4), (1, 0.15), (2, 0.8), (7, 0.15), (24, 0.02)]:
        a = exact_density(j, q)
        b = independent_liouvillian_density(j, q)
        assert trace_norm(a - b) < 3e-11, (j, q)
        assert abs(np.trace(a) - 1) < 2e-13
        assert np.linalg.eigvalsh(a)[0] > -1e-12
        n += 3
    for j in [8, 25, 80, 240, 800]:
        omega = math.hypot(j, 1)
        delta = 1 / (omega + j)  # avoids subtractive cancellation
        rho_bound = 2 * math.sqrt(1 - j / omega)
        bell_bound = 2 * math.sqrt(2) * rho_bound
        for k in [0.01, 0.1, 0.4, 0.7, 1, 1.4, 3, 12, 200]:
            rho = exact_density(j, k * delta)
            ideal = ideal_density(k)
            assert trace_norm(rho - ideal) <= rho_bound + 1e-10
            assert abs(bell_value(rho) - ideal_bell(k)) <= bell_bound + 1e-10
            assert abs(bell_value(ideal) - ideal_bell(k)) < 2e-12
            n += 3
    for j in [0.2, 1, 2, 8, 30]:
        q = 1e-8
        zero_reset_limit = math.sqrt(((2 * j * j + 1) ** 2 + 1) / (j*j + 1) ** 2)
        assert abs(bell_value(exact_density(j, q)) - zero_reset_limit) < 2e-6
        assert zero_reset_limit < 2
        n += 2
    for k in np.geomspace(0.02, 50, 101):
        assert ideal_bell(k) <= math.sqrt(5) + 1e-13
        n += 1
    assert abs(ideal_bell(1) - math.sqrt(5)) < 1e-14
    n += 1
    print(f"PASS: {n} independent matrix, bound, limit, and profile assertions")
    for j in [20, 100, 500]:
        q = 1 / (math.hypot(j, 1) + j)
        print(f"j={j}: B(j,delta_j)={bell_value(exact_density(j, q)):.12f}; asymptote={math.sqrt(5):.12f}")


if __name__ == '__main__':
    run()
