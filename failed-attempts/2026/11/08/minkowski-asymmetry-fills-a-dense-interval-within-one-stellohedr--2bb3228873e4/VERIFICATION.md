---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Using published sharp subset inequalities x_i>=1, x(I)<=U_|I| for the generalized parking-function polytope, the reflected-inclusion condition gives y_i>=S_n+lambda and sum y_i<=lambda U_n+n; thus lambda T>=n(S_n-1). The uniform center with s=n(S_n-1)/T satisfies all subset constraints because top-k averages of strictly increasing S_j-1 dominate the global average. Equality of coordinate and full-sum constraints forces uniqueness. Explicit b(h) sequences yield the dense (1,n) interval in the fixed b_1>=2 stellohedron type and cube/simplex limits. Local exact rational checks corroborate these algebraic inequalities. The proof is mathematically sound.

## originality

FAIL

Earlier October 11 polymatroid independence-polytope Minkowski-center theorem covers the same principal result by a nontrivial but direct specialization. After translation x_i -> x_i-1, use f(I)=sum of largest |I| values among S_j-1 (a normalized monotone submodular function). Its singleton capacity is B=S_n-1 and f([n])=T. The earlier all-subset density formula has maximum at full set and yields s=nB/T; full-set density tightness implies unique center, translated to exactly the submitted one. The remaining dense interval is a routine substitution in that formula together with earlier Bayer combinatorial-type theorem; no independent original theorem remains.

## value

FAIL

A general structural asymmetry theorem already yields the complete exact parameter formula and uniqueness, while the dense range is an elementary one-dimensional rational-parameter interpolation between limiting cube and simplex. Without a new mechanism or independently useful invariant beyond the prior specialization, the final claim is a covered application rather than a novel, motivated mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
