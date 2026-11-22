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

# Reproduction and checks

Install the declared `requirements.txt` dependency and run `python3 verify.py`. The source enumerates barycentric chains of the two-skeleton of a simplex, cyclic translation orbits and all integral signed boundary maps for widths 5, 6, 7, 8, 9, 10 and 12. It verifies the boundary-square identities, Euler characteristic formula and the predicted quotient two-dimensional cell counts; at widths 5 through 9 it also obtains integer Smith forms of relators after a maximal tree is contracted, checking first integral homology exactly. The verified run printed `CYCLIC_KNESER_SINGULAR_QUOTIENT_CHECKS_OK`.

These finite experiments do not prove the unrestricted theorem or establish publication priority. The general fixed-point and fundamental-group conclusions follow from the explicit group action and Armstrong's theorem, not from extrapolating Smith forms. The equivariant two-skeleton reduction is supported by a separately published orbitwise collapse theorem, which is cited in `RESULT.md`.
