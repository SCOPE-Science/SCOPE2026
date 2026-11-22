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

For n>=3 and alpha in (0,1), the asserted C* is the Jleli–Samet sharp constant with exactly the Hoang–Moen–Pérez Riesz normalization; it is not a new sharpness proof. Separating the k=0 alpha^-2 hypergeometric term yields gamma_{n,1} C*=(1-alpha)Q_n(alpha)/alpha*(1+alpha² R_n(alpha)). Coefficient bound 0<A_{n,k}<=C(k+1)^alpha and its first two logarithmic derivative variants, times O((k+1)^-2), bound the series R_n and derivatives uniformly for all n>=3, 0<=alpha<=1/2; summability at exponent 1/2 is crucial. Normalized gamma ratios U_n,V_n have bounded second derivatives, so [V_n-W_n]/alpha=delta_n+O(alpha) with dimension-independent remainder and delta_n=ln2+[psi(n/2)-psi((n-1)/2)]/2. Since N^{-alpha/2} is exact external factor and log U_n=O(alpha), n->infinity with alpha ln n ->lambda gives e^{-lambda/2} ln2 and the noncommuting iterated limits. The fixed-n Laurent coefficient follows from R_n(0)=[zeta(2)+psi_1(n/2)]/4 and quadratic gamma expansion. Independent positive-series numerics at alpha=.03 in dimensions 3,6,20,200 corroborated O(alpha) gap errors, but the analytic uniform bounds carry the quantifiers. The primary paper Proposition 6.1 and related equations were inspected in the PDF with page screenshots.

## originality

PASS

PASS best-of-knowledge for a dimension-uniform opposite small-order remainder and joint alpha log n crossover; exact C*(n,alpha) and its series are acknowledged established. The new result is a quantitative asymptotic estimate derived from, not independent of, that series; possible overlooked remarks or easy corollaries of existing sharp constants remain a residual priority risk.

## value

PASS

The competing sharp and classical upper constants share a 1/alpha divergence, so their finite difference is not determined by leading-order BBM behavior. The sharp dimension-uniform remainder and exponential-in-1/alpha crossover quantify how this comparison changes with dimension, including noncommuting limits. This is a motivated endpoint/asymptotic fact rather than a renaming of the earlier sharp value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
