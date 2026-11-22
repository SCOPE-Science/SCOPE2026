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

# Reproduction and scope

Run `python3 check.py` with Python 3.8 or newer; it uses only the standard library and does not require external files, services or datasets.

The checker evaluates every valuation on every labelled simple graph of order at most six, separately tests structural complete-multipartite classification, and for valid graphs tests all possible single-edge insertions and deletions against the formulas. It computes labelled census coefficients from separate Bell and assembly recurrences. Expected terminal output: `VERIFY_OK graphs=33868 valuation_assignments=2131019 edit_checks=24796`.

The proof of the unrestricted quantifiers rests on the neighbourhood and bridge arguments in `RESULT.md`, not on the finite run. The equality of aggregate insertion and deletion counts is the edge-toggle involution; it is not inferred from numerical agreement. No higher-order edit robustness, directed-frame result, independent audit, or automated formal certification is claimed.
