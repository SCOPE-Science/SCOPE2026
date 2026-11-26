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

For 0<α<1, q(1)=1 and 1≤q(n)≤n, so all nested arguments are defined and strictly earlier. The forcing gives the recursion by construction. With s_j=q(j)−q(j−1)∈{0,1} and t_n=n−q(n−1), t_(n+1)−t_n=1−s_n, giving Δf(n)=s_(n+1)−(1−s_n)s_(t_n+1) for n≥2; the n=1 step is floor(2α). For α<1/2 the first two increments being zero means u={α(n−1)}<1−2α, with this upper boundary excluded. Because t_n=(1−α)(n−1)+u, a decrement then occurs exactly when {v+αu}≥1−α, with v={α(1−α)(n−1)}. Rational independence of 1,α,α² is equivalent to that of 1,α,α(1−α); the two-dimensional Weyl criterion applies since every nonzero integer-frequency dot product is nonintegral. The polygonal/modular test region has null boundary and v-section length α at every eligible u, so its density is α(1−2α); the index shift does not affect the limit. At α=√2−1, α²=1−2α and v≡3u modulo one. In the only possible decrement strip, (3+α)u<(3+α)α²=1−α<1, so the fractional-part test fails strictly, even at boundary-sensitive indices. All successive differences are consequently 0 or 1 at that parameter.

## originality

PASS

Prior work establishes the same nested recursion, Beatty-derived forcing, and upper-range slowness. The audited addition is the exact lower-range decrement density under rational independence together with a strictly below-half quadratic resonance. Neither the inspected results for this model nor analogous floor-iteration results cover that pair of assertions.

## value

PASS

The established upper half supports slow forcing throughout. Below it, the exact decrement rate shows a positive-density obstruction for almost every parameter, while the silver-ratio parameter shows that the cutoff is not a necessary condition for slowness. Together these settle a natural question about the threshold and locate an explicit arithmetic exception rather than reporting isolated counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
