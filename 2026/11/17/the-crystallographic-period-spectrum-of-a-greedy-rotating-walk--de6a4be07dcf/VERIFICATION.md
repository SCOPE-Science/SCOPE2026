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

Execute `python3 verify.py` from this directory using Python 3.9 or later. This requires only the Python standard library. The script creates the complete five-line rational arrangement in the unit square, confirms its 10 face, 19 edge and 10 vertex strata, and exhaustively follows the greedy return graph for every integer offset in the two analytically justified rectangles. It prints the stratum period-set histograms and four explicit witnesses, then `EXHAUSTIVE_RATIONAL_STRATA_CERTIFICATE_OK`.

The analytic trapping argument in `RESULT.md` proves that the finite rectangles overcover every eventual phase-zero state of every infinite orbit. No random testing is used for a universal conclusion. The exact checker does not address rational denominators other than three and six; the other three cases have an elementary coordinate proof. The mathematical and publication-priority conclusions have not received independent audit.
