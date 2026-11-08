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

# Reproducible verification

Run `python3 verify_rule232.py` with standard Python 3 (no third-party packages). `verify_rule232.log` is the captured output of the actual packaged script.

The checker constructs the synchronous three-input majority update directly for every \(n=3,4,\ldots,18\) and every one of its \(2^n\) states. It determines the first periodic entry using direct one- and two-step recurrence checks at every step, independently computes the initial disagreement-bond gap prediction, computes a new transfer matrix for each time cutoff and compares the exact integer traces with the cumulative simulated counts. It also validates the maximum \(\lfloor(n-1)/2\rfloor\), the exact \(2n\) maximizer population and the exceptional initial two-cycle. The total checked is 524280 labelled starting configurations; the log ends in `VERIFY_OK`.

The tested interval is finite. The proof for every \(n\ge3\) instead uses the local invariant, parity-conditioned bond encoding and a transfer-word bijection. The probabilistic limit is a separate asymptotic argument; finite simulation cannot establish it for all sizes. No external audit or certification has been performed.
