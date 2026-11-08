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

# Reproducible verification

The standalone source file `verify_fourier_triad.py` is embedded in the same package. With Python 3 and SymPy available, run `python verify_fourier_triad.py`. It enumerates all signed zero-sum Fourier quadruples for the three positive frequencies, independently integrates the trigonometric quartic by symbolic cosine integration, verifies the exact one-variable derivatives, counts real roots in specified rational intervals using exact polynomial root isolation, checks both algebraic endpoint resultants and the exact amplitude symmetrizations, and tests 240 seeded complex coefficient triples by independent convolution. It reports `ALL_FOURIER_TRIAD_CHECKS_PASSED` only if every assertion succeeds.

The checker was run successfully on the complete bundled source: all exact symbolic assertions, Sturm-style root counts, algebraic endpoint resultants, and 240 seeded complex-coefficient diagnostics passed. The positive cubic roots were estimated as 0.2776482755356 and 0.8764907989146, with fourth-moment ratios 1.2206918950372 and 3.4080115812182.

All symbolic equations concern exact arithmetic; decimal output is diagnostic. The 240 random trials are neither exhaustive nor an infinite proof. The universal claims instead follow from the explicit inequalities and endpoint analysis in `RESULT.md`. The references' contents were inspected through publicly accessible full HTML renderings, not inferred merely from downloads. No independent mathematical audit has been performed.
