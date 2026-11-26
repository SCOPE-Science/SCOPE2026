---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The displayed spectral theorem and Cesàro inequality are correct. The gap of a pair k<l is 4|sin((l-k)a) sin((l+k)a+θ)|. If n is odd, the lower bound uses sin a and the smaller of sin θ and sin(a-θ); pairs ((n-1)/2,(n+1)/2) and (0,n-1) attain the respective branches. If n is even, sum and difference have the same parity modulo n. Even sums give sin θ and nonzero even differences give sin(2a), attained at (1,n-1); odd sums give sin(a-θ) and odd differences give sin a, attained at (0,n-1). These witnesses include n=3,4 and give zero at the appropriate endpoints. One branch increases and the other decreases, so their unique crossing gives π/2 or n arctan(tan(a)/3); the optimal values and limits follow by substitution and small-angle expansions. The n(n-1) off-diagonal position terms each carry magnitude 1/n² and integrate to at most 2/(Tg_n) after time averaging, yielding the displayed inequality. Line 55 reverses the direction in prose: the optimizer maximizes the denominator g_n and minimizes the right-hand side, not the denominator itself. It need not optimize actual mixing. Independent direct all-pair comparisons at 48 size–flux points agreed within 1.33e-15 and all eight explicit optimum values agreed.

## originality

FAIL

The indexed dephasing result states the same minimum over distinct indexed Fourier labels, the same gap branches, the same unique optimum in the half-circle and both parity limits, for arbitrary positive hopping. Its finite-time channel bound also implies the pointwise estimate. This is exact distinct-record coverage, not a priority claim based on its later November 2 catalogue date.

## value

FAIL

Optimizing a worst-pair dephasing scale on a magnetic ring is a meaningful objective. For this package, however, the exact optimizer and benchmark are already covered along with a stronger dephasing statement; the site-wise bound is a projection of that channel inequality and the wording correction would add no scientific result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
