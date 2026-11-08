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

Run `python3 verify.py` with Python 3 standard library and no external data. It exhaustively reconstructs the binary search tree from each of the \(n!\) insertion orders for \(3\le n\le8\), then independently evaluates internal leaves and rank depths. Exact rational comparisons cover the conditional local-maxima lemma, the direct covariance, and the claimed closed formulas. For every key of every order \(3\le n\le120\), it also checks reconstruction from conditional minimum events and the predicted signs.

The verified output from the packaged program is:

`VERIFY_OK 423989 exact assertions; exhaustive n<=8; all ranks n<=120`

The remaining infinite-order claim is established by the exact indicator decomposition, conditional integration, telescoping and sign arguments in `RESULT.md`; finite enumeration is not an infinite proof. The verifier does not establish independent peer validation, historical novelty, stronger probability bounds, or the corresponding result for nonuniform insertion orders.
