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

Run `python3 verify_ranks.py` and `python3 verify_states.py` using Python 3.10 or newer with no third-party dependencies. Both are standalone and construct the labelled graph afresh; no historic files or network services are needed.

The first program checks adjacency-power ranks and fixed-subspace dimensions for all 49 ordered pairs of shore sizes 2 through 8. The second directly traces all 1,233,152 initial binary states across eight graphs and checks the predicted primitive orbit populations, first-entry cumulative counts, and sharp final-depth witnesses. The tested sizes and their exact success counts appear in the programs and in `RESULT.md`.

The checks were executed successfully before packaging, and they should be rerun from embedded file bytes after extraction for transport verification. Finite tests cannot establish any universal quantified assertion over all shore sizes or all characteristic-two fields; the explicit algebraic proof supplies those claims.
