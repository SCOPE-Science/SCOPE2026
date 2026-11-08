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

Execute `python3 verify.py` in the same extracted directory. `verification_output.txt` contains exact deterministic output of the verifier. It checks every state in five finite cases using an independent direct orbit walk and constructs the cyclotomic polynomial by exact polynomial division. The total number of states in these cases is 932,979. The tests do not certify the proof for all primes or all moduli. The analytic argument uses integral quotient rings, Smith normal forms, cyclotomic identities, and inclusion-exclusion. No independent audit is claimed.
