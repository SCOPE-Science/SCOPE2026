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

The standalone source `check_integral_rotation.py` constructs every cell directly from the labelled six-rung prism, computes exact integer signed simplicial boundaries, and checks the chain identity. It tracks unimodular basis changes through full matrices and verifies their inverses, zero boundaries of all six resulting cycles, and vanishing images of the original degree-three boundary in the six homology coordinates.

The program outputs the rank-six integral degree-two homology, the complete six-by-six integer rotation matrix, the regular rational character, and the Smith diagonal \((1,1,1,1,3,0)\) for \(R-I\). The accompanying `check_output.txt` records its actual local execution output; the statements follow from the complete finite calculation and the explicit quotient-generator relation argument in `RESULT.md`, not from that output alone.

Reproduce with `python3 check_integral_rotation.py` under Python 3 with NumPy and SymPy. This is a bounded computation for one explicitly fixed simplicial complex. It does not establish results for arbitrary prism widths or constitute independent expert assessment.
