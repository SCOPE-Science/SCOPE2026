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

Reflection and independent killing give the defective Brownian hitting density and Laplace transform. The standardized conditional density is φ(v) times (1+v/√q)^(−3/2) exp(v³/[2√q(1+v/√q)]) on v>−√q. On |v|≤q^(1/12) its linear correction is (v³−3v)/(2√q) with the stated integrable Gaussian-weighted remainder. The exact conditional MGF satisfies log M_q(t)≤t² for |t|≤√q/4, so ±q^(1/12)/2 as Chernoff parameters control the complement. Thus the first-order absolute integral is E|Z³−3Z|/(4√q), yielding the positive stated C_*. The binomial success count with p=m/N and iid conditional marks may be coupled first in its count and then in its marks, giving the bound mδ_q+m²/N. The one-point sector over the sign-positive density set gives the lower bound, because its binomial/Poisson mass difference is O_m(N^−1). The min distribution follows from the exact absence-of-points formula and subtraction of the no-success atom. Given the first successful particle and time, the other particles are independently conditioned on no success by that time; being alive and unabsorbed is a subset of that event, giving the ratio in Eq. (5). Compact success-conditioned mark windows force the conditional binomial mean to infinity uniformly and give log mean log N−q/2−v√q/2+o(1), with vanishing relative count error. Tightness then yields the joint limit including vanishing probability of no other live searcher. This gives a process-level order, not a process-level leading constant. The live population is √N times a random subpower factor, not Θ(√N) in the sense of a multiplicatively tight ratio.

## originality

PASS

The success threshold, scalar Poisson count/empty atom at fixed m, conditional inverse-Gaussian law, single-mark TV order, and finite-N first-arrival survivor-count formulas are known or direct implications of known results. The supported distinct claims are the explicit first-order single-mark TV coefficient, the two-sided sharp whole-cloud comparison at synchronized critical scaling, and the tied first-arrival/logarithmic live-count law. No inspected result establishes those new conclusions under the same assumptions. This is a bounded assessment, not a priority claim for standard marking or normal approximation machinery.

## value

PASS

The natural window keeps the eventual number of successes nondegenerate. A sharp whole-cloud approximation quantifies errors for all successful-arrival statistics, while the joint live-count limit gives an informative population response that a first-hitting-time law alone misses. At a given first-arrival mark, the log count resolves a diverging fluctuation scale despite vanishing relative binomial noise. The value is in this quantitative joint description, not in the known threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
