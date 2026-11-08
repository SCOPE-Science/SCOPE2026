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
# Verification of the claimed local-derivation classification

Run `python3 verify.py` with an ordinary Python 3 installation in the same directory. No third-party modules are required. The checker constructs the infinitesimal exterior-square action directly from wedge products and exact modular arithmetic. For ranks three and four over the field with three elements it enumerates every central bivector and tests the complete set of linear local-value constraints on a central operator; the solution-space dimensions are nine and sixteen. In rank five over the field with three elements, sampled decomposable inputs give dimension twenty-five; rank four over five elements gives sixteen. The program also explicitly constructs pointwise derivation witnesses for 2,250 cases across ranks two through six and prime fields of orders three, five and seven. The reproducible recorded output appears in `verification_output.txt`.

Finite samples cannot prove an identity for all coefficient fields or all generator ranks. The general argument is the exterior-square tangent-preserver lemma and direct evaluation construction in `RESULT.md`. Characteristic two and nonlinear local maps are not treated. No independent audit or formal proof certificate is claimed.
