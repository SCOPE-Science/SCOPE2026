---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Every competitor has crossing block W with zero diagonal and holding probabilities fixed by its row and column sums. Write s for the total crossing weight and μ for SLEM on the mean-zero space. The part-sign Rayleigh quotient is 1-2s/n, so s≤n(1+μ)/2. The trace on opposite-sign mean-zero pairs is (n-1)-(n-2)s/n, since ||proj_{1-perp}(e_i+e_j)||²=2-4/n for i≠j. Bounding that trace by (n-1)μ gives s≥n(n-1)(1-μ)/(n-2). Together these give μ≥n/(3n-4), attained by the uniform candidate: its nonconstant eigenvalues on the three indicated spaces are -μ*, (n-4)/(3n-4) and μ*. At equality the positive semidefinite μI-P has zero trace on the opposite-sign mean-zero space U and annihilates it. Vectors (e_j-e_k,-e_j+e_k)/2 force all allowed weights in each row or column to be equal; the edge set linked by row or column is connected for n≥3. Quantitatively the trace defect on U is at most (3n-4)δ/2. The inequality (μI-P)²≤2μ(μI-P) on the mean-zero space gives a residual norm at most sqrt(μ(3n-4)δ) on every unit vector in U. Taking the same coordinate contrasts bounds single row/column steps by twice that quantity. Distinct edges have distance at most three (use a spare index for reciprocal edges); then the spread is at most six times the residual bound. The two inequalities on s bound the average discrepancy by δ/(n-2). These steps include n=3 and allow zero crossing weights and disconnected competitors. `python3 /workspace/branches/independent_math_replay.py 3` independently checked 1,270 direct spectra for n=3..12, including skew, nearly optimal and disconnected examples. These numerical checks supplement the all-size proof.

## originality

PASS

The minimum SLEM and the invariant optimizer are already covered, both by the edge-transitive theorem and by the a=0 boundary of a distinct matching-channel result. The supported advance is the full-feasible-set equality analysis and quantitative entrywise bound. Neither earlier symmetrization guarantees equality in the needed positive-semidefinite residuals for arbitrary competitors without additional analysis.

## value

PASS

A unique invariant representative does not normally identify all minimizers of a nonsmooth convex spectral objective. The result identifies all allowed and holding weights and quantifies how close full-feasible-set near-minimizers must be. The square-root scale is substantive: adding a sufficiently small skew circulation on three indices of W preserves row and column sums and changes some entries linearly, while the active positive eigenvalue shifts quadratically by coupling opposite-sign and same-sign transverse modes with distinct eigenvalues. No sharp prefactor is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
