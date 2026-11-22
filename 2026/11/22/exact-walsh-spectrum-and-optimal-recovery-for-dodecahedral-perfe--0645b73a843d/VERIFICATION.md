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

## Reproducibility

Run `python3 verify.py` with Python 3.9 or newer. The certificate uses only the Python standard library. It checks the graph isomorphism, the two complete matching enumerations, 2048 signed coefficient classes in each of two graph encodings, the independent Walsh transform, all 30 edge marginals and 435 edge pairs, exact projection-kernel inversion, and the derived full Fourier rank and nullity. Expected result begins with `PASS:`.

## Limits

Computations are exhaustive for the specified dodecahedral graph but make no assertions for infinite graph families. The extension from 2048 sign classes to all 1073741824 Boolean frequencies follows from the exact vertex-star switching argument in `RESULT.md`. Minimality among unrestricted projections follows from finite-group translation averaging. The independent mathematical audit remains not performed.
