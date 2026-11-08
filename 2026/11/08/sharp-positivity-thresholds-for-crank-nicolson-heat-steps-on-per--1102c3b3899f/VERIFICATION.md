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

# Reproduction and boundaries

Run `python artifacts/verify.py` with the Python 3 standard library. The bundled output reports `PASS: 3602 standalone deterministic checks` after reconstructing exact rational periodic heat matrices and elementary finite Fourier identities. Exact inversion checks cover selected \((d,n)\) pairs; the rational three-by-three polynomial and the dimension/side sample inequalities were tested independently of symbolic derivations. Separately, the elliptic root \(0.5881972836856281148591326751432091073597\) was computed from the explicitly stated modulus-convention complete elliptic integral at 40 decimal digits.

Analytic verification, not the finite script, is needed for the strict monotonicities at all \(d,n\), the all-state positivity equivalence, the exact one-dimensional finite-period correction, and the uniform high-dimensional asymptotic. The proof includes the Bessel ratio Riccati argument, the Fourier/Green formulas, the two-dimensional moment-to-elliptic reduction, and uniform bounded-moment Taylor remainder. No independent audit has been performed.
