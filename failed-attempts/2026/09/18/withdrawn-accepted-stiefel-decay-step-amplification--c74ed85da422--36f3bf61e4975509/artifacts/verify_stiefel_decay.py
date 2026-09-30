#!/usr/bin/env python3
"""Numerical checks for the Stiefel polar-retraction identities in RESULT.md."""
import numpy as np


def polar(Y):
    U, _, Vt = np.linalg.svd(Y, full_matrices=False)
    return U @ Vt


def tangent_projection(W, G):
    S = 0.5 * (W.T @ G + G.T @ W)
    return G - W @ S


def principal_angles(W, Q):
    c = np.linalg.svd(W.T @ Q, compute_uv=False)
    return np.arccos(np.clip(c, -1.0, 1.0))


rng = np.random.default_rng(20260918)
max_gram = 0.0
max_scale = 0.0
max_chord = 0.0
max_graph = 0.0
max_sequential = 0.0
min_sigma_margin = np.inf

for n, r in [(9, 3), (12, 4), (15, 5)]:
    Z = rng.standard_normal((n, r))
    W, _ = np.linalg.qr(Z)
    G = rng.standard_normal((n, r))
    D = tangent_projection(W, G)
    A = W.T @ D
    B = (np.eye(n) - W @ W.T) @ D

    for eta, lam in [(0.07, 0.4), (0.35, 1.2), (0.8, 0.7)]:
        a = 1.0 - eta * lam
        assert a > 0
        Y = a * W - eta * D
        H2 = Y.T @ Y
        target_H2 = a*a*np.eye(r) + eta*eta*(D.T @ D)
        max_gram = max(max_gram, np.linalg.norm(H2-target_H2, ord='fro'))

        R_fused = polar(Y)
        R_eff = polar(W - (eta/a)*D)
        max_scale = max(max_scale, np.linalg.norm(R_fused-R_eff, ord='fro'))

        R_task = polar(W - eta*D)
        R_sequential = polar(a * R_task)
        max_sequential = max(max_sequential, np.linalg.norm(R_sequential-R_task, ord='fro'))

        sD = np.linalg.svd(D, compute_uv=False)
        chord_formula = 2.0*np.sum(1.0 - a/np.sqrt(a*a + eta*eta*sD*sD))
        chord_direct = np.linalg.norm(R_fused-W, ord='fro')**2
        max_chord = max(max_chord, abs(chord_formula-chord_direct))

        sY = np.linalg.svd(Y, compute_uv=False)
        sigma_formula = np.sqrt(a*a + eta*eta*sD*sD)
        min_sigma_margin = min(min_sigma_margin, np.min(sY)-a)
        assert np.allclose(sY, sigma_formula, rtol=1e-12, atol=1e-12)

        # Exact graph formula for subspace principal angles.
        Zgraph = (-eta * B) @ np.linalg.inv(a*np.eye(r) - eta*A)
        Qf, _ = np.linalg.qr(R_fused)
        theta = principal_angles(W, Qf)
        tan_theta = np.tan(theta)
        sZ = np.linalg.svd(Zgraph, compute_uv=False)
        max_graph = max(max_graph, np.max(np.abs(np.sort(tan_theta)-np.sort(sZ))))

# A deterministic horizontal example showing strict movement amplification by fused decay.
n, r = 8, 3
W = np.vstack([np.eye(r), np.zeros((n-r, r))])
B = np.zeros((n, r))
B[r:r+r, :] = np.diag([0.3, 0.7, 1.1])
D = B
eta = 0.4
vals = []
for lam in [0.0, 0.5, 1.0, 1.5]:
    a = 1.0 - eta*lam
    R = polar(a*W - eta*D)
    vals.append((lam, np.linalg.norm(R-W, ord='fro')))

print(f"max_gram_identity_residual={max_gram:.3e}")
print(f"max_effective_step_identity_residual={max_scale:.3e}")
print(f"max_chordal_formula_residual={max_chord:.3e}")
print(f"numpy_version={np.__version__}")
print(f"max_principal_angle_graph_residual={max_graph:.3e}")
print(f"max_sequential_decay_noop_residual={max_sequential:.3e}")
print(f"minimum_sigma_min_minus_a={min_sigma_margin:.6e}")
print("horizontal_example_chordal_distances:")
for lam, dist in vals:
    print(f"  lambda={lam:.1f}  distance={dist:.12f}")
assert all(vals[i+1][1] > vals[i][1] for i in range(len(vals)-1))
