---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For all k,r>=0, every complement of a selected (01)^k in (01)^(k+r) is a concatenation of r pairs 01 or 10 (prefix-balance parity); any maximal 10-block run consumes a distinct deleted 01 pair. Conversely inserting a 0 before and 1 after each 10-run produces a valid aligned alternating host, and extra deleted pairs may be appended. Counting j runs via 2j chosen block-boundaries gives binom(r+1,2j); saturation exactly r<=2k. Independently enumerated all deletion subsets in a bounded (k,r) grid and checked both binomial forms exactly. Unbounded claim is established by the constructive argument, not finite counts.

## originality

FAIL

The earlier complete published theorem contains the same residual language, binomial counting, minimal run budget and all-words cutoff. The submitted claim is an exact alphabet/parameter substitution, not merely a related algorithm.

## value

FAIL

The exact iff run criterion, per-run counts, sharp saturation, and unique first missing word are already supplied together in a November 2 publication in precisely this fixed-host/fixed-pattern complement setting. Relabeling a,b as 0,1 and m as r is not a substantive new mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
