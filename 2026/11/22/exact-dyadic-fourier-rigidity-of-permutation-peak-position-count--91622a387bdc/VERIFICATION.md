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

# Reproducible checks and their limits

Run `python3 verify_peak.py` with Python 3.10+ and the standard library only. The source file is included in the same package. The performed run printed `PASS 12442 exact checks` and no exception.

The script compares the entire integer Walsh transform, obtained through exact descent-set counting by inclusion-exclusion, with the exact rational expansion of joint peak events derived from tangent coefficients. It checks all subsets of \(\{2,\ldots,n-1\}\) for \(1\le n\le13\); it directly enumerates all permutations at \(1\le n\le8\). It verifies the claimed common valuation, spectrum gcd, and peak-free count over those finite ranges.

The checks support the implementation and boundary cases. They are not a proof for arbitrary \(n\); the proof for all dimensions is the alternating-block factorization and odd-denominator recurrence in RESULT.md. No independent audit has been performed.
