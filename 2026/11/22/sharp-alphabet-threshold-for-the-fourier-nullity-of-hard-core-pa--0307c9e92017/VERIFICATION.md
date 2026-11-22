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

The character-orthogonality reduction and integer-polynomial root-divisibility argument prove the result for all finite abelian groups, lengths, and admissible alphabet orders. The exact continuation check in `verify.py` enumerates every trivial/nontrivial frequency pattern through length 16 for several alphabet orders above the threshold. A separate check sums characters directly over admissible words for cyclic alphabets of orders 2, 3 and 4 at lengths 7, 6 and 5, respectively. The algebraic boundary example is also checked for seven consecutive values of its parameter.

Run `python3 verify.py` using a standard Python 3 installation. Direct complex evaluation has a tolerance of `1e-8` only in this independent finite check; the theorem proof and its all-pattern checks use exact integer arithmetic. Computation does not establish the infinite theorem and does not substitute for the argument in `RESULT.md`.
