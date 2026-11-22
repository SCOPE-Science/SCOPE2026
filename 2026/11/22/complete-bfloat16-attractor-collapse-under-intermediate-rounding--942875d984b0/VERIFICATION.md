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

# Reproduction

Execute `python3 verify_bfloat_spm.py` in a directory containing the attached standalone file. The program uses only the Python standard library's exact-rational `fractions`, integer bit manipulations and graph algorithms. It computes all 16,257 successors of each rule and performs every calculation with exact integers or rationals; the host's binary floating-point rounding is not used. Both rational rounding implementations produce identical successor arrays, and both exhaustive graph decompositions agree on each state's basin and preperiod. The asserted cycle table and 2,205 changed successors are produced directly by this computation.

`certificate.json` records the 3 and 2 cycles, their sorted exact 16-bit codes, the complete basin cardinalities and the SHA-256 digests of the entire successor arrays. Recomputing the digests checks transcription of the finite arrays but does not replace the executable exact proof. No infinite-state or real-measure claim is inferred from this finite certificate.
