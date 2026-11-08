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

# Reproducibility and verification

Run `python3 verify_parking.py` with Python 3 standard library. The code constructs independent exact first-dimer recurrences, evaluates the three analytic moment formulas with rational Taylor polynomials, and enumerates every possible edge-priority ordering through nine sites, which is equivalent to the terminal discrete parking law. Its fresh execution passed 523 exact assertions. It also checks all finite signs through one hundred sites and the exact remainder threshold \(R_{11}<1/6\).

The printed finite sign checks do not establish negativity beyond the tested range; that is proved in `RESULT.md` using the explicit decreasing analytic bound and \(e<3\). The limiting constant follows from analytically controlled Taylor remainders. Independent external mathematical audit or certification has not been performed.
