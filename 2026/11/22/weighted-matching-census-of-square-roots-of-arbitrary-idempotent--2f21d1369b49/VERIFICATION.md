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
# Reproducible verification

Run `python3 verify_roots.py` using only the Python standard library. The command was executed from the same packaged source file, and its exact stdout is in `verification_output.txt`.

The script enumerates all \(n^n\) functions for \(1\le n\le7\), groups by the actual square \(g^2\), discards non-idempotent squares, checks the exact root count for every remaining \(f\), and independently evaluates the stated formal exponential series using rational arithmetic. For \(u=1,2,3\), it also verifies the rank-weighted enumerator for all seven fully enumerated degrees. The largest enumeration has \(7^7=823543\) input maps. Exact arithmetic is used throughout.

Reproduced total counts for \(n=1,\ldots,7\): \(1,4,25,194,1791,19312,237637\). The formal-series value at \(n=8\) is \(3280524\); it is not claimed to have been exhaustively enumerated. The output ends with `FIXED_IDEMPOTENT_SQUARE_ROOT_PROFILE_VERIFIED`.

The finite checks are not a substitute for the infinite bijective proof in `RESULT.md`. No Lean, external expert, or independent audit was performed.
