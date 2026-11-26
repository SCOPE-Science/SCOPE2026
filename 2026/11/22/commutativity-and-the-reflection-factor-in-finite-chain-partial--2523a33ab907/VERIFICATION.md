---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The proof of the mixed incidence census in `RESULT.md` uses the idempotent centralizer criterion, distinguishable affine extensions in rank at least two, forest counts for nonzero translations, orbit counts for reflections, and overlap corrections in ranks zero and one.

Run `python check_commutation.py`. It enumerates distinct finite-chain partial isometries for \(2\le n\le7\), compares both orders of composition as partial maps, and checks the exact mixed census and the known total size. `check_output.txt` is the recorded output and also reports the small-size all-pair totals. These finite totals do not establish a general count; the all-size mixed census follows from the proof.
