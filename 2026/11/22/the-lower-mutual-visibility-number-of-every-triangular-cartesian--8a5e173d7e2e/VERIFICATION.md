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

The complete normalized search is given in `canonical_check.py`; its BFS only walks edges that decrease distance to the target and excludes any selected internal node. It reports seven types, 133 feasible triples and 132 in-column extensions, with the unique vertical triangle exception. The graph-distance normalization lemma in `RESULT.md` upgrades this finite check to arbitrary path length.

An independent verifier `verify_strip.py` constructs shortest paths by choosing the vertical-switch column, then checks every triple and the four-set witness on labelled triangular cylinders for all lengths from 2 to 12. Its full output, together with the normalized checks, is included in `CHECKS.txt`.

No computer check by itself establishes novelty, infinite-dimensional extrapolation, or independent review. The proof relies on the explicitly stated reduction lemma; finite experiments do not replace that lemma.
