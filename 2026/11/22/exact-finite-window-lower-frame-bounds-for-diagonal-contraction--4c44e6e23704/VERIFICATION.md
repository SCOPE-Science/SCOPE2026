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

The complete proof of the all-horizon theorem appears in `RESULT.md`. Run `python3 verify.py` on the embedded standard-library script. The observed output is `FINITE_WINDOW_FRAME_CHECK_OK 1013`, including finite positive-matrix tests, all-sign optimizers, random competitors, rational limiting examples, and high-precision short-window constants.

The program does not enumerate all dimensions, all continuous horizons, or all real rate configurations; those quantifiers are established by the analytical total-positivity and Perron arguments. The short-time expansion is proved using a rescaled Gram matrix and shifted-Legendre normalization. The older infinite-horizon and small-time asymptotic results are attributed separately.
