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

`verify.py` enumerates all actual partial maps in the candidate family, tests equality of both composed partial functions by computing their surviving sources, and compares the result with the run-factorization formula and an independent four-state bivariate rank DP for all \(1\le N\le8\). It also checks the extremal centralizer sizes and the number of maximizers for \(1\le N\le10\). The file `verification_output.txt` contains the output of a successful replay; the final marker is `VERIFY_OK`.

These finite experiments do not establish the infinite theorem; the general proofs are in RESULT.md. No external or independent validation has been performed.
