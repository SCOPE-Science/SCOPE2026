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

# Reproduction and limits

The proof is in `RESULT.md`, based on active-cut decomposition and exact finite-field rank-one counts; it proves the theorem for all prime powers and every integer \(n\ge4\).

For a Python standard-library-only exhaustive small-case check, execute `python3 checker.py`. This enumerates upper triangular matrices over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\), including a nonprime field. It verifies the radius-four formula in the parameter instances declared in the source. For an independent exhaustive binary check through dimension six, run `cc -O2 -std=c11 checker.c -o checker && ./checker` using a C compiler supporting GCC/Clang's `__builtin_clz` intrinsic.

Observed Python run: `ALL_CHECKS_PASSED`, with sphere values \(s_2(4,4)=173\), \(s_3(4,4)=3526\), and \(s_2(5,4)=397\). Observed C run: `ALL_CHECKS_PASSED`, including \(s_2(6,4)=711\) from all \(2^{21}\) upper triangular binary matrices. Both checkers were executed from the included source contents. No numerical experiment establishes a theorem for infinitely many parameters: that conclusion uses the full combinatorial proof.

All inspections and calculations pertain to the stated rank definition; no external formal certification or independent mathematical audit has been performed.
