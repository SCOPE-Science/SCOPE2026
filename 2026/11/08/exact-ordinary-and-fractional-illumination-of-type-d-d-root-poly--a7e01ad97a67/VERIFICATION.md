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

# Reproduction and limits
Run `python3 verify_root_family.py` with Python 3; no external packages are needed. It enumerates every signed two-sparse vertex for each integer dimension from four through fifteen, checks all inward inequalities directly in exact integer arithmetic and confirms that every vertex occurs in exactly one direction's illuminated set. A dimension-three comparison is supplementary and not part of the new general claim. The exact output ends with `ROOT_FAMILY_EXACT_OK`. The dimension-free proof in RESULT.md, not the finite enumeration, establishes the theorem for all integers at least four. Independent mathematical audit has not been performed.
