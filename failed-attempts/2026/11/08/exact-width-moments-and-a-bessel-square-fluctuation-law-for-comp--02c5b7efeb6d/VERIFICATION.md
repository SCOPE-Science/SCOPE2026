---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For symmetric edge roots of K(p,q), Gaussian support is S=max|X_i-Y_j| and intrinsic spherical width is W=2S/R with R chi distributed and independent of direction. Conditioning on Gaussian sample min/max gives exact CDF F_{p,q}(t), integrating the survival function and dividing by E R^r yields all positive moments. For p=q=m, four asymptotically independent Gaussian maxima give max of two independent sums of Gumbels; exponential products yield Bessel-square CDF, beta-integral gamma MGF and cumulants 2 gamma +1 and 3. Independent K(2,3) Gaussian CDF quadrature (~0.5140) versus a 140k Monte Carlo estimate (~0.5121), plus gamma differentiation, confirmed normalization; finite Monte Carlo does not prove asymptotics.

## originality

FAIL

FAIL: The already-published October 18 complete-bipartite width theorem gives the same exact finite Gaussian-support CDF, the same balanced Bessel-square limit distribution, and first two centered moments convergence. The submitted finite r moment formula is the standard survival integral combined with the independent chi radius, and the gamma MGF/cumulants are directly determined by that prior same limiting distribution. No substantive mathematical remainder survives.

## value

FAIL

FAIL: While metric width laws for this natural polytope family are generally worthwhile, the entire submitted incremental content is an elementary integral-transform and Mellin/cumulant evaluation of an already complete exact finite distribution and limiting law. It does not provide an unknown structural invariant, new boundary or genuinely new classification after the implication comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
