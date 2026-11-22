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

# Reproducibility and limits

Run `python3 verify.py` beside `RESULT.md`. The script uses exact integer arithmetic and Python `Fraction`, requiring no external libraries. It directly compares the floor-GCD indicator and the residue model for 693 parameter combinations at 219 indices, checks a predicted period shift, and in 95 instances computes every index in a complete predicted period to verify exact least period and totient density. The documented output is `PRIME_SQUARE_FLOOR_COPRIMALITY_OK 693 FULL_PERIOD_DENSITIES 95`.

These finite checks do not establish any infinite universal statement. The proof rests on invertibility modulo the index, CRT prime witnesses, a degree-\(k\) binomial first derivative and an exact small-divisor calculation. Inaccessible unindexed equivalent mathematical literature remains a bibliographic risk. Independent mathematical validation has not been performed.
