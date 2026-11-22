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

The exact root counts are derived in `RESULT.md` by a closed matrix-path formula, a finite-support classification that is valid for every exponent, and a linear-functional fiber count. The independent checker `check_power_fibers.py` is self-contained Python 3. Executing `python check_power_fibers.py` yields the recorded checks in `checker_output.txt`. It enumerates all matrices for \((m,q)=(2,2),(2,3),(2,4),(3,2),(3,3),(4,2)\), and enumerates all relevant first and second superdiagonals for \((3,4),(4,3),(5,2),(6,2),(7,2)\), multiplying matrices directly over prime fields and \(\mathbb F_4\). It checks *every* target in the three-dimensional image, not sample targets. The checker also independently enumerates zero-support patterns for six exponents.

These finite tests are finite sanity checks, not a proof of all parameters. The proof in `RESULT.md` treats the infinite parameter family. The sole group translation requires the binomial identity at characteristic-power exponents. Independent validation has not been performed.
