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

# Verification of the finite marked-base spectrum

`verify.py` independently enumerates order insertions and all cut-depth words, then compares the results with the rational generating series from the theorem. An extension of a base is counted if deleting the new labelled elements recovers each original adjacent old cut-depth as the maximum depth on the intervening new gaps. All counts are integer exact.

In the recorded run, 420 exhaustive small extension instances matched, eight exact Vandermonde determinants matched, 455 entire fiber multiplicities matched, and the three-point example agreed through arity four. The exact all-arity proof is in `RESULT.md`; this finite verification is not an infinite certificate. The checker makes no authorship, independent-audit, or novelty claim.
