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

The greedy arch terminals, followed by a symbol absent from the remainder, witness nonuniversality when the arch count is below k. The two factor monitors act differently: before saturation, a run of d zeros in the forward monitor makes every future completion impossible, whereas the reverse monitor allows all initial zeros, represented by one pending state. Away from the end levels the reachable nondead states have two empty remainder versions, one pending-one version, and d−1 pending-zero versions, realized by alternating prefixes and unary appends. The level-zero and saturated level sizes are respectively d+1 and d+1 forward, versus 3 and d reverse. With r arches still needed, shortest legal completions from empty, pending-zero and pending-one are (10)^r, 1(01)^(r−1) and 0(10)^(r−1), of lengths 2r and 2r−1 as applicable, including d=2. This separates levels and empty/pending classes, and the pending-zero witness also excludes pending one. Appending 0^(d−t)1(01)^(r−1) separates same-class nonsaturated monitor counts j<t (including t=1 for empty remainders); after saturation only the monitor witness is needed. Counting the one dead residual gives exactly the stated complete DFA sizes, also for k=1. Reversal preserves the all-length-k subsequence condition, reverses the forbidden factor, and hence preserves word counts despite the exact state gap d−1.

## originality

PASS

The inspectable prior work supplies arch factorization, regular intersection algorithms, and special cases of universality with factor/run restrictions, but not this pair of exact minimal complete DFA classifications. Neither the fixed language reversal nor the resulting additive gap follows from those statements without a specific quotient analysis.

## value

PASS

The object combines two natural recognition problems, each of which has a simple monitor; bare avoidance even has the same d+2 complete states in both directions. The exact d−1 gap for their intersection holds at every universality level and isolates the directional effect of terminal versus initial runs. This provides a reusable exact benchmark for deterministic recognition and shows what reversal-invariant word counts and generic intersection bounds cannot determine.

The dated certificate retains the supplied scientific assessment, sources and limitations.
