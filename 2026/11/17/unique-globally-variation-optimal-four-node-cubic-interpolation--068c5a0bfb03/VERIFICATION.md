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

The attached `verify.py` is a self-contained Python/SymPy/NumPy checker. It reconstructs the cubic Lagrange basis, verifies cardinality and the jump decomposition, checks the three exact discriminant-based formulas by symbolic polynomial identities and admissible-domain signs, verifies the strict monotonic derivatives, certifies the unique-root bracket using rational square-root enclosures, and independently integrates each jump interpolant between derivative critical points on 400 deterministic random asymmetric grids.

Analytical facts not reducible to finite testing are proved in RESULT.md: Rolle localization of the two derivative roots, full-interval variation decomposition, exact operator norm attained by one-jump data, strict reduction of all asymmetric grids to the symmetric family, and uniqueness of the minimizer. The random tests are supportive checks, not the source of all-parameter validity. No external independent audit has been performed.

Run from the directory containing `verify.py` using `python verify.py` with Python 3.10+, SymPy and NumPy available. No downloaded data or external services are needed.
