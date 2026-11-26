---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

PASS applies to the repaired maximum-realized-count theorem, not to the frozen statement that one structure realizes every possible atomic type. With q=s=1 and two parameters a<b, the interior type S(a,x)∧S(x,b) is possible in a<x<b, but cannot coexist with any generic interior type, because double adjacency forces an interior gap of size one. Both are possible even with S(a,b) false. The corrected RESULT and slogan explicitly distinguish attaining a sharp cardinality from realizing a union of possible types. Verified the bound by disjoint contributions: m equality types, at most (m+1)^q generic gap vectors, and at most 2sm distinct nonparameter vertices occupying named successor slots. Exact successors can cause multiple slots to share one vertex but not increase this bound. To attain it, assign one generic point per vector and a distinct marker per slot; in each order place the parameters as prescribed, place its own markers next to them, and keep all unrelated markers in a gap away from any designated parameter adjacency. The resulting marker types differ by unique slots and all generic types differ by gap vector. The m=0 case takes one point, and any extremizer needs at least M elements. For one order, both exterior gaps need at least two unmarked positions and each interior gap at least three; this is necessary and sufficient to attain the three separate bounds, including distinct slot witnesses. The marked subset is determined by the gap vector, and subtracting the minimum lengths gives the binomial numerator, zero for N<4m+1. The log of the positive quotient is −3m²/N+O(m/N+m³/N²) at the claimed finite-c scale and the quotient is bounded by exp(−m(3m+1)/N) above that scale. A separate small direct truth-vector enumeration for m=2 confirmed no nine-type carrier below N=9 and favorable subset counts 1,3,6,10,15 for N=9,…,13; it is only a diagnostic, not a proof. Reviewed the frozen VERIFICATION.md and verify.py, which check attained cardinality rather than the false cross-structure assertion.

## originality

PASS

The repaired distinct contribution is simultaneous sharp atomic capacity for arbitrary prescribed parameter-order permutations in the mixed named signature, including the characterization that links the one-order maximum to gap clearance. The binomial spacing count and its square-root profile are not credited as independently original; they follow from classical separated-set enumeration once the model-theoretic event is identified. The comparison is best of current knowledge.

## value

PASS

The natural finite-model invariant is the largest diversity of local configurations seen by a single structure over a prescribed common named base. The separable but potentially conflicting exact-successor witnesses make sharp simultaneous attainment, with a minimal carrier for each set of prescribed parameter permutations, more informative than counting individually consistent types or quoting separate per-order capacities. The one-order spacing equivalence gives a useful interpretation of when that sharp cardinality is attained in a model sampled by random marks; value does not rest on the classical binomial calculation alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
