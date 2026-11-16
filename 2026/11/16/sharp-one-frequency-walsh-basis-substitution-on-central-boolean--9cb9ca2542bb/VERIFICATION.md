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

## Reproducible checks
Run `python3 verify.py` in the extracted package, requiring Python 3.8 or later and no third-party dependencies. The checker verifies the closed integer Krawtchouk identity for all indices in radii 1 through 20, independently enumerates actual Fourier coefficients on all central Boolean Hamming balls for radii 1 through 5, checks vanishing on all nonzero even frequencies, checks the complete even-basis Parseval coefficient identity and verifies the optimizer locations.

## Logical scope
The all-radius claim is proved by antipodal pairing, exact Krawtchouk duality, the Gram rank-two perturbation and binomial ratio/Stirling calculations. No finite checker certifies this infinite theorem on its own. Independent mathematical audit was not performed.
