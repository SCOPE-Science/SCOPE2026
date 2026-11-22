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

# Reproduction and verification

Run `python3 verifier.py` using Python 3's standard library. `verifier_output.txt` records the output from the delivered source code. The executable enumerates all ordered two-new-vertex oriented diagrams over each named transitive tournament through five vertices and rejects exactly those with a directed cyclic triangle, checking both orientations and nonedges. It also evaluates the transfer matrix for base sizes through 100 and compares exact rational adjacency-type proportions for strict decay over the same finite range.

The infinite proof does not rest on the checked range. Its critical deductions are: (i) the three-symbol unary-word characterization; (ii) the single simultaneous forbidden pair for a directed edge; (iii) the transfer matrix and exact formal generating function; (iv) a direct rational inequality strictly positive for every nonnegative integer. The theorem does not assert uniform sampling of vertices, priority in all prior literature, or independent verification.
