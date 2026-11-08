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

# Reproduction and scientific limits

Run `python3 mcgee_rips_verifier.py` with Python 3 and the standard library. The provided output file contains the actual stdout of the bundled program. The program constructs the specified graph without third-party data, checks every shortest path using both BFS and Floyd–Warshall, verifies all 96 elementary radius-two collapses against the current face poset, enumerates every radius-three face, and independently checks the six distance-four four-cycles and the exact join face polynomial.

The theoretical deductions used after the finite checks are: a connected graph retracts to a wedge of its cycle-rank many circles; an elementary simplicial collapse is a homotopy equivalence; the independence complex of a disjoint graph union is the simplicial join of the component independence complexes; and a sixfold join of zero-spheres is a five-sphere. These are integral homotopy statements, not extrapolations from finite-field homology.

The program's scope is exactly the finite twenty-four-vertex graph defined in the result, so it does not establish results for arbitrary cages. Publication-priority comparisons rely on accessible primary results; incomplete coverage of unindexed or inaccessible literature is a separate limitation. No independent audit has been performed.
