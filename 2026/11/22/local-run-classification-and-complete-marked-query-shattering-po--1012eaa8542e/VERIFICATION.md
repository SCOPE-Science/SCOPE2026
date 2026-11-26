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

For a fixed marked equality-query support, two positive answers at one vertex are incompatible; an all-positive trace forces different targets across selected edges. A 101 trace forces equal outer targets on a selected triple: if all three targets are distinct, the middle must be the very colour it is forbidden to use. Overlap makes four consecutive targets alternate, and 1001 forces equal adjacent middle colours. The fully selected triangle has only six colourings and cannot realize eight traces. Conversely, the displayed path traces for the allowed runs all work, and each nonempty gap can be filled greedily until its final interior vertex, which has at most two forbidden colours, even when the two boundary positions refer to the same selected vertex. The empty support extends by any proper colouring. Counting ordered marked-run/positive-gap lists with a distinguished run start gives exactly n/r, also for periodic patterns; expanding yields both coefficient formulas. For n at least 4 a selected triple induces two edges in n cases and exactly one edge in n(n-4) cases, giving the stated cubic coefficient. Blocks of three selected plus one gap, with at most one shorter block in the remainder, attain the rank bound. For even cycles of order at least six, a one-query extension in an alternating gap exists precisely when its two selected endpoint targets agree, giving twice the number of proper ternary colourings of the auxiliary cycle. An independent trace-bitset implementation agrees for all one-query-per-vertex supports through n=9 and directly verifies alternating facets at n=6,8,10,12 (12,36,60,132). The multi-query obstruction and all-n classification rest on the proof, not finite tests.

## originality

PASS

The prior same-family scalar VC rank and four-consecutive-query obstruction are credited and excluded from the originality decision. The full iff criterion for marked supports, its coefficientwise enumerator, and the alternating nonpurity count are distinct on the inspected evidence.

## value

PASS

The known rank answers only how large a shattered support can be. The iff characterization decides every concrete marked support, the polynomial records exact frequencies by size, and nonpurity exhibits systematically smaller inclusion-maximal supports. These are natural structural questions for the same learning concept, not arbitrary finite examples or a recomputation of the rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
