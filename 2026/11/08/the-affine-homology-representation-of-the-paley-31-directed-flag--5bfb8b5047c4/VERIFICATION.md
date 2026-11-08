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
# Reproducibility and bounds
Run `python3 verify.py` in a standard Python 3 environment. This standalone script builds the quadratic-residue Paley tournament, enumerates its entire transitive-subtournament complex, computes each mod-two chain rank, checks consecutive boundary composition, enumerates every affine symmetry, and checks the complete rational character identity. All loops have finite explicit ranges; no random sampling is used.

The actual recorded output is `verification_output.txt`. Confirm the final marker `PALEY31_AFFINE_HOMOLOGY_CHARACTER_PASS`, the face vector (31,465,3255,9765,10695,3255,465), the mod-two ranks (30,435,2820,6945,2790,465), the character-value multiplicities (960 at one identity, -1 at 30 translations, 0 at 434 remaining elements), and invariant dimensions 2 and 30.

Mod-two ranks and Euler characteristic prove the rational homology concentration, but do **not** prove a lack of integral torsion. The representation character statement is about rational homology. The mathematical arguments converting finite calculations into the representation theorem are supplied in `RESULT.md`. No independent mathematical audit is asserted here.
