---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

On im(t), t is an involution by t^3=t, so every other point is one step from a fixed point or two-cycle. The law et=e makes e constant on each t-component, te=e puts each target at a t-fixed vertex, and e^2=e makes that target its own image. Thus a fiber of e is precisely a distinguished rooted star and a multiset of other stars and two-cycle components; fibers themselves form an unordered multiset. For size j>=2, the unordered leaf-count pairs with sum j-2 yield floor(j/2) two-cycle types. Excluding every such type is exactly the t=t^2 condition; hence the subtraction of Euler transforms counts all and only the rank-three compatible-pair orbits. There is no t^2=e cancellation when t!=t^2, since then te=t^3=t would force e=t. The formal logarithmic derivative gives both divisor recurrences. The cited classification and essentiality apply in the claimed n>=5 generator regime; small-index coefficients have the compatible-pair interpretation.

## originality

FAIL

A distinct indexed result, Plane partitions and exact generator ranks for endomorphism monoids of full transformation semigroups (05f93685b217), demonstrably covers the entire rank-three contribution, giving exactly the same nested Euler product and the same fiber decomposition within a stronger enumeration. This is a coverage decision for this independent review, not a claim that the other record predates the frozen work or that it derived the formula independently. Its catalogue date is later and the relation between the derivations is not established.

## value

PASS

On mathematical substance the general rank-three orbit count solves an explicitly posed part of the minimal-generator enumeration and the structural bijection explains what the products count. It is not merely finite table recomputation. The duplication as a standalone result is accounted for under originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
