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

The point and line avoidance operators reverse inclusions and satisfy B⊆alpha(A) iff A⊆beta(B). Extensivity on each shore and antitonicity give alpha beta alpha=alpha and its dual, hence F³=F. The image is the Cartesian product of the two avoidance images; these images are in bijection by restriction of alpha and beta. The update swaps two symbols, so r fixed points and choose(r,2) primitive two-cycles follow. For each recurrent state the one-step predecessors form the product of the two avoidance fibers; summing these products over the one or two phases counts exactly the full attractor basin including recurrent points. A separate replay constructs each shore's update by lowest-set-bit recursion, builds the full successor table and checks every one of its 262144 destinations per graph; it reproduces every EXPECTED_COUNTS.json field and both full histograms. The resulting fixed counts (110,112,113) rise while fixed-attraction totals (914,912,911) fall, and nonrecurrent states exist in each system. Incidence checks give the required cubic linear configurations. For an independent exhaustiveness check, uncollinear pairs form a 2-factor; for the four partitions 9, 3+6, 4+5, 3+3+3, exact-covering the remaining pairs by line triples gives 2, 6, 0, 12 labeled solutions on fixed 2-factors, respectively, and quotienting by their automorphism groups gives 1, 1, 0, 1 classes. Distinct Levi six-cycle counts also rule out identification by swapping shores. Bokowski–Pilaud Table 1 independently reports the required combinatorial count; the k=3 row is credited there to Betten–Brinkmann–Pisanski, distinct from the authors' topological enumeration.

## originality

PASS

Do not credit the configuration classification, the universal closure identity, the product-of-fibers rule or the maximal-independent-set interpretation as new. The distinct checked claim is the complete numerical basin and orbit comparison across all three smallest inequivalent cubic point–line incidence types, including the direction reversal between the number of equilibria and the total fixed-basin mass. No distinct covering table or theorem yielding those exact data without new graph-specific fiber calculations was established in the examined sources.

## value

PASS

The graph set is the first nontrivial complete comparison class of cubic point-line geometries, not an arbitrary selection of instances. An exact attractor-by-attractor basin benchmark distinguishes the types even while degree, update, and transient bound are fixed. The contrast in fixed-attraction population versus fixed-point count matters for using equilibrium counts to describe random initial conditions; those are different measurable aspects even in this minimal setting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
