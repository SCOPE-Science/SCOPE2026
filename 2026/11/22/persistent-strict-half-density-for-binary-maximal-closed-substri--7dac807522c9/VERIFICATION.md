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

The standalone `verify.py` directly tests closedness by enumerating all proper borders and all their occurrences; it independently tests both one-step maximality conditions. It checks every prescribed interval for both parity families for parameter values from 2 through 30 and, for the smaller values through 9, exhaustively enumerates all crossing MCS intervals at the chosen cut. `verification-output.txt` is the actual standard output from executing that source. The exact infinite claim depends on the written longest-border/context proof, not on extrapolation from these checks. No independent audit is asserted.
