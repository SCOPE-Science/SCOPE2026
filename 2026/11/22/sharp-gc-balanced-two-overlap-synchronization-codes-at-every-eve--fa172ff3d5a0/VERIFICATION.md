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

Run `python3 verify.py` in the extracted package. The script enumerates exactly 280 four-letter boundary assignments and verifies the upper integer coefficient profile \((20,36,36)\), the twelve attaining templates and the construction's profile \((0,8,20,8,0)\). It checks all even lengths from four to twenty-six by exact arithmetic and compares the coefficient formulas with independently constructed actual word sets at lengths four and six.

The infinite-length conclusion does not follow from finite word enumeration. It follows from the stated three boundary coefficient inequalities, the binomial ratios, and the analytic inequality \(0\le r_2\le r_1<1\). The 280-case certificate is exhaustive because all combinations of two disjoint first/last symbol sets and every assignment of their shared two-letter pairs are considered. The package requires only the Python 3 standard library; no network data or external solver is necessary to replay it.

No external or independent mathematical audit has been performed. Literature priority remains subject to further primary-source access and independent comparison.
