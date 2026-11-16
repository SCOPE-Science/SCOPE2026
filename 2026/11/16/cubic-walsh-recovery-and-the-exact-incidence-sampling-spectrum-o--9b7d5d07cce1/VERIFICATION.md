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

Both verification programs construct the labelled systems independently and check the claimed ranks: `verify_exact.py` uses exact cover and exact-integer annihilating-polynomial and trace calculations; `verify_orbit.py` uses the full symmetric-group relabelling orbit and finite-field Gaussian elimination. The first program uses only the Python standard library. The second needs NumPy and checks ranks modulo \(10007\), which does not by itself prove rational ranks. The proof of rational rank rests on the integer polynomial and trace identities plus relabelling transitivity. All claimed results concern only labelled order-nine Steiner systems and degree at most three.
