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

# Reproducibility and verification

Run `python3 VERIFY.py` using Python 3.9 or later with only the standard library. The direct generator explicitly constructs the two corner-block orientations and all row/column strips. It validates distinctness, normalization and each adjacent Monge inequality for dimensions 2 through 9 (496 vertices), and exactly recomputes the norms and the five integer moments of orders 0 through 4 using `fractions.Fraction`. It additionally compares finite-size logarithmic quantile probabilities under tilt parameters -3, 0 and 3 for side-length cutoff 100000.

Successful output: `MONGE_VERTEX_MOMENT_TILT_PASS vertices=496 exponents=0..4 critical_windows=-3,0,3`.

The universal vertex-completeness premise comes from Proposition 5.1 of Erickson–Kretschmann, arXiv:2311.07522. The convergence, critical window and moment divergence are proved analytically in `RESULT.md`, not by finite testing. The numerical critical-window check uses a stated finite-size tolerance of 0.07 because logarithmic convergence is slow. The calculation does not constitute independent scientific validation.
