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

# Computational verification

The exact state space consists of sixteen four-letter palindrome targets and a 16-bit visited subset. The proof of completeness is the Hamiltonian overlap reduction in `RESULT.md`. `verify_dp.cpp` uses a bottom-up exact integer dynamic program, independently implemented from the Python recurrence. Its actual executed output at alphabet size four was `q=4 n=16 min=44 optimal target orders=5472`.

`verify_enumeration.py` uses top-down cached recursion. It visits every minimum-cost tour, constructs its cyclic word, verifies each target appears exactly once, checks that the 5,472 normalized outputs are distinct, and computes full permutation/reversal orbits. The actual executed output was `ENUMERATION_OK 44 5472 5472 124 {48: 105, 24: 17, 12: 2}`. The program reads the included `representatives.csv` and verifies exact equality with the reconstructed 124 representatives and their orbit sizes.

Run `python verify_enumeration.py`; for an independent implementation compile `verify_dp.cpp` using a C++17 compiler and run the resulting executable with argument `4`. These are exhaustive finite certificates, not random tests or claims about other alphabet sizes. No independent external validation has been performed.
