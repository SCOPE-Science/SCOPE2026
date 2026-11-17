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

# Reproducibility and limits

The exact all-ring theorem follows from the three-time parity equation and the independence polynomial of the step-two graph, as detailed in `RESULT.md`. Exhaustive programs corroborate the rule normalization and the finite-size specialization; they do not purport to prove an infinite assertion by enumerating finitely many states.

Run `python3 verify_direct.py` for direct third-iterate evolution of every binary pair on each cyclic ring of length 3 through 10, checking the complete distribution over the number of temporal one-hot columns. Its standard output is reproduced exactly in `direct.out`.

Run `python3 verify_transfer.py` for an independent local truth-table expansion, cyclic transfer graph, recurrent-component test, and exact graph traces through length 24. Its standard output is reproduced exactly in `transfer.out`.

Both checks use only standard Python 3 and were executed from the embedded source code. No probabilistic approximation or external proof service is needed. Mathematical review is same-model only; independent mathematical audit has not been performed.
