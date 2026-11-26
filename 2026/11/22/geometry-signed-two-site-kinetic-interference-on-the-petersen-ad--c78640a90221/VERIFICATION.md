---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

A maximal intersecting family of two-subsets is a full star or a triangle: after an intersecting pair, an edge omitting their common point must be the triangle-closing edge and excludes every other addition. Thus K can only be 3 or 4. The next eligible arrival is an exponential race of the still-eligible unheard clocks; memorylessness keeps their original rates after the previous eligible arrival, and future attempts at ineligible sites can be discarded. Conditioning on the race winner gives the deletion recurrence for the full distribution q_S(k), with q_empty(0)=1. A separately written exact symbolic check visited 52 reachable eligible sets per marking geometry and canceled the numerator of the difference from each claimed probability. An independent enumeration of all 2^10 subsets found five maximal stars and ten maximal triangles. Private replay: python3 /workspace/branches/86e90c5d-2cf0-4f3a-992b-8c6df57f0b03/independent_distribution.py (SymPy); check.log in the same directory records the small path check and the exact identities. The supplied scripts were inspected, not executed. All denominator factors are positive for positive rates; the exact relation is delta_adj=-2 delta_nonadj, with the quotient defined only when the common interaction term is nonzero.

## originality

PASS

The strongest distinct corpus match uses precisely the same Kneser model and star-versus-triangle observable, but changes the rates of a full distinguished-point star at once, not of two independently tunable sites. The established random-greedy recurrence is a general method and is credited; the checked literature does not yield the simplified two-rate geometry interaction.

## value

PASS

The Petersen graph is a natural small test with two inequivalent pair geometries and nontrivial terminal sizes. The exact law quantifies the first rate interaction not suppressed by vertex transitivity: opposing signs for the two geometries, with a constant magnitude ratio throughout the two-dimensional rate domain. This gives an exact heterogeneous-rate benchmark, not just an enumeration of uniform orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
