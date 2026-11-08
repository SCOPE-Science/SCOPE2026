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

# Reproduction and scope of the checks

Run `python3 checker.py` using Python 3.8 or newer. Its expected final line is `COMPAT_RANK3_VERIFIED direct_pair_checks= 21343 q3_classes= 4 threshold=4`.

The program separately computes each rank-one ordered-pair signature from the four Venn cells and by direct enumeration of all possible third nonempty subsets, for every pair in every one- through seven-atom frame. It then verifies pointed back-and-forth profiles, truncated symbolic count identities over a broad finite grid, the four observed rank-three theory classes, and the direct witnesses for each sharp boundary. No external packages, network, input datasets, hidden certificates or other artifacts are needed.

The bound-free step is a mathematical one: truncation of the four count variables at two, stabilization of the attainable truncated splits beyond total four, and the explicit finite table of attainable rank-one profiles. Finite checks alone do not establish the infinite theorem. No independent audit or external formal proof validation has been performed.
