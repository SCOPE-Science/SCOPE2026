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

The theorem is proved analytically in RESULT.md. To replay the executable checks, run `python3 checker.py` from this directory. The script uses only the Python 3 standard library. During preparation it returned `PASS 48 exact rational assertions / numerical quadrature comparisons` and printed the exact numerators \((-3/4)+(21/2)s\) and \(s^2-(5/2)s+1\).

The exact tests compute rational coefficients, verify both example reversal frequencies, and check full polynomial coefficient rank for finite dimensions 2 through 10. A separate quadrature loop compares direct time-domain integrals against the rational formula at 21 pairs of parameters and frequencies. These diagnostics do not prove the arbitrary-dimension statement; the proof rests on the interlacing of strictly positive rational sums, the even-rational-function rigidity argument, and rank-nullity. No external validation has been performed, and historical novelty is subject to the literature-access limitations described in REVIEW.md.
