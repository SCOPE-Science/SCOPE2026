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

The accompanying `verify_four_run.py` is standalone standard-library Python 3. Execute `python3 verify_four_run.py`; no external files or packages are required. The checker constructs all substring intervals and directly tests the closed-border definition, then removes intervals admitting a closed one-symbol extension. For each of 17,484 four-run test configurations it compares the resulting complete interval set with the separate explicit classification and its count. A second coefficient check enumerates all four-run words over 2-, 3-, 4- and 5-symbol alphabets through length 14 and compares every coefficient of the formal generating function; it separately checks normalization to the unweighted four-run count. Both checks passed in the reviewed run.

The all-alphabet and all-length assertion follows from the proof's exact border classification and formal power-series identities, not from finite extrapolation. The finite checks do not independently certify the symbolic argument. No independent mathematical audit was conducted. Relevant historical priority is not fully determined.
