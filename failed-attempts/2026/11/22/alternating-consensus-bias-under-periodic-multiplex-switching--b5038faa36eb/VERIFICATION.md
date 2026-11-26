---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

On the zero-sum subspace the loop-free complete-graph walk acts by −1/(n−1), so BA^k=U+r_k(B−U) in the stated column-update order. For k≥2 the product is positive because A^k is positive. For k=1, (BA)_{ij}=(1−B_{ij})/(n−1); rows of the odd-cycle vertices are positive, every row reaches one of those vertices, and all diagonal entries are positive. This gives primitivity. Products within a block preserve constants and contract the sup norm, so convergence at block endpoints gives convergence at all phases. The stationary equation gives the resolvent; the row-ℓ¹ contraction of B on signed vectors gives the stated geometric series tail and strict onset inequality. Weighted degree reversibility and uniqueness of the stationary law of B prove uB=u exactly for constant weighted degrees. In the triangle, symmetry and the third-coordinate stationary equation give π_{k,3}=1/(3+r_k); odd k gives a value above 1/3 and even k a value between 1/4 and 1/3. No general all-k or temporal-oscillation claim is needed. The supplied finite rational check was inspected, not executed.

## originality

FAIL

Shiu–Naghizadeh do not state the signed all-k formula or the all-large-k parity test. But the resolvent and signed leading term are a direct rank-one instance of the classical stationary perturbation identity, on the very switched product already analyzed by that paper. The threshold is the elementary tail bound on the resulting Neumann series, and the triangle is their already published k=1 witness with the same one-dimensional indeterminate r carried through its stationarity equation. This is a mechanical specialization, not an exact-duplicate claim. The conclusion does not rely on unavailable full text or on treating the prior O(ρ₂(A)^k) magnitude estimate alone as a signed one.

## value

FAIL

The distinction between a signed limit response and an unsigned convergence rate is meaningful. In this frozen complete-layer case it is exhausted by the first coefficient of the standard rank-one stationary perturbation and the already studied triangle; the onset estimate is the generic geometric remainder. There is no new nonroutine witness, wider sign theorem beyond that reduction, or independent invariant here that would support acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
