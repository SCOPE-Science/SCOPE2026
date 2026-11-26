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

The matched initial state is s times each roof's own capacity, with the same q within that roof for both drying intervals. Set z=qCs and use x>y. In one roof, if neither first event fills it, the two second-event overflow arguments differ by −(1−q)(x−y), so the order difference is nonpositive. If even the smaller first event fills it, z≤qC implies both second events also fill it; the difference is zero. In the intervening straddling regime, substituting the first-event caps gives −(1−q)(C−z−y)<0 if qC+y≥C. Otherwise the difference is min(z+x−C,(1−q)z−qy); the first argument is positive, and the second has strictly positive slope. The three regimes occur in order as s increases, hence there is at most one strict sign change on a single roof. I derived all knot candidates by solving the first and unsaturated-second spill equalities, with constant second overflow when the first event fills the store, then evaluated each affine piece by exact mass balance. The four interior knots are 85/108,65/81,5/6,35/36. The five joint-overflow differences have slopes 2/25,−403/25,2/25,47/25,2/25, and none of the knots or endpoints is a zero. Of their five candidate roots only 5/8,635/806,45/47 belong to their pieces. The signs alternate from D(0)=−1/20 to D(1)=3/100. This establishes exactly three distinct strict reversals and the minimality of two roof types for that phenomenon; a finite sample alone would not.

## originality

PASS

Pass the heterogeneous two-roof three-reversal construction and the sharp minimal number of types, not the general idea of a capped store or its single-store crossover. The strongest same-day comparator uses precisely the single-store runoff difference after identifying its antecedent absolute water with z=qCs. Its mixed-saturation threshold is the same equality (1−q)z=qB written in the inter-event loss variable. This is material overlap, including a route to the single-roof sign bound; it does not imply the three zero crossings of a positive sum evaluated along two different roof responses. No inspected result gives that aggregation claim.

## value

PASS

The sum of two minimal storage responses is an informative obstruction to transferring a single-roof order rule to aggregated runoff. Matching initial fractional fill and reversing the same two depths keeps the comparison well defined; differing capacities and drying move branch thresholds so one component's negative interval interrupts the other's sign progression. The exact three switches and proof that one component cannot achieve them give a sharp structural counterexample rather than an arbitrary set of simulated curves.

The dated certificate retains the supplied scientific assessment, sources and limitations.
