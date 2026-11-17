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

# Reproduction and limits

Run `python check_suspension_doubles.py` with Python 3.9+. Install `networkx` using `pip install -r requirements.txt` to include the icosahedron example. The checker directly constructs the simplicial double from all suspended tetrahedra and independently forms the opposition multigraph from the triangles. It verifies connected components, componentwise Betti ranks, exact vertex/edge counts, face-transversal enumeration and three-colorability for the included finite inputs, including 96 deterministic edge flips of bipyramids. Its ending status line is `SUSPENSION_DOUBLE_OPPOSITION_TRICHOTOMY_PASS`.

Recorded output is stored in `CHECK_OUTPUT.txt`. The infinite classification does not follow from the finite runs; the proof in `RESULT.md` establishes it from tetrahedral incidence, dual-face connectedness and graph homotopy. This package provides no external or independent mathematical audit and no certified implementation of generic surface recognition beyond the listed triangulations.
