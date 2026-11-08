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

The standalone exact-integer `ns3_verify.py` was executed and returned `VERIFY_OK`, covering all 5044 primes congruent to 1 modulo 6 below 106000 and listing precisely the 28 exceptional primes, last 1399. For selected fields it independently checks the cubic-residue and quadratic-nonresidue conditions by Euler's criterion. It also checks the analytic threshold using a floating-point assertion only as a secondary sanity check; the actual proof of positivity relies on the displayed strict integer-square inequality. This code does not prove the Weil bound or replace a proof for arbitrarily large primes. No independent mathematical audit has occurred.
