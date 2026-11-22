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

Execute `python3 verify_exhaustive.py` and `python3 verify_independent.py` from this directory with Python 3. Both require only the standard library. Their recorded outputs appear in `exhaustive_output.txt` and `independent_output.txt`. The exhaustive checker maps every ternary word of lengths zero through ten, independently generates every candidate output, and checks fixed Parikh counts. The second checker uses a debt-counter dynamic program unrelated to the recursive hare implementation, compares the binomial formula for every length zero through 39, and tests the rational generating-function recurrence.

The infinite-language identity, nonregularity, sharp saturation, rational formal series and exponential asymptotic are established in `RESULT.md`; finite verification is not offered as a proof for infinite length. Historical priority and external validation have not been independently certified.
