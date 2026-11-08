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

The standalone `verify_bands.py` reproduces finite witnesses for each integer \(K\) from 1 through 5, with separated Gaussian ranges chosen according to the stated construction, and compares the explicit density–polarization matrix discriminant against the normalized inequality.

Run: `python3 verify_bands.py`. The supplied execution reports 97 passed finite checks. These checks are not a proof of the bound for arbitrarily large \(K\). The proof uses two independent mathematical arguments: alternating signs force \(2K\) positive zeros, and the real-exponential-polynomial zero bound prevents extra or repeated zeros. The implicit-function and tail-monotonicity argument then gives exactly \(2K+1\) oscillatory components for sufficiently small positive propulsion.

The material concerns the linearized two-field approximation, not the full microscopic particle model. Independent audit has not been performed.
