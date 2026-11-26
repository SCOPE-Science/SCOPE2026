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

For a queried adjacent pair followed by a queried position, assigning 00 to the pair and 1 later cannot extend: avoiding 001 forces the suffix after 00 to be all zero. Conversely, with no adjacent queried positions fill holes with ones. If there is a terminal adjacent pair, fill holes before it with ones and fill the suffix with zeros if the pair is 00 (otherwise ones). This handles all short lengths too. Splitting supports into independent sets and those with pair ending at t gives the stated I_n+z^2 sum I_{t-3}, including the empty prefix at t=2. Summing gives the rational series. Equivalently for k>=2 the sorted positions have gaps at least two except the last gap, which may equal one. Subtracting 0,1,...,k-2,k-2 from the positions bijects to k-subsets of [n-k+2], giving binom(n-k+2,k); size zero and one give 1 and n. Thus the largest k is floor(n/2)+1 for n>=1. Independent replay: python3 /workspace/branches/shattering_reproduction.py. The projected DFA oracle confirmed all 8190 labeled support decisions for n=1..12 and the claimed polynomials at n=8 and n=12.

## originality

FAIL

A distinct indexed all-single-trigram classification already covers the substantive exact support criterion, up to coordinate reversal. Its same-day date does not establish temporal priority, but neither is it the identical record. The polynomial, series and rank are direct enumeration of that very support family and do not restore a distinct finding. Failure is for demonstrable equivalent coverage of the claimed mathematics, not a failed download.

## value

FAIL

A complete support theorem for the canonical avoidance language would be useful as a distinct result. Once its exact support classification is credited to the all-trigram coverage, the remainder is a direct independent-set summation or gap compression, and the scalar dimension is just its degree. There is no independently valuable distinct exact claim to repair this record into as submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
