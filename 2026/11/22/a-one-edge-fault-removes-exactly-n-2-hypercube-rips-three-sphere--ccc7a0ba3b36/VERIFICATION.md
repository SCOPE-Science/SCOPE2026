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

# Finite reproducibility and proof dependencies

Run `python3 verify_hypercube_fault.py` using Python 3.9 or later; no packages or network are needed. The script builds both shortest-path metrics by breadth-first search and all radius-two Rips faces by sorted-clique recursion, then computes boundary ranks over \(\mathbb F_2\). It also checks that the edge link consists exactly of two cliques with a matching between them.

The run recorded in `verification_output.txt` checks dimensions \(3\) through \(6\). The resulting faulty third Betti numbers are \(0,7,46,205\), against intact counts \(1,9,49,209\). The metric check verifies that exactly one unordered pair changes its distance. These are reproducible finite cross-checks, **not** certificates for arbitrary dimension or integral torsion.

The integral and infinite-dimensional assertion follows instead from the explicit edge-link homotopy, the relative long exact sequence, and primitive images of the coordinate three-cube fundamental classes, together with Adamaszek–Adams' intact-cube theorem. The bar comparison also uses the known nullhomotopy of successive scale inclusions for intact hypercubes. No independent audit has been performed.
