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

# Verification of the exact radial Mahler law

The hypotheses and polarity normalization are explicit in `RESULT.md`. Run `python check.py` with a Python 3 standard-library interpreter. It verifies rational enclosures for \(\sqrt5\), strict signs for the derivative cubic on opposite sides of the unique root, and a rational inequality placing the maximizer strictly past the unit-radius configuration. Decimal approximations in its output are **not** used as proof of universal assertions.

The exact analytic argument proves the volume formulas and all parameter ranges. Separate direct numerical polytope comparisons checked \(\tau=0.95,1,1.009,1.1,1.25,h^{-1},1.3\) with errors less than \(2\times10^{-14}\); those checks only corroborate the analytical calculation. The plateau after \(h^{-1}\) is an exact homothety, not an extrapolation.

Correctness, originality and value have undergone the documented self-review. No independent audit or external formal certification has been performed. Some historical full-text sources remain partially inaccessible, so historical priority is provisional.
