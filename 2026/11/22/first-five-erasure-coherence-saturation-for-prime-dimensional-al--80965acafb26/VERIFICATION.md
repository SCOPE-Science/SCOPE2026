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

# Verification

From the directory containing the exported files run `python CHECK.py` using Python 3.10+ with NumPy. The certificate exhausts every 5-subset at primes 5, 13 and 17 (7476 total) with modular integer Legendre symbols; checks every triple-sign in nine explicit admissible witnesses for primes 29 to 101; reconstructs the actual normalized cubic Alltop vectors, five-column Gram matrices, expected eigenvalues and complete frame tightness in each witnessed dimension. The observed final message is:

`CHECK_OK excluded_five_sets=7476 explicit_witnesses=9`

The all-prime assertion is proved analytically by the quadratic Gauss sum, exact triangle indicator expansion, elliptic Hasse estimate and Paley graph Hoffman independence bound. Numerical eigenvalue checks verify normalization and witness realization but do not certify the infinite statement by enumeration.

The equality characterization is exact; when saturation is absent, this document makes no claim of an exact alternative optimum. Independent mathematical audit has not been performed.
