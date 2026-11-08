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
# Reproducibility and scope of verification

Run `python3 verify.py` from the directory containing this document. The verifier uses only the Python standard library. It constructs every allowed face from the exact per-page triangle exclusion inequality, checks reduced simplicial boundary ranks over \(\mathbf F_2\) and \(\mathbf F_3\), and compares the resulting Betti numbers with the proposed integral ranks. It independently computes signed fixed-face traces for three generators: the common-edge endpoint swap, a private-vertex swap, and a page swap, and compares them with characters predicted by the integral tensor/exterior representations. A successful execution emits the line recorded in `verify_output.txt`.

The exhaustive finite tests cover the listed bounded parameter pairs only, not all integers; finite-field agreement does not exclude general-parameter torsion. The mathematical proof, rather than this code, establishes the infinite-family wedge decomposition and integrality. Verification is not independent validation.
