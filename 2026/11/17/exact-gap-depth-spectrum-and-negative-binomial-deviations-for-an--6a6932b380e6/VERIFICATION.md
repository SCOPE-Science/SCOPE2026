---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The primary Appendix B.1 provides the full shift, strongly separated branch images, generation multiplicities and r^-k affine contractions. Multiplying branch counts for compositions of S into n positive parts gives N_{n,S}; summing logs of r^-k gives exact length 2r^-S. Stirling cylinder covers for S/n near m give the upper bound H(m)/(m logr), with m=1 from the delta-neighborhood limit. A finite alphabet Bernoulli law truncated from geometric mean-m and adjusted with an extra depth restores the exact mean m; the finite strongly separated IFS dimension theorem and entropy continuity give a matching lower bound, so this is not extrapolation of a finite enumeration or an unsupported countable-symbol theorem. Differentiation of H(m)/m gives log(2/(m-1))/m² and the maximum m=3, high-m floor log2/logr. Since each depth-k branch has conformal mass 3^-k, aggregation gives P(k)=(1/3)(2/3)^(k-1), independent under full shift; the multinomial generating function gives P(S_n=S)=N_{n,S}3^-S. Uniform Stirling for m=S/n in compact (1,infinity) gives exp(-n[m log3-H(m)])/[sqrt(2 pi n m(m-1))]*(1+O(1/n)); at S=n probability 3^-n exact. Independent enumerator checked all composition totals n=1..5, S=n..n+5; finite checks validate only combinatorial ingredients.

## originality

PASS

Best-of-knowledge originality; four explicit comparisons and actual primary-source material inspections below. Knowing total dimension is a maximum over conditional levels, not the function of the prescribed finite m. Nor does invariance/conformality alone give a local central prefactor without exact branch weights and Stirling expansion.

## value

PASS

The stage depth of a Cantor gap is a canonical symbolic/geometric observable of the published natural return map, and the precise Hausdorff dimension for every finite average depth reveals a stratification not present in its known total dimension. The high-mean positive dimensional floor and precise atypical-depth probabilities are potentially reusable quantitative orbit statistics; ordinary negative-binomial algebra is not the value claim by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
