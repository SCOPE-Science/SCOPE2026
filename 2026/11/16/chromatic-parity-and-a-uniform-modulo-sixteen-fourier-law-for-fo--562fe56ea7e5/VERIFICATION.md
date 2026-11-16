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

# Reproduction notes

Run `python3 check.py` in the same directory. Only the Python 3 standard library is required. Expected line:

`CHROMATIC_FOURIER_RESIDUE_PASS graphs= 75 general_coefficients= 16932 biclique_balanced_coefficients= 28224 direct_checks= 99`

All values are computed with integer arithmetic; no floating-point comparison or randomized seed is involved. The checker constructs proper colouring incidence arrays and applies a separate in-place Walsh butterfly. It verifies balanced/unbalanced residues, and cross-checks full biclique colour counts against a Stirling-number formula and selected frequencies against direct signed enumeration. The mathematical proof is in RESULT.md. Tests through four vertices and part sizes four are finite corroboration, not an infinite-domain proof. Independent validation has not been performed.
