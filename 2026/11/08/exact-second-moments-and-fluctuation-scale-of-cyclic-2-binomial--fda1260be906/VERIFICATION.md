---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

At fixed weight the scattered-01 count determines the whole signature; moving a zero to the end subtracts 2h and moving a one adds 2m−2h. Thus a collision modulo 2m can only be between opposite cuts by coprimality, and it occurs exactly when the corresponding half-window has h ones. There are no larger classes, and C is the sum of the m collision indicators. At lag d, splitting into alternating arcs d,m−d,d,m−d, imposing both balance equations and the total count gives counts a,h−a,a,h−a. This yields the exact joint count and hence both exact moment formulas, including empty summands. For the asymptotics, Stirling gives P(I_0=1)∼1/sqrt(πm q), q=p(1−p). Conditional on I_0=1 the two halves are independent fixed-weight samples; the lag-d return probability is the squared mass sum of Hypergeom(m,h,d). Its mode is within O(1) of d h/m; Stirling at the mode bounds the maximum mass by K/sqrt(1+d(m−d)/m) uniformly (entropy concavity bounds the exponential factor by one, and d or m−d bounded is immediate). For interior lag fractions, uniform Stirling expansion on any fixed standard-deviation window gives the normal mass; outside L standard deviations, the squared-mass tail is bounded by the maximum mass times L^−2 by Chebyshev. This yields the exact interior limit 1/(2 sqrt(πm q x(1−x))). The maximum bound controls endpoint strips with integrable x^−1/2 and (1−x)^−1/2 envelopes. Expanding E C²/m gives the integral π/2 with prefactor 1/(πq); subtracting the squared scaled mean gives (π−2)/(2πq). No weak limit is needed. Even the interpretation as nonconcentration at the sqrt(m) scale is justified: conditioning on the first of three balanced cuts forces equal block counts in two independent halves across three block lengths l_i partitioning m. The maximum joint block-count mass is at most K sqrt(m)/sqrt(l_1 l_2 l_3), by representing the counts by independent binomials conditioned on their sum h. With the first balance factor this gives the joint probability bound K/sqrt(l_1 l_2 l_3); summing over the two gaps and a starting cut gives E C³=O(m^{3/2}). Thus the squared rescaled deficits are uniformly integrable, and the positive limiting variance excludes convergence in probability to a constant.

## originality

PASS

The deterministic signature identity and sharp cyclic diversity bounds are overlapping results, explicitly outside the finding's novelty claim. The finding is the random finite moment pair and the asymptotic constants in the gcd-two stratum. Neither the closely matching deterministic catalogue result nor the inspected class-size and ordinary bridge-local-time results supply these. Same-day catalogue chronology is not inferred.

## value

PASS

Gcd two is the first arithmetic stratum where signatures collide, not an arbitrary choice of parameters. Sharp deterministic bounds do not say whether the typical deficit is order one or order m. The exact moment pair and strictly positive order-m variance determine its typical mean and fluctuation scales with explicit density dependence, a useful quantitative benchmark for any fuller law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
