---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

If a_i=A_ii and b_i=(A²)_ii, the sampled gain is b_i/a_i with weight a_i/S. Zero a_i means Ae_i=0, so no quotient is needed there. Summing gives q. In an eigenbasis decomposition with W_ij=|U_ij|², take J with weight λ_j/S and randomize it to I via W. Then I has the pivot marginal and G_i is E[λ_J|I=i]. Ordinary and conditional Jensen give both convex-order bounds simultaneously. The identity basis attains the spectral law. The trace-zero matrix A²−qA has an orthonormal zero-diagonal frame: choose a zero-quadratic-form unit vector in the span of two opposite-sign eigendirections, then repeat on the trace-zero compression. This works over the reals and in the Hermitian case. Thus the lower endpoint is also attained for all convex losses, and the diagonal condition is necessary and sufficient. The variance is pointwise continuous on the orbit even at a_i=0 because b_i²/a_i≤λ_max² a_i. The real orbit is the continuous image of SO(n) since multiplying a frame by an eigenvector sign flip does not change the conjugated matrix; the unitary orbit is also connected. Therefore the two attained variance endpoints fill the entire stated interval. The one-dimensional and equal-positive-eigenvalue cases give zero variance; the exact (1,4) planar illustration checks the nondegenerate endpoints.

## originality

FAIL

The mean is already the trace of the known one-step expected map, and the full additional claim is a direct application of classical likelihood-ratio data processing and real/complex Schur–Horn for two spectral probability vectors. The decisive implication covers the full convex envelope and both simultaneous endpoints, not just the individual variance inequality. The variance interval and determinism criterion are immediate topology and the equality equation, respectively. This is not a claim that the cited RPCholesky algorithm papers literally state the envelope.

## value

FAIL

The example clarifies that first-step mean invariance does not ensure identical convex risk. But the submitted exact orbit result gives the textbook best and worst experiments for a pair of probability vectors, specialized to a known pivot ratio; all endpoints, the deterministic equation and the variance interval are immediate from the general theorems and continuity. No new one-step invariant beyond those implications, later-step theorem, or construction with a new algorithmic constraint is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
