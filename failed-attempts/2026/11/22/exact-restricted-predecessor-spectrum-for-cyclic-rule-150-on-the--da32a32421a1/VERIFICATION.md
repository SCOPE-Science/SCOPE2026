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

The difference recurrence repeats a length-three block; if 3 does not divide n only the zero periodic solution is possible. For n=3k, toggling a nonzero kernel pattern, e.g. (110)^k, is admissible exactly when each block of the source is independently 100 or 010. Thus each of the three nonzero differences yields 2^(k−1) unordered pairs. Two such admissibility classes intersect only at the corresponding constant choice of a one-site phase, so only the three period-three sources have two distinct partners. They all produce 1^n; its fourth full-shift predecessor is 1^n itself, inadmissible. Counting pairs and total sources (the Lucas trace) proves all positive fiber counts and the claimed image size. The unique-recovery fraction and exponential estimate then follow. At n=1 and 2 the literal three-XOR rule is the identity and the source counts are 1 and 3. Independent enumeration through n=18 reproduced the source and fiber counts, including the triple, as finite corroboration.

## originality

FAIL

Two distinct indexed Resultary records explicitly cover the same indexed, cyclic, input-only no-11 Rule 150 spectrum for every n≥3, with the same image count and triple. One also gives the same unique-recovery rate and exponential estimate. This establishes coverage, not priority between same-date records. The only scope extension is two identity maps at n=1,2, a check of the repeated-neighbor convention rather than a distinct surviving result.

## value

FAIL

The all-length ambiguity and capacity phenomenon is mathematically motivated, but the frozen record adds no substantively distinct invariant to the exact indexed classifications. Its only uncovered instances are the immediate one- and two-site cancellation checks, which do not change the phenomenon or resolve a separate worthwhile boundary question. No distinct valuable remainder supports a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
