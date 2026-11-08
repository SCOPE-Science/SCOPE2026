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

# Verification of the finite-field parabola Fourier interpolation theorem

The theorem is proved by a complete orthogonal decomposition into multiplicative-character sectors plus the two-dimensional constant/zero sector. The nonstandard singleton-fiber nonvanishing lemma uses cyclotomic irreducibility over the \(p-1\)-st root-of-unity field; the pure quadratic rank uses nonzero minors of the prime-order Fourier matrix. No finite computation is used to replace these all-prime arguments.

Run `python3 check_parabola.py` with Python 3 standard library. The checker computes actual phase matrices over auxiliary modular fields with primitive \(p\)-th roots, obtains **lower bounds** on complex cyclotomic matrix rank from nonzero minors, and compares those with symbolically proved upper bounds. Because reduction may lose rank, it tries multiple auxiliary primes rather than treating a single modular failure as a complex singularity. It tests all 204 weight pairs for \(p\) in \(\{3,5,7,11\}\) and 35 more weight pairs for five larger primes, totaling 239. It also tests 24 character-sector action, nonzero/zero pattern, and two-by-two trace/determinant identities using complex floating-point cross-checks.

Successful checker marker: `PARABOLA_FOURIER_EXACT_MODULAR_RANK_AND_CHARACTER_SPECTRUM_PASS rank_cases=239 spectral_cases=24`.

These computational tests are finite corroboration only. No independent mathematical audit, formal proof assistant, or external certification has been performed. Historical priority is bounded by the sources explicitly checked in the review.
