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

# Reproducible checks and limits

Run `python verify_bruteforce.py` and `python verify_transfer.py` with a Python interpreter and SymPy installed (the latter program uses exact symbolic algebra). Files `bruteforce_output.txt` and `transfer_output.txt` contain the captured successful outputs from these exact standalone sources. The brute-force implementation directly enumerates all binary inputs for \(3\le n\le16\), verifies every nonzero-output fibre's segment product and the zero-fibre avoidance count, and reports the moment. The transfer implementation constructs the \(16\)-state paired-symbol transition matrix and the \(4\)-state forbidden-block matrix, checks both characteristic polynomials using exact integer coefficients, verifies thirty-five coefficients of the squared-segment generating series, and compares the independent renewal and trace moments for \(3\le n\le36\). It also reports numerical approximations to the dominant algebraic root; these approximations do not certify a root independently of the exact polynomial and positive renewal proof.

The theorem for unbounded \(n\) follows from the exact combinatorial identity, finite determinant calculation, and renewal singularity argument in `RESULT.md`. The finite computations provide cross-checks, not an exhaustive proof over all ring sizes. Historical-priority uncertainty is documented in `REVIEW.md` and `AUDIT.json`.
