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

# Reproduction of the finite integral certificate

Use Python 3 with SymPy installed and run `python checker.py`. The bundled output `VERIFICATION_OUTPUT.txt` records the expected exact results. The program enumerates all 78,125 column assignments with digits in \(\{0,1,2,3,4\}\); 25,684 satisfy row capacities. It checks all 128,338 Hasse cover edges, acyclicity by topological sort, every pair of the matching, and the integer Morse boundaries using recursively signed gradient replacements. The two Smith diagonal profiles are all units: twice for degree four to three and 122 times for degree five to four. Composition is zero, and the face-number alternating sum independently gives reduced Euler characteristic \(-148\).

Acyclicity is proved for this finite complex by exhaustive traversal; integer Smith forms (not ranks over a field) establish absence of hidden torsion. In the ordinary, nonaugmented face poset, the paired empty face is deleted and its vertex becomes the unique critical zero-cell. Critical cells occur only in dimensions three through five, providing simple connectivity. The Hurewicz and Whitehead arguments are written in `RESULT.md`.

The computation does not claim an all-board theorem; the title and claims apply only to the precisely specified seven-column four-row complex. This is a reproducible computational mathematical proof but not an independent mathematical audit.
