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

The self-contained standard-library script `checker.py` can be run with `python3 checker.py` from the extracted files. It passed 1192 assertions on the exact rational parameters, normalization identity, equality of the two global peaks, finite candidate threshold at \(\theta=1/5\), inequalities for the successive ratios and parameter-side diagnostics. Rational arithmetic is exact where claimed.

The infinite tail is proved by the sign of \(b(k+2)(9-k)-1\) for **all** \(k\ge6\), rather than by testing finitely many indices. The asymptotic constants come from an analytic minimizer argument with both boundary regimes excluded, not a finite numerical scan. The checker is evidence for implementation integrity and numerical consistency, not independent proof of unbounded quantifiers, asymptotic uniformity or priority.

The completed review is same-model only. No external mathematical audit, publication or historical-priority certification is claimed.
