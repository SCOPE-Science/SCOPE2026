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
# Verification and limits

The proof in RESULT.md establishes the parameterwise classification for every odd finite field of characteristic other than three, not merely for tested finite fields.

Run `python3 verify_hesse.py` in a standard Python 3 interpreter. It checks the complete smooth marked-parameter census over prime fields of orders 5, 7, 11, 13, 19 and 31 using independent projective point enumeration; checks the flex-tangent cubic restriction for all base-field flexes in characteristics 7, 13, 19 and 31; and enumerates all points over two quadratic field extensions, at sizes 25 and 49, as an independent test of extension-field zeta consequences. The expected final line is `HESSE_CUBIC_SURFACE_FROBENIUS_VERIFIED`.

Computations over these sample fields cannot prove a statement about all primes. The proof instead uses the explicit nine flex-tangent factorizations, complete twenty-seven-line enumeration, Frobenius action on cube roots, and standard Picard/cohomological trace facts for smooth cubic surfaces. No external or independent mathematical audit was performed.
