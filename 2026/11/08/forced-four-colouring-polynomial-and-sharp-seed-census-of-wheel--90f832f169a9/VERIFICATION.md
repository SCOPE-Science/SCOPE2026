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
Run `python verify.py` with Python 3.9 or newer; the verifier uses only the standard library. It checks the original adjacency-based local rule exhaustively on all partial assignments for wheel rim orders \(4\) to \(7\); compares them with an independent direct classification of proper rim colourings and blank sets; checks the exact twelve-state transfer coefficients against direct structural counts through rim size \(10\); and tests closed minimum-seed formulas through \(12\). A successful run ends with `VERIFY_OK`. The tests are finite and cannot themselves prove correctness for arbitrary rim size. This independent-audit field records that no separate independent audit has been performed.
