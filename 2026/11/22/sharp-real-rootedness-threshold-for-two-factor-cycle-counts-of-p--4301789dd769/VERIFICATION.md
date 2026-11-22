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

The attached `prism_twofactor_verify.py` is standalone Python 3 code using only the standard library. Run `python3 prism_twofactor_verify.py` in the same directory as this file. It constructs the simple graph \(C_n\square K_2\), independently enumerates all perfect matchings, takes the complementary edge set and counts its connected cycle components for each spanning two-factor.

The direct census matches the complete closed-form coefficient distribution and an independently enumerated cardinality-matching polynomial of the base cycle for all \(3\le n\le14\). The exact first-three-coefficient Newton-defect algebra and its positive sign are checked for both parities at every integer \(4\le m\le200\). Low-order boundary polynomials are compared with explicit integer tables. The expected final checker output contains `VERIFY_OK` and includes `EXHAUSTIVE_MATCHING_COMPLEMENT_CYCLE_CENSUS_PASS 12`, `FIRST_NEWTON_OBSTRUCTION_EXACT_INTEGER_CHECK_PASS 394`, and `SMALL_BOUNDARY_CERTIFICATES_PASS n=3..9`.

Finite tests do not prove assertions at arbitrary length. The proof in `RESULT.md` separately gives exhaustive symbolic matching classification, exact formulas and positive all-order Newton-defect inequalities. Known total and Hamiltonian counts are tested for consistency, not claimed as discoveries. No independent external mathematical audit has been performed.
