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
# Checks and limits

The standalone verifier `verify_halfway_period.py` enumerates the lattice points independently of the residue-class closed form for 13 odd parameters (3 through 27) and dilations 0 through 93: 1,222 exact integer comparisons. It also checks the rational constituent polynomials against proper divisors of the proposed period in each tested case. The infinite proof is analytic: integer congruence counting plus parity and residue-0 period obstruction. No independent audit has been performed. The full family of all odd parameters has not been computationally enumerated, and is not claimed to have been.
