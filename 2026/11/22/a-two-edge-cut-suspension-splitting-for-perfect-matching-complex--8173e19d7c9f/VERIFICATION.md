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

# Verification and scope

`checker.py` uses exact combinatorial perfect-matching enumeration and exact mod-two matrix elimination. Run `python checker.py` with Python 3 and no third-party dependencies. It checks both-cross/zero-cross parity in the twelve-vertex example, all 234 maximal simplices, the complete face vector, the intersection of the two subcomplexes, and every mod-two reduced boundary rank. Its output supplies finite evidence for the explicit example; the unrestricted integral homotopy formula is established by the written parity, intersection, star-contraction and homotopy-pushout argument.

The decomposition is nonequivariant and relies on all four specified perfect-matching complexes being nonvoid. The checker is not a computer proof of the general theorem. Independent audit: not performed.
