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

# Verification of periodic-cylinder closure bounds

The analytical derivation is contained in `RESULT.md`. Run `python3 checks/verify.py` in the extracted package directory. The script uses only the Python 3 standard library, generates admissible words and their finite closing periods, computes exact graph-matrix traces, and verifies upper and lower inclusions for all integer deficits in the finite cases it tests. Exponential-moment values are finite-length illustrations, not proof of their limiting orders.

For the three-symbol no-repeat graph it tests lengths 4–11, for the golden-mean graph lengths 4–13, and for the period-two bipartite graph lengths 4–8. The exact infinite claims use Perron–Frobenius theory, positive closed-walk estimates along the graph period, and an exact tail-sum identity. No external software, independent audit, or numerical infinite certification was used.
