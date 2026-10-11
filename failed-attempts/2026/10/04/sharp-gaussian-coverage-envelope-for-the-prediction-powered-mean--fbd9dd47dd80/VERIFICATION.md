---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Gaussian independence reduces coverage exactly to \(\mathbb E h_z(Q)\), where \(h_z(q)=2\Phi(z\sqrt q)-1\) is strictly concave and \(Q\) is a weighted sum of two independent normalized chi-squares. Expanding both chi-squares into iid \(\chi_1^2\) variables, pairwise averaging of coefficients gives \(\chi^2_{N+n-2}/(N+n-2)\le_{cx}Q\), while concentration on the block with fewer degrees of freedom gives \(Q\le_{cx}\chi^2_{\nu_*}/\nu_*\). Concavity yields the two central-Student bounds, strictness identifies the upper balance condition, and a boundary variance ratio gives sharpness below. The numerical example \((n,N,z)=(10,100,1.96)\) was independently recomputed as \(0.9183555945395834\le\mathrm{coverage}\le0.9474279305425579<0.9500042097035590\).

## originality

FAIL

Richter's open full article already gives the exact Student-bridge representation of this Behrens--Fisher statistic for every variance ratio, identifies the two endpoint Student laws and the balanced \(t_{N+n-2}\) law, and writes the denominator as the same weighted sum of normalized chi-squares. Once that representation is read, the claimed global envelope follows from the standard one-line majorization fact for weighted iid sums: averaging two coefficients reduces the sum in convex order, while the most concentrated feasible coefficient vector has exactly the smaller degrees of freedom. Applying the strictly concave central-normal function then gives both bounds and the equality condition. Under the required implication-level standard, this is a routine optimization of a stronger published distributional representation, analogous to extracting an extremal profile from a known pointwise formula.

## value

PASS

The coverage envelope is practically informative for normal-critical prediction-powered intervals: it quantifies the full finite-Gaussian undercoverage range and identifies the best and worst nuisance ratios. The record fails because this useful conclusion is too direct an optimization of known Behrens--Fisher distributional structure, not because the statistic lacks relevance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
