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

# Reproduction and limits

Execute `python3 verify.py` with Python 3; no third-party modules or data files are required. It checks each finite-degree polynomial identity symbolically over exact rational coefficients using only standard-library arithmetic. Each certificate is therefore an identity for arbitrary parameters, not a finite search. It also enumerates all vertex subsets and tests shortest-path triples for the two- and three-part graphs (orders ten and fifteen) to check the underlying general-position polynomial directly, and samples further integer parameters only as a sanity check.

Observed output:

```text
SYMBOLIC_ALL_PARAMETERS_POSITIVE_COEFFICIENT_CERTIFICATES_OK
SHARP_FAILURES_AND_SAMPLE_PARAMETERS_OK
INDEPENDENT_GEODESIC_ENUMERATION_OK 2 vertices 10 sets 88
INDEPENDENT_GEODESIC_ENUMERATION_OK 3 vertices 15 sets 294
VERIFY_OK
```

The infinite claim uses the proved combinatorial classification, the exact symbolic coefficient identities, and strict log-concavity of the binomial sequence. No finite graph search alone proves an infinite-family claim. A separate independent mathematical audit has not been performed; literature priority remains provisional.
