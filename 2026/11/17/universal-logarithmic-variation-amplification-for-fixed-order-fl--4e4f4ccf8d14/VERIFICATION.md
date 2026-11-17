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

The proof establishes the assertion for every fixed positive blending degree and every sufficiently large grid, uniformly over single-jump locations; it is not an extrapolation from numerical experiments.

Reproduction: in the same directory, run `python verify_fh_bv.py` with Python 3, NumPy and SciPy installed. The checker tests exact integer binomial weights, vanishing alternating sums, prefix coefficient bounds, 6,120 exact prefix/denominator assertions, and high-order quadrature of 1,920 finite jump-response values. The final expected line is `ALL_FIXED_ORDER_FH_BV_CHECKS_PASS`.

The finite test set does not certify the global asymptotic law, the continuous variation integral for every input, or absence of previous published equivalents. Those are addressed by the written proof and literature comparison. The bounded-remainder constant is not optimized, and no independent audit has been performed.
