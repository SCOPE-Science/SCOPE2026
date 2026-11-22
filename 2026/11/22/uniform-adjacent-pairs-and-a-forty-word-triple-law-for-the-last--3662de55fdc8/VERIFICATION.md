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

# Verification record

Invoke `python3 verify.py` (Python standard library only) alongside the other delivered files. Exact verified facts: each of 64 states has five incoming transitions; all 4-step transition counts lie in the integer range 4 to 16; each 4-step row totals 625; the 64 possible triples have multiplicity histogram 12 times 16, four times eight, 24 times four, and 24 times zero in the total of 320 state-digit cases; each of 16 pairs has multiplicity 20 out of 320.

A separate full-integer factorial computation agreed at indices 0 through 500, and the derived state triple prediction agreed for every index from 10 through 59,997 (59,988 triples). This certificate checks finite algebra and arithmetic; the recurrence, 4-step positivity, Doeblin contraction and base-five interval decomposition together justify the claimed infinite frequencies. The supplied script does not certify absence from all published literature. Independent audit has not been performed.
