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

Run `python3 verify.py` (Python 3.10+ standard library) in the same directory. Expected terminal line: `DURER_DIHEDRAL_ORBIT_HOMOTOPY_OK`.

The program reconstructs the full 18-edge graph, checks 1037 matching faces and 166087 flags, canonicalizes all flags under 12 graph symmetries into 14313 orbit cells, validates 6411 genuine free-face collapses, and proves the quotient fundamental group trivial by 329 reversible presentation eliminations. It verifies signed boundary-square identities and all 744 integral unit reductions, leaving one zero-cell and two three-cells. Reproduction checks are exhaustive for the single explicitly bounded graph, not for arbitrary generalized Petersen graphs. The final homotopy equivalence additionally uses Hurewicz and homological Whitehead arguments given in RESULT.md. No independent review or external certification is asserted.
