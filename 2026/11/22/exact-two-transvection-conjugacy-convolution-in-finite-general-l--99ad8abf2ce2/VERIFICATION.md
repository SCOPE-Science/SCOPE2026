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

Run `python check_transvections.py` using a standard Python 3 interpreter. The first checker independently implements finite fields, direct finite-rank matrix arithmetic and classification of the product of a fixed canonical transvection with **every** nonidentity transvection in fifteen finite instances. Its output is `CHECK_OUTPUT.txt` and all fifteen cases passed. It tests each row numerator, every nonzero trace parameter and total normalization. Separately run `python check_target_fibers.py`; it enumerates **both** transvections in five finite cases, testing all prescribed product targets and class-uniformity. Its output is `TARGET_CHECK_OUTPUT.txt` and all five cases passed. These computations are finite and are not a proof of the general formula.

The mathematical proof uses linear-algebraic counts rather than computational extrapolation, including all boundary dimensions and prime-power fields. The prescribed-target formula depends on classical general-linear centralizer cardinalities stated in the result. Historical priority and independent mathematical verification have not been established. The first exact-day archival anchor used is the 2009-04-14 arXiv submission of Adan-Bante–Harris; the earlier 1992 Hildebrand article is explicitly credited but supplies a month rather than an exact public date in the available record.
