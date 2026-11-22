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
# Reproducibility and verification

From the root folder of the extracted artifact, run `python3 code/checker.py`. No network, proprietary dependency, precomputed simplicial facet table, or external scientific service is required. Its machine-readable output is in `evidence/checker_output.json`.

The checker reconstructs the 20-vertex graph, its 36 edges, 450 perfect matchings and 183,544 simplices; it checks each of 88,171 elementary collapse pairs is a genuine codimension-one free pair. The resulting core has face vector (36, 427, 1850, 3129, 1759). The checker then verifies connectivity via a spanning tree and 392 triangle-relator eliminations, exact \(\partial^2=0\), unit-only Smith reductions with ranks 392, 1458 and 1671, and the complete sixteen-element signed Lefschetz trace table for the rational symmetry character.

The digest `4c419d1d85e24ce6f8ee53dfe566a82a565d6fca41099685d8a4aecc00764e4e` commits to the **sequence of generated free-face pairs** in order, encoded as ASCII decimal bit masks `face,coface` per line. Recomputing is necessary for substantive validation; a stored log or hash alone is not a mathematical proof. Standard topology theorems (Hurewicz and Whitehead) turn the verified simple connectivity and integral homology into the homotopy equivalence.

Limitations: This is a finite exact calculation for \(C_4\square P_5\) only. The full graph-symmetry representation is asserted over \(\mathbb Q\); the integral representation and the quotient's integral homotopy remain undetermined. External article and prior-claim comparisons retain published-priority uncertainty. Independent mathematical audit has not yet been performed.
