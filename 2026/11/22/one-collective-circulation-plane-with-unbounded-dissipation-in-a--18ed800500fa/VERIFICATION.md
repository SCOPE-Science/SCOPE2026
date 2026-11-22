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
# Verification

The analytical proof establishes the claims for all integer network dimensions and positive real parameters; finite checks do not substitute for that proof. The standalone `verify.py` reconstructs each stationary covariance by exact-rational Gaussian elimination of the complete Lyapunov linear system, then checks the antisymmetric stationary current, the cubic rank-two spectral identity, reservoir heat conservation, and both reservoir and Gaussian-current entropy production formulas.

Command: `python3 verify.py`

Observed output: `ALL_BATH_EXACT_RATIONAL_CHECKS_PASSED 36`.

The cases cover dimensions 2–5, three different positive pinning/coupling pairs, and equal and unequal temperature configurations. No external packages or network access are required. The three-bath exact moment constraints and divergence are verified symbolically in the proof; the checker is deliberately not misrepresented as an exhaustive real-parameter or large-dimension validation. The public source comparisons and scope restrictions are stated in RESULT.md and REVIEW.md.
