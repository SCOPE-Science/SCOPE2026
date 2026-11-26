---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For the trace-one PSD model of K the reflected rank-one generator corresponds to (1+t)I/3-t uu^T, so its least eigenvalue gives the exact containment threshold t=1/2. Rayleigh support gives the two maxima in RESULT.md. The real Vandermonde on the ordered trace-zero, Frobenius-unit eigenvalue circle is proportional to sin(3θ), with normalized density (3/2)sin(3θ). By spectral reflection the baseline is sqrt(3) times the integral of cos(θ)sin(3θ) from 0 to π/3, namely 9sqrt(3)/16. For k=(2t-1)/sqrt(3)>0 each switch occupies a chamber end of angle arctan(k). Differentiating the total increment with respect to k has no moving-boundary term because the support excess is zero there; integration of (3/2)cos(θ)sin(3θ) to arctan(k) gives 3k²(3+k²)/(4(1+k²)²). Its zero-at-k=0 primitive is 3k³/(4(1+k²)). This gives the claimed monotonicity, endpoint, cubic coefficient 2/sqrt(3) and third-derivative jump 4sqrt(3). The switch intervals meet only at a tie when t=1. Reviewed RESULT.md, VERIFICATION.md and verify.py without executing the supplied file. Finite numerical checks are supplementary; the calculation above covers the full parameter interval.

## originality

PASS

Best of current knowledge, the distinct contribution is the evaluated mean-width profile and its cubic onset for this particular reflection hull, not the projector body, support-function calculus or Vandermonde law.

## value

PASS

Mean width is a canonical Euclidean invariant of the diameter-normalized projector body. The profile quantifies how the extremal reflected orbit begins changing that invariant, distinguishing immediate set enlargement from third-order mean-width sensitivity. The explicit coefficient and endpoint are useful for quantitative comparison with other width or symmetrization bounds; this is not just the PSD containment test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
