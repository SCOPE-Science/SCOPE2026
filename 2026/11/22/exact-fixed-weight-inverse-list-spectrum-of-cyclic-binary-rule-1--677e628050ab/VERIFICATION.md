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

The included `CHECK.py` program needs only Python 3. Run `python CHECK.py` to recompute complete fixed-weight inverse-fiber histograms by independent direct enumeration for every length \(1\le n\le18\) and every weight \(0\le w\le n\). This covers 189 parameter slices and 524286 binary inputs, including small-ring repeated-neighbor conventions. Separately it runs exact integer coefficient and boundary checks through \(n=240\).

All-length validity rests on the four-element kernel classification, the pair/triple/quadruple anchored counts and binomial-moment inversion in `RESULT.md`. Exhaustive finite tests do not certify the infinite statement. No independent mathematical audit has been performed.
