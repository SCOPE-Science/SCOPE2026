---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Angular frequency n−1 survives the projection; integrating t=|z|² gives the unprojected squared norm (n+1)q_{n+1} and the sole projected coefficient squared n q_n² (zero for n=0). The residual cannot vanish: it is nonzero inside the disk and the multiplier vanishes outside, which no nonzero entire function can do. The factorial tail bounds every positive Schatten power at fixed T. With d_n=q_n(1−q_n), r_n=Pr(X=n+1), the exact identity is λ_n=q_n+n d_n−(n+1)r_n. On compact u windows the Poisson CLT and local mass bound give uniform λ_n/T→Φ(u)Φ(−u). Chernoff gives d_n≤C exp(−c(n−T)²/T) on [T/2,2T], exponential smallness on the left and geometric summability past 2T (the Poisson mass ratios are ≤1/2 there). This proves the tail sup bound and the level counts because all positive submaximal levels of the limit have measure-zero boundaries. It proves the stated Riemann sums, with q_n→1 uniformly below (1−δ)T and exponentially small beyond (1+δ)T. For p>1 the sharp upper bound is obtained by applying the coarse C_p bound only to the complement of the fixed A√T window: bulk is negligible and the rescaled edge tail is at most C_p times a Gaussian-tail integral tending to zero with A. For p<1 subadditivity and λ_n→1 on the strict bulk give both inequalities. At p=1 use a=√q_n, b=√(n d_n), c=√((n+1)r_n): the loss in replacing √(a²+b²−c²) by a+b is bounded by min(a,b)+c using √x−√(x−c²)≤c. In a relative δT window min(a,b)≤1 and Cauchy–Schwarz bounds the c sum by √(2δT+O(1))√T; outside, both losses are o(T). This yields 1+I₁. I₂ is the mean positive part of an N(0,2) difference. Inspected CHECK.py by reading; its quadratures and truncated spectra are diagnostics, not what controls the infinite sums.

## originality

PASS

Qualified for the exact hard-cutoff anti-analytic Hankel spectrum and combined Schatten laws. The normalized Gaussian-product edge, including its constants after taking the appropriate square root/power, is inherited and is not assigned independent priority.

## value

PASS

For a canonical cutoff of the simplest anti-holomorphic coordinate the trace has simultaneous contributions from distinct populations, and assigning only the conventional boundary contribution would give the wrong leading coefficient. The exact mode sequence and sharp Schatten split are useful benchmarks for general localization theorems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
