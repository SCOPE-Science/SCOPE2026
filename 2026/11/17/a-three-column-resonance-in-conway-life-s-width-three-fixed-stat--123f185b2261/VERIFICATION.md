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

# Verification of the width-three Conway Life fixed-state count

Run `python3 verify_transfer.py` with Python 3 and SymPy installed. It constructs the explicit sixteen-state transfer, checks all directed components and every coefficient of its exact characteristic polynomial, verifies the ten-state polynomial, the positive Perron-vector inequalities and the Sturm root count, and prints trace counts through circumference sixteen. Its captured output is `transfer_output.txt`.

Independently run `c++ -O3 -std=c++17 verify_direct.cpp -o verify_direct && ./verify_direct`. This program does not use the transfer criteria; it constructs neighbor masks from coordinates, asserts eight distinct neighbors per site, and tests each possible binary configuration for circumference three through seven, comparing against the theorem. Its captured output is `direct_output.txt`.

The verified triple-neighbor local equivalences, exact transfer characteristic factorization, primitive-component structure and rational Collatz–Wielandt bounds establish the all-size result. Finite enumeration alone cannot prove the infinite family. The supplied verification does not enumerate all temporal basins or periods, and no independent expert validation is claimed.
