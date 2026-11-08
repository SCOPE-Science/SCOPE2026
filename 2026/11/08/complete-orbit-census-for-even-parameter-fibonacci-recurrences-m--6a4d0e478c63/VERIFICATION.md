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

# Verification and boundaries

A direct proof of the infinite formula is given in `RESULT.md`. The crucial symbolic equalities are \(A^2=KA+I\), \(A^4-I=4uA(I+uA)\), and \(\det(I+uA)=1+u^2\) with \(u=K/2\) odd. The last determinant has exact two-adic valuation one. Repeated squaring establishes the exact invariant-factor valuations for every exponent, which are then transformed into modular fixed-point counts. The total cycle count is obtained by exact divisibility and summation, not numerical extrapolation.

The checker `verify_cycles.py` is self-contained and uses Python integer arithmetic. It checks the Smith valuations via gcd-of-entries and determinant, and separately traverses each state of each complete finite permutation. Execute `python3 verify_cycles.py` in a directory containing the file, and compare its output with `checker_output.txt`.

Check range: \(K\in\{2,6,10,14,18,22\}\), \(1\le r\le7\), \(0\le j\le8\) for matrix valuations. This gives 42 complete state-space enumerations and 54 integer-matrix tests. Not checked by finite experiment: unbounded \(r\), all odd \(u\), or the absence of a publication in an unindexed venue. Independent audit is not performed.
