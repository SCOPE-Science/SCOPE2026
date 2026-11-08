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

# Independent reproducibility instructions
Run `python3 CHECK.py` in the extracted directory. It uses only the Python standard library. The program constructs exact power tables for primitive roots in the quotient of the integer polynomial ring by the appropriate cyclotomic polynomial, enumerates all functions and all first-coordinate-injective candidate spectra for three small complete cases, checks every character inner product, and verifies the predicted multiplicity histogram. Results: \((p,q)=(3,4)\) has counts \(48,12,4\) at multiplicities \(4,16,64\); \((3,8)\) has counts \(384,96,24,8\) at \(8,32,128,512\); \((5,4)\) has counts \(960,60,4\) at \(4,64,1024\). The analytic proof in RESULT.md establishes all odd primes and all dyadic orders \(q\ge4\) without relying on these checks.

Scientific review is same-model only. Independent mathematical audit has not been performed.
