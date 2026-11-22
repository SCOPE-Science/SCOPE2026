---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and reproducibility

Run `python checker.py` with SymPy available. The script checks, using exact symbolic arithmetic, the copula's derivative factorization, uniform margins, the four bilinear corner values, the published three-dimensional dependence definitions, and the coordinate inverse that realizes every feasible interior-diameter-excluded point.

The exact inequalities for all real parameters follow from affine interpolation of a bilinear polynomial on a square and the complete range of \(1-2z\) on \([0,1]\). The 160 seeded rational probes test representative finite choices and are not claimed as an exhaustive search or infinite-domain proof. The explicit source example \((\alpha,\beta)=(5,2)\) has a verifiable eleven-unit corner maximum. The global extrema are witnessed by \(\lambda=\pm1\), \(\alpha=\beta=1/2\); the range of all equality witnesses is proved analytically.

Scientific limits: only the stated polynomial copula is classified; the original formulas for the rank coefficients are reused, not rediscovered; the priority comparison is necessarily bounded by accessible literature. Independent audit: not performed.
