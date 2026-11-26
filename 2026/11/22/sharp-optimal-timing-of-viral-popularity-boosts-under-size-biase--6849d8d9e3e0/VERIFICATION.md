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

For one size-biased draw (all users eligible), the conditional diversity multiplier is f(S,r)=1-[r/(S+r)]². The total is deterministic and the tower rule gives a positive product times D₀>0. At fixed pre-swap total S, the diversity-factor difference for b,a versus a,b is 2Sab(a−b)/[(S+a)(S+b)(S+a+b)²]; e.g. after extracting S/(S+a+b)² the difference reduces to 2ab/(S+b)−2ab/(S+a). The next total and all other factors agree. Adjacent inversion removal proves the unique minimizing boost sequence for expected H; reversing the argument proves the maximum, with ties at the extrema only for identical boost sequences. T=1 or all equal boosts have just one sequence class. This does not assert injectivity among nonextremal orders. The periodic auxiliary product has equal sums of the Gamma shifts in numerator and denominator, so the powers cancel; bounded martingale convergence justifies the expected limit. The stated M=1 value and large-M equivalent follow by telescoping and Γ(x)∼1/x. Independent exact state enumeration verifies the 2/3 and 31/45 witnesses and small nonuniform cases; it is not an all-permutations proof.

## originality

PASS

Credit time-dependent-urn second-moment recurrences and the motivating publicity model as antecedents. The supported distinction is strict chronological ordering of an arbitrary prescribed multiset of positive single-recipient additive boosts, not the recurrence or the model itself. The strongest indexed timing result concerns a different Friedman–Pólya control and does not establish arbitrary sized-boost sorting. Primary access limits leave the priority assessment provisional.

## value

PASS

The comparison solves a natural exact fixed-budget scheduling problem for arbitrary positive sizes, distinguishes equal-budget schedules and identifies both unique extremizers independent of initial scores. The strict exchange sign and invariance of the future product make this more than computing the known second moment of one schedule.

The dated certificate retains the supplied scientific assessment, sources and limitations.
