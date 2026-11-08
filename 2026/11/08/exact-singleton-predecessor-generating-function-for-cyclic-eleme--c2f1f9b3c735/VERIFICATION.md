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

# Reproducibility and exact verification

The standard-library program `verify_finite_state.py` builds the two four-state Rule 54 de Bruijn generators from the truth table, constructs all 410 reachable capped matrices by breadth-first closure, checks both successors for every state, reconstructs the indicator for exactly one cyclic predecessor, and checks the complete 410-coordinate identity leading to the order-14 recurrence after three steps. It then checks the exact numerator and denominator coefficients and series through degree 89. Successful execution prints `CERTIFICATE_OK`.

The independent program `verify_direct.py` directly evaluates the local Boolean update on each of the \(2^n\) labeled inputs for every \(1\le n\le18\), counts predecessor multiplicities and checks the exact singleton sequence. It does not import or reference the matrix implementation. Successful execution prints `DIRECT_OK`.

To reproduce, extract all embedded files to the same directory and execute both scripts with Python 3; no external Python dependencies or hidden data files are required. The all-length theorem is deduced from the finite exact operator identity, not from agreement on a finite list of coefficients.

Limits: no independent scientific audit has been performed. This certificate covers one synchronous elementary Rule 54 update on binary cyclic rings; it does not cover multi-step preimages, other rules, unindexed necklaces, or a full historical priority survey.
