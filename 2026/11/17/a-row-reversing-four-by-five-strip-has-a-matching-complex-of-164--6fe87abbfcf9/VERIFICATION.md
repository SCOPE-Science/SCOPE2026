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

# Reproducibility

Run `python3 verify_twisted_grid.py` with a standard Python 3 interpreter. It regenerates the graph and its matching complex instead of relying on externally saved simplices. The output is an exact single-line JSON object, expected in `EXPECTED.json`.

The program independently explores all 255300 augmented faces; for each of the two pivot orders it checks every pairing, all gradient-path arcs and the absence of directed cycles. For the first order it reconstructs the signed integral 181-by-17 boundary and executes 17 unimodular integer cancellations. For the reverse order it reconstructs the critical five/six and six/seven maps, verifies their unit ranks and their zero composition. The full forward sparse matrix is included in `MORSE_BOUNDARY.tsv`.

The verification is an exhaustive finite proof certificate for the specified graph, not a claim about an infinite graph family. No external mathematical audit has been conducted.
