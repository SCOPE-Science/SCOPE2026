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

The zero-based pair formula and both asymptotic extrema are correct. For n≥4 each factor has a 1 at an odd global position: its at least two odd positions complement consecutive preimage letters, which cannot both be 1. This rules out opposite-parity collisions. Decimation gives preimage length floor(n/2) at even starts and ceil(n/2) at odd starts. Since R is nondecreasing, the first repeat is strictly earlier in the even-start class, where both indices double. The base pairs (2,0), (3,2), (4,0) follow by literal comparison. Iterating to base 2 or 3 gives the stated dyadic partition and subsequential ratios; the ratio is never below 1 or above 3/2.

## originality

FAIL

A distinct indexed Resultary entry states the entire R formula, recurrence, and both limiting extrema under the same convention. This establishes substantive overlap, not relative priority. The indexed entry does not state the general Q formula; the same parity proof, however, preserves the index of the earlier partner under decimation, so Q is obtained by carrying the known collision witnesses through the recurrence. No distinct substantive remainder is established.

## value

FAIL

The prefix invariant and its nondyadic law are worthwhile mathematics in themselves, but the full law and oscillation are already covered in the indexed comparison. The added mate is the earlier witness propagated by the same decimation with the same two nontrivial small lengths. No nonroutine independent result about first occurrences remains to justify a repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
