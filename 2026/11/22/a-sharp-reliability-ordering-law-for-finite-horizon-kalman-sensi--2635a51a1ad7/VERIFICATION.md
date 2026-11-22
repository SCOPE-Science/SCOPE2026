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

# Reproduction and limits

Run `python3 verify.py` from the package directory (Python 3.9+; standard library only). The test constructs every two-to-five-observation permutation in four rational test scenarios, checks their terminal covariance distributions under exact fractions, and rechecks the commutator and a two-prior reversal witness. The observed result after a clean replay from embedded files is:

`PASS: 14884 exact-rational identities, schedule comparisons, and finite CDF inequalities`

The theorem for every finite number of sensors and all admissible parameters is a symbolic adjacent-interchange proof. This finite verification is a reproducibility aid, not an exhaustive proof over a continuum of inputs or an independent validation.
