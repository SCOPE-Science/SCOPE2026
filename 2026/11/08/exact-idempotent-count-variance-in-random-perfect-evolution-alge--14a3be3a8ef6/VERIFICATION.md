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

# Verification of the finite-field idempotent-count second moment

The mathematical proof is in `RESULT.md`, particularly the exact pair-count and the support-sign binomial computation. A standalone finite checker is provided at `checks/variance_checker.py`; run it from this package's root using `python3 checks/variance_checker.py`. It uses only the Python standard library, constructs finite-field arithmetic for the prime fields and the extension fields of orders \(4\), \(8\), and \(9\), tests invertibility by elimination, and enumerates nonzero idempotents for every invertible matrix in its stated test cases.

The checker compares exact rational means and variances with the theorem, and separately counts exceptional independent pairs whose coordinatewise squares become dependent for \(q^n\le81\). Ten complete finite parameter pairs were tested, culminating in `VERIFY_OK` recorded verbatim in `checks/variance_verification_output.txt`. Every tested count was exhaustive **within its specified finite parameter pair**, not across the theorem's infinitely many pairs.

For the test \((q,n)=(3,3)\), there are 11,232 invertible matrices and variance \(23/26\). For \((q,n)=(2,4)\), the 20,160 invertible matrices have variance exactly one. The script has been executed with the packaged contents.

Limitations: these finite checks do not establish correctness in arbitrary dimensions or fields; that depends on the symbolic proof. No external independent audit or formal proof certificate is claimed.
