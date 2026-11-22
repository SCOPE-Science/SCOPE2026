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

# Verification record

The directly executable, standard-library-only `verify_symmetrization.py` iterates all Apéry pairs with parameters between one and thirty, checks additive closure and pseudo-Frobenius numbers from their definitions, and verifies the two complete output-membership formulas, output symmetry, defect supports, and ordered pair counts. Observed output: `VERIFY_OK; all eligible Apéry pairs a,b<=30; pseudo-symmetric cases: 30`.

The computation covers a finite parameter rectangle and does not prove any infinite assertion. The accompanying proof establishes the complete two-family parametrization, literal row-deletion arithmetic, and an exhaustive modular classification of potential offending sums for arbitrary positive parameters. No independent mathematical audit has been performed.
