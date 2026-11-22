---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Flow decomposition into 0-1 source/sink path vertices is valid; strict convexity in each argument puts every maximizer at vertices. For path indicators the squared distance equals the symmetric-difference edge count. Adding a missing internal vertex increases this distance, so the union covers all internal vertices. Shared edges then correspond exactly to adjacent common vertices; removing one endpoint of a shared edge from one path increases the distance, excluding shared edges at an optimum. The remaining common core must be an independent set in the path on 3..N-2, of cardinal floor((N-3)/2). Independent-set maximum placement yields one odd and k-1 even cores; k private vertices have 2^(k-1) unordered assignments. Cases N=3,4 and nonvertex points were explicitly checked; no enumerative inference is used for all N.

## originality

PASS

Compared this final mathematical assertion with semantically relevant published findings and primary material by implication, not title; known tools and special-case results were excluded from the new part. Remaining source-access limitations are explicit.

## value

PASS

The exact natural Euclidean diameter and complete antipodal-pair census of an established complete-DAG unit-flow polytope form a useful rigid global optimization and face-independent metric fact, not merely another f-vector computation; the parity-dependent equality configurations can support future geometric questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
