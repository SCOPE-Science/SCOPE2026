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

# Reproduction and boundaries

Execute `python3 check_psk7.py` using Python 3. The script requires only standard-library integer/rational arithmetic. It enumerates all \(q^5\) normalized exponent arrays separately for each integer \(q\) from 2 through 7, with totals 32, 243, 1024, 3125, 7776, and 16807.

The exact energy profile sums 91 ordered pairs for each array, and the cosine values are enclosed with outward rational bounds using Machin's arctangent identity and an explicit Taylor remainder. A winner profile is compared against *every* nonmatching profile using disjoint intervals; all matching winners are counted. The expected final output line is `SEVEN_PSK_EXACT_ENUMERATION_PASS`. This verifies finite-alphabet global optimality; it does not evaluate or certify the continuous-phase problem, nor other lengths or alphabets above seven.

Independent mathematical audit: not performed.
