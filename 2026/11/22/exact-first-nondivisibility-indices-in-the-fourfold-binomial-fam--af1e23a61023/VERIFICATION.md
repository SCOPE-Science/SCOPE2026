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

The complete first-failure formula is proved by an integer binomial identity, Kummer's theorem, an exact closed two-step finite-state reachability certificate, and an explicit witness at the boundary. Run `python checker.py` with Python 3 to replay the finite-state proof certificate and the separate finite regression tests. The code is self-contained and uses only Python standard-library arithmetic; it enumerates a fixed finite state set rather than extrapolating an infinite property from finite index testing.

All-parameter coverage depends on the correctness of the transition semantics and the two-step closure, whose concrete states and formulas are present in `RESULT.md` and `checker.py`. The program is not an independent mathematical audit. The primary original article was inspected in full text, but absolute historical priority and independent verification remain open.
