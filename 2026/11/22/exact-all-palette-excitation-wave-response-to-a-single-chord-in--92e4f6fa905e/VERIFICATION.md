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

A vertex that fires in an F^k-fixed configuration cannot wait at zero: firing again after exactly k steps leaves just enough time for the forced refractory sequence and the next immediate excitation. A vertex that never fires is zero throughout the period; connectedness excludes this beside a rotating vertex. Thus all nonzero F^k-fixed states rotate, have least period k, and are exactly the colorings where each vertex has a successor-colored neighbor. For k>=3 a successor edge has at most one direction, so a directed cycle is one of the three stated simple cycles. With the selected cycle fixed, path increments have an initial run of -1, then the first increment c not -1 if present, then only +1. The increment sum gives exactly one c at each first-exception index, excluded by the stated congruence; the all-minus case gives the indicator. Reversal identifies the two endpoint signs, and coloring each internal site one less than its left neighbor proves positive path multiplicity. The long-cycle waves satisfy a resonant chord cycle in either phase direction; the two chord cycles in their intersection must agree on the chord direction and then both long arcs are forced. Thus every resonant pair intersects in exactly 2k states. Triple resonance would require k to divide 2, excluded. Inclusion-exclusion and division by k establish the orbit count. For k=4 the number excluded is zero for even L, and for L=4t+1 or 4t+3 it is 2t or 2t+2 respectively; the correction is +1 only in the latter odd case. This gives the stated distance-three law, including n=5 and the two-resonance cases. Independent direct checks of proper divisors, path words and the four-color substitution all passed.

## originality

PASS

Pass is for the exact all-palette single-chord orbit census and its explicit defect/amplification law. The rotating criterion and directed resonance mechanism are elementary precursors, and the prior three-color theta method is substantial overlap; novelty is not assigned to these ingredients. No inspected stronger statement gives the census including both arbitrary palettes and the length-one arm.

## value

PASS

The effect of a single added edge on existence and abundance of coherent periodic waves is a natural finite-network perturbation question. The result evaluates that exact response across each palette and both arc lengths, rather than supplying only existence or an instance-by-instance transfer calculation. The distance-three chord separates the effect from the divisibility condition of a bare ring: all n>=5 support four-waves, with an exact size-growing count rather than zero or two.

The dated certificate retains the supplied scientific assessment, sources and limitations.
