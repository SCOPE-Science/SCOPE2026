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

# Reproducibility and scope

Run `python3 pappus5cut_verifier.py` with Python 3 and its standard library. The script explicitly defines all vertices and edges. No remote service, numerical tolerance, external data or third-party package is needed.

The verifier checks all \(262144\) vertex masks and compares a facet down-closure construction with an independent Boolean-zeta-transform membership test. It enumerates the \(324\) connected and \(8244\) disconnected induced five-sets; verifies the eighteen induced six-cycles and their one-to-one match with missing twelve-vertex faces; generates a specified augmented discrete-Morse matching and converts it to an ordinary matching; then exhaustively verifies directed acyclicity on all \(2296998\) Hasse incidences. The resulting ordinary critical cells are one vertex and \(2074\) twelve-cells, so the cited discrete-Morse theorem proves the claimed homotopy equivalence. The script also checks the independent reduced Euler characteristic.

The recorded `pappus5cut_verification_output.txt` is included for comparison. The critical scientific evidence is the reconstruction and verification performed by the standalone program, not an unexamined log. Exact graph size, homotopy type, and numerical checks hold only for the graph and complex defined in the manuscript. Independent external audit has not been performed.
