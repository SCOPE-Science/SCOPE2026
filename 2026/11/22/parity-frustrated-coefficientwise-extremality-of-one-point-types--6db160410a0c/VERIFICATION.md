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

Execute `python3 check.py` in a directory containing the supplied script and `verification_output.txt`. The script requires only the Python standard library and prints `VERIFY_OK` followed by the recorded counters and extrema; its output matches the included log.

The checker tests 502 orientations using direct ternary-state enumeration, 4,080 orientations using independent support-defect and transfer enumerators, all polynomial coefficient inequalities, exact cubic defect values, cyclic parity and equality-class counts, and explicit direct extremes for orders nine through eleven. The finite checks do not prove the universal claim: the proof of the support decomposition, cyclic parity, cubic count and matrix identities is in `RESULT.md`. Exact asymptotic rates are derived from explicit characteristic polynomials and the primitive/positive matrix Perron theorem, not from numerical extrapolation.

Independent mathematical audit has not been performed. Historical originality remains provisional, subject to wider literature review.
