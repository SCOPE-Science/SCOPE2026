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

# Reproduction of finite exhaustive theorem

Run `python3 verify.py` with Python 3.9 or later. The script uses only the standard library and no external graph census or dependency. Compare its stdout byte-for-byte with `verification_output.txt`; the final line must be `ALL_TESTS_PASS`.

The generation enumerates unlabelled trees from one vertex to ten vertices by attaching each new leaf to every vertex of every smaller tree. Isomorphism is eliminated with a canonical parenthesis encoding obtained by recursively encoding *every* possible rooted view of a tree, sorting child encodings and taking the minimum. This is an exact canonical invariant, so it cannot merge nonisomorphic trees. Every nontrivial tree is obtained by leaf attachment because it has a leaf; consequently the generation is exhaustive at every order.

Independent-set masks are exhaustively enumerated to obtain the two numerical statistics \(I,D\). The unique ten-vertex collision is verified to have \(I=160\), \(D=8649\), hence \(t_1=160\), \(t_2=34249\). Its distinct third-arity statistic is obtained from \(J\) and independently checked by an eight-state tree recurrence with three internal graph patterns for each witness. No randomized or floating-point calculations appear. `census_10.csv` contains the 106 complete ten-vertex representatives and their actual invariant counts.

The universal Henson graph existence/equivalence argument is a mathematical proof in `RESULT.md`, not a finite experimental assertion. The numerical uniqueness is limited to all trees on at most ten vertices. This package supplies no independent expert audit and no certification of priority beyond the documented literature comparisons.
