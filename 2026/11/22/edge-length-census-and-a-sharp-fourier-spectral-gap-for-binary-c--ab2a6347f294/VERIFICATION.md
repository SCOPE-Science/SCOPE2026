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

# Reproduction and limits

Run `python3 check_spectrum.py` with Python 3 standard library. It independently enumerates minimal zero-sum differences at parameter pairs `(1,2), (1,3), (1,7), (2,2), (2,3), (2,4), (2,5), (3,3), (3,4), (4,3), (4,4)`. It compares calculated per-vertex move counts against the closed degree by length, and checks completeness for lengths at most three. It enumerates all four-label Fourier characters at `n=3,4` and compares their exact eigenvalues against the closed histogram expression. It exhaustively checks the proposed sharp eigenvalue inequality and equality patterns for all four-color histograms for `n=2,...,15`. The expected success line is `FULL_CTP_EDGE_AND_FOURIER_EXACT_PASS`.

The tests are finite; the general edge theorem is established by the binary-circuit classification and the rank-two spectral gap for all `n>=16` by the analytical inequalities in RESULT.md. This verification is same-model only; no independent audit or external certification was performed.
