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

The proof uses Fourier orthogonality on the full two-dimensional quotient character group, two exact finite-field quadratic-form counting identities, and a classification of isotropic versus anisotropic one-dimensional annihilators. The explicit spectrum and dimension-dependent rank comparison are algebraic statements for all odd prime powers; finite tests are supplementary.

Run `python3 CHECK.py` with the Python standard library. The checker directly enumerates fibers over all projection directions for \(q\in\{3,5,7,9,11\}\), both discriminant classes and both nonzero-radius classes, including the nonprime field of nine elements. It verifies the spectrum multiplicities, cardinalities, maximizing directions, and direct Gram Fourier identities for representative types at \(q=3,5\).

Observed: `CHECK_OK configurations=1300 multiplicity_assertions=5200 direct_gram_classes=24 fields=3,5,7,9,11`.

The direct Gram computations use floating complex characters with a fixed tolerance; the universal proof and every finite fiber-count assertion use exact field arithmetic. No external independent audit was undertaken. The theorem does not treat frequency masks that are not entire linear planes.
