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

The two ordinary Python 3 verification programs are standalone, do not read remote resources, and have no nonstandard dependencies. They can be executed from any current directory using their relative or absolute paths.

`verify_translation.py` implements exact integer polynomial arithmetic and verifies all equations describing the normalized conic, tangent incidence, other intersection point, and next tangent. It also checks translation-coset and reversal counts over quadratic extensions for \(p=3,5,7,11,13\). Successful completion prints `VERIFY_TRANSLATION_OK`.

`verify_flags.py` implements the ground-field and degree-two extension field operations independently, enumerates every pair of rational finite conic and tangent parameters, checks the tangent incidence equation, follows the actual two-step geometric correspondence, and distinguishes simple versus repeated-vertex cycles. For \(p=3,5,7,11\) and extension degrees one and two, the number of unoriented simple polygons is respectively \(0,1,0,2,0,3,0,5\). Successful completion prints `VERIFY_FLAGS_OK`.

The proof of the theorem for all odd prime powers is symbolic and combinatorial, not inferred from these finite computations. Characteristic two, conic pairs of type \((4)\), and polygon counts using non-rational vertices or tangent points are outside the claim. No independent mathematical audit has occurred.
