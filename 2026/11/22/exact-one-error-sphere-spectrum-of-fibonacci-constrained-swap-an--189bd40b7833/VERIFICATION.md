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

# Reproducibility

Run `python verify.py` with Python 3 in the directory of the other files. No external modules or datasets are needed.

The executable enumerates every linear `11`-free binary word of lengths 1 through 20 and counts its distinct `11`-free outputs under each possible single replacement and adjacent unequal-bit swap. It compares this output count with the proposed local `101` count. A separate finite-state recurrence tracks the last two input bits and occurrences of `101`, giving an independent way to count the distribution through length 100. The closed binomial formula, degree-support claim, extremizer multiplicities and first-moment identity against the known exact edge count are checked through length 100.

The proof in `RESULT.md` is the basis for the all-length statements; no finite enumeration is asserted to certify infinitely many inputs. The asymptotic mean/variance follow from the rational generating function and simple dominant-root analysis rather than numeric extrapolation. There is no independent external audit or machine proof certificate.
