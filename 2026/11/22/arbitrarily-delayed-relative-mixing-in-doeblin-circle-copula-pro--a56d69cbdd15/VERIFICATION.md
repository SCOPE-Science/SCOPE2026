---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Both marginals integrate to one by circular translation. The projection onto uniforms commutes with the reflected-walk transition, so the pure n-step density discrepancy is scaled by ε^n; the reflected increments alternate signs, giving the stated lag kernel and TV bound. Markov conditioning at the two boundary states gives the bound by the essential density discrepancy; endpoint rectangles shrinking to Lebesgue points give equality even for infinite supremum. For maximal correlation the corresponding centered operator norm is on real sine/cosine blocks with eigenvalues ±ε|fhat_a(k)|. Riemann–Lebesgue and the strict triangle inequality yield a attained nonzero maximum less than one for the unmixed generator. The oscillatory gamma integral with the tail integrated by parts gives leading phase exp(−iπ(1−a)/2) and power k^(−(1−a)), uniformly locally in a with error O(k^−1). If n(1−a)>1, the lag Fourier series is absolutely summable. Otherwise its real coefficients are eventually positive and bounded below by a constant times k^(−n(1−a)), including at odd n where the limiting phase has positive cosine. At zero the Fejér means then diverge, since the weights at k up to half the order are at least 1/2. This rules out essential boundedness also at equality. For even lag the nonnegative series attains the absolute discrepancy supremum at zero, and Parseval gives the two-step rational formula. At a_m the summed error after raising magnitudes to power 2m is bounded uniformly by a summable k^(−1−a_*) for a positive a_* near the boundary, leaving the zeta pole with residue ε^(2m)c(a_m)^(2m)/m in the variable a_m−a. Taking a=1−1/L for L≥2 and sufficiently small ε gives the claimed separation; L=1 allows any a>0.

## originality

PASS

The rotating/reflected copula construction, signed convolution product and relevant Fourier representation are covered; regeneration and the spectral formula are direct operator consequences, not independently novel ingredients. The retained distinction is the quantitative cusp calculation: first finite relative-mixing lag, including odd lags and equality, exact finite even-lag values with the explicit critical pole, and the resulting arbitrarily long initial plateau of infinite ψ under arbitrarily small one-step ρ. No inspected statement establishes that classification for this generator.

## value

PASS

The parameterized example gives a sharp counterexample to interpreting rapid total-variation regeneration or small maximal correlation as control of relative event dependence. It separates the quantities for a prescribed number of lags, then identifies mathematically how the separation ends, including the precise blow-up of even-lag values. The cutoff and transition are meaningful for interpreting uniform density error in singular copula models, irrespective of the known Fourier and regeneration tools used to derive them.

The dated certificate retains the supplied scientific assessment, sources and limitations.
