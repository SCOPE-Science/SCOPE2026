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

After reflection, all coordinatewise nearest sites along the segment are in the endpoint rectangle contained in the diamond. The finite and infinite tessellations therefore give the same positive-length sequence, since the half-integer lines are met only at isolated parameters; no segment runs along one. Distinct crossing times count the traversals, which cannot repeat a cell by convexity. Simultaneity requires the coprime reduced coordinates both odd; in that case the g common times are (2h+1)/(2g), 0≤h<g. Removing endpoint cells yields the claimed count, including both axes. The two endpoint ranks must be highest; summing their probability needs no independence across visibility events. The uncorrected diamond shell has 4m sites, and the exceptional primitive ordered pairs of positive odd coordinates of sum 2k are indexed by reduced residues modulo 2k; the four signs and the factor two in the rank probability give the factor eight. The correction at R=2 is already nonzero. The derivative bound on h(x)=1/[x(x+1)] makes the kth group O(k^-2) after summing g. For 2kg>R the small-k tail adds O(R^-1 sum_(k≤R/2) 1/k), and the large-k tail is O(R^-1); the harmonic baseline has the asserted constant and O(R^-1) remainder. Independent summation with a tail bound certifies the displayed decimal rounding.

## originality

PASS

The square-lattice logarithmic-growth suggestion and the one-edge rank law are prior. The inspected sources do not give or imply the exact diamond-center expected degree, the coefficient 8 in log R or the convergent arithmetic offset. The half-integer crossing calculation is an ingredient, not an asserted independently novel digital-geometry theorem.

## value

PASS

The result quantifies a stated all-direction lattice-visibility question with an exact expected degree, a sharp divergent coefficient and an offset measuring degeneracies of square Voronoi cells. This gives a benchmark for a fixed window and height-null model; it is not an all-vertex or almost-sure degree law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
