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

The standalone `verify.py` uses NumPy and SciPy. Execute `python verify.py` in the directory containing the files. It checks the full complex Lyapunov equation for 150 positive-hopping, positive-loss combinations with one to ten cells and separately confirms the large-loss trimmed-chain spectral ratio identity for 56 combinations with two to fifteen cells. It does not prove any infinite-size limit; the all-size parity, reflection and perturbation arguments are in `RESULT.md`. The complete text of a close 2026 paper on local loss in SSH chains was not accessible, so literature priority is qualified. Independent validation is not claimed.
