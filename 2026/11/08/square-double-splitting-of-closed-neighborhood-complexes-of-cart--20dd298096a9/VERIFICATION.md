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

# Verification

Execute `python3 verify.py` using the Python standard library. `verify_output.txt` records the completed run. The verifier rebuilds every simplex from the closed neighborhoods for ten connected products with no three- or four-cycles in either factor. It then executes each prescribed free-face deletion and checks *all* remaining cofaces at the moment of deletion, independently regenerates the predicted two-dimensional double-square complex from the product squares, and verifies exact equality of the face sets. An independent mod-two boundary matrix reduction computes degree-one and degree-two Betti numbers of the resulting complex.

The test products include edge-by-edge, edge-by-path, path-by-path, star-by-edge, star-by-path, pentagon-by-edge, pentagon-by-path, pentagon-by-pentagon and pentagon-by-hexagon. All ten passed. For the pentagon-by-pentagon case, there were 575 nonempty original simplices, 175 elementary collapses and 225 residual nonempty simplices with face vector \((25,100,100)\); the computed reduced mod-two Betti ranks were \((2,26)\). The pentagon-by-hexagon case had face vector \((30,120,120)\) and mod-two Betti ranks \((2,31)\).

The universal statement for all finite connected triangle- and four-cycle-free factors follows from the proof in `RESULT.md`, not from these ten computations. Integral homotopy equivalence is obtained by explicit elementary collapses and nullhomotopic disc attachments, not inferred from field homology. No independent external mathematical review or numerical certification has been performed.
