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

Expanding the residual covariance gives Var(M)-2 Cov(N1,M). The Poisson shift identity gives Cov(N1,M)=lambda times the probability of a strict unique minimum of species 1; a tie does not change the minimum when one count is increased. The tail sums count E M and E M^2 with weights 1 and 2k-1. At small lambda the M=1 term is lambda^m+O(lambda^(m+1)); the second moment contribution from M>=2 is bounded by E[N1^2; N1>=2] times Pr(N1>=2)^(m-1), hence O(lambda^(2m)). The N1=0 contribution to the strict-minimum probability is lambda^(m-1)+O(lambda^m); the remainder is bounded by Pr(N1>=1)Pr(N1>=2)^(m-1). This gives C_m=-lambda^m+O(lambda^(m+1)). The iid Poisson CLT gives a joint Gaussian limit; bounded fourth moments of the centered/scaled minimum imply convergence of its first two moments. The strict-minimum event has a Gaussian-null boundary and limiting probability 1/m. Integrating the Gaussian minimum density m phi Q^(m-1) by parts gives the stated first and second moments. Normalizing phi^2 and phi^3 makes the residual Q powers equicorrelated orthant probabilities with correlations 1/3 and 1/4. The two-dimensional arcsine formula follows by the angular measure of two intersecting half-planes; in dimension three expansion in signs and central symmetry eliminate all odd terms, leaving the sum of the three pair terms. My separately written rational check /workspace/branches/check1.py confirms all the displayed open enclosures, using the squared mean formula and bounding pi, sqrt(3) and the two arcsines. Finally the Poisson sums are continuous by compact-uniform tail domination, so the five-species sign transition implies at least one zero at positive loading.

## originality

PASS

The capacity model, two-input extrema, and normal order-statistic methodology are prior. The verified two-count minimum results already imply the two-species covariance by a direct reduction. The supported distinct contribution is the multicomponent residual pair covariance and the negative-to-positive high-loading change from four to five required species, together with the low-loading sign. The inspected strongest assembly and extrema results do not imply that multicomponent finding.

## value

PASS

The prior capacity model gives a natural, well-defined residual pair rather than an arbitrarily chosen finite statistic. Its covariance measures fluctuations not addressed by a mean product deficit. The opposite asymptotic signs at four and five and the five-component loading crossover distinguish a common-minimum effect from the negative low-loading regime, supplying a useful exact benchmark without requiring kinetic applicability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
