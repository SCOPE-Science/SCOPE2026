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

Use `python3 verify.py` with a standard Python 3 interpreter; no third-party packages are needed. The checker reconstructs the complete labelled wheel and independently simulates each possible leak using the ordinary unique-white-neighbor rule for every initial subset for rim lengths 4 through 11. It checks the two-window characterization, coefficient counts from an independently implemented truncated transfer walk, and the inclusion-minimal count formula. It also compares transfer counts with cyclic-word enumeration through rim length 16.

Observed successful messages included `W_4: brute forcing / transfer / minimal OK`, `W_11: brute forcing / transfer / minimal OK`, `TRANSFER_EXTENDED_OK`, and `WHEEL_ONE_LEAK_VERIFY_OK`. The proof for all integer lengths is symbolic, relying on the first-force analysis, the cycle lemma and the closed-walk trace bijection, not on finite experimental extrapolation.

The independent audit has not been performed. Literature-priority verification is necessarily provisional.
