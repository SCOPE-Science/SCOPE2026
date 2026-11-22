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

## Actual checks
The self-contained script `verify.py` enumerated all \(2^{n-1}\) masks and all \(n-1\) unit steps for \(n=2,4,8\). It confirmed sharp coefficients \(1,3/2,11/4\) and the **exact** random-mask means \(1/2,1,13/8\) respectively. Random checks for four larger dyadic sample lengths exercised the independent spectral-mask upper bounds and agreement of strict-chamber soft-threshold differences with their predicted projections (560 test pairs).

## Unproved limits and reproducibility
Neither the exact full asymptotic leading coefficient of the sharp two-input multiplier nor a closed formula for its finite-dimensional maximum is claimed. The checker is finite only; the general sharp exponent and binomial expected law follow from the mathematical proof in `RESULT.md`. Run `python3 verify.py`. All data and tests are generated reproducibly from the embedded standard-library script.
