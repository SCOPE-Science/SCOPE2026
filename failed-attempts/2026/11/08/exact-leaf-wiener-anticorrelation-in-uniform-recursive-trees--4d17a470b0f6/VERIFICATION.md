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

For a uniform parent U in T_m, put J=1 when U is a rooted leaf and S equal to its transmission. Then the increments of L and W are 1-J and m+S. In the update of Q, the average increase of old-leaf transmissions contributes Q_m/m+L_m, removal contributes -(Q_m+L_m)/m, and the new leaf contributes m+2W_m/m. Since E L_m=m/2 for m>=2 and Q_2=W_2=1, E(Q-W) telescopes to (m-1)(m-2)/4. The conditional covariance of the increments is -Q_m/m+2L_m W_m/m^2. Adding the covariance of the conditional means gives C_{m+1}=(m+1)C_m/m+E(W_m-Q_m)/m. Division by m+1 yields the stated harmonic formula via the summand 1+2/m-6/(m+1). It includes the zero cases n=2,3 and every n>=4 contributes a strictly negative term. The leaf-variance recurrence v_{m+1}=(1-2/m)v_m+1/4, starting at m=2, gives v_n=n/12 for n>=3. Neininger's variance constant for unordered-pair W supplies exactly the stated correlation coefficient.

## originality

FAIL

Two earlier distinct Resultary findings contain the same exact covariance and transmission excess under the same uniform-parent, rooted-leaf, unordered-pair conventions. The sign, leading order, and correlation refinement are immediate consequences of those identities and established marginal variances. This is demonstrated coverage, not a failure of external retrieval or a claim about scholarly-publication priority.

## value

FAIL

The mixed statistic is a natural local–global dependence measure and the underlying exact result is useful. This submission adds no distinct mathematical invariant to the two earlier exact treatments; sign, aggregate comparison, and correlation normalization are routine consequences, not a surviving new result for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
