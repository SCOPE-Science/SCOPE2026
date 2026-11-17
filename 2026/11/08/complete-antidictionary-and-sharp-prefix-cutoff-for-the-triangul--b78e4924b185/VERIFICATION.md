---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The gap 1 0^a 1 occurs once; a two-one factor 0^l 1 0^a 1 0^r is present iff 0<=l<=a-1 and 0<=r<=a+1. These inequalities yield exactly 0^a1 0^a1 and 1 0^a1 0^(a+2), plus 11; an overlap argument rules out minimum absences with >=3 ones. Length counts produce (z^2+z^6)/(1-z^2), deterministic one-counter recognition and nonregularity. Earliest 0^N forces N(N+3)/2 prefix, and the unique early occurrences of every remaining length-N factor give sufficiency. Independently compared all factor sets/MAWs and one-character cutoff sharpness for 1<=N<=15.

## originality

PASS

Best-of-knowledge original complete infinite triangular-marker antidictionary and sharp finite-prefix cutoff. General increasing-gap factor-complexity calculations and finite run-length encoded MAW data structures do not directly identify the proposed infinite forbidden language or optimal stabilization threshold. No equivalent theorem found in the actual Resultary searches.

## value

PASS

Minimal absent factors are natural compact generators of a factorial language. An explicit infinite two-run-gap obstruction basis and the least prefix that captures every bounded factor give precise reusable word-combinatorics and pattern-avoidance data, not a routine recomputation of subword complexity. Both the all-N cutoff and deterministic-context-free/nonregular distinction are independent natural invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
