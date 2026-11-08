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

The symbolic proof in `RESULT.md` establishes the result for all parameter values in its exact domain. Reproduce the separately implemented finite checks with `python3 artifacts/check.py`; its saved stdout is `artifacts/check_output.txt`. The checker tests the gap, Frobenius and entire pseudo-Frobenius spectra against a shortest-path Apéry computation for every odd base from 5 through 151 and all permitted widths, and checks selected examples by direct reachability from the original interval generators. No computational enumeration is asserted to certify infinitely many cases.
