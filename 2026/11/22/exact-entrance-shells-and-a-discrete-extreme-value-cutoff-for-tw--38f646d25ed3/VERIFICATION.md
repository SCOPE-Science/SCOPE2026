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

Commuting shifts and OR idempotence give offsets t+j(s−1), j=0,...,t, in the t-step dependence. Within the rotated source class the order has period m because (s−1)/g is coprime to m. Every class saturates to its OR at time m−1; thereafter the class-constant states rotate bijectively, so this set is exactly the recurrent locus. For 0<=t<m, a zero class qualifies separately; a nonzero class qualifies precisely when its largest cyclic run of zeros is <=t. Every qualifying nonzero word gives a unique marked closed path in the run-length automaton because ones reset the state; an all-zero word has no closed path. This proves the trace census, and at t=m−2 exactly the m singleton words per class fail, including the m=2 boundary. The saturated map tests one bit of information per source class, so one phase with w active classes has (2^m−1)^w inputs and the orbit basin sums d disjoint phases. At t=h+c−1, any bad nonzero class is exactly an occurrence of 1 followed by h+c zeros. Overlaps are incompatible and disjoint blocks independent; for each fixed factorial moment j only O_j(m^(j−1)(h+c)) ordered start tuples are lost. The moments converge to those of Poisson(2^(−c−1)); applying the zero-count probability and independence across g classes gives the stated limit. The fixed g,c and sufficiently large h ensure admissible offsets and block lengths. Independent functional-graph peeling plus cyclic inclusion-exclusion and direct phase-fiber enumeration agreed across 45 systems and 32776 starts (3<=n<=11, all allowed s). Replay: python3 /workspace/branches/independent_reproduction.py 2.

## originality

PASS

The distinct contribution is the simultaneous network-specific transient and basin description, based on the exact moving-window reduction for arbitrary offsets. Periodic necklaces, exact Bernoulli circular-run counts considered in isolation, and dependent rare-block Poisson approximation are established and not new. No inspected result covers this full OR-network census by specialization.

## value

PASS

For the natural synchronous disjunctive system the result measures more than a known periodic skeleton: one gcd controls the full labelled entry distribution, phase weights, and the separation between sharp worst-case and stochastic clocks. Changing the second jump while keeping n fixed can change the entire distribution. The network-specific link to an exact run statistic makes the basin and transient law useful as benchmarks for disjunctive systems, even though the run formulas themselves are classical.

The dated certificate retains the supplied scientific assessment, sources and limitations.
