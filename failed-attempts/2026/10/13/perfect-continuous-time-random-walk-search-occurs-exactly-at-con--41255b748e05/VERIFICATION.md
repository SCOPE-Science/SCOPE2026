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

With the given degree inner product and π=d_w/(2m), exact transfer up to phase preserves energy moments. Hs=−√π e_w and (e_w,Pe_w)_d=0 force γ=1−π by the first moment. The squared target image then gives R_w=||Pe_w||²=d_w/(2m−d_w). Cauchy–Schwarz bounds R_w below by d_w divided by the sum of degrees of the neighbors; this is at least d_w/(2m−d_w). Equality forces equal neighbor degrees and no nonneighbor because all degrees are positive. Conversely a universal apex with k-regular base has π=1/(k+2), and the span of its unit vertex state and the normalized constant on the base is invariant even when the base is disconnected. At the forced γ the two-state block squares to I/(k+2) and maps s to −e_w/√(k+2); its exact exponential gives all stated perfect times and the probability law. This includes k=0 and a two-vertex graph. The cone over P3 has R_w=4/9>3/7 for the apex, so universality alone fails. Independently written exact quadratic-field block checks for 0≤k≤12 and the P3 cone check are replayable with python3 /workspace/branches/9909a74a-ffc2-4579-b873-50462f33f873/independent_check.py. The frozen checker was inspected but not executed: its degree census is rational, its block checks floating point; neither is the all-graph proof.

## originality

FAIL

The full mirrored statement of a distinct indexed Resultary theorem for reversible Markov chains covers the graph classification, the unique tuning, the entire success curve and every perfect time by direct specialization. Neither the different normalization of the written Hilbert-space measure nor the graph-specific equality proof changes the result. This is verified mathematical coverage, not a claim about priority between same-date records.

## value

FAIL

The model-dependent distinction from combinatorial-Laplacian search is mathematically useful. As a candidate distinct finding, however, the graph theorem and all exact constants are an immediate graph specialization of the verified existing criterion. The same moment/equality framework appears there, and the frozen record supplies no further invariant or uncovered class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
