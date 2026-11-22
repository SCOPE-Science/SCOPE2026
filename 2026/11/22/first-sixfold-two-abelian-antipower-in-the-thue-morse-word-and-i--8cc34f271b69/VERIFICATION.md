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

# Reproduction

Run `python3 verify_factors.py` and `python3 independent_check.py` with the two supplied files alongside this document. Both require only the Python 3 standard library. Both must exit successfully after showing the five-length maximal-exponent vector, twelve length-thirty witnesses and occurrence density `1/8`.

The first checker enumerates all factors of length at most 35 in a complete 512-symbol substitution prefix, and computes their frequencies by exact rational even/odd preimage recursion. The second independently generates all factors inside the four 128-symbol two-block substitution images and computes the exact density from 64 start offsets weighted by rational two-letter frequencies. The proof of factor completeness and the exact frequency identity are in RESULT.md. Both programs were executed successfully against their supplied paths. The result establishes no claims about larger block lengths or other infinite words. Independent mathematical audit has not been performed.
