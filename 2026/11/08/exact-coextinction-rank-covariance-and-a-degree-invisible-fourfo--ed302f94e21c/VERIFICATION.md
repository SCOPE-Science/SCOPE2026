---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For nonempty primary neighbor sets A,B, represent uniformly random removal order by continuous iid priorities. With union size u and d=n-u outside vertices, decompose T_A=J_A+sum X_z and T_B=J_B+sum Y_z; restricted-order covariance C0=-((a-c)(b-c))/((a+1)(b+1)) and maxima covariance C_M=c/((a+1)(b+1)(u+2)). Conditional covariance for outside indicators gives exact formula (n+1)/((a+1)(b+1))*(c*(n-u)/(u+2)-(a-c)*(b-c)/(u+1)). Diagonal and disjoint boundaries checked. Robustness R=sum T_Ai/(m(n+1)) makes variance pairwise sum. Independent exhaustive primary-permutation enumeration for ALL nonempty ordered (A,B) at n=2..6 (9,49,225,961,3969 pairs) matched exact rational formula; both four-primary two-regular graphs enumerated over 24 removal orders: 1/1800 versus 1/450, means 2/3. Finite tests support, but universal proof is priority-order conditioning.

## originality

PASS

Earlier extinction robustness work establishes degree-only mean and discusses variance/distributions, and fixed-horizon covariance-sign papers address survival counts after a specified number of removals. The submitted covariance of both final-neighbor removal ranks is a joint integrated-time statistic dependent on intersection c, with an exact negative/positive sign boundary and degree-matched variance separation; none of the examined published results explicitly supplies its rational formula.

## value

PASS

The pairwise signed rank covariance solves a natural previously open second-moment question for randomly ordered primary extinctions. The fourfold variance gap between degree-identical networks proves ecological robustness uncertainty is structurally non-degree-determined even when mean is; this is a motivated exact structural counterexample, not only raw numerical enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
