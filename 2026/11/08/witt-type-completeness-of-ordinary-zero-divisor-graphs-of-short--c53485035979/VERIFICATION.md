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

Run `python check.py` beside `verification_output.txt`. The script performs exact finite-field arithmetic in fields of order 2, 3 and 4, enumerates every ordered radical element and tests zero products of all unordered distinct pairs. It computes degree histograms and edge counts directly and compares with the claimed formulas for ten cases covering the parity and Witt-type cases. The recorded output is the standalone file `verification_output.txt`. The tests are finite corroboration; correctness for every finite field and dimension follows from the symbolic proof and the standard finite-field bilinear-form classification. Independent audit has not been performed.
