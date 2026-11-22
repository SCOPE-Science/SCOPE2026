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

The included `checker.py` uses Euler's criterion and two independently implemented counting methods. It compares all eight frequencies and the elliptic quartic sum for every prime from 5 to 997 and exhaustively prints the small-prime table. The proof supplies the non-computational inequality for all primes at least 37, so the finite check only needs to cover 5,7,11,13,17,19,23,29,31 to establish sharpness. The checker is reproducible with standard Python and finite integer arithmetic. It cannot independently establish that an equivalent theorem has never been published.
