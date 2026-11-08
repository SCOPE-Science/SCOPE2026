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

The analytical proof works for all integers \(d\ge3\), \(1\le k\le d\); the \(k\ge3\) restriction is exactly the injective regime. The source and equatorial fourth-moment identities are proved directly from rotational invariance, and the diagonal/off-diagonal decomposition determines every eigenvalue and its multiplicity. A two-coordinate harmonic supplies the obstruction for fewer than three equators.

The bundled checker independently assembles generalized Gram matrices from spherical fourth moments, resolves all eigenvalues for \(3\le d\le11\), and tests weight perturbations and spherical Monte Carlo moments. Replay command: `python check_equator.py`. Expected output: `EQUATOR_QUADRATIC_CHECKS_PASS 670`.

Finite numerical checks do not prove the uniform theorem, uniqueness of optimizers, or the absence of covered earlier literature. The proof in RESULT.md supplies the mathematical argument. The result does not concern scalar Funk–Radon means, arbitrary section orientations, or discrete/noisy sampling. No independent mathematical audit has occurred.
