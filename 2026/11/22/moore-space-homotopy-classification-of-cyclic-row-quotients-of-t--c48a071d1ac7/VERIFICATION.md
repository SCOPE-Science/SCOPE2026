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

# Reproducibility and limits

Run `python3 verify.py` with Python 3 and its standard library. The program enumerates row-rotation orbits of nonattacking rook faces at widths three through eleven, tests their exact cell counts, checks the boundary-of-boundary identity, and replays the explicit free-group word cancellations used for the family theorem. Its final line is `VERIFY_OK`.

The unrestricted theorem is proved symbolically in RESULT.md. The finite program cannot certify all widths by itself. The code uses no external data or precomputed matrices. Independent mathematical validation has not been performed.
