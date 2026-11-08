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

Run `python3 verify.py` from the extracted package directory. The script prints `VERIFY_OK 554 exact rational assertions` after enumerating the relative ranks of all original and refreshed independent edge samples for cycle sizes \(2\le n\le4\), all refreshed counts, checking exact rational probabilities, comparing strict log-convexity and small-noise bounds at several rational refresh probabilities, and exhaustively checking cycle-length-profile extremizers for bounded total cycle-edge budgets. 

These are separate finite checks of the claimed identities. The all-order conclusions are established by the algebraic and analytic arguments in RESULT.md; no finite enumeration is construed as an infinite proof. The original and refreshed weight laws are both iid atomless and the Bernoulli refresh indicators are independent. No independent audit is asserted.
