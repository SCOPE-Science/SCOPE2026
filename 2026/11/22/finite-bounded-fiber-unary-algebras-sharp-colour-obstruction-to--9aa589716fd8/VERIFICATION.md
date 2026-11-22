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

The all-parameter mathematical argument in RESULT.md establishes the theorem. `verify.py` independently enumerates 13,169 diagrams of finite uncoloured unary functions, with a common substructure of one to three points, extensions of at most four points, and caps 1, 2, and 3. For every diagram it checks both embeddings, consistency of the quotient function and all incoming-fiber bounds. It also checks the fiber-count arithmetic in both obstruction families for each cap from 2 to 8; the incompatible-colour premise is proved symbolically rather than enumerated as an interpreted structure. The expected output is `AMALGAM_VERIFIED 13169 uncoloured test diagrams; color and strong obstructions k=2..8`.

These experiments are finite; they are not a proof of arbitrary finite sizes or of the Fraïssé-limit statements. The latter use a recursive amalgamation proof and the standard extension-property argument. Historical priority is provisional. Independent validation has not been performed.
