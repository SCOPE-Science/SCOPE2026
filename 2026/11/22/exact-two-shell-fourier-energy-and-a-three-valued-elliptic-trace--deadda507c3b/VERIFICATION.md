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

# Reproduction and verification notes

The source file `check_even_shells.py` runs under standard Python 3 with no third-party packages. The command `python check_even_shells.py` reproduces the reported checks. It constructs \(\mathbb F_p\) and quadratic extensions \(\mathbb F_{p^2}\) explicitly and evaluates quadratic characters using field multiplication rather than floating-point approximations.

The observed successful run checked the ordered two-sum convolution by direct enumeration for 21 test configurations, counting 5,722,928 ordered pairs. These cover dimensions \(2\), \(4\) and \(6\), both split/nonsplit determinant classes, and finite fields of orders \(3\), \(5\), \(7\), \(9\) and \(25\). In separate tests over fields of orders \(3\), \(5\), \(7\), \(9\), \(11\), \(13\), \(17\), and \(25\), it checked all 74 allowed nonzero second-radius ratios at fixed first radius, the family trace cancellation, the exact mean energy and the singular-quartic evaluations. Every check completed successfully.

The proof's unbounded quantifiers, all finite-field extension degrees and arbitrary even dimensions are justified by the algebraic arguments in RESULT.md, not inferred from finite enumeration. Smooth elliptic Frobenius traces are only assigned away from singular ratios; those ratios use the explicitly calculated correction numbers. No external independent mathematical audit has been performed.
