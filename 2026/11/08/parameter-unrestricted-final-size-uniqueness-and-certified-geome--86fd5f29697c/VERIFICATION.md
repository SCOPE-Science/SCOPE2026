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

# Reproduction and evidential limits

Run `python checker.py` with Python, SymPy and mpmath installed. The script checks two exact derivative identities, tests a rational two-group example against each of four previously imposed hypotheses, reproduces the logarithmic fixed point with high-precision arithmetic, tests the certified bounds for iterations \(0\) through \(40\), and performs \(500\) deterministic pseudorandom model probes. It separately checks that the zero-seed boundary can have multiple algebraic fixed points.

The general uniqueness, monotonicity and error bounds are proved in `RESULT.md`; random tests establish no universal theorem and cannot independently certify originality. Literature comparison relied on the primary preprint and related full-text general fixed-point works. Full-text inspection of one older epidemic final-size article was unavailable; it is identified in the references. No external independent validation is asserted.
