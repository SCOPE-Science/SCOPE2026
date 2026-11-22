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

# Verification details

The exact reproducibility programs are `universal_six.py`, `paley20.py`, and `paley20_pfaffian.py` (Python 3 standard library). Run all three; each prints its complete integer frequency table and an explicit PASS assertion.

`universal_six.py` proves its finite exhaustiveness by fixing a switching normalization and iterating all 1,024 assignments to the ten remaining independent signs. It tests the full Pfaffian-square signatures and the equivalence between the maximizer type and switching transitivity.

`paley20.py` creates the complete Paley skew conference matrix using the nineteen-field quadratic character; checks all entries of its Gram identity; enumerates all 38,760 unordered erasure sets; and computes the relevant cubic coefficients by trace and fraction-free determinant. Independently `paley20_pfaffian.py` enumerates the same 38,760 masks using four-/six-Pfaffian formulas, verifying the six counts without using the determinant/trace implementation. Exact assertions check all six counts and their sum.

The mathematical reduction from a six-erasure Parseval frame error to the spectrum of the principal six-by-six compression, and comparison of the exact roots, are analytic proof steps in `RESULT.md` rather than consequences of the finite output alone.

Only the particular twenty-vector frame has the asserted distribution. No independent audit or external validation has been performed.
