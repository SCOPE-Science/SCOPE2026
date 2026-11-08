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

The theorem is proved analytically in `RESULT.md`, including the boundary sectors and all equality cases. The associated independent numerical test uses genuine geometric overlaps of two intervals and a separate numerical integral rather than re-integrating the closed formula. Run:

```sh
python3 verify.py
```

It uses only Python 3 standard-library modules (`math`, `random`) and a fixed pseudorandom seed. A successful run prints `CHECKS_OK 6171`, representing 180 independently quadrature-compared random input triples plus 5,082 parameter-grid minimum checks and 909 deficit-grid checks.

The Simpson quadrature uses a logarithmic change of variables to resolve small overlap thresholds. Numerical tolerances allow for finite precision. A passing computational test cannot certify the claimed continuum of parameter values; the overlap-distribution proof and analytic minimization establish those statements. No independent audit, external theorem-prover verification, or historical-priority certification is represented.
