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

The standalone `checker.py` tests both the upper-bound combinatorics and the acyclic construction directly. It performs an exhaustive three-chain-free search for every Boolean-lattice witness family at hypothesis counts 0 through 4, and evaluates the precise rule semantics for all hypothesis assignments at every extremal context for counts 0 through 8. It additionally tests interval convexity and minimal-obstruction witnesses. Invoke `python checker.py`; the expected final line is `ALL_CHECKS_OK`.

The general infinite parameter statement is justified by the proof in `RESULT.md`; finite tests alone cannot certify it. The exact relationship to every older order-convex Helly theorem has not been exhaustively established. Independent mathematical auditing has not been performed.
