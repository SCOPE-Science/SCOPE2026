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

# Verification record

The analytical derivation from nine edge-crossing predicates is contained in `RESULT.md`. The accompanying `verify.py` uses the actual prism vertices and nine edges to count section vertices for independently generated Gaussian normals, rather than inferring counts from the formula being tested. It also performs direct angular quadrature for the event probabilities. The executable was run from the file embedded alongside this note, with its output:

`VERIFY_OK heights=7 plane_normals=1260000 exact_integrals=14 max_absolute_sampling_error=0.00219519 pentagon_optimum_H=0.531469551064 pentagon_probability=0.385155805674`

The seven tested values of \(H\) were \(0.12,0.35,0.5314695510636118,0.8,1,2.5,8\). The numerical quadrature was required to agree with the closed forms to \(10^{-12}\); Monte Carlo sampling errors were compared with six nominal standard errors plus \(0.001\). The root check used a numerical bracket and an additional local-maximum comparison. These tests are finite and do not prove the exact continuum identities or the uniqueness of the optimum; those follow from the complete analytic argument and the strict derivative inequality.

To reproduce, run `python verify.py` with installed `numpy` and `scipy` in the directory containing the standalone file. No external data or services are required.
