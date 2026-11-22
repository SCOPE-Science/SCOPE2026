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

For |z|<=R<1, |sech²(sz)|<=sec²(sR) by |cosh(x+iy)|²=sinh²x+cos²y, hence |tanh z|<=c_R|z|, c_R=tan R/R, equality at z=iR. At a maximum-modulus vertex, undirected nonnegative Laplacian coupling cannot increase the modulus, so upper Dini M'<=-(alpha-beta c_R)M. Synchrony z_i=iR gives outward motion at negative delta and nonzero equilibria at delta=0. With delta>0 the analytic f' satisfies Re f'<=-alpha+beta+beta c_R² M(t)²; the Laplacian Poincare inequality integrates to ||Pz(t)||<=exp[beta tan²R(1-e^{-2delta t})/(2delta)]e^{-(alpha-beta+kappa lambda2)t}||Pz(0)||. A small Fiedler-vector perturbation has a nonzero limiting rescaled projection by an integrable cubic forcing, certifying uniform exponent sharpness. Euclidean-to-Kobayashi comparison on |z|<=R gives the pairwise metric bound. No claim extends beyond this polydisc.

## originality

PASS

Sarkar 2026 full HTML specifically predicts the six-cycle transverse rate 1.85 from linearization and numerical observation and gives a weaker uniform node contraction estimate around 0.402; it does not prove all-initial-data all-graph nonlinear disagreement at exact optimal spectral-gap rate or an all-radius iff invariant-polydisc boundary. The pre-existing linear prediction is clearly credited. Generic 2014 synchronization and 2023 structural contraction papers do not supply these sharp model-specific quantified bounds.

## value

PASS

The motivating holomorphic-network study explicitly exhibits a large gap between certified node-wise contraction (~0.402) and graph-spectral decay (~1.85) on a six-cycle. A theorem replacing that empiricism with a globally valid nonlinear all-graph optimal exponent, sharp invariant-disc radius and Kobayashi-distance control is a motivated quantitative contribution, beyond textbook linearization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
