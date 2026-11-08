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

# Executed finite verification and proof certificate

Run `python3 verify.py` in this directory. The script requires no external packages, network access, or other files. Its complete input graph is explicitly declared, and all arithmetic is exact integers or bit-level arithmetic over the field with two elements.

The successful execution enumerated all 16,383 nonempty subsets of the fourteen directed arcs, accepted exactly 280 valid multipaths with face vector (14,64,114,76,12), and built 834 incidences of the full Hasse diagram. It reconstructed 134 disjoint face–coface pairs and 12 critical cells (one 0-cell, five 2-cells, six 3-cells). A full directed-graph topological sort visited all 280 faces, verifying acyclicity. Recursive signed Morse cancellation gave zero in every entry of the integral map from the six critical 3-cells to the five critical 2-cells. The original simplicial mod-two complex independently had Betti vector (1,0,5,6,0).

The file `matching_certificate.json` records all fourteen ordered arcs, all critical face masks and all 134 matched mask pairs, with each integer mask specifying selected arc indices by its one bits. The script rebuilds it deterministically; `verify_output.txt` records the actual successful execution. No computational claim extends beyond this finite complex. The integral homotopy step also uses the standard discrete-Morse CW theorem and Hurewicz theorem, as explained in `RESULT.md`.

Independent auditing has not been performed.
