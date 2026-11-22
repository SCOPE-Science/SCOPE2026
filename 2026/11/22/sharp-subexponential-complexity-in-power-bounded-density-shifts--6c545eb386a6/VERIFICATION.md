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

# Verification notes

The complete all-length argument is in `RESULT.md`. The critical nonstandard step is the three-range local-window bound for the separated-marker family. The upper comparison counts unrestricted words and is used only as an upper bound; the lower family satisfies **all** local constraints, including windows crossing cell boundaries and the zero-padded endpoints.

Run `python3 check.py` from the extracted package. The recorded run printed `PASS: 468 finite combinatorial cases; exact integer powers used`. Tested rational exponents were \(1/2\), \(2/3\), and \(3/4\); the constructed large-cell examples used the first two. Numeric experiments do not prove the asymptotic for arbitrary real parameters. No independent audit or external validation was conducted.

Historical-priority material is limited by lack of access to the original full text of Stanley's 2013 article, as separately recorded in the scientific review.
