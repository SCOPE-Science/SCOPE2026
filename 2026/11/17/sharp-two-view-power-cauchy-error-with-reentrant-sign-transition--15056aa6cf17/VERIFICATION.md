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

# Reproduction

From the directory containing these files, run `python verify.py` with Python 3. No downloaded data, external libraries or remote services are needed. The checker performs 7,264 comparisons and prints `PASS`. It covers angular normalizations, global extrema for a sample of exponents, sign tests on the three strict intervals, and two elementary lower-bound test directions for random admissible weighted rules.

# Analytic checks

The infinite quantifiers rely on the proof rather than on samples. In particular, (i) a heaviest-node test yields \(\max F\ge1/2\); (ii) the longest empty projective gap yields \(\min F\le2^{-p/2}\); (iii) the orthogonal rule saturates both bounds by convexity; (iv) the arcsine third-order Lobatto identity and cubic Hermite remainder control the exact sign for all real exponents; and (v) degenerating rectangles realize the geometric supremum over convex bodies. Numerical experiments cannot establish uniqueness or the signs for untested real \(p\); these follow from the analytic arguments.

Historical priority remains contingent on literature completeness. No independent mathematical audit has been performed.
