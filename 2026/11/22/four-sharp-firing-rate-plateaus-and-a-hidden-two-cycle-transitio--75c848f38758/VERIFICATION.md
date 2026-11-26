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

Starting from the stated forward projection, the lifted map is order preserving and commutes with unit translations, bounding the displacement between any two phase orbits by one period after alignment. Each orbit eventually cycles on the three residues; fixed phases, pairs, and cyclically or anticyclically ordered triples give respectively 1, 2, 3, and 3/2 firings per period. Greedy times are no later than those of any feasible periodic schedule from the same initial event, so it suffices to test feasible representatives of these candidate greedy cycles. A forward triple requires s ≤ a; a pair requires s ≤ max_g min(g,1−g) = min(c,1−c) (when c ≥ 1/2, b ≤ 1−c); a reverse triple requires s ≤ 1−c. A fixed phase is always feasible. This proves both staircases including c = 1/2, tied gaps, and inclusivity. The reverse-triple argument classifies candidate greedy 3/2 cycles; arbitrary nongreedy schedules of the same rate need not take only that form. Independently rebuilt the concrete map in integer twelfths at every gap boundary inside (0,1) and in every intervening cell. Up to cyclic rotation, the interval lists in twelfths were (3,5,4), (4,8), (5,7), (7,9,8), and (12), giving the five displayed variances and confirming the factor-four drop just above s = 1/3. The bounded reproduction corroborates the example, not the universal proof.

## originality

PASS

The supported distinct contribution is the explicit all-parameter three-phase staircase and the rate-invisible interval-law switch in the example, not the projection recurrence, phase rotation method or firing-rate quantization alone. None of the inspected comparators states or supplies the combined classification. This is a best-of-knowledge comparison, not a priority determination.

## value

PASS

This is a complete sharp classification for the smallest clock supporting a reverse three-cycle. It also demonstrates a genuine observable distinction beyond the rate: the two adjacent rate-two regimes have different repeating intervals and variances. The result can be used directly to choose a clock or travel time in the stated model, without an empirical neuron-performance claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
