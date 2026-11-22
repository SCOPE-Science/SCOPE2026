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

# Verification

`checker.py` is standalone and uses only the Python standard library. Run `python3 checker.py` to enumerate all eligible adjacent coefficient pairs over tested complete blocks using Lucas's formula and finite-field inverses. On the delivered version it returned `CHECK_OK 57254`.

The comparison includes \(p=2\) through depth eight, \(p=3\) through depth five, \(p=5\) through depth four, \(p=7\) and \(p=11\) through depth three, and \(p=13\) through depth two. At all tested odd primes the independent quadratic-character ratio sum matches \(\chi_p(-1)/p\). The checker also tests Lucas's modular binomial computation against exact integer binomial coefficients. These checks are finite; the induction-free proof covers all primes and depths.

Scientific priority is based on the cited literature and available text. Broad older digital-distribution articles could contain an implicit evaluation; their full text was not available in this comparison. Independent mathematical review has not been performed.
