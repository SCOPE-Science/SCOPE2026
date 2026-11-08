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

# Reproducible checks

Run `python verify.py` in an environment with SymPy installed. The script constructs a full labeled-vertex residual-state recursion independent of the reduced \(k\)-state proof, checks it for \(1\le n\le7\), exhausts all uniform edge-order permutations through \(n=3\), verifies nineteen exact polynomial coefficients, and compares mean/variance recurrences at \(n=100000\) to their derived asymptotic constants. It also checks normalization and parity support.

The generating function, moment constants and central limit theorem for every \(n\) follow from the written recurrence, differential equation and complex coefficient estimates. Neither finite enumeration nor a successful checker execution alone establishes those infinite statements. All computations use exact rational arithmetic except the final large-index moment comparison. Source precedence and historical priority remain subject to independent investigation.
