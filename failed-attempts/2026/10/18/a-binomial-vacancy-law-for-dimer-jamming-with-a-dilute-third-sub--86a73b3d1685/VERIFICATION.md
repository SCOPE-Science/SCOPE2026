---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The next accepted edge is uniform among edges of the current free-vertex graph: all those edges have survived in the unexplored order and eligibility can only be lost. The three transition weights are ab, ac, bc. For a fixed free C vertex, the chance of matching on the next acceptance is 1/(ab/(a+b)+c) >= 1/(s+r), s=min(a,b). Before s first drops below h the chain must traverse every level from n to h, so conditioning at the first departure attempt at each level gives the telescoping survival bound (h+r-1)/(n+r). Union over r vertices. Pre-sample independent uniforms for the successive C matches and use the same uniforms for fair coins, whether or not each uniform ends up being used. The endpoint probability differs from 1/2 by at most r/(4h) whenever s>=h because |a-b|<=r. The probability of any early mismatch is at most r^2/(4h). On the good event, c=0 and A-B matches exhaust the smaller part, leaving the absolute coin imbalance. This proves the stated TV bound for every admissible integer h including h=n and covers small n by the same inequality, even when vacuous. h near sqrt(nr) gives the growing-r estimate; the binomial CLT and TV contraction under scaling transfer the half-normal limit. The r=2 graph admits a perfect matching by using one third-part vertex with each principal part and matching the remaining principal vertices. Read the frozen verification note and script: exact count-state and labeled-state recurrences, three exhaustive order tests, and finite rational inequalities; reported counts were not independently replayed and are not required for the analytic argument.

## originality

FAIL

A distinct published index entry covers the same central theorem: same uniform random-edge greedy process on K_{n,n,r}, same folded-binomial TV target and fixed-r limit, and same r=o(n^{1/3}) half-normal regime. Both give finite-size coupling estimates of the same effective scale by early depletion and endpoint coupling. The frozen h-dependent inequality has different constants and formal range; the comparator does not state that literal inequality, but this difference does not supply a distinct substantive vacancy law or convergence regime. This is a judgment of strong material catalogue overlap, not of chronological priority, copying, or identity of the records.

## value

PASS

The law isolates a nonvanishing jamming defect in a natural dense, perfectly matchable (for r=2) perturbation of a balanced graph. It predicts finite-size fluctuations and quantifies convergence that vacancy fractions and parity alone cannot see. This is substantive mathematical value of the theorem as a result, not originality credit for a second formulation or for changes in constants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
