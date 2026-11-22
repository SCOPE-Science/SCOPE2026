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

Run `python3 CHECK.py` from the directory containing this file and the script. It uses only the Python standard library and computes the uncolored power-partition values independently using their exact coefficient recurrence, modulo a sufficiently large power of two. It verifies divisibility and normalized parity across 500 parameter/target cases: ten even bases 2 through 20 and depths up to 11, with forty exact valuation witnesses at the all-ones index.

The universal claim is proved in RESULT.md using formal coefficient extraction, an integral polynomial summation operator and a Bernoulli denominator bound. Neither finite tests nor logarithmic output are treated as proofs for arbitrary base and depth. Independent mathematical audit is not yet performed; future independent comparison with alternative formulations in older congruence literature is appropriate.
