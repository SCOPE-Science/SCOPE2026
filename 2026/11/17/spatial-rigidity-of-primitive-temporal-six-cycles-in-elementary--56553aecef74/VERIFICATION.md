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

The finite graph proof checks every possible ordered triple of temporal words at heights 1, 2, 3, and 6, then computes exact strongly connected components and certifies simple-cycle degrees. This is an exhaustive finite proof of the all-circumference claim through the closed-walk bijection.

Compile and execute `transfer_certificate.cpp` using a C++17 compiler; compare standard output with `transfer_output.txt`. Run `python3 direct_enumeration.py` and compare standard output with `direct_output.txt`; it independently checks original rule evolution on all rings from three to sixteen sites and the halfway shift identity on lengths eight and sixteen.

The independent direct enumeration alone would not prove a result for every ring circumference; the transfer-graph argument supplies that step. Historical originality remains subject to accessible-source limitations. No independent external audit was performed.
