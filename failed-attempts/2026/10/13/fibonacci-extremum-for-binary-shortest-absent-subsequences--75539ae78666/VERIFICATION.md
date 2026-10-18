---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Kosche et al. global alternating-arch extremal reduces the fixed-universality maximum to binary transfer counts (p,q)->(p+q,q) for 01, (p,q)->(p,p+q) for 10, starting (1,1). Alternating increases the smaller coordinate, yielding consecutive Fibonacci counts and total F_{k+3}. A word of minimum length 2k has precisely k arches 01/10 and the coordinatewise Fibonacci envelope gives equality only at alternating orientations, the two bit-complement words. Directly compared with complete independent October 4 earlier proof, which derives exactly the same recurrence and equality mechanism. C PASS, even though O fails.

## originality

FAIL

DECISIVE PRIOR COVERAGE. An earlier published Resultary record dated 2026-10-04, Fibonacci extremals for shortest absent subsequences of binary words, states and proves globally that for any binary word of universality index k, |SAS(w)|<=F_{k+3}, attained by alternating 01,10 arches. Its transfer-matrix argument also states equality for min-length 2k must follow alternating choices; it further proves the stronger fixed-length profile M_{2m}=F_{m+3}, M_{2m+1}=2F_{m+1}. Full prior RESULT.md was read at Git blob 3058952ccaacd03efd47ecdd80dfbee1d6e3b158. The October 13 submission is therefore covered exactly by prior theorem, not merely close parameter coincidence. Reject O; no repair attempted.

## value

PASS

The exact Fibonacci maximum count and extremizing word classification are mathematically motivated natural invariants of shortest absent subsequences; their correctness and potential utility do not overcome proven earlier coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
