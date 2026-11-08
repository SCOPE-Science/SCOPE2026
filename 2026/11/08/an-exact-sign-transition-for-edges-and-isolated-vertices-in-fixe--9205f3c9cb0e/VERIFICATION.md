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

# Reproducibility

The complete finite checks are contained in `verify.py`. Run `python3 verify.py` using the Python standard library. The package checker enumerates weighted hypergeometric occupancy profiles with exact rational arithmetic; for small hosts it independently enumerates all \(k\)-element vertex subsets. It also checks the independent-retention covariance and critical-size scaling using rational arithmetic.

The checker passed 903 exact assertions when executed from the package. These computations test finitely many instances and are not an exhaustive proof of the statements for all \(r,m,k\). The all-parameter proof is given in RESULT.md. The historical originality review identified general joint-occupancy literature whose full text was inaccessible, so publication priority remains conditional on further source examination.
