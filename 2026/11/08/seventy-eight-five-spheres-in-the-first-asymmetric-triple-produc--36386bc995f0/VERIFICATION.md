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

# Reproducibility and finite proof limits

`verify_product.py` is a standalone Python 3 program requiring only the standard library. Run `python3 verify_product.py` and compare its full JSON output to `verification_output.json`. It rebuilds the 24-vertex categorical graph, computes its 72 edges, enumerates faces independently using selected-neighbor degree constraints and forbidden centered triples, tests three acyclic matchings over the complete Hasse graph, and computes mod-two Morse boundary ranks for the independent mixed-order reduction.

The primary and reverse matchings each have 17,415 pairs, one critical vertex and 78 critical five-cells; complete acyclicity is checked on 34,909 nonempty faces and 191,232 Hasse incidences. This produces the integral wedge homotopy equivalence through Forman's discrete Morse theorem. The third reduction has nine critical four-cells, 95 five-cells and eight six-cells, with respective fifth- and sixth-differential ranks nine and eight over the two-element field. Graph, face, matching and rank assertions are evaluated by the code, rather than being inferred from an existing output file.

The proof is exhaustive only for the stated finite graph; it does not certify any infinite parameter family. The verification is reproducible but not an independent external audit.
