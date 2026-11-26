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

For i≠j the entry is h(a_ij−hΔ_ij/2); missing edges and edges with Δ_ij≤0 cannot constrain h≥0. The diagonal is at least [1+(1−hλ_i)^2]/2, and row sums are one. In a row of maximal exit rate M>0 the diagonal exceeds one for h>2/M, so some constraining edge exists. Every constraining entry stays negative after its first positive zero, which proves the entire interval, not just a first crossing. Dividing Δ_ij by a_ij gives a denominator at most 2M, with equality exactly when both exits are maximal and the two-step alternative has zero weight. The star has threshold 2/(m+1); even exact equality in the upper universal bound is possible for a single one-way edge to an absorbing vertex. Q=0 is handled separately; the regular common-neighbor formula is for d>0.

## originality

PASS

The supported distinction is the exact all-step horizon and necessary-and-sufficient SSP-equality motif for an arbitrary fixed finite directed weighted generator. The unweighted regular graph restriction and the star limiting witness have concrete catalogue overlap and are not credited as original. The available older threshold literature did not establish the full directed weighted result; this is a best-of-knowledge decision.

## value

PASS

This turns a uniform sufficient time-step rule into an exact per-generator admissibility test and identifies the specific local bottleneck that prevents a larger completed step. The one-way-edge and star regimes explain why the generic bound can miss by a factor of two. The useful content is the complete directed classification, not the standard SSP decomposition or a triangle count alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
