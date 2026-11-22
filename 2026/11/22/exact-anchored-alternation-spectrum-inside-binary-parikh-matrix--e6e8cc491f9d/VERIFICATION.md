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

## Checks and reproducibility

The proof is self-contained apart from the classical Hardy–Ramanujan partition asymptotic and the described earlier partition bijection. The full enumerator and mean identities follow from the unique gap representation; no finite script is used as a substitute for proof.

Run `python3 verify_direct.py` for direct word checks and `python3 verify_stable.py` for independent partition checks. `verification_output.txt` contains their actual terminal output. The direct check covers 42 compositions and 3,424 literal words. The partition check covers all area values from 0 through 35 inclusive. Larger values and the asymptotic estimates are justified symbolically, not by extrapolation.
