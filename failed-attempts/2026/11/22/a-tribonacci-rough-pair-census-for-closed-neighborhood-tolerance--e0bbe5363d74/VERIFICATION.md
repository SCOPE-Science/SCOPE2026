---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The three output symbols encode the ordered approximation pair exactly. Duplicate endpoint bits reproduce the shorter closed neighborhoods, and the overlapping pair states impose consistency across the entire input. Only the subsets of pair states meeting {00,11} accept. Directly recomputed all 12 reachable states (8 accepting) and the weighted seven-state complement quotient, with acceptance preserved and distinct letters counted separately. Eliminating the transfer equations gives B=1/(1−t−t²−t³), F=(1+t)²B, and the asserted A. The first five coefficients, including the empty path, follow, and numerator degree four gives the recurrence from n=5. The smallest modulus pole is uniquely positive and simple: equality in |t+t²+t³|≤|t|+|t|²+|t|³ on its circle forces t positive. This yields the stated growth and exponential reduction relative to 2^n. Read VERIFICATION.md and verify.py by inspection. Independent direct bitmask enumeration agrees through n=16, including a_16=19009; the all-length certificate is the transition calculation and formal series, not the finite check.

## originality

FAIL

The distinct same-day forest ambiguity record gives exact feasibility of every observation on the identical closed-neighborhood relation, including paths with n≥2. Its edge-cover/parity condition yields the entire path generating function by a short run decomposition, not just by exponential enumeration of inputs or by numerical coincidence. This is demonstrable mathematical coverage, irrespective of which record appeared first; no priority ordering follows from their shared date.

## value

FAIL

Distinct approximation observations are a natural image-capacity invariant, but the frozen contribution is this single path census and its consequences. Its exact fraction, recurrence, and growth all follow from the existing forest feasibility characterization by elementary path-run parity and ordinary series algebra. The alternate automaton proves the same consequence and the record does not establish an independent extension or a distinct structural invariant beyond it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
