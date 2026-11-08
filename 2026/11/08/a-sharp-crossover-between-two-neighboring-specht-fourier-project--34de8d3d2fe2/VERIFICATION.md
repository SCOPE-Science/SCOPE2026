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
# Verification and reproducibility

`python3 verify.py` in the same directory as `finite_certificate.tsv` runs only Python 3 standard-library exact arithmetic. It checks every finite sign up to degree 29 against the separately stored exact fractions, reconstructs the zero-small-cycles coefficients both by the logarithmic-derivative recurrence and signed inclusion–exclusion, verifies the second moment of both irreducible characters is one, and directly enumerates the 46,224 permutations of orders four through eight. The exact degree-30 comparison and rational inequalities validate the constants used by the analytic proof.

The all-degree claim is proved by the explicit entire-function coefficient argument in RESULT.md, not by the finite checks. No computation establishes an unrestricted claim by sampling. The checker is not an independent mathematical audit; no separate audit has been performed.
