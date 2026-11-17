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

## Reproducible computation
Run `python verify_dual_box_h1.py` with Python 3 and SymPy installed. The script constructs each original hypergraph and its incidence dual. Rather than trusting a precomputed face list, it enumerates maps from the four vertices of a square to hypergraph vertices, requires each cube edge to map into one hyperedge, and drops coordinate-degenerate cubes. The complete signed \(2\)-boundary lattice is expressed in an integral cycle basis for \(\ker\partial_1\), then reduced to Smith normal form. This computes integral \(H_1^{\Box}\) including torsion.

The executable checks six families, including two loose uniform cycles with different homology and an asymmetric nonuniform incidence relation; the last line is `DUAL_BOX_H1_INTEGRAL_FINITE_CHECK_PASS`. Recorded output is in `verification_output.txt`. The exhaustive enumeration applies only to those six finite instances. The unrestricted duality is proved independently in `RESULT.md`, using the two-section chain identification and inverse witness constructions.

## Limits
The computation does not certify homology in higher degrees and does not establish hypergraph homotopy equivalence. The finite cases do not replace the proof for arbitrary hypergraphs. There has been no independent audit.
