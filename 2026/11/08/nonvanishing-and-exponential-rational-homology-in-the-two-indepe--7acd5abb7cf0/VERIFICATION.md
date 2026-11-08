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

# Verification notes
The standalone code `verify_square_cycle.py` uses the original 16-state signed transition rule and computes the exact characteristic polynomial using Newton identities over integers, without an external algebra package. It also computes independent direct face sums for every \(5\le n\le16\) and checks the two local predicates separately. The recorded output file `verify_square_cycle.out` ends in `ALL_CHECKS_PASS`.

For a reproducible replay in a folder containing both files, run `python3 verify_square_cycle.py`; its standard output is the provided text file. The characteristic-polynomial step is exact integer arithmetic. The 7-step positive recurrence plus the displayed initial values proves universal nonvanishing by induction, so the claim does not require extrapolation of finite enumeration. The asymptotic and rational homology bound are mathematical deductions described in RESULT.md; no numerical root approximation is used as proof.

No independent mathematical validation has been carried out, and these checks neither identify individual Betti numbers nor classify homotopy types.
