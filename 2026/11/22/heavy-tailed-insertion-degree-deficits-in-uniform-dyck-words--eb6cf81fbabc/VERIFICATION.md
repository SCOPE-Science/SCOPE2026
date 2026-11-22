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

# Reproduction and limits

Run `python3 check.py` with Python 3.8 or newer, with no external dependencies. The checker enumerates all Dyck words of semilength 1 through 8, constructs every result from one up-step and one down-step insertion and checks output distinctness, the exact source-wise component formula, fixed-remainder Catalan identity and aggregated deficit values. Independently it verifies coefficient identities by an integer recurrence for semilengths 1 through 150. The actual replay returned `VERIFY_OK`. These finite computations corroborate, but do not prove, the all-order result; that is established in the proof's Catalan generating-function and tightness arguments. The source-specific degree identity comes from Bernini et al. (2013), not from this verification. Independent external audit has not been performed.
