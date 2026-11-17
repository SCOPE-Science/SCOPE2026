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

# Reproduction and scope

The theorem is analytical. To replay the supplementary finite moment and scalar-dynamics diagnostics, run `python CHECK.py` with Python 3; only the standard library is used. The expected output is `PASS: 86 deterministic moment, sign, and series assertions`. The checker computes exact rational Legendre coefficients and moments at orders \(3,5,7,9\), compares the predicted leading moment coefficients, and exercises the exact contrast map using 80-term high-precision moment series at contrasts \(0.1\) and \(0.2\). It also samples a few Legendre bounds; that finite sampling is not the proof of global positivity.

The universal proofs are in `RESULT.md`: harmonic Kubo–Ando representation and explicit shift reduction; analytic expansion of \(H(u)/H(-u)\); uniqueness of compact moment measures; monotone interval squeeze for global consensus; a perturbed logarithmic affine recurrence for the double-exponential profile; and Legendre orthogonality plus Rodrigues' formula for exact all-orders attainment and no finite collision. The independent mathematical audit has not been performed. No checker certifies originality or infinite-dimensional statements by itself.
