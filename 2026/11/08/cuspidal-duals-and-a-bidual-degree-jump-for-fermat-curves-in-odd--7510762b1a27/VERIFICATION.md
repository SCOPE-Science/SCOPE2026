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

## Reproduction

Run `python3 verify_fermat_dual.py` using Python 3 (standard library only). The expected stdout is archived as `verification_output.txt`; successful output ends with `ALL_DUAL_AND_BIDUAL_FINITE_CHECKS_PASSED`.

The verifier constructs \(\mathbb F_9\) and \(\mathbb F_{25}\) as quadratic extensions, exhausts all 91 and 651 projective points respectively, and compares the Fermat locus, the discriminant equation of the proposed dual, the image under coordinatewise squaring and the Gauss map image. It checks field-rational singular points and a gradient identity on torus points. The two finite-field checks are not exhaustive over algebraic closures, nor do they test all powers \(p^e\); the written proof establishes those claims.

The singularity normal form follows from an explicit étale local change of coordinates, and the bidual degree follows from an independently justified generically birational power morphism. These assertions are mathematical, not computational certifications. No independent audit has been performed.
