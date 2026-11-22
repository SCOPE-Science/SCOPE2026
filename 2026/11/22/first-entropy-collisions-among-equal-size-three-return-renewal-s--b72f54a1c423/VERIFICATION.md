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

Execute `python3 check_renewal.py` from this package. It requires Python 3 and the standard library only. The check constructs every unordered three-petal length multiset at the specified graph order, rejects the prohibited repeated length-one loop, computes each Perron polynomial over exact rationals, and applies exact Euclidean gcd plus Sturm sign variations at 1 and positive infinity. Assertions force the two unique first collision pairs, and also verify their exact shared cubic factors. This establishes the finite classification through the stated boundaries, not at larger graph orders. Separately, the closed-walk return decomposition gives the zeta and entropy formulas in RESULT.md. No external checker or independent mathematical audit is claimed.
