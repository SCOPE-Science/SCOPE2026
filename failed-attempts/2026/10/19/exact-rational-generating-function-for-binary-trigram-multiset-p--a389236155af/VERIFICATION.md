---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

A vector spells a linear word exactly via an Euler trail: each active vertex lies in one weak component, with balanced degrees or the unique +1,−1 pair. In the loopless graph every directed cycle uses both 01 and 10, and every edge touches at least one of these. Any separate balanced active component must have a cycle; a nonzero imbalance pair cannot be split across components because each component's total imbalance is zero. Thus the nonloop support is connected when nonempty. A loop may be added only at an incident vertex, except for the two one-vertex loop-only families. The degree equations, threshold f≥max(0,d−b−u), and loop boundary corrections then count each feasible vector once, with the empty vector included exactly once. In a separate exact algebra replay, grouping b and d by zero versus positive and summing on the signed difference of their excesses reproduces the full rational identity; an appended-bit suffix/profile DP also agrees through n=44. Replay: `python /workspace/independent_checks_1_4.py 3`. The pole at 1 gives (13/12)/4!=13/288, and choosing one word per profile proves the exact codebook bound. The finite DP is corroboration, not extrapolation.

## originality

FAIL

The exact all-length formula and codebook interpretation are demonstrably covered by a distinct indexed finding on the identical observation, with the same word-length offset and fraction; the leading asymptotic is also covered by an earlier dated indexed finding. This is a coverage determination, not an inference of earlier priority for the exact fraction from the later dated catalogue entry. No independent surviving contribution is apparent in the alternative geometric summation for this small graph.

## value

PASS

Varshney–Goyal motivate this precise observable by source coding without read positions. An exact count of the observation alphabet pins down the optimal zero-error codebook for every blocklength and distinguishes support effects lost by mere degree counting. That is a substantive natural enumeration, even though the matching indexed result prevents a new-finding disposition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
