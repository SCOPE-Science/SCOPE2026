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

# Reproduction and verification

Run `python3 check.py` using the Python standard library. The program directly constructs the finite ternary Cantor digit sets, enumerates all pairs at depth \(1\) through \(8\), checks every modular fiber against the independent matrix implementation, checks all exceptional-digit binomial counts, and verifies the exact energy recurrence. It also independently iterates the two quadratic moments through depth \(34\). The observed output from the packaged code is `CHECK_OK 9935 finite exact assertions plus floating-point sanity check`.

The finite experiments cannot establish infinite-depth conclusions. The proof in `RESULT.md` supplies the all-depth two-state carry matrices, two quadratic-moment identities, conditional output-digit law, and the strong law argument. The closed-form and numerical dimension float checks in the program are diagnostic only, not evidence for exact identities. The abstract recurrence's prior OEIS listing is acknowledged. External independent audit remains unperformed.
