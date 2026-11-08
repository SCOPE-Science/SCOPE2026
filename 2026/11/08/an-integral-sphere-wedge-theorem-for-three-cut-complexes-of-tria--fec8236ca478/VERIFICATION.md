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

# Reproducibility and verification

`verify_triangular_cut.py` uses Python's standard library and does not require network access. Run `python3 verify_triangular_cut.py` in the directory containing the file. Its exact observed output appears in `verification_output.txt`. It constructs dual faces from their star/four-vertex characterization and separately checks the induced-three-connectivity definition for every subset at \(n=5,6\). For each \(n=5,6,7,8,9\), it exhaustively constructs the discrete-Morse matching, checks all matched pairs belong to the Hasse diagram, enumerates all nonempty-face Hasse incidences, and topologically sorts the directed matching graph to verify acyclicity. The output reports critical face counts; the unique 37-face relative matching is a repeated local pattern.

The calculation does not exhaust infinitely many graphs. The printed `THEOREM_LOCAL_AND_FINITE_CHECKS_PASS` refers to finite cases and the universal local pattern. The mathematical proof for all \(n\ge5\) is in `RESULT.md`: facet classification, support-fiber patchwork, integral combinatorial Alexander duality, simple connectivity, Hurewicz and Whitehead. External independent audit is not performed.
