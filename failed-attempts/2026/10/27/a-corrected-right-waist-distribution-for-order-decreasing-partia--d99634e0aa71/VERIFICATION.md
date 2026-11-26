---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Let m=n−k. Fixing the unique input mapped to k gives m+1 choices. On inputs 1 through k−1 the rank-r recurrence is a(t,r)=a(t−1,r)+(t−r+1)a(t−1,r−1), with a(0,0)=1; hence a(t,r)=S(t+1,t+1−r). The remaining m inputs may use any s of the k−1−r unused image labels, with precisely binom(m,s)(k−1−r) falling s choices. These steps give a reversible count including k=1 and k=n; the empty map supplies waist zero. At k=3 this is (m+1)(m²+4m+5), whose excess over 5 binom(n,3) is binom(n−2,3). Independent direct enumeration through n=5, using an omit-or-assign recursion with unused y≤x, gave rows (1,1), (1,2,2), (1,3,6,5), (1,4,12,20,15), (1,5,20,51,74,52); thus the first failure is at n=5 and the least failing k there is 3. Umar's printed p. 121 states precisely the contradicted positive-waist conjecture. The uploaded script was inspected, not run. The all-size result is analytical, not certified by the finite rows.

## originality

FAIL

The exact corrected distribution, including each rank-refined waist count, is a direct specialization and subtraction of the classical factorial rook factorization for Ferrers boards. This is stronger coverage of the mathematical claim, not an assertion that Umar or the textbook explicitly wrote down the discrepancy. The correction is true, but the claim as submitted does not clear the stated originality standard.

## value

PASS

An explicit documented correction to a published conjecture about the same semigroup and statistic is useful to readers of that literature. The first failure and the all-size waist-three error diagnose the incorrect formula rather than just supplying an unexplained small table. This value attaches to the correction, not to the known Ferrers counting mechanism as a new technique.

The dated certificate retains the supplied scientific assessment, sources and limitations.
