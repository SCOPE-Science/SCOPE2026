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

## Executed checks
Run `python3 verify.py` using the packaged source, from the directory containing it. This enumerates all 512 masks for the base 3-by-3 graph and checks all 36 group elements against the sign character; separately checks 144 group elements at width four, every face-preserving retract at widths three through five, and integral lattice dimension identities. Recorded standard output is in `verification_output.txt`.

## Scope of verification
The finite character calculation establishes the base representation because the integer rank-one statement is independently provided by the published Theorem 1.4. The general result follows from the explicit retraction proof, not finite extrapolation. Originality is a best-knowledge literature comparison, not a certification of absence of unknown results. No independent mathematical audit was performed.
