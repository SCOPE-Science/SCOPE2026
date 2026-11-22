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

The result is established by the written proof in `RESULT.md`. The accompanying standalone `verification_check.py` uses no third-party packages. Execute `python3 verification_check.py` from this directory.

The checker compares direct polynomial row ranks mod \(p\) against the closed two-block profile for \(p=2\) and \(3\), with prime-power separation and many admissible block lengths. It independently enumerates all free initial-coordinate strings for small \(t\), extends them by the homogeneous finite-difference recurrence, and compares the resulting observed pattern set to \(p^{r_E(t)}\). Output of the checked package is:

`PASS: two-block ranks 510 direct initial words 68279`

All finite tests passed; they are not a substitute for a proof in the unbounded time, prime, separation or block-size parameters. No independent audit or validation is claimed.
