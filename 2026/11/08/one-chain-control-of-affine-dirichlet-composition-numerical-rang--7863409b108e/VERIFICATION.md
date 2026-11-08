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

# Verification

Run `python3 check.py` with standard Python 3. The script passed `DIRICHLET_DW_JACOBI_CHECK_OK 22575 exact rational assertions` using only `fractions` and standard-library arithmetic. It checks finite positive pivots and their determinant identity, positive-definite stability under reducing weights for negative supporting multipliers, integer orbit decomposition on a bounded domain, and explicit omitted-weight identities.

The proofs for all real parameters and infinite Hilbert spaces are in RESULT.md. The script alone cannot establish them. The referenced publication's Section 5 was read; an older 2004 full article remained inaccessible and is a publication-priority risk.
