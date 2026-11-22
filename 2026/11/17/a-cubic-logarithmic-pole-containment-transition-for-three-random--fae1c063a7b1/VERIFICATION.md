---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For independent uniform-surface points in a cap of radius alpha, heights z_i are i.i.d. uniform in [cos alpha,1] and azimuths i.i.d. uniform; horizontal cone enclosing has probability 1/4. Sorting azimuths yields positive complementary gaps b_i with sum pi, unconditional planar simplex density 1/(2pi^2). On that event pole inclusion is exactly sum sin(b_i) z_i/sqrt(1-z_i^2)>0. For alpha<=pi/2 all z_i>=0 so plateau 1/4 holds. When h=-cos alpha>0, the excluded volume integral over [-h,1]^3 is exact. In any region m=min sin b_i>=h^gamma, q(z)=z/sqrt(1-z^2) linearizes uniformly on the contributing O(h^(1-gamma)) positive heights; translating by +h gives simplex volume h^3(sum a_i)^3/(6 product a_i). For one b_i=t to zero, integrand ~4sin(beta)/(3t); sum of three edge integrals gives 8gamma log(1/h), hence loss (4/pi^2)h^3log(1/h) after bounding t<h^gamma and gamma to 1. At one degenerate gap the logarithmic coefficient partitions two negative heights versus one as 1 versus 1/3 (3:1); the three edges have equal symmetry weights; restrictions h^v<=t<=h^u give logarithmic-scale uniformity and factorized weak marked law. The discarded all-three-negative mass is O(h^3). The bundle contains an independent Cartesian determinant test and Sobol integral but these finite checks do not prove logarithmic asymptotics.

## originality

PASS

Four statement-level comparisons distinguish the specified result from the inspected primary-source coverage; best-of-knowledge priority, not an absence-of-search novelty guarantee. 

## value

PASS

A fixed-pole hull crossing the hemispherical convexity boundary is a natural geometric probability transition. The cubic-log rather than analytic Taylor law is caused by angular-gap degeneracy; its exact coefficient, signs 3:1 and uniform logarithmic gap mark resolve a nontrivial geometric rare-event mechanism distinct from the classical 1/4 plateau.

The dated certificate retains the supplied scientific assessment, sources and limitations.
