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

For deletion starts i<j, the only potentially differing output coordinates are i through j−1, where one output reads w_s and the other w_(s+2). Equality classes are intervals in the ordered list of starts; the number of distinct outputs minus one thus counts lag-two mismatches. This includes n=2, where all three sources have a single empty output. Checked the 00,01,10 suffix automaton, characteristic recurrence and initial values. Independently, writing a source with r≥1 ones by its leading and trailing zero strings and its positive inter-one zero gaps, the lag-two mismatch score is 2r minus the two endpoint-pair one-counts and minus twice the number of one-zero gaps. For each end use A=1+z+uz²/(1−z); for each inter-one gap use B=z+u²z²/(1−z). Thus the series with z^n is 1/(1−z)+z A²/(1−zB)−1−2z; division by z² simplifies exactly to the displayed rational function. The recurrence gives the three claimed degrees and leading coefficients: only u²F_n contributes at top degree for n≡0,1, and F_(n+2) additionally contributes one for n≡2. Direct output deduplication on all 17,706 source words of lengths 2–18 independently reproduced the entire small spectra and the explicit lists of maximizing words. Differentiation at u=1 gives 2z(1+z)/(1−z−z²)²; comparison of its double pole with the total-count simple pole at ρ=(√5−1)/2 gives slope 2ρ²/√5=3/√5−1. Thus the mathematical claims as stated are correct.

## originality

FAIL

Demonstrable equivalent coverage, not just a similar channel: the distinct indexed tandem-duplication record e78ed24d338c proves that its exact length-two duplication count on precisely the same source words is 1+the same lag-two mismatch statistic, pointwise. The known burst-deletion formula gives the exact same count pointwise. Hence the whole claimed spectrum, the sharp maximum, the extremizing source set and its multiplicities, and the source mean are covered or mechanically transferred. The records have the same indexing date; no priority, authorship, or chronological claim is being made. The direct deletion-specific argument is correct, but distinct mathematical content sufficient for acceptance is not established.

## value

FAIL

The Fibonacci language and its degree distribution are well motivated, and the results are useful as a description of the channel. As a distinct contribution, however, this exact invariant and its optimization are already mechanically determined by the verified tandem count and the existing burst formula. The alternative deletion derivation and the elementary word list give no further structural separation of the channels, no new invariant, and no surviving substantive repair of the original claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
