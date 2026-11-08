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

# Reproducibility and limits

Run `python3 tau_magma_verify.py` in the directory containing the standalone file. Python 3 standard library suffices. The recorded output is `verification_output.txt` and terminates with `VERIFY_OK`.

The program checks cycle identities in ranks two through four, calculates the socle from its definition in ranks two through five, and exhaustively checks all operation-preserving permutations in ranks two and three both with and without the distinguished-point requirement. At rank four it constructs all predicted pointed and unpointed maps and tests the operation law, uniqueness and counts; it does not enumerate all permutations of the sixteen-element underlying set. Linear pointed maps are checked by additivity; rank-five orders are arithmetic evaluations of the formula only. All-rank completeness follows from the intrinsic left-translation-orbit proof in `RESULT.md`, not from computational extrapolation.

The scientific literature comparison examined the 2026 Byott–Jasko preprint in detail, while the older foundational Rump paper and the broad retraction theorem were available only at abstract level. Historical priority remains qualified; no independent audit or external certificate is asserted.
