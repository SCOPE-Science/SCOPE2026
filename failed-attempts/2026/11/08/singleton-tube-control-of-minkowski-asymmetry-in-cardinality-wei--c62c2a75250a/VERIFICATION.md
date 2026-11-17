---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS: Weighted simplex lower and upper tube supports L_s=Σ_{j<=s}(s-j+1)w_j and M_s=T-L_(n-s) imply centered margins D_s=Σ_{j=2}^{n-1} min(s,j-1)w_j+s*w_n/n and U_s=Σ min(n-s,j-1)w_j+(n-s)w_n/n. With all weights positive, singleton D_1 minimal and U_1 maximal, strictly for other tube sizes. Summed singleton reflection inequalities force unique uniform center; formula is their ratio. Independent exact rational n=3..7 support calculations agree. No infinite weight claim is inferred from finite enumeration.

## originality

FAIL

FAIL: The earlier stronger primary published mathematical finding covers the claimed exact theorem and all substantive consequences. The current extra strictness for positive w_n, and the open weight-image range, are algebraic corollaries of the prior exact formula, not a surviving independent scientific result. O fails decisively despite correctness.

## value

FAIL

FAIL: The all-weight Minkowski asymmetry formula and unique uniform center were already published on 2026-10-18 for nonnegative cyclic length-homogeneous simplex sums, a stronger domain. The purported sharp range (1,n-1) is an immediate weighted-mean and continuity consequence; strict binding singleton facets follow from the same prior support function. No separately motivated new invariant or classification survives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
