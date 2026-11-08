---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Finite verification

The attached `verifier.py` uses only Python 3's standard library and reconstructs the Desargues graph without fetching data. The captured output `verifier_output.json` comes from running that exact script.

Two separate face-membership evaluations agree for all \(2^{20}=1,048,576\) vertex subsets. The complex has 434,221 faces including the empty face and 3,663,100 immediate face incidences. An explicit staged vertex matching yields 217,103 pairs plus one critical vertex and thirteen critical nine-simplices. The complete directed Hasse-graph topological sort consumes all 434,221 nodes; a second run in reverse vertex order independently yields the same cell dimensions and passes the same acyclicity test. No unexamined faces or adjacency incidences remain.

The order-ten cyclic action was checked to preserve every graph edge. Its tenth-level rational character was computed both by orbit-union enumeration and by direct signed invariant-simplex traces over the entire chain complex. The independent calculations agree on all ten powers and verify one invariant rational line.

The finite program checks a fixed graph and is not a proof for an infinite graph family. It does not determine integral representation lattices or equivariant homotopy types. The mathematical inference from verified acyclic matchings to a CW model uses Forman's discrete Morse theorem, and the passage to a sphere wedge uses the absence of intermediate-dimensional CW cells. No independent external audit is claimed.
