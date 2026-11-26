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

Distinct rotations conflict and a nonprimitive word self-overlaps. At unequal zero gaps the longer-gap orientation is unique, giving floor((n-1)/2)(q-1)^2 primitive orbits. At n=2m+2 the equal-gap distinct-color necklaces are indexed by unordered color pairs. For representatives 0^i a 0^m b 0^(m-i) and 0^j c 0^m d 0^(m-j), a=d makes the prefix and suffix of length m+i-j+1 equal to 0^i a 0^(m-j); the length lies in [1,n-1]. The first- and last-marker color sets are disjoint, with at most one word per ordered pair, giving at most floor((q-1)^2/4). The proposed construction attains both bounds: every word ends at its second marker, hence any matching proper prefix and nonempty suffix would have just one marker at the end, with its leading zero count at least the initial gap of the prefix word and no greater than the final internal gap of the suffix word. In the construction those gap ranges are separated except at equal gaps, where the colors are disjoint. At n=2 the same extremum is directly the product of two disjoint color-set sizes, including zero at q=2. Saturation forces the unequal-gap coverage and the stated equal-gap restriction. The deficit is positive exactly for q≥4.

## originality

FAIL

A separate same-day Resultary record, 121924a58cfc, states the identical optimum for every q≥2 and n≥3 under exactly the same word and overlap constraints, the same necklace deficit and a reversal-equivalent construction. Its proof gives the same equal-gap color separation and forces the same unequal-gap saturation. The date does not establish which record came first; the failure is demonstrable duplicate scientific coverage, not an asserted priority order. The sole domain extension n=2 is the immediate disjoint-endpoint-color product.

## value

FAIL

An exact colored-marker capacity and its gap obstruction have mathematical interest, but no distinct worthwhile increment is established in this frozen record over the substantively identical mirror theorem. Reversing the construction, restating its saturation, and adding the elementary n=2 disjoint-color product do not supply a new motivated boundary result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
