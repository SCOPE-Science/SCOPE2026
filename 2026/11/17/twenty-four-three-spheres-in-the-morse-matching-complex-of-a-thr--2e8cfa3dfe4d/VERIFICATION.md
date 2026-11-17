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

# Executable verification

Run `python verify.py certificate.json` in a directory containing the supplied two files; Python 3 standard library only. The program reconstructs the base complex, all 21 Hasse incidences, the ordinary Morse-matching complex of 2,121 nonempty simplices, its face vector, the full certificate partition and the directed acyclicity of the 1,048 reversed face-poset cover edges. It separately computes the reduced mod-two simplicial boundary ranks. Actual replay output is embedded as `verification_output.txt`.

The acyclic matching has one critical vertex and 24 critical three-dimensional simplices. Discrete Morse theory therefore supplies an integral homotopy equivalence to a CW complex with one zero-cell and 24 three-cells, hence a wedge of 24 three-spheres. The mod-two ranks are corroboration only and do not independently establish integral homotopy. No automated verification of unpublished equivalence claims or independent human mathematical review is asserted.
