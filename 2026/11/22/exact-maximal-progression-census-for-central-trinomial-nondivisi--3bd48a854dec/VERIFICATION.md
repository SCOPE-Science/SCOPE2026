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

# Reproduction and mathematical scope

Run `python3 checker.py` using Python 3. No third-party dependencies or unpublished auxiliary files are required. The executable reconstructs exactly the allowed-digit carry transitions, asserts 24 reachable carry states and 294 nonzero directed weighted transitions, and computes the exact characteristic polynomial and its matrix annihilation identity. It then verifies the whole rational-function cross-product identity by integer polynomial arithmetic, and separately compares the first four progression counts against direct brute-force enumeration and the first 150 central-trinomial coefficients against the digit criterion.

The finite-state and polynomial identities establish all integer depths by Cayley--Hamilton. Numerical samples alone would not establish an infinite theorem. The supplied program verifies the critical finite calculation; independent external validation is not represented.
