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

The independent small-graph simulator exhaustively processed all initial ternary states for rim sizes 3 through 10, agreeing with both exact transfer counts. `checks/verify_wheel.py` also checks the stated characteristic polynomials. The separate C light-cone checker exhaustively processed all 43,046,721 possible combinations of a 15-site initial window and hub phase, confirming equality of its central site's states after four and seven updates. The finite-radius lemma proves this suffices for all rim orders. The direct analytic no-tricolored-triangle argument covers the complementary extinction case. Neither checker establishes historical novelty or constitutes independent validation.
