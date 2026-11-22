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

The proof is fully algebraic and covers every integer \(q\ge3\), \(r\ge2\). Its critical steps are the run-length bound \(r+1\), uniqueness of cyclic consecutive-letter pairs for \(q\ge3\), maximal full-block count, one-symbol left fringe, \(r\)-symbol right fringe, and double-substitution construction of every attaining factor.

Reproduce bounded checks with `python3 verify_factors.py` and `python3 verify_prefix.py` in the same directory. Both programs use Python standard library only. `verify_factors.py` reports `PASS: 245 exact length checks across 49 parameter pairs`; `verify_prefix.py` reports `PASS: 12 parameter pairs with independent direct windows`. The paired `.out` files contain the original full outputs. Finite computations cannot alone establish universal bounds; these are independent sanity checks against the proof. Independent audit is not performed.
