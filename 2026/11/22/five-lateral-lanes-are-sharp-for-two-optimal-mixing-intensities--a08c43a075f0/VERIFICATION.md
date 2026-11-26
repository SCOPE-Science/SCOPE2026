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

For the dimensionless time x=mT, the derivative of the fixed score is a sum of at most n−1 distinct real exponentials. The multiplicity-counting Rolle argument bounds its zeros by n−2 unless it vanishes identically; two strict interior maxima require an intervening derivative zero. For five lanes, independently computed exact rational bounds from the direct signed Taylor series of xQ (not the supplied uniformization checker) establish +,−,+,− at x=0,1/2,1,4 for both q endpoints, hence for all intermediate q. The three forced roots are simple and exhaust the zero budget. Bisecting in exact arithmetic and using contraction of the stochastic semigroup to bound the derivative gives late-minus-early peak gaps in (−0.102309,−0.102273) at 95 and (0.089833,0.089870) at 97, on the 100C scale. The lane-four probability derivative has a double zero at zero by shortest-path counting and is eventually positive by the first cosine mode (probability coefficient −√5/10). It is initially positive; a negative excursion would require two crossings and an isolated tangency would also use at least two multiplicities. Neither fits the one remaining zero, so p'(x)>0 for x>0. Smooth simple stationary branches therefore have a strictly increasing late-minus-early gap, by differentiation at stationarity. At the unique tie both heights exceed the initial value 42 and the limiting value (109+q)/5, and there are no other extrema that could compete.

## originality

PASS

The supported distinction is sharp attainability for one fixed terminal suitability on an equal-rate path, and a uniquely tuned pair of equal global optima. The generic exponential zero bound and the analogous five-state first-passage threshold are not the contribution. None of the strongest inspected statements gives this path/reward/tie conjunction.

## value

PASS

The minimum number of lanes makes this a structural counterexample to unimodality rather than an arbitrarily tuned time trace. The equal-height construction goes further: a single smooth mixing control has two separated true global optima, not just competing local optima. This is useful as a benchmark for idealized transport optimization even without a field-calibrated interpretation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
