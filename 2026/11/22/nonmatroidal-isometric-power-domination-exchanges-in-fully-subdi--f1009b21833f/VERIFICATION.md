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

Re-audited the unchanged theorem with the corrected scope of contribution. A residual cycle's edge subdivisions are initially unobserved, and no endpoint could force the first of these because it still has two such neighbors. If an original is selected it exposes each remaining original via the connecting subdivision. If none is selected, two unobserved originals would create a residual triangle; one unobserved original forces the residual forest to be its spanning star, which the observed originals and then one subdivision can finish. With all originals observed, peeling leaves finishes exactly the forests. For fixed omitted original set R, internal sensors complement a forest and all exterior subdivisions are free; Cayley's labeled tree count gives the EGF. The lower bound n-r+binom(r-1,2) for r>=1 ties n-2 only at r=2,3, giving exactly the two minimum types. Adjacent A–A states exchange omitted originals, A–B states are adjacent iff the omitted pair lies in the triple, and B–B adjacency requires the same triple or internal sensor. These cases give the degrees and edge count. The explicit path via omitted pairs maximizes overlap and attains the lower bound (n-2)-|S intersect T|; for distinct triples with different sensors this uses pairs sharing all common originals. Disjoint pair/triple or triple/triple omissions give the stated radius and diameter when feasible, with all eccentricities 1,2,3 respectively at n=3,4,5 by the same formula. In the nonmatroid witness both candidate replacements leave the subdivision incident to a selected original, so neither is an optimum, and four distinct original labels are necessary for that witness. Inspected the bundled C++ and Python code without executing it: the former checks all initial sensor subsets through n=6, the latter independently compares polynomials through n=5 and checks exchange metrics from the classified family through n=9. The analytic proof, not extrapolation, establishes the result for all n>=3.

## originality

PASS

The repaired RESULT and REVIEW acknowledge exact overlap: another same-day record gives the identical forest criterion and minimum family and implies the enumerator; both slide records give the minimum family. These are no longer claimed as distinct contributions. The supported remainder is the all-pairs isometry and its failure to imply matroid basis exchange, with the exact unrestricted replacement geometry. No order is inferred from the shared date.

## value

PASS

The repaired distinct contribution separates metric-geodesic flexibility from matroidal basis exchange in a natural optimization problem, all orders at once. A planner can achieve the absolute minimum possible number of replacements between any two optima despite a failure of the single-prescribed-element exchange axiom. The degrees and eccentricities show how that flexibility varies with optimum type. This is not a restatement of the identical minimum family or the adjacent-token slide theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
