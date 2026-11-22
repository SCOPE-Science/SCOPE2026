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

# Verification scope

`verify_dodeca_fault.py` is a standalone reconstruction from the defining twenty vertices and thirty edges of the dodecahedral graph. It uses Python 3.9+ and the exact integer Smith-normal-form implementation from SymPy. Run `python3 verify_dodeca_fault.py`; compare its output to `VERIFIER_OUTPUT.txt`. The matrix and eight-triangle cycle data are in `MORSE_CERTIFICATE.json` and are generated afresh by the verifier.

The script checks thirty-six intact perfect matchings by both a unique least-vertex recursion and a separate subset-dynamic-programming count. It forms all twenty-four perfect matchings after each of the three cyclic edge-type representatives is deleted, then exhaustively constructs the corresponding \(20,977\) nonempty simplices. It verifies an acyclic discrete-Morse matching by topological sorting all \(111,362\) directed Hasse incidences for each representative, constructs exact signed integer Morse boundary matrices, and checks the exact Smith factors. It also constructs a nonbounding mod-two two-cycle in the faulty complex and independently verifies that this eight-triangle cycle is not a boundary among the intact complex's original \(2,180\) triangles and \(5,790\) tetrahedra. Cyclic rotation covers all thirty graph edges.

The chain data and graph are entirely finite, and no enumerated subset is replaced by a sample. The homotopy conclusion additionally invokes the standard discrete Morse theorem, integral Hurewicz, and the classification of three-cell attaching maps to a wedge of two-spheres. The integral torsion inclusion uses naturality of the universal coefficient theorem and the explicitly checked nonzero mod-two map. No computations are claimed beyond this graph, and the map on free third homology was not checked. Independent external validation has not been carried out.
