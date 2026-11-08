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

# Reproduction of finite checks

Run `python3 verify_mixed_energy.py` in a directory containing that file. The verifier tabulates differences directly from \(H_\lambda(N)\) and \(H_\mu(N)\), with no invocation of the proof's root-count or Hensel formulas. It checks odd prime powers at multiple unit parameter pairs, including \(\lambda=\mu\), parameters distinct modulo \(p\) in both square classes, and parameters congruent modulo positive powers. It also directly checks CRT products at odd composite moduli. It raises an exception on the first discrepancy and prints `VERIFY_OK` only after all specified comparisons succeed.

The proof's singular-count identity is additionally verified by direct enumeration for small prime powers, by comparing the number of \((A,B)\) with both entries divisible by \(p\) and prescribed product to the stated formula. None of these finite tests establishes the general theorem independently; the mathematical argument is in `RESULT.md`. No external audit is represented.
