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

Exact \(n\ge4\) covariance and binomial-moment claims are proved by deleting two prescribed leaves and applying the Prüfer correspondence. The second-factorial-moment enumeration has an \(n=4\) special case; its general formula starts at \(n=5\). The all-size sign follows from a monotone real-variable function, not finite extrapolation. Expanding the exact moments proves the limiting correlation without claiming a bivariate CLT.

Reproduce finite checks with `python3 check.py` using Python 3.9+ and only the standard library. The source enumerates the entire Prüfer space for each \(n=4,5,6,7,8\), compares five exact rational moments, all admissible exact binomial moments, and positivity for \(9\le n\le350\). Expected terminal output: `VERIFY_OK 1076`. The checker does not constitute a formal proof for arbitrary \(n\).

The underlying probability distribution, originality relative to implicit pattern enumerators, and all analytic steps have not been independently reviewed.
