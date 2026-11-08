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

# Verification of the exact cycle–clique induced-forest formulas

The supplied `verify.py` can run using Python 3 standard library only. It constructs all edges of each test graph, tests acyclicity by union–find on the induced edge set, and tests inclusion-maximality by attempting to adjoin each omitted vertex. It separately implements cyclic-word conditions and enumerates gap compositions corresponding to the closed coefficient formula. The graph-level implementation does not assume the cyclic formula.

One completed run passed all eight direct-graph profiles with \(189696\) masks and \(3404\) facets; it also passed \(24\) gap-coefficient comparisons and sharp spectrum checks at cycle lengths \(4\) through \(11\).

The verifier checks finite instances, not an infinite statement, and does not compute homotopy groups or establish external priority. The unrestricted proof is the combinatorial argument in `RESULT.md`.
