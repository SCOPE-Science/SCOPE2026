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

# Verification of the all-parameter geodesic formula

`artifacts/verify_original.py` builds the original crown graph for every \(3\le n\le7\), reconstructs vertex-to-vertex and vertex-to-edge distances from the graph, checks lower-cardinality impossibility by exhaustive subset testing, enumerates all minimum resolving sets, constructs actual token slides, and counts shortest routes by breadth-first search.

`artifacts/verify_quotient.py` independently uses a weighted symmetry quotient with exactly \(3n-2\) states: a vacancy at index zero is described by its number of selected opposite-side landmarks; with a nonzero vacancy, the bit at index zero and the opposite-side count on other indices determine the orbit. Every transition's multiplicity counts the specific labelled token choices. Weighted breadth-first shortest-path counting verifies the formula through \(n=100\).

Execution output for both programs is embedded as `artifacts/verification_output.txt`. The mathematical proof in `RESULT.md` demonstrates all orders. The test data have not been externally or independently audited.
