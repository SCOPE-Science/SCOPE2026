---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

At a=7/17 the endpoint orbit is exactly 7,3,11,12,10,14,6,5 in integer coordinates divided by 17; 0 and 1 form a separate boundary two-cycle. My exact replay /workspace/branches/audit_period_graph.py computed the cell images [11,17], [7,11], [5,7], [3,5], [12,14], [10,12], [6,10], [0,6] in the same coordinates. Because image endpoints are partition boundaries, a transition between cell interiors must cover the whole target cell; isolated endpoint hits are handled by the boundary orbits. The four graph components are simple cycles (0,7), (1,4,6,3), (2), (5). Every infinite itinerary eventually stays on a simple cycle, and contraction of its inverse branches makes an infinite cyclic itinerary a single periodic point. The exact replay solved each cyclic affine equation: the (0,7) candidate is on the boundary, not an interior orbit; the other solutions are the stated four-cycle and the two fixed points. This distinction is slightly obscured by the phrase 'interior graph cycles' in the frozen proof, but it does not alter the list or the boundary argument. Nested survivor sets exclude all other periods at smaller a; the old orbits survive even at a=2/5 and the eight-cycle requires a>=7/17. This proves the zeta formula at all orders, not merely the finite-period diagnostic. The compact restriction is continuous; the survivor is countable by finite preimages of finitely many orbits, and invariant measures give full mass to the periodic points by recurrence. The dimension and topological entropy are therefore zero.

## originality

PASS

The supported addition is the all-real symmetric interval-map classification beyond 2/5, including the unique eight-cycle and all-order zeta jump at 7/17. The strongest distinct indexed comparisons cover the preceding phase, a different postcritical parameter, or the circle quotient. The primary decreasing-Lorenz abstract and indexed Theorem 1.2 description give general symbolic-survivor machinery, not an exact periodic census in the available passages. The finite graph calculation is additional mathematical work; this is a bounded best-of-knowledge judgment, not a claim of exhaustive priority.

## value

PASS

The next sharp phase of a natural one-parameter hole family is motivated by the preceding period-four onset. The result distinguishes a genuine jump in exact orbit counts and zeta from any change in entropy or dimension. The all-order classification, including exclusion of hidden intermediate periods, is useful for later phase and bifurcation analyses and is not just a finite-period search.

The dated certificate retains the supplied scientific assessment, sources and limitations.
