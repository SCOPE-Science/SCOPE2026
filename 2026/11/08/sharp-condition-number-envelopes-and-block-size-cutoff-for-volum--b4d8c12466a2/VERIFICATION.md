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

## Checks executed

The standalone `check_envelope.py` was run with Python 3 and printed `PASSED exact rational assertions: 497970`. It exhaustively covers integer spectral grids for dimension 2 through 7, cap 2 through 4, and all block sizes; it verifies probability normalization, both inequalities, and equality for the extremizing two-level family. This does not prove any infinite-dimensional-parameter statement. The universal analytic proof is in `RESULT.md`.

## Reproduction

Run `python3 check_envelope.py` using the Python standard library. No external data or package is required. The numerical checker only tests its explicitly enumerated cases; the proof covers real eigenvalue spectra, arbitrary dimensions and real condition caps.
