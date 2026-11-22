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

The reproducibility file `verify.py` was run using Python 3 with no third-party packages. All asserted statements completed, including direct checks on all Ferrers shapes for 84 parameter families with \(m\le8\), a word/path and insertion test on 18,359 boundary words, and exhaustive labelled Boolean-state tests for the listed boards up to 20 squares. In particular the original dynamics has 6, 4, 32, 14, 302, 116, 88 and 88 fixed configurations on boards (2,2), (2,3), (3,3), (3,4), (4,4), (4,5), (5,3), (3,5), respectively.

The proof of the infinite-family count is structural and uses the local corner criterion, a bijection changing the longer width by two, and exact formal power-series matrix summation. Exhaustion is independent corroboration for finitely many cases, not an infinite certificate. Only row/column relabelling classes of fixed states are counted; no assertion about labelled counts at large dimensions, transient entrance times or cycle populations is verified.
