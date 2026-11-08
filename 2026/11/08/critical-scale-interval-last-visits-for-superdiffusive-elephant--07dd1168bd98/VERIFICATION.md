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

# Verification scope

Run `python3 verify.py` using Python 3 and NumPy. The program checks finite-state transition and martingale identities by exact rational arithmetic, verifies finite-horizon interval entrance by two exactly equivalent algorithms (dynamic programming and full path enumeration for small cases), and compares simulated Brownian suprema and swept-interval widths with theoretical identities. The run prints its assertion count, constants and diagnostic outcomes.

The closed-form asymptotic is established analytically in `RESULT.md` conditional on the cited LLT and FCLT. Finite tests and numerical samples do not establish limits at arbitrary \(n\), and the source preprints' lemmas are not independently validated here. No third-party paper is embedded. Independent mathematical review has not been performed.
