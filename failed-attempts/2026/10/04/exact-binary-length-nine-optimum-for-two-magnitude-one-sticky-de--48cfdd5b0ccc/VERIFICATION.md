---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The channel was reconstructed from runs: choose zero, one, or two distinct runs of length at least two and shorten each chosen run by exactly one without erasing it. The two package implementations agree on all 512 sources. Independently, all 512 balls and all 894 possible outputs were rebuilt and an exact set-packing MILP over the output-incidence constraints attained and proved optimum 120. The supplied 120-word packing and exact rational dual weighting of total mass 120 provide a second, transparent primal/dual certificate.

## originality

PASS

Wang--Vu--Tan define exactly the at-most-\(t\), per-run limited-magnitude channel and reduce it to asymmetric limited-magnitude errors, but their results are general constructions and redundancy bounds rather than an exact binary \(n=9,t=2,\ell=1\) packing number. Targeted semantic search found no covering small-parameter value.

## value

FAIL

Although the value 120 is correct, original on the bounded search, and rigorously certified, the record does not establish why binary length nine is a mathematically natural cutoff, first exceptional case, or boundary, nor does it classify optima or reveal a structural mechanism beyond the finite packing/dual certificate. Under the shared value standard, a computationally convenient isolated parameter without an independent reason that this exact fact is likely to be needed is too arbitrary; correctness, reproducibility, and novelty alone do not supply value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
