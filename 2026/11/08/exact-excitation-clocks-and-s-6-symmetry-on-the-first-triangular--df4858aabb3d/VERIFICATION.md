---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Exact space has 3^15=14,348,907 ternary states indexed by the 15 two-subsets of six points, with neighbors precisely disjoint pairs (degree six). The single-valued synchronous update gives a finite functional digraph. Removing all indegree-zero states leaves only directed cycles; following every remaining cycle and unwinding deletions labels all starting states by least period and entry distance. Independently wrote and compiled a C++17 exhaustive successor/peeling/cycle/S6 quotient implementation: it visited all 14,348,907 states and obtained 1 fixed cycle, 1,258,232 period-three cycles, 90 period-four, 180 period-seven, max transient 10 with 1,440 states, and all 26 (t,p) counts; exhaustive S6 action on 270 long-cycle representatives gives orbit sizes 45,45 and 180. Graph automorphism S6 follows from six maximum intersecting families of size five (stars). No infinite-family extrapolation.

## originality

PASS

Independent exhaustive 14,348,907-state and S6 quotient confirms meaningful full classification beyond general rate formulas.

## value

PASS

KG(6,2) is the first triangle-containing KG(n,2); for a natural deterministic excitable rule the exact state-space census and sharp entrance-time distribution are complete finite invariants, while symmetry resolves two distinct period-four wave shapes and one period-seven wave shape. The group-orbit classification is motivated structurally and may be used as a benchmark for other Kneser excitation dynamics, not an arbitrary slice of unrelated numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
