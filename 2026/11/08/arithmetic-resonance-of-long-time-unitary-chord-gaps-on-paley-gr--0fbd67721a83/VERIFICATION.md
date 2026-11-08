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

The file `verify.py` is an executable, standard-library-only reproducibility check for the exact interval comparison and three sample Paley graph constructions. Run `python3 verify.py` from the extracted package root. The expected terminal line is `ALL_CHECKS_PASS`.

Its rational proof certificate computes bounds for \(\pi\) using Machin's identity with finite alternating arctangent sums, for square roots with integer-square-root flooring, and for cosine with finite alternating Taylor bounds and argument monotonicity. This confirms \(R_3<C_3<R_1\). The proof of the all-orders assertion is analytical and is in RESULT.md. Computations on three finite fields and finite midpoint quadrature cannot certify infinitely many graphs or a limiting time average.

The full text of the most directly relevant recent source was not obtainable; this is an originality-review limitation. No external independent audit or certification is asserted.
