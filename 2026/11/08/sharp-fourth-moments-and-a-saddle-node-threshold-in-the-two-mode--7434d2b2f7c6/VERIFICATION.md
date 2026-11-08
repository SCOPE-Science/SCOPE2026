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

## Reproduction
Run `python check_ch.py` with SymPy 1.14.0. This executes exact algebraic assertions for Poisson raw moments through degree eight, the first two Charlier-mode orthogonality, the normalized fourth-moment stationary polynomial, its discriminant, the rational Sturm sign changes, and the global-minimum comparison certificate. The checker is evidence for the explicitly stated identities, and not an external or independent certification.

## Boundaries
The infinite-parameter conclusions follow from the displayed analytic proof and Sturm/positivity certificates. Representative sample root counts are ancillary only. Mathematical priority beyond the inspected sources is not certified.
