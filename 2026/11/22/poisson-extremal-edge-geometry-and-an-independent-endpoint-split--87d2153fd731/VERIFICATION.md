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

Run `python check.py` with Python 3 and its standard library. The checker exhaustively enumerates all labelled trees encoded by Prüfer sequences for orders two through eight (280,392 trees in total). Its 906 exact assertions verify single-edge and two-edge forest probabilities and falling-factorial moments up to order three for fixed extreme-edge regions. The executed output concludes: `PASS: 906 exact assertions, including 262,144 labelled trees at n=8`.

The independent mathematical audit is not performed. These finite checks corroborate exact identities; the limit proof is contained in RESULT.md, using controlled overlapping-edge tuple counts, mixed factorial moments, and the atom-argmin continuous-mapping argument. Finite numerical checks are not substitutes for those arguments.
