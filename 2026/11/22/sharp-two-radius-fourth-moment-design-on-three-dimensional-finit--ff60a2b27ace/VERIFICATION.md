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

# Verification of the exact two-radius design theorem

The mathematical proof is in `RESULT.md`. The supplementary standard-library Python program `checker.py` calculates ordered pair sums directly on the finite vectors and compares each target against a separate character/discriminant formula, then checks total additive energy and the small-field minimum. Its finite sample includes prime fields of orders 3, 5, 7 and 11, every radius pair in the extension field of order 9, and representative sign/resonance classes in the extension field of order 25. The code uses only ordinary exact integers and finite-field digit arithmetic and needs no external dependencies.

Reproduce by running `python3 checker.py` after extracting all files from this package. The trace of a successful execution ends with `PASS 100 direct convolution and energy enumerations` (the exact number can change if more cases are added to the accompanying implementation). This is a regression test, not a computational proof of the all-field assertion. The general quadratic-count lemma, the polynomial inequalities, and the four small-field symbolic comparisons are proved in `RESULT.md`.

An independent audit has not been performed. No proof-assistant certification is asserted.
