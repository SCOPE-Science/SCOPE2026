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
# Reproducibility and verification

Run `python verify_fibers.py` and `python verify_literal.py` using an ordinary Python 3 interpreter. Both are standalone and require only the Python standard library. The first enumerates all rank-one square-zero factors using a unique normalized image-line representative and compares bracket fibers, matrix ranks, spectral restrictions, and total mass. It implements \(\mathbb F_4\) explicitly as \(\mathbb F_2[a]/(a^2+a+1)\). Its exhaustive all-target cases are \((n,q)=(2,2),(2,3),(2,4),(2,5),(2,7),(3,2),(3,3),(3,4),(4,2)\). For \((n,q)=(3,5)\), all attained targets and the total mass are checked, but not all unattained matrix targets.

The second program independently enumerates literal matrices and forms commutators through ordinary matrix products for prime-field cases \((2,3),(2,5),(3,2),(3,3),(4,2)\), then compares all obtained fiber sizes. Outputs are recorded in `checks.txt`. These reproducible finite checks are not an infinite proof; the mathematical proof appears in RESULT.md.

Independent audit was not performed. No external validation certificate is asserted.
