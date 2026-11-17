---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The frozen RESULT.md erasure inclusion-exclusion expresses all nonzero-lag correlations in a factored cosine product, with two exceptional lags corrected separately. Expanding its squared moduli produces the displayed Gauss sum G_p(u) and the exactly stated congruence-class formula, and square scaling r=u d^2/4 proves spacing invariance. Pólya-Vinogradov via quadratic-character Fourier transforms supplies both residue signs within O(sqrt(p)log p) intervals, giving the asymptotic O((log p)^2/sqrt(p)) error. Direct independent complex autocorrelation for primes 3,5,7,11,13 and all roots with d=1 agreed numerically to <1e-6; this only corroborates the exact all-prime proof.

## originality

PASS

PASS best of knowledge: The primary Gregoratti–Arteaga–Broquetas paper establishes perfect periodic Zadoff–Chu autocorrelation, Fourier phases and OFDM continuous-time properties for full sequences, not exactly two fully erased cyclic positions or their all-root integrated squared sidelobe spectrum. Resultary one-erasure work concerns a distinct deletion count. The submitted exact two-erasure Gauss-sum formula and sharp two-prime-class minima are not a restatement of those claims. Residual risk remains from specialized partial-period / punctured-sequence engineering literature not fully retrieved.

## value

PASS

The integrated squared periodic sidelobe energy after two complete erasures is a natural code-degradation invariant; the exact spectrum, spacing invariance, and different prime-class sqrt(p) savings could be used in cyclic correlation design and are not merely a renaming or trivial single-case computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
