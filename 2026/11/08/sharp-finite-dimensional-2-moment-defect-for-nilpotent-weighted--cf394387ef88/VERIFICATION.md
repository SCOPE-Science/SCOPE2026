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

# Reproducible verification and scope

Run `python3 check_embry_defect.py` with Python 3 and no dependencies. The observed output was:

`EMBRY_DEFECT_CHECK_OK 29038 assertions`

The program uses exact rational matrix multiplication to test the formula for the second Embry residual of finite shifts. High-precision decimal arithmetic checks the constructed extremizers, all recurrence steps and numerous other feasible profiles; a finite floating-point computation probes the asymptotic error. The code checks **finite cases only**. The all-dimensional minimax and asymptotic assertions require the complete inequality and summation proof in `RESULT.md`.

The standalone checker is embedded in the same package. No independent audit or external theorem certification has been performed.
