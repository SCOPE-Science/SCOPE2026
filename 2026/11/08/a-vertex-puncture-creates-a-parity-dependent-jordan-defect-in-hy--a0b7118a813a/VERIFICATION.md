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

The complete proof in `RESULT.md` establishes the Jordan forms and sharp first-entry counts over every finite characteristic-two field. The essential algebraic checks are the two identities \(A^2=dI\) and \(B^2=dI+bb^{\mathsf T}\), the full-cube square-zero ranks, the even-dimensional rank argument and the odd-dimensional invariant-space decomposition. None of these is inferred solely from finite enumeration.

`check_jordan.py` directly calculates binary adjacency matrices, matrix products, ranks, and parity-specific polynomial identities for dimensions 2 through 8, reporting the Jordan signatures. Its captured output is `check_jordan.out`.

`check_orbits.py` independently enumerates every initial state on punctured cubes in the five cases \((d,q)=(2,2),(3,2),(4,2),(2,4),(3,4)\), checks the exact entry times and periodic populations, and reports the results in `check_orbits.out`. Its finite-field representation uses a polynomial-basis label so addition is bitwise XOR; only addition occurs in the update.

Limits: ranks of finitely many test matrices do not establish arbitrary dimension; state enumeration is exhaustive only for the named cases; these scripts do not assess whether a theorem has appeared in unindexed literature. Independent audit has not been performed.
