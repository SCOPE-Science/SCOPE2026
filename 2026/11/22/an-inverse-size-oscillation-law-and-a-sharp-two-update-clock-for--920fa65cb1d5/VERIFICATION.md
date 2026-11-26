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

Both endpoints see exactly the totals outside their partner pair. A global lead of at least two gives consensus in one update. For two strictly tied leaders the monochromatic leader pairs flip, mixed leader–third pairs collapse to the other leader, and AB and CC retain their types. Initial tie plus equality of the two leader–third pair counts forces equality of the monochromatic leader-pair counts; the reduced output is a two-cycle exactly when there is a pair to flip. Otherwise an unequal count of leader–third pairs creates a margin of at least two. With a triple tie, each mixed pair becomes the third opinion and monochromatic pairs stay; thereafter the complete-graph update on the pairs is determined by which pair totals tie at the top. For a unique lead by one with unique runner-up, the displayed new margin and the odd parity of v−w leave only v=1,c=u=w=0 (immediate oscillation) and w=1,c=u=v=0 (one-step predecessor) outside the consensus cases. With tied runners-up the new lead is at least r−1 for r≥3; r=1 gives the 24 exceptional fixed states of AB+AC type. The mutually exclusive input sectors and labeled multiplicity give the census; the stated witnesses require two updates when m≥3, while the maximum at m=2 is one. In the dominant sector, the projected increment support includes 0 and both signed basis directions and the covariance determinant is 8/81. The joint lattice local limit on its maximal lattice, summed along the fiber at first two coordinates zero and normalized by the projected local limit, gives a conditional centered normal with variance 1; hence the strict third-place event contributes 1/2. The other sectors are exponentially small and O(m⁻³ᐟ²), respectively. The constant is therefore (3/2)·9/(4π√2). Separate bounded direct-neighborhood checks at m=2–5 and weighted profile checks at m=2–12 matched the formulas and cutoff; the uploaded scripts and reported output were inspected, not executed. The analytical argument establishes the infinite-size claims.

## originality

PASS

The strongest comparisons share the graph family, the three-opinion tie rule, or the general period-two conclusion, but not the hypotheses and conclusions needed for the sharp clock and basin census. No inspected theorem implies the count or its inverse-size probability.

## value

PASS

The all-size classification addresses a natural dense graph family where exact ties survive. The sharp first-entry bound distinguishes transient length from least period, and the exact basin census explains why recurrent oscillation has inverse-size probability despite exponentially many primitive two-cycles. Neither fact is a generic period-two corollary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
