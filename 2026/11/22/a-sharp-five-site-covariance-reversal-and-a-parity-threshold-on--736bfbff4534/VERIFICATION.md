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

# Verification record

The exact finite verifier `verify.py` is self-contained and needs Python 3.9 or later. Run it from the extracted package with `python3 verify.py`; it builds independent-set counting polynomials by direct subset enumeration, then computes each marked-pair covariance numerator as an integer polynomial. Its complete graph census covers exactly 1,099 labelled simple graphs on one to five vertices and all 10,650 unordered pairs; the output certifies exactly 60 labelled exceptions, all isomorphic to the five-vertex fan with the marked endpoints.

The executable additionally independently checks the closed covariance identity for fan path sizes \(4\le n\le11\). These finite tests **do not** establish an all-size theorem; the analytic proof uses the exact path recurrence and continuant identity, Descartes' rule, and characteristic-root bounds. The asymptotic threshold correction is obtained by expansion of an exact root equation, not numerical fitting. The raw program output is reproducible; no external packages, data files, random generators or hidden calculations are required.

Limits: only homogeneous positive activity, finite simple graphs and the designated endpoint pair are covered. No full graph-family covariance sign classification, arbitrary site-weight theorem, thermodynamic phase transition, or independent audit is asserted. Historical priority is not certified.
